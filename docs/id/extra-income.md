# Pendapatan Tambahan

## 1. Tujuan

Modul **Pendapatan Tambahan** membantu Anda mencatat pendapatan non-rutin tanpa siklus tetap seperti:
- Penjualan Online
- Freelance
- Bonus
- Hadiah Uang Tunai
- Pendapatan tidak teratur lainnya

Berbeda dengan **Pendapatan Berkala**, pendapatan tambahan tidak memiliki siklus otomatis, Anda harus memasukkan secara manual setiap kali.

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Mencatat pendapatan acak, non-rutin
- Melacak total pendapatan dalam periode waktu
- Menganalisis tren pendapatan tambahan
- Menghitung ke anggaran bulanan

## 3. Layar Terkait

- Daftar pendapatan tambahan
- Tambah pendapatan baru
- Edit pendapatan

## 4. Penggunaan Utama

### 4.1 Tambah Pendapatan Tambahan

1. Buka **Fungsi** → Pilih **Pendapatan Tambahan**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Isi informasi:
   - **Kategori**: Pilih atau buat kategori baru
   - **Jumlah**: Masukkan jumlah yang diterima
   - **Tanggal**: Pilih tanggal uang diterima (default adalah hari ini)
   - **Catatan**: Deskripsi detail (opsional)
4. Ketuk **Simpan**

### 4.2 Lihat Daftar Pendapatan

1. Buka **Fungsi** → Pilih **Pendapatan Tambahan**
2. Daftar ditampilkan sesuai tata letak yang dikonfigurasi (1, 2, 3, atau 4 kolom)
3. Gunakan **Pencarian** untuk memfilter berdasarkan kategori atau catatan
4. Pilih **Filter Waktu**: Hari Ini / Minggu Ini / Bulan Ini / Bulan Lalu / Kustom

### 4.3 Edit Pendapatan

1. Buka daftar pendapatan tambahan
2. Tekan lama pada item untuk mengedit
3. Pilih **Edit** dari menu
4. Perbarui informasi
5. Ketuk **Simpan**

### 4.4 Hapus Pendapatan

1. Buka daftar pendapatan tambahan
2. Tekan lama pada item untuk menghapus
3. Pilih **Hapus** dari menu
4. Konfirmasi penghapusan

## 5. Ilustrasi UI (Wireframe)

### 5.1 Layar Daftar

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Pendapatan Tambahan        │
├─────────────────────────────────────────┤
│  [🔍 Cari...]                           │
│  [Bulan Ini ▼] [Minggu Ini] [Hari Ini] │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Penjualan Online                    │ │
│  │ Rp300.000                           │ │
│  │ 11/15/2024                          │ │
│  │                                    │ │
│  │ [Edit] [Hapus]                      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                           │ │
│  │ Rp600.000                           │ │
│  │ 11/14/2024                          │ │
│  │                                    │ │
│  │ [Edit] [Hapus]                      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Total: Rp900.000                       │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Layar Tambah/Edit

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Tambah Pendapatan Tambahan │
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Penjualan Online ▼]                    │
│                                         │
│  Jumlah *                                │
│  [Rp300.000]                             │
│                                         │
│  Tanggal *                               │
│  [11/15/2024]                            │
│                                         │
│  Catatan                                 │
│  [Menjual Produk A]                     │
│                                         │
│  [Simpan] [Batal]                        │
└─────────────────────────────────────────┘
```

## 6. Logika & Aturan

### 6.1 Tata Letak Tampilan

- Anda dapat mengonfigurasi jumlah kolom: 1, 2, 3, atau 4 kolom
- Tata letak disimpan dalam pengaturan dan berlaku untuk semua daftar pendapatan tambahan

### 6.2 Filter Waktu

- **Hari Ini**: Hanya menampilkan pendapatan dari hari ini
- **Minggu Ini**: Dari awal minggu hingga hari ini
- **Bulan Ini**: Dari awal bulan hingga hari ini
- **Bulan Lalu**: Seluruh bulan sebelumnya
- **Kustom**: Pilih rentang waktu kustom

### 6.3 Pencarian

- Pencarian dalam **nama kategori** dan **catatan**
- Tidak peka huruf besar/kecil
- Pencarian real-time saat mengetik

### 6.4 Integrasi Anggaran

- Pendapatan tambahan dihitung ke "Pendapatan Tambahan" dalam anggaran
- Membantu Anda melacak total pendapatan bulanan

## 7. Catatan Penting

- **Tidak Ada Siklus**: Pendapatan tambahan tidak memiliki siklus otomatis, Anda harus memasukkan secara manual setiap kali
- **Bisa Dihapus**: Anda dapat menghapus pendapatan apa pun
- **Integrasi Anggaran**: Pendapatan tambahan secara otomatis dihitung ke anggaran bulan saat ini

