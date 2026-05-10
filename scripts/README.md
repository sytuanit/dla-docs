# Scripts Guide

Tai lieu nay huong dan cach su dung 2 script:

- `generate-promo-screenshots.py`
- `scale-app-store-preview-video.ps1`

## 1) `generate-promo-screenshots.py`

Script dung de tao anh promo App Store (kich thuoc `1242x2688`) tu anh capture goc `screenshot-{n}-capture.png`, ket hop voi noi dung marketing trong file `screenshot-14-marketing.json`.

### Dau vao / Dau ra

- Dau vao:
  - `dla-docs/scripts/screenshot-14-marketing.json`
  - Anh capture trong `dla-docs/screenshots/{locale}/`, ten dang:
    - `screenshot-11-capture.png`
    - `screenshot-12-capture.png`
    - `screenshot-13-capture.png`
    - `screenshot-15-capture.png` (neu dung)
    - `screenshot-20-capture.png`
    - `screenshot-21-capture.png`
- Dau ra:
  - iOS: `dla-docs/screenshots/{locale}/screenshot-{n}.png`
  - Android: `dla-docs/screenshots-android/{locale}/screenshot-{n}.png`

### Yeu cau

- Python 3
- Thu vien Pillow:

```bash
pip install pillow
```

### Cach chay

Chay mac dinh (locale `vi`, tao 11/12/13, ca iOS va Android):

```bash
python generate-promo-screenshots.py
```

Chay cho 1 locale va 1 platform:

```bash
python generate-promo-screenshots.py --locale en --platform ios
python generate-promo-screenshots.py --locale vi --platform android
```

Chi tao mot so screenshot:

```bash
python generate-promo-screenshots.py --only 11 13 20 21
```

Chay tat ca locale co trong JSON:

```bash
python generate-promo-screenshots.py --all-locales --only 13 20 21
```

### Tham so chinh

- `--locale <key>`: locale key trong JSON (mac dinh `vi`)
- `--all-locales`: chay tat ca locale trong `screenshot-14-marketing.json`
- `--only <N...>`: danh sach screenshot index (mac dinh `11 12 13`)
- `--platform ios|android|both`: chon nen tang (mac dinh `both`)

### Mapping noi dung slogan

- `11` -> `sub[0]`
- `12` -> `sub[1]`
- `13` hoac `15` -> `headline`
- `20` -> `sub[0]`
- `21` -> `sub[1]`

Neu thieu slogan hoac thieu anh capture, script se `Skip` va in ly do.

---

## 2) `scale-app-store-preview-video.ps1`

Script scale video ve chuan App Store Connect app preview `886x1920`, dong thoi chuan hoa ve **CFR 30 fps**.

Mac dinh script:

- Resize video ve `886x1920` (theo `-FitMode pad` hoac `crop`)
- Trim toi da `30` giay
- Encode H.264 (`libx264`) voi bitrate trung binh `4M`
- Output ten: `<basename>_886x1920.mp4`

Neu dung `-FpsOnly`, script **khong resize** ma chi chuan hoa fps, output: `<basename>_cfr30.mp4`.

### Yeu cau

- Windows PowerShell
- `ffmpeg` (co the cai nhanh bang):

```powershell
winget install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements
```

### Cach chay

Scale toan bo video trong thu muc (khong de quy):

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos"
```

Scale + de quy subfolder:

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -Recurse
```

Chon cach fit:

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -FitMode pad
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -FitMode crop
```

Chi fix fps (giu nguyen do phan giai):

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -FpsOnly
```

Khong trim 30s:

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -MaxDurationSeconds 0
```

Dieu chinh bitrate:

```powershell
.\scale-app-store-preview-video.ps1 -InputDirectory "D:\path\to\videos" -VideoAvgBitrate 3M
```

### Tham so chinh

- `-InputDirectory` (bat buoc): thu muc chua video
- `-FitMode pad|crop` (mac dinh `pad`)
- `-Recurse`: quet ca subfolder
- `-MaxDurationSeconds` (mac dinh `30`, dat `0` de tat trim)
- `-FpsOnly`: chi chuan hoa CFR 30 fps, khong resize
- `-VideoAvgBitrate` (mac dinh `4M`)

### Dinh dang video duoc xu ly

- `.mp4`, `.mov`, `.m4v`, `.avi`, `.mkv`

Script bo qua file da xu ly (ten ket thuc `_886x1920` hoac `_cfr30`).

---

## Goi y quy trinh de dang upload App Store

1. Tao promo screenshots:
   - Chuan bi `screenshot-*-capture.png`
   - Chay `generate-promo-screenshots.py`
2. Chuan hoa app preview video:
   - Chay `scale-app-store-preview-video.ps1` (khong `-FpsOnly` neu can ra dung `886x1920`)
3. Kiem tra lai do dai video (< 30s) va kich thuoc truoc khi upload ASC.
