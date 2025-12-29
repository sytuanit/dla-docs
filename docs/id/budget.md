# Anggaran

## 1. Tujuan

Modul **Anggaran** membantu Anda merencanakan dan melacak pengeluaran bulanan, memastikan Anda tidak melebihi anggaran yang ditetapkan. Modul ini secara otomatis menghitung berdasarkan:
- Pendapatan berkala Anda
- Pengeluaran berkala Anda
- Pengeluaran harian aktual

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Merencanakan pengeluaran bulanan
- Mengontrol agar tidak melebihi anggaran
- Melacak tingkat tabungan
- Melihat analisis pengeluaran berdasarkan kategori
- Membandingkan anggaran antar bulan

## 3. Layar Terkait

- Buat anggaran (pertama kali atau salin dari bulan sebelumnya)
- Lihat ringkasan anggaran
- Riwayat anggaran per bulan
- Saran salin dari bulan sebelumnya

## 4. Penggunaan Utama

### 4.1 Buat Anggaran Pertama Kali (Kasus A)

1. Buka **Fungsi** → Pilih **Anggaran**
2. Jika tidak ada anggaran, aplikasi akan secara otomatis membuka layar **Buat Anggaran**
3. Aplikasi secara otomatis menghitung dan menampilkan:
   - **Pendapatan Berkala**: Total dari semua pendapatan berkala aktif (readonly, menampilkan rincian)
   - **Pengeluaran Berkala**: Total dari semua pengeluaran berkala aktif (readonly, menampilkan rincian)
   - **Total Anggaran (sebelum tabungan)**: Dihitung otomatis = Pendapatan Berkala - Pengeluaran Berkala
4. Masukkan **Tingkat Tabungan**: % tabungan (0-100%, wajib)
5. Lihat **Jumlah Tabungan** dan **Anggaran Pengeluaran** dihitung otomatis
6. Ketuk **Simpan Anggaran**

### 4.2 Salin Anggaran dari Bulan Sebelumnya (Kasus C)

1. Buka **Fungsi** → Pilih **Anggaran**
2. Jika bulan saat ini tidak memiliki anggaran tetapi bulan sebelumnya memiliki, aplikasi akan menampilkan layar **Saran Salin Anggaran**
3. Pilih salah satu opsi:
   - **Salin seluruh anggaran bulan sebelumnya**: Aplikasi secara otomatis menyalin tingkat tabungan, menghitung ulang pendapatan/pengeluaran berkala dari data saat ini, dan membuat anggaran segera
   - **Salin & Sesuaikan**: Aplikasi menavigasi ke layar buat anggaran dengan tingkat tabungan yang sudah diisi dari bulan sebelumnya, Anda dapat menyesuaikan sebelum menyimpan
   - **Buat Anggaran Baru**: Menjalankan alur buat anggaran dari awal (Kasus A)
4. Jika memilih "Salin & Sesuaikan", sesuaikan tingkat tabungan jika perlu
5. Ketuk **Simpan Anggaran**

**Catatan**: Saat menyalin, Pendapatan Berkala dan Pengeluaran Berkala dihitung ulang dari data berkala saat ini (tidak disalin dari bulan sebelumnya), hanya tingkat tabungan yang disalin.

### 4.3 Lihat Ringkasan Anggaran (Kasus B)

1. Buka **Fungsi** → Pilih **Anggaran**
2. Jika bulan saat ini memiliki anggaran, aplikasi akan membuka layar **Ringkasan**
3. Lihat informasi:
   - **Anggaran Pengeluaran**: Batas pengeluaran yang ditetapkan
   - **Terpakai**: Jumlah yang dibelanjakan (termasuk pengeluaran harian dan varians pendapatan/pengeluaran)
   - **Tersisa**: Jumlah tersisa dalam anggaran
   - **Tingkat Penggunaan**: % anggaran yang digunakan (dengan warna peringatan)
   - **Varians Pendapatan & Pengeluaran dari Rencana**: Varians dari rencana awal
   - **Pengeluaran Harian berdasarkan Kategori**: Analisis pengeluaran detail berdasarkan kategori

### 4.4 Edit Anggaran Bulan Saat Ini

