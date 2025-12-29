# Pengeluaran Harian

## 1. Tujuan

Modul **Pengeluaran Harian** membantu Anda mencatat pengeluaran rutin, non-tetap seperti:
- Makan & Minum
- Belanja
- Transportasi
- Hiburan
- Pengeluaran fleksibel lainnya

Berbeda dengan **Pengeluaran Berkala**, pengeluaran harian sering bervariasi dalam jumlah dan frekuensi, tanpa siklus tetap.

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Mencatat pengeluaran acak, non-rutin
- Melacak pengeluaran harian untuk mengontrol anggaran
- Menganalisis tren pengeluaran berdasarkan kategori
- Melihat total pengeluaran dalam periode waktu

## 3. Layar Terkait

- Daftar pengeluaran harian
- Tambah pengeluaran baru
- Edit pengeluaran

## 4. Penggunaan Utama

### 4.1 Tambah Pengeluaran Harian

1. Buka **Fungsi** → Pilih **Pengeluaran Harian**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Isi informasi:
   - **Kategori**: Pilih kategori (atau gunakan kategori default jika dikonfigurasi)
   - **Jumlah**: Masukkan jumlah yang dibelanjakan
   - **Tanggal**: Pilih tanggal pengeluaran (default adalah hari ini)
   - **Catatan**: Deskripsi detail (opsional)
4. Ketuk **Simpan**

### 4.2 Lihat Daftar Pengeluaran

1. Buka **Fungsi** → Pilih **Pengeluaran Harian**
2. Daftar ditampilkan sesuai tata letak yang dikonfigurasi (2, 3, atau 4 kolom)
3. Gunakan **Pencarian** untuk memfilter berdasarkan kategori atau catatan
4. Pilih **Filter Waktu**: Hari Ini / Minggu Ini / Bulan Ini / Bulan Lalu / Kustom

### 4.3 Edit Pengeluaran

1. Buka daftar pengeluaran harian
2. Tekan lama pada item untuk mengedit
3. Pilih **Edit** dari menu
4. Perbarui informasi
5. Ketuk **Simpan**

### 4.4 Hapus Pengeluaran

1. Buka daftar pengeluaran harian
2. Tekan lama pada item untuk menghapus
3. Pilih **Hapus** dari menu
4. Konfirmasi penghapusan

### 4.5 Atur Kategori Default

1. Buka **Pengaturan** → **Kategori** → **Kategori Pengeluaran Harian**
2. Ketuk pada kategori yang ingin Anda set sebagai default
3. Pilih **Set sebagai Default**
4. Saat menambah pengeluaran baru, kategori ini akan otomatis dipilih

## 5. Ilustrasi UI (Wireframe)

### 5.1 Layar Daftar

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Pengeluaran Harian        │
├─────────────────────────────────────────┤
│  [🔍 Cari...]                           │
│  [Hari Ini ▼] [Minggu Ini] [Bulan Ini] │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Makan│ │ Belan│ │ Taksi│            │
│  │      │ │ ja   │ │      │            │
│  │      │ │      │ │      │            │
│  │ Rp30k│ │Rp120k│ │Rp15k│            │
│  │      │ │      │ │      │            │
│  │ 11/15│ │ 11/15│ │ 11/14│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Kopi │ │ Lain │ │      │            │
│  │      │ │      │ │      │            │
│  │      │ │      │ │      │            │
│  │Rp15k│ │Rp60k│ │      │            │
│  │      │ │      │ │      │            │
│  │ 11/13│ │ 11/12│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Total: Rp240.000                      │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Layar Tambah/Edit

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Tambah Pengeluaran Harian│
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Makan Keluar ▼]                        │
│                                         │
│  Jumlah *                                │
│  [Rp30.000]                              │
│                                         │
│  Tanggal *                               │
│  [11/15/2024]                            │
│                                         │
│  Catatan                                 │
│  [Makan siang dengan teman]             │
│                                         │
│  [Simpan] [Batal]                        │
└─────────────────────────────────────────┘
```

### 5.3 Menu (Tekan Lama)

```text
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐ │
│  │ Makan Keluar                         │ │
│  │ Rp30.000                             │ │
│  │ 11/15/2024                            │ │
│  │                                       │ │
│  │ [Edit] [Hapus]                        │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Logika & Aturan

### 6.1 Tata Letak Tampilan

- Anda dapat mengonfigurasi jumlah kolom: 2, 3, atau 4 kolom
- Tata letak disimpan dalam pengaturan dan berlaku untuk semua daftar pengeluaran

### 6.2 Filter Waktu

- **Hari Ini**: Hanya menampilkan pengeluaran dari hari ini
- **Minggu Ini**: Dari awal minggu hingga hari ini
- **Bulan Ini**: Dari awal bulan hingga hari ini
- **Bulan Lalu**: Seluruh bulan sebelumnya
- **Kustom**: Pilih rentang waktu kustom

### 6.3 Pencarian

- Pencarian dalam **nama kategori** dan **catatan**
- Tidak peka huruf besar/kecil
- Pencarian real-time saat mengetik

### 6.4 Kategori Default

- Jika Anda telah mengatur kategori default, saat membuka layar tambah, kategori tersebut akan otomatis dipilih
- Catatan juga dapat diisi otomatis berdasarkan kategori (jika dikonfigurasi)

### 6.5 Total Pengeluaran

- Total pengeluaran dihitung berdasarkan filter waktu yang dipilih saat ini
- Ditampilkan di bagian bawah daftar

## 7. Catatan Penting

- **Tidak Ada Siklus**: Pengeluaran harian tidak memiliki siklus otomatis, Anda harus memasukkan secara manual setiap kali
- **Bisa Dihapus**: Anda dapat menghapus pengeluaran apa pun (tidak seperti pengeluaran berkala)
- **Tidak Ada Integrasi Anggaran**: Pengeluaran harian tidak secara otomatis dihitung ke anggaran (Anda harus melacak sendiri)
- **Kategori Kustom**: Anda dapat membuat kategori baru di Pengaturan

