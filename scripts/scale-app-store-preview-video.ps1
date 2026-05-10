<#
.SYNOPSIS
  Scale all videos in a folder to App Store Connect preview size 886x1920.

.DESCRIPTION
  **App Store Connect app previews must be 886×1920 px** (that exact frame size). This script’s
  **default mode** scales each video to 886×1920 (**-FitMode pad** or **crop**) **and** forces CFR 30 fps.

  Input is always a directory. Each supported video file is encoded to a sibling file named
  "<basename>_886x1920.mp4" (resize + CFR 30 fps), or "<basename>_cfr30.mp4" when using **-FpsOnly**.

  Forces constant 30 fps (CFR). App Store Connect rejects app previews above 30 fps and
  variable frame rate from many screen recordings — see Apple App Preview specs.

  For upload to ASC, **omit -FpsOnly** unless the source is already exactly 886×1920 and you only
  need fps/VFR fixes.

  **"Your app preview is too large"** on App Store Connect often means:
  - **Duration over 30 seconds** (even slightly — ASC misreports as "too large"); or
  - **File / bitrate** too high for processing.

  By default this script **trims to 30 seconds** and uses a **~4 Mbps** AVC target to keep files small.

  Requires ffmpeg. Install: winget install Gyan.FFmpeg
  Resolves ffmpeg from PATH, WinGet Links, or WinGet Packages.

.PARAMETER InputDirectory
  Folder containing source videos (.mp4, .mov, .m4v, .avi, .mkv).

.PARAMETER FitMode
  pad  = scale down to fit inside 886x1920, letterbox/pillarbox black bars if needed (default).
  crop = scale up then center-crop to 886x1920 (no bars, may lose edges).

.PARAMETER Recurse
  Include videos in subfolders (same relative path, output next to each source).

.PARAMETER MaxDurationSeconds
  Cap output at this many seconds from the start. Default **30** (App Store Preview limit). **0** = no `-t` trim (full source length). For sources already under 30s, default **30** does not shorten them — ffmpeg stops at end of input.

.PARAMETER FpsOnly
  Do **not** resize — output stays at the **source resolution**. Only normalizes to **constant 30 fps**
  (CFR). Output: `<basename>_cfr30.mp4`. **Not valid for App Store Connect** unless the source is
  **already 886×1920**. For typical phone screen recordings, run **without -FpsOnly** so outputs are
  **`_886x1920.mp4`**.

.PARAMETER VideoAvgBitrate
  Target average video bitrate for libx264 (e.g. 3M, 4M, 5M). Lower reduces file size if ASC still complains.
#>
# Cách chạy: 
# .\scale-app-store-preview-video.ps1 -InputDirectory ".\video" -MaxDurationSeconds 0 -Recurse  
param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string] $InputDirectory,

  [ValidateSet('pad', 'crop')]
  [Alias('Mode')]
  [string] $FitMode = 'pad',

  [switch] $Recurse,

  [int] $MaxDurationSeconds = 30,

  [switch] $FpsOnly,

  [string] $VideoAvgBitrate = '4M'
)

$ErrorActionPreference = 'Stop'

function Get-FfmpegPath {
  $fromCmd = Get-Command ffmpeg -ErrorAction SilentlyContinue
  if ($fromCmd) {
    return $fromCmd.Source
  }

  $wingetLink = Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Links\ffmpeg.exe'
  if (Test-Path -LiteralPath $wingetLink) {
    return $wingetLink
  }

  $pkgRoot = Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Packages'
  if (Test-Path -LiteralPath $pkgRoot) {
    $hit = Get-ChildItem -Path $pkgRoot -Directory -ErrorAction SilentlyContinue |
      Where-Object { $_.Name -match 'Gyan\.FFmpeg|ffmpeg' } |
      ForEach-Object {
        Get-ChildItem -LiteralPath $_.FullName -Recurse -Filter 'ffmpeg.exe' -ErrorAction SilentlyContinue |
          Select-Object -First 1
      } |
      Select-Object -First 1

    if ($hit -and (Test-Path -LiteralPath $hit.FullName)) {
      return $hit.FullName
    }

    $anyBin = Get-ChildItem -Path $pkgRoot -Recurse -Filter 'ffmpeg.exe' -ErrorAction SilentlyContinue |
      Select-Object -First 1
    if ($anyBin -and (Test-Path -LiteralPath $anyBin.FullName)) {
      return $anyBin.FullName
    }
  }

  foreach ($p in @(
      "${env:ProgramFiles}\ffmpeg\bin\ffmpeg.exe",
      "${env:ProgramFiles(x86)}\ffmpeg\bin\ffmpeg.exe"
    )) {
    if ($p -and (Test-Path -LiteralPath $p)) {
      return $p
    }
  }

  return $null
}