1. Pada layar **Ringkasan Anggaran**, ketuk tombol **"Edit Anggaran"**
2. Aplikasi menampilkan layar edit dengan:
   - **Pendapatan Berkala** dan **Pengeluaran Berkala**: Tetap nilai lama (readonly)
   - **Tingkat Tabungan**: Terisi dari anggaran saat ini (dapat diedit)
3. Ubah tingkat tabungan jika perlu
4. Lihat jumlah tabungan dan anggaran pengeluaran otomatis diperbarui
5. Ketuk **"Simpan Anggaran"**

**Catatan**: Saat mengedit, Pendapatan Berkala dan Pengeluaran Berkala tidak dihitung ulang (tetap snapshot lama), hanya tingkat tabungan dan anggaran pengeluaran yang diperbarui.

### 4.5 Lihat Riwayat Anggaran

1. Buka **Fungsi** → Pilih **Anggaran**
2. Pilih **Riwayat** dari menu
3. Lihat daftar anggaran untuk bulan-bulan sebelumnya
4. Ketuk pada bulan untuk melihat detail

### 4.6 Lihat Detail Pengeluaran berdasarkan Kategori

1. Buka layar **Ringkasan Anggaran**
2. Scroll ke bawah ke bagian **Analisis berdasarkan Kategori**
3. Ketuk pada kategori
4. Lihat daftar pengeluaran dalam kategori tersebut

## 5. Contoh & Ilustrasi UI

### 5.1 BUDGET-01: Buat Anggaran Pertama Kali untuk Bulan Saat Ini

**Tujuan**: Buat anggaran pertama kali agar aplikasi secara otomatis menghitung dan melacak pengeluaran bulanan berdasarkan pendapatan dan pengeluaran berkala.

**Langkah**:
1. Buka layar Fungsi, pilih "Manajemen Anggaran"
2. Aplikasi secara otomatis mendeteksi tidak ada anggaran dan menampilkan layar "Buat Anggaran"
3. Lihat info yang dihitung otomatis: Pendapatan Berkala, Pengeluaran Berkala, Total Anggaran (sebelum tabungan)
4. Masukkan tingkat tabungan: 20
5. Lihat jumlah tabungan dan anggaran pengeluaran dihitung otomatis
6. Ketuk tombol "Simpan Anggaran"

**Hasil**: Anggaran disimpan untuk bulan saat ini, secara otomatis menavigasi ke layar "Ringkasan Anggaran".

**Ilustrasi UI**:

```text
[ Card: Buat Anggaran November 2025 ]
+------------------------------------------------+
||                                                |
|| Pendapatan Berkala                Rp18.000.000|
||  • Gaji Saya (Bulanan)         Rp18.000.000|
||                                                |
|| Pengeluaran Berkala              Rp13.740.000|
||  • Listrik (Bulanan)              Rp510.000|
||  • Air (Bulanan)                  Rp255.000|
||  • SPP untuk BN (Bulanan)         Rp4.080.000|
||  • Sarapan & Kopi (Mingguan x 4)  Rp540.000|
||  • Cicilan Rumah (Bulanan)       Rp6.300.000|
||                                                |
|| (Data ini diambil secara otomatis)            |
+------------------------------------------------+

[ Card: Total Anggaran (sebelum tabungan) ]
 ------------------------------------------------
||   Rp18.000.000 (Pendapatan Berkala)           |
|| - Rp13.740.000 (Pengeluaran Berkala)           |
||-----------------------------------------------|
|| = Rp4.260.000                                   |
 ------------------------------------------------

[ Card: Tingkat Tabungan ]
 ------------------------------------------------
|| Berapa yang ingin Anda tabung?                |
||                                                |
|| Tingkat Tabungan (%)                            |
|| [  Input (wajib): 20  ]                        |
||                                                |
|| → Setara: Rp855.000                            |
 ------------------------------------------------

[ Card: Anggaran Pengeluaran ]
 ------------------------------------------------
||    Rp4.260.000 (Total Anggaran (sebelum tabungan))|
|| -  Rp855.000 (Jumlah Tabungan)                  |
||-----------------------------------------------|
|| = Rp3.405.000                                   |
||                                                |
|| (Termasuk makanan, transportasi, kopi, belanja kecil...)
 ------------------------------------------------

[ Button ]
 -------------------------------
||      Simpan Anggaran              |
 -------------------------------
```

