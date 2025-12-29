# Cadangan & Pemulihan

## 1. Tujuan

Modul **Cadangan & Pemulihan** membantu Anda:
- Mencadangkan semua data aplikasi ke file
- Memulihkan data dari file cadangan
- Melindungi data dari kehilangan karena kesalahan perangkat atau instalasi ulang aplikasi

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Mencadangkan data sebelum menginstal ulang aplikasi
- Mentransfer data ke perangkat baru
- Memulihkan data setelah kehilangan data
- Membuat cadangan berkala

## 3. Layar Terkait

- Layar cadangan
- Layar pemulihan

## 4. Penggunaan Utama

### 4.1 Cadangkan Data

1. Buka **Pengaturan** → **Cadangan & Data** → **Cadangan**
2. Lihat informasi:
   - Jumlah record yang akan dicadangkan
   - Ukuran file yang diharapkan
3. Ketuk **Cadangan**
4. Pilih lokasi penyimpanan (Sistem file)
5. File cadangan akan dibuat dengan nama: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Simpan file ini di tempat yang aman (cloud, komputer, dll)

### 4.2 Pulihkan Data

1. Buka **Pengaturan** → **Cadangan & Data** → **Pulihkan**
2. Pilih file cadangan dari sistem file
3. Lihat informasi file:
   - Tanggal pembuatan cadangan
   - Jumlah record
   - Ukuran file
4. **Peringatan**: Pemulihan akan menimpa semua data saat ini
5. Ketuk **Pulihkan**
6. Konfirmasi pemulihan
7. Tunggu proses pemulihan selesai
8. Aplikasi akan secara otomatis memuat ulang

## 5. Ilustrasi UI (Wireframe)

### 5.1 Layar Cadangan

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Cadangkan Data             │
├─────────────────────────────────────────┤
│  Informasi Cadangan                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Jumlah Record                       │ │
│  │ 1.234 record                        │ │
│  │                                    │ │
│  │ Ukuran yang Diharapkan              │ │
│  │ ~2,5 MB                             │ │
│  │                                    │ │
│  │ Data yang akan dicadangkan:        │ │
│  │ • Pendapatan Berkala                │ │
│  │ • Pengeluaran Berkala               │ │
│  │ • Pengeluaran Harian                │ │
│  │ • Anggaran                          │ │
│  │ • Tabungan                          │ │
│  │ • Pinjaman                          │ │
│  │ • Acara Khusus                      │ │
│  │ • Kategori                          │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Cadangkan]                            │
└─────────────────────────────────────────┘
```

### 5.2 Layar Pemulihan

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Pulihkan Data              │
├─────────────────────────────────────────┤
│  Pilih File Cadangan                     │
│                                         │
│  [Pilih File...]                        │
│                                         │
│  Informasi File                         │
│  ┌───────────────────────────────────┐ │
│  │ File: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Dibuat: 11/15/2024 10:30          │ │
│  │                                    │ │
│  │ Jumlah Record: 1.234              │ │
│  │                                    │ │
│  │ Ukuran: 2,5 MB                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Peringatan                          │
│  Pemulihan akan menimpa semua data     │
│  saat ini. Apakah Anda yakin?          │
│                                         │
│  [Pulihkan] [Batal]                     │
└─────────────────────────────────────────┘
```

## 6. Logika & Aturan

### 6.1 Format File Cadangan

- File cadangan adalah format JSON
- Nama file: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Berisi semua data: pengguna, kategori, transaksi, anggaran, dll

### 6.2 Data yang Dicadangkan

- Semua tabel dalam database
- Termasuk data sistem dan data pengguna
- Tidak termasuk: pengaturan aplikasi, preferensi (bahasa, mata uang)

### 6.3 Pemulihan

- Pemulihan akan menghapus semua data saat ini
- Kemudian mengimpor data dari file cadangan
- Aplikasi akan secara otomatis memuat ulang setelah pemulihan selesai

### 6.4 Validasi

- Aplikasi memeriksa format file sebelum memulihkan
- Memeriksa kompatibilitas versi (jika ada)
- Menampilkan error jika file tidak valid

## 7. Catatan Penting

- **Cadangkan Secara Rutin**: Sebaiknya mencadangkan secara berkala (mingguan atau bulanan)
- **Simpan di Beberapa Tempat**: Simpan file cadangan di beberapa tempat (cloud, komputer, USB)
- **Pulihkan Akan Kehilangan Data Saat Ini**: Pastikan Anda telah mencadangkan data saat ini sebelum memulihkan
- **Tidak Dapat Dibatalkan**: Setelah pemulihan, tidak dapat dibatalkan