function Invoke-ScaleOneVideo {
  param(
    [Parameter(Mandatory = $true)]
    [string] $FfmpegExe,

    [Parameter(Mandatory = $true)]
    [string] $InputFile,

    [Parameter(Mandatory = $true)]
    [string] $OutputFile,

    [Parameter(Mandatory = $true)]
    [ValidateSet('pad', 'crop')]
    [string] $FitMode,

    [int] $MaxDurationSeconds = 0,

    [switch] $FpsOnly,

    [Parameter(Mandatory = $true)]
    [string] $VideoAvgBitrate
  )

  $vf = if ($FpsOnly) {
    'fps=30,setsar=1'
  }
  elseif ($FitMode -eq 'pad') {
    'scale=886:1920:force_original_aspect_ratio=decrease,pad=886:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30'
  }
  else {
    'scale=886:1920:force_original_aspect_ratio=increase,crop=886:1920,setsar=1,fps=30'
  }

  $avgMbps = 4.0
  if ($VideoAvgBitrate -match '(\d+(?:\.\d+)?)\s*M') {
    $avgMbps = [double]$Matches[1]
  }
  $maxMbps = [math]::Min(12.0, [math]::Round($avgMbps * 1.375, 2))
  $bufMbps = [math]::Round($maxMbps * 2.0, 2)
  $maxrateStr = "${maxMbps}M"
  $bufsizeStr = "${bufMbps}M"

  $ffmpegArgs = @(
    '-y',
    '-i', $InputFile
  )
  if ($MaxDurationSeconds -gt 0) {
    $ffmpegArgs += @('-t', "$MaxDurationSeconds")
  }
  $ffmpegArgs += @(
    '-vf', $vf,
    '-fps_mode', 'cfr',
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-b:v', $VideoAvgBitrate,
    '-maxrate', $maxrateStr,
    '-bufsize', $bufsizeStr,
    '-profile:v', 'high',
    '-pix_fmt', 'yuv420p',
    '-movflags', '+faststart'
  )
  if ($FpsOnly) {
    $ffmpegArgs += @('-c:a', 'copy')
  }
  else {
    $ffmpegArgs += @(
      '-c:a', 'aac',
      '-b:a', '96k',
      '-ar', '44100',
      '-ac', '2'
    )
  }
  $ffmpegArgs += @($OutputFile)

  & $FfmpegExe @ffmpegArgs
  return $LASTEXITCODE
}

$resolvedDir = $null
try {
  $resolvedDir = (Resolve-Path -LiteralPath $InputDirectory).Path
} catch {
  Write-Error "Input directory not found: $InputDirectory"
}

$item = Get-Item -LiteralPath $resolvedDir -ErrorAction Stop
if (-not $item.PSIsContainer) {
  Write-Error "Path must be a directory, not a file: $resolvedDir"
}

$ffmpegExe = Get-FfmpegPath
if (-not $ffmpegExe) {
  Write-Error @'
ffmpeg not found.

Install (run in PowerShell):
  winget install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements

If winget is not on PATH, try:
  & "$env:LocalAppData\Microsoft\WindowsApps\winget.exe" install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements

Then close this terminal, open a new one, and run the script again.
'@
}

$gciParams = @{
  LiteralPath = $resolvedDir
  File        = $true
}
if ($Recurse) {
  $gciParams['Recurse'] = $true
}

$videoExt = @('.mp4', '.mov', '.m4v', '.avi', '.mkv')
$files = @(Get-ChildItem @gciParams |
  Where-Object {
    $ext = $_.Extension.ToLowerInvariant()
    $videoExt -contains $ext -and $_.BaseName -notmatch '_886x1920$|_cfr30$'
  })

if ($files.Length -eq 0) {
  Write-Error "No video files found in: $resolvedDir$(if ($Recurse) { ' (recursive)' })"
}

Write-Host "ffmpeg: $ffmpegExe"
Write-Host "InputDirectory: $resolvedDir"
Write-Host "FitMode: $(if ($FpsOnly) { '(FpsOnly - no resize)' } else { $FitMode })"
Write-Host "MaxDurationSeconds: $(if ($MaxDurationSeconds -le 0) { '(no trim)' } else { $MaxDurationSeconds })"
Write-Host "FpsOnly: $FpsOnly"
Write-Host "VideoAvgBitrate: $VideoAvgBitrate"
Write-Host "Files: $($files.Length)"
Write-Host ""

if ($FpsOnly) {
  Write-Warning 'FpsOnly: output is NOT resized. App Store previews require 886x1920 - omit -FpsOnly for *_886x1920.mp4 outputs.'
}

$fail = 0
foreach ($f in $files) {
  $outPath = Join-Path $f.DirectoryName ($f.BaseName + $(if ($FpsOnly) { '_cfr30' } else { '_886x1920' }) + '.mp4')
  Write-Host ">>> $($f.Name) -> $([System.IO.Path]::GetFileName($outPath))"
  $code = Invoke-ScaleOneVideo -FfmpegExe $ffmpegExe -InputFile $f.FullName -OutputFile $outPath -FitMode $FitMode -MaxDurationSeconds $MaxDurationSeconds -FpsOnly:$FpsOnly -VideoAvgBitrate $VideoAvgBitrate
  if ($code -ne 0) {
    Write-Warning "ffmpeg exited $code for $($f.FullName)"
    $fail++
  }
}

if ($fail -gt 0) {
  Write-Error "$fail file(s) failed."
}

Write-Host "Done. $($files.Length) file(s) OK."
