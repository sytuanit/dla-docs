# Pengaturan

## 1. Tujuan

Modul **Pengaturan** memungkinkan Anda mengonfigurasi aplikasi sesuai kebutuhan pribadi Anda, termasuk:
- Bahasa dan mata uang
- Notifikasi
- Kategori
- Cadangan dan pemulihan data
- Keamanan (kata sandi, Face ID)

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Mengubah bahasa atau mata uang
- Mengaktifkan/menonaktifkan notifikasi
- Mengelola kategori (tambah, edit, hapus, set default)
- Mencadangkan atau memulihkan data
- Mengubah kata sandi atau mengaktifkan Face ID

## 3. Layar Terkait

- Layar pengaturan utama
- Pengaturan dasar
- Pilih bahasa
- Pilih mata uang
- Kelola kategori
- Cadangkan data
- Pulihkan data
- Ubah kata sandi
- Aktifkan Face ID / Sidik Jari

## 4. Penggunaan Utama

### 4.1 Ubah Bahasa

1. Buka **Pengaturan** → **Tampilan & Bahasa** → **Bahasa**
2. Pilih bahasa yang diinginkan
3. Aplikasi akan secara otomatis memuat ulang dengan bahasa baru

### 4.2 Ubah Mata Uang

1. Buka **Pengaturan** → **Tampilan & Bahasa** → **Mata Uang**
2. Pilih jenis mata uang
3. Semua jumlah akan ditampilkan dalam unit baru

### 4.3 Aktifkan/Nonaktifkan Notifikasi

1. Buka **Pengaturan** → **Notifikasi**
2. Toggle switch **Notifikasi**
3. Jika diaktifkan, Anda akan menerima pengingat tentang:
   - Pendapatan berkala jatuh tempo
   - Pengeluaran berkala jatuh tempo
   - Rekening tabungan jatuh tempo
   - Acara khusus mendatang

### 4.4 Kelola Kategori

1. Buka **Pengaturan** → **Kategori**
2. Pilih jenis kategori untuk dikelola:
   - Pendapatan Berkala
   - Pendapatan Tambahan
   - Pengeluaran Berkala
   - Pengeluaran Harian
3. Tambah/Edit/Hapus kategori
4. Set kategori default (untuk pengeluaran harian)

### 4.5 Cadangkan Data

1. Buka **Pengaturan** → **Cadangan & Data** → **Cadangan**
2. Pilih lokasi penyimpanan (Sistem file)
3. Ketuk **Cadangan**
4. File cadangan akan dibuat

### 4.6 Pulihkan Data

1. Buka **Pengaturan** → **Cadangan & Data** → **Pulihkan**
2. Pilih file cadangan
3. Konfirmasi pemulihan
4. **Catatan**: Pemulihan akan menimpa data saat ini

## 5. Ilustrasi UI (Wireframe)

### 5.1 Layar Pengaturan Utama

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Pengaturan                 │
├─────────────────────────────────────────┤
│  Tampilan & Bahasa                       │
│  ┌───────────────────────────────────┐ │
│  │ Bahasa                             │ │
│  │ Bahasa Indonesia            →       │ │
│  │                                    │ │
│  │ Mata Uang                           │ │
│  │ IDR (Rp)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notifikasi                              │
│  ┌───────────────────────────────────┐ │
│  │ Notifikasi                    [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Cadangan & Data                        │
│  ┌───────────────────────────────────┐ │
│  │ Cadangan                      →    │ │
│  │                                    │ │
│  │ Pulihkan                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Kategori                                │
│  ┌───────────────────────────────────┐ │
│  │ Kelola Kategori                →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Keamanan                                │
│  ┌───────────────────────────────────┐ │
│  │ Kata Sandi                      →    │ │
│  │                                    │ │
│  │ Face ID / Sidik Jari           →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logika & Aturan

### 6.1 Bahasa

- Didukung: English, Bahasa Indonesia, Tiếng Việt, 日本語
- Mengubah bahasa akan memuat ulang seluruh aplikasi
- Kategori sistem akan secara otomatis diterjemahkan ke bahasa baru

### 6.2 Mata Uang

- Setiap bahasa memiliki mata uang default (misalnya, IDR untuk Bahasa Indonesia)
- Anda dapat memilih mata uang yang berbeda
- Semua jumlah akan diformat sesuai mata uang yang dipilih

### 6.3 Notifikasi

- Notifikasi hanya berfungsi ketika aplikasi memiliki izin
- Waktu notifikasi tergantung pada setiap fungsi dan dapat dikonfigurasi:
  - Pendapatan/Pengeluaran Berkala: `notificationTime1`, `notificationTime2` (default 16:00 & 19:00)
  - Rekening Tabungan & Pinjaman: `notificationTime1`, `notificationTime2` (default 10:00 & 19:00)
  - Acara Khusus & Langkah Persiapan: sesuai dengan `reminderTime` yang Anda masukkan
  - Dapat menonaktifkan notifikasi untuk setiap jenis secara terpisah (di masa depan)

### 6.4 Kategori

- Kategori sistem tidak dapat dihapus, hanya dinonaktifkan
- Kategori pengguna dapat dihapus (jika tidak digunakan)
- Setiap jenis kategori independen (pendapatan berkala, pengeluaran harian, dll)

## 7. Catatan Penting

- **Cadangkan Secara Rutin**: Sebaiknya mencadangkan data secara berkala untuk menghindari kehilangan data
- **Pulihkan Akan Menimpa**: Pemulihan akan mengganti semua data saat ini
- **Kata Sandi**: Jika Anda lupa kata sandi, Anda dapat mereset (akan menghapus data)