---

### 5.2 BUDGET-02: Lihat Ringkasan Anggaran Bulan Saat Ini

**Tujuan**: Lihat situasi pengeluaran dibandingkan dengan anggaran yang ditetapkan, termasuk jumlah yang digunakan, tersisa, dan analisis berdasarkan kategori.

**Langkah**:
1. Buka layar Fungsi, pilih "Manajemen Anggaran"
2. Aplikasi secara otomatis mendeteksi anggaran ada dan menampilkan layar "Ringkasan Anggaran"
3. Lihat Card 1 - Anggaran Bulanan: Anggaran Pengeluaran, Terpakai, Tersisa, Tingkat Penggunaan
4. Lihat Card 2 - Varians Pendapatan & Pengeluaran dari Rencana
5. Lihat Card 3 - Pengeluaran Harian berdasarkan Kategori
6. (Opsional) Klik pada "Anggaran Pengeluaran ›" untuk melihat dialog detail yang menjelaskan perhitungan anggaran

**Hasil**: Menampilkan informasi lengkap anggaran bulan saat ini dengan progress ring/bar dan warna yang sesuai.

**Ilustrasi UI**:

```text
[ Card 1 – Anggaran November 2025 ]
┌──────────────────────────────────────────────┐
│ Anggaran November 2025                       │
│                                             │
│ Anggaran Pengeluaran ›      Rp3.405.000     │
│ Terpakai                  Rp525.000         │
│  • Pengeluaran harian              Rp720.000│   
│  • Varians pendapatan      -Rp2.400.000    │
│  • Varians pengeluaran       +Rp120.000    │
│ Tersisa              Rp1.560.000            │
│                                             │
│                    15,4%                    │
│   (Anda telah menggunakan 15,4% dari anggaran pengeluaran bulan ini)
│   (Anda akan segera menghabiskan anggaran pengeluaran bulan ini)
│                                             │
│                               [Lihat Riwayat]│
└──────────────────────────────────────────────┘

[ Card 2 – Varians Pendapatan & Pengeluaran dari Rencana ]
┌──────────────────────────────────────────────┐
│ Varians Pendapatan & Pengeluaran dari Rencana│
│                                              │
│ Pendapatan Berkala                           │
│  • Gaji Saya                 +Rp1.200.000   │
│    (Rp7.200.000 > Rp6.000.000)               │
│                                              │
│ Pengeluaran Berkala                          │
│  • SPP untuk BN              -Rp60.000      │
│    (Rp4.260.000 > Rp4.200.000)               │
│                                              │
│ Total Varians Pendapatan:        +Rp3.600.000│
│ Total Varians Pengeluaran:        -Rp120.000│
└──────────────────────────────────────────────┘

[ Card 3 – Pengeluaran Harian berdasarkan Kategori ]
┌──────────────────────────────────────────────┐
│ Pengeluaran Harian berdasarkan Kategori     │
│ (Makanan, transportasi, kopi, belanja kecil...)
│                                             │
│ Total Pengeluaran Harian: Rp720.000         │
│                                             │
│ Makanan              Rp360.000    50% [█████---------]│
│ Transportasi         Rp180.000    25% [███-----------]│
│ Kopi                 Rp120.000    17% [██------------]│
│ Belanja Kecil        Rp60.000     8%  [█-------------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03: Edit Anggaran Bulan Saat Ini

**Tujuan**: Menyesuaikan tingkat tabungan untuk mengubah anggaran pengeluaran bulan saat ini.

**Langkah**:
1. Pada layar "Ringkasan Anggaran", ketuk tombol "Edit Anggaran"
2. Aplikasi menampilkan layar edit (serupa dengan layar buat anggaran)
3. Lihat info saat ini: Pendapatan Berkala, Pengeluaran Berkala (tetap nilai lama)
4. Ubah tingkat tabungan menjadi 25
5. Lihat jumlah tabungan dan anggaran pengeluaran otomatis diperbarui
6. Ketuk tombol "Simpan Anggaran"

**Hasil**: Anggaran diperbarui, kembali ke layar "Ringkasan Anggaran" dengan nilai baru.

**Ilustrasi UI**: Serupa dengan BUDGET-01 (layar buat anggaran), tetapi nilai Pendapatan Berkala dan Pengeluaran Berkala readonly dan tetap dari anggaran lama.

---

### 5.4 BUDGET-04: Salin Anggaran dari Bulan Sebelumnya Saat Memulai Bulan Baru

**Tujuan**: Menggunakan kembali anggaran bulan sebelumnya untuk menghemat waktu membuat anggaran baru, dengan opsi untuk menyesuaikan jika perlu.

**Langkah**:
1. Buka layar Fungsi, pilih "Manajemen Anggaran"
2. Aplikasi secara otomatis mendeteksi bulan saat ini tidak memiliki anggaran tetapi bulan sebelumnya memiliki, menampilkan layar "Saran Salin Anggaran"
3. Pilih "Salin & Sesuaikan"
4. Aplikasi menavigasi ke layar buat anggaran dengan tingkat tabungan yang sudah diisi dari bulan sebelumnya
5. (Opsional) Sesuaikan tingkat tabungan jika perlu
6. Ketuk tombol "Simpan Anggaran"

**Hasil**: Anggaran baru dibuat untuk bulan saat ini, secara otomatis menavigasi ke layar "Ringkasan Anggaran".

**Ilustrasi UI**:

```text
[ LAYAR ]  Anggaran Desember 2025
┌──────────────────────────────────────────────┐
│ Desember 2025 tidak memiliki anggaran       │
│                                              │
│ Bagaimana Anda ingin membuat anggaran bulan baru?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Salin & Sesuaikan ›                      │
│    Petunjuk: Salin anggaran November 2025 dan sesuaikan│
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Buat Anggaran Baru ›                      │
│   Petunjuk: Jalankan alur Buat Anggaran lagi        │
│                                              │
└──────────────────────────────────────────────┘
```

Setelah memilih "Salin & Sesuaikan", layar buat anggaran akan menampilkan serupa dengan BUDGET-01, tetapi tingkat tabungan sudah terisi dari bulan sebelumnya.

## 6. Logika & Aturan

### 6.1 Kasus

- **Kasus A**: Buat anggaran pertama kali (tidak ada anggaran untuk bulan apa pun)
- **Kasus B**: Bulan saat ini memiliki anggaran → Lihat ringkasan
- **Kasus C**: Bulan saat ini tidak ada, tetapi bulan sebelumnya memiliki → Saran salin

### 6.2 Perhitungan Otomatis

- **Pendapatan Berkala**: Total dari semua `recurring_income` aktif
- **Pengeluaran Berkala**: Total dari semua `recurring_expense` aktif
- **Pengeluaran Harian**: Total dari `daily_expense` dalam bulan
- **Total Anggaran**: Pendapatan Berkala + Pendapatan Tambahan
- **Tabungan**: Total Anggaran × Tingkat Tabungan

### 6.3 Integrasi dengan Modul Lain

- Saat mengonfirmasi pendapatan berkala → Secara otomatis memperbarui anggaran
- Saat mengonfirmasi pengeluaran berkala → Secara otomatis memperbarui anggaran
- Pengeluaran harian secara otomatis dihitung ke anggaran

### 6.4 Peringatan Melebihi Anggaran

- Aplikasi akan menampilkan peringatan ketika pengeluaran melebihi anggaran
- Peringatan ditampilkan di layar Beranda dan dalam notifikasi

### 6.5 Snapshot

- Saat membuat anggaran, aplikasi membuat snapshot item pendapatan/pengeluaran untuk menyimpan status pada saat itu
- Snapshot digunakan untuk perbandingan dan analisis

## 7. Catatan Penting

- **Satu anggaran per bulan**: Anda perlu membuat anggaran untuk setiap bulan
- **Edit anggaran**: Anda dapat mengedit anggaran bulan saat ini dengan mengubah tingkat tabungan. Pendapatan Berkala dan Pengeluaran Berkala akan tetap tidak berubah (snapshot) untuk memastikan akurasi
- **Perbarui otomatis**: Anggaran secara otomatis diperbarui ketika Anda mengonfirmasi pendapatan/pengeluaran
- **Salin dari bulan sebelumnya**: Fitur salin membantu Anda menghemat waktu membuat anggaran

