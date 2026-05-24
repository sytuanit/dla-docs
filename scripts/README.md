# Scripts Guide

Tai lieu nay huong dan cach su dung cac script:

- `generate-promo-screenshots.py`
- `generate-store-screenshots.js`
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
- `13` hoac `15` -> `headline` (string hoac array `[tren anh, duoi anh]`; promo 15: [0] tren, [1] duoi screenshot)
- `20` -> `sub[0]`
- `21` -> `sub[1]`

Neu thieu slogan hoac thieu anh capture, script se `Skip` va in ly do.

---

## 2) `generate-store-screenshots.js`

Script resize anh promo da ghép (`screenshot-{n}.png`) ve cac kich thuoc upload cho Google Play / App Store Connect. Chi xu ly **cac file duoc chon** trong `selected-screenshots.json` (hoac file JSON tuong tu truyen qua CLI).

### Dau vao / Dau ra

- Dau vao (phone):
  - iOS: `dla-docs/screenshots/{locale}/screenshot-{n}.png` (anh da qua `generate-promo-screenshots.py`)
  - Android: `dla-docs/screenshots-android/{locale}/screenshot-{n}.png`
- Dau vao (iPad, tuy chon):
  - `dla-docs/screenshots-ipad/{locale}/screenshot-{n}.png` — chi xu ly file trung ten voi danh sach da chon
- File chon anh:
  - Mac dinh: `dla-docs/scripts/selected-screenshots.json`
  - Dang JSON: mang ten file, hoac `{ "screenshots": ["screenshot-11.png", ...] }`
- Dau ra:
  - `dla-docs/screenshots-resized/{locale}/<folder>/<ten-file-goc>.png`

Cac kich thuoc dich (fit `contain`, nen trang `#ffffff` neu lech ty le):

| Thu muc output | Kich thuoc | Nguon |
|----------------|------------|--------|
| `android-1080x1920` | 1080×1920 | `screenshots-android/` |
| `ios-1290x2796` | 1290×2796 | `screenshots/` |
| `ios-1242x2688` | 1242×2688 | `screenshots/` |
| `ios-2048x2732` | 2048×2732 | `screenshots-ipad/` (neu co) |

Moi lan chay, script **xoa va tao lai** toan bo `screenshots-resized/`.

### Yeu cau

- Node.js
- Cai dependency trong `dla-docs/`:

```bash
cd dla-docs
npm install
```

Script dung thu vien `sharp` (da khai bao trong `package.json`).

### Cach chay

Tu thu muc `dla-docs/` (khuyen nghi):

```bash
npm run screenshots:generate
```

Hoac goi truc tiep:

```bash
node scripts/generate-store-screenshots.js
```

Dung file chon anh khac (duong dan tuong doi hoac tuyet doi):

```bash
node scripts/generate-store-screenshots.js scripts/selected-screenshots.json
node scripts/generate-store-screenshots.js path/to/my-selection.json
```

### Vi du `selected-screenshots.json`

```json
[
  "screenshot-11.png",
  "screenshot-12.png",
  "screenshot-13.png",
  "screenshot-20.png",
  "screenshot-21.png"
]
```

Script se resize **tat ca locale** co trong `screenshots/`; moi locale phai co **day du** cac file trong danh sach chon, neu thieu se dung va bao loi.

### Luu y

- Chi nhan file khop pattern `screenshot-*.{png,jpg,jpeg,webp}`.
- Can co it nhat mot thu muc locale duoi `screenshots/` (vd. `screenshots/vi/`).
- Android lay tu `screenshots-android/`; iOS phone tu `screenshots/`; iPad tu `screenshots-ipad/` (bo qua neu thu muc khong ton tai).
- Output la PNG chat luong cao, phu hop copy len console upload store.

---

## 3) `scale-app-store-preview-video.ps1`

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
   - Chuan bi `screenshot-*-capture.png` (chup tu app hoac copy vao `dla-docs/screenshots/{locale}/`)
   - Chay `generate-promo-screenshots.py`
2. Resize ve kich thuoc store:
   - Cap nhat `selected-screenshots.json` (danh sach `screenshot-{n}.png` can upload)
   - Chay `npm run screenshots:generate` trong `dla-docs/`
   - Lay file tu `screenshots-resized/{locale}/<android-1080x1920|ios-1290x2796|...>/`
3. Chuan hoa app preview video:
   - Chay `scale-app-store-preview-video.ps1` (khong `-FpsOnly` neu can ra dung `886x1920`)
4. Kiem tra lai do dai video (< 30s) va kich thuoc truoc khi upload ASC / Play Console.
