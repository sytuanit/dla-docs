# Pinjaman Bank

## 1. Tujuan

Modul **Pinjaman Bank** membantu Anda mengelola pinjaman bank, termasuk:
- Melacak jumlah pinjaman, suku bunga, jangka waktu
- Mengelola jadwal pembayaran
- Menghitung bunga per periode (jika berlaku)
- Mengelola denda keterlambatan pembayaran
- Pelunasan dini (jika diperlukan)

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda memiliki:
- Pinjaman bank
- Perlu melacak jadwal pembayaran
- Ingin menghitung bunga dan denda
- Perlu pengingat saat pembayaran jatuh tempo

## 3. Layar Terkait

- Daftar pinjaman
- Tambah pinjaman baru (4 langkah)
- Edit pinjaman
- Detail pinjaman dan jadwal pembayaran
- Pelunasan dini

## 4. Penggunaan Utama

### 4.1 Tambah Pinjaman Baru (4 Langkah)

#### Langkah 1: Informasi Dasar

1. Buka **Fungsi** → Pilih **Pinjaman Bank**
2. Ketuk tombol **+** (FAB)
3. Isi informasi:
   - **Bank**: Pilih atau buat bank baru
   - **Nama Pinjaman**: (misalnya, "Pinjaman Rumah")
   - **Jumlah Pinjaman**: Jumlah pokok
   - **Tanggal Pencairan**: Tanggal uang diterima
   - **Jangka Waktu**: Jumlah tahun
   - **Jenis Bunga**: Suku bunga promosi/mengambang atau suku bunga tetap
4. Ketuk **Selanjutnya**

#### Langkah 2: Konfigurasi Suku Bunga

**Jika memilih "Suku Bunga Promosi/Mengambang":**
- Aktifkan **Memiliki Suku Bunga Promosi** (jika berlaku)
- Masukkan **Bulan Promosi** dan **Suku Bunga Promosi**
- Tambahkan periode suku bunga mengambang:
  - Pilih tahun dan rentang bulan
  - Masukkan suku bunga (%/tahun)
  - Pilih **Mengambang** atau **Tetap**

**Jika memilih "Suku Bunga Tetap":**
- Masukkan **Suku Bunga Tetap** (%/tahun)

Ketuk **Selanjutnya**

#### Langkah 3: Konfigurasi Denda

1. Aktifkan **Memiliki Denda Keterlambatan Pembayaran** (jika berlaku)
2. Tambahkan periode denda:
   - Pilih tahun dan rentang bulan
   - Masukkan **Tingkat Denda** (%/tahun)
3. Ketuk **Selanjutnya**

#### Langkah 4: Konfirmasi dan Simpan

1. Tinjau informasi:
   - Total jumlah yang harus dibayar
   - Jadwal pembayaran yang diharapkan
2. Ketuk **Simpan**

### 4.2 Lihat Detail Pinjaman

1. Buka daftar pinjaman
2. Ketuk pada pinjaman
3. Lihat informasi:
   - Informasi dasar
   - Jadwal pembayaran
   - Jumlah dibayar / Tersisa
   - Suku bunga dan denda

### 4.3 Tandai Periode Pembayaran sebagai Dibayar

1. Buka detail pinjaman
2. Temukan periode pembayaran jatuh tempo (badge "Belum Dibayar")
3. Ketuk **Tandai sebagai Dibayar**
4. Isi informasi:
   - **Tanggal Pembayaran Aktual**: Tanggal dibayar (default = hari ini)
   - **Bunga Aktual Dibayar**: Bunga aktual yang dibayar (default = bunga yang direncanakan)
   - **Catatan**: (opsional)
5. Lihat **Total Pembayaran Aktual** dihitung secara otomatis (pokok + bunga aktual)
6. Ketuk **Konfirmasi**

### 4.4 Perbarui Suku Bunga Saat Ini

1. Buka detail pinjaman (hanya ditampilkan jika saat ini dalam periode suku bunga mengambang)
2. Ketuk **Perbarui Suku Bunga Saat Ini**
3. Isi informasi:
   - **Suku Bunga Baru**: Suku bunga baru (%/tahun)
   - **Tanggal Efektif**: Tanggal mulai menerapkan suku bunga baru (default = awal periode saat ini)
   - **Catatan**: (opsional)
4. Ketuk **Simpan**
5. Periode yang belum dibayar dari periode saat ini seterusnya akan diperbarui dengan suku bunga baru

### 4.5 Pelunasan Dini

1. Buka detail pinjaman
2. Ketuk **Hitung Jumlah Pelunasan**
3. **Langkah 1 - Masukkan Informasi Pelunasan Dini:**
   - Pilih metode: **Pembayaran Sebagian** atau **Pelunasan Penuh**
   - Pilih tanggal pelunasan dini (default = hari ini)
   - Masukkan jumlah pelunasan dini (jika sebagian)
   - Lihat **Denda Pelunasan Dini** dihitung secara otomatis
4. Ketuk **Selanjutnya**
5. **Langkah 2 - Bandingkan Opsi:**
   - Lihat perbandingan antara "Tidak Ada Pelunasan Dini" dan "Pelunasan Dini"
   - Lihat hasil: Penghematan bunga, pengurangan waktu
6. Ketuk **Konfirmasi Pelunasan Dini**

### 4.6 Edit Pinjaman

1. Buka detail pinjaman
2. Ketuk **Edit** (hanya edit nama, catatan, bank)
3. Edit informasi yang dapat diedit:
   - **Nama Pinjaman**: Dapat diedit
   - **Bank**: Dapat diubah
   - **Catatan**: Dapat diedit
   - **Jumlah Pinjaman, Tanggal Pencairan, Jangka Waktu, Suku Bunga**: Hanya dapat diedit jika belum ada pembayaran
4. Ketuk **Simpan**

## 5. Contoh & Ilustrasi UI

### LOAN-01: Buat Pinjaman Baru (Pinjaman Rumah dengan Suku Bunga Promosi)

**Tujuan**: Buat pinjaman baru untuk melacak pinjaman rumah, suku bunga promosi, dan jadwal pembayaran bulanan.

**Langkah**:
1. Buka **Fungsi** → Pilih **Pinjaman Bank**
2. Ketuk tombol **+** (FAB) untuk menambah pinjaman baru
3. **Langkah 1 - Informasi Dasar:**
   - Pilih bank: Bank of America
   - Masukkan nama: "Pinjaman Rumah - Apartemen Downtown"
   - Masukkan jumlah pinjaman: Rp3.000.000.000
   - Pilih tanggal pencairan: 04/01/2023
   - Masukkan jangka waktu: 10 tahun (dihitung otomatis = 120 periode)
   - Pilih waktu notifikasi: 10:00 dan 19:00
   - Pilih jenis bunga: "Saldo Menurun"
   - Ketuk **Selanjutnya**
4. **Langkah 2 - Konfigurasi Suku Bunga:**
   - Aktifkan "Memiliki Periode Suku Bunga Promosi"
   - Masukkan: 6 bulan pertama @ 6,0%/tahun
   - Tambahkan periode selanjutnya:
     - Tahun 1 (bulan 7-12): 9,0%/tahun, mengambang
     - Tahun 2 (bulan 13-24): 9,5%/tahun, mengambang
     - Tahun 3 seterusnya: 10,0%/tahun, mengambang
   - Ketuk **Selanjutnya**
5. **Langkah 3 - Konfigurasi Denda Pelunasan Dini:**
   - Aktifkan "Terapkan Denda Pelunasan Dini"
   - Masukkan denda: Tahun 1-3: 2,0%, Tahun 4-5: 1,5%, Tahun 6+: 1,0%
   - Ketuk **Selanjutnya**
6. **Langkah 4 - Konfirmasi:**
   - Tinjau informasi ringkasan
   - Ketuk **Buat Pinjaman**

**Hasil**: Pinjaman berhasil dibuat, jadwal pembayaran 120 periode dibuat secara otomatis, notifikasi dijadwalkan.

**Wireframe - Langkah 1: Informasi Dasar**

```text
┌─────────────────────────────────────────┐
│ <  Tambah Pinjaman                      │
├─────────────────────────────────────────┤
│ Nama Pinjaman *                          │
│ [Pinjaman Rumah - Apartemen Downtown]  │
│                                          │
│ Bank *                                    │
│ [Bank of America ▼] [+ Buat Baru]        │
│                                          │
│ Jumlah Pinjaman *                        │
│ [Rp3.000.000.000]                        │
│                                          │
│ Tanggal Pencairan *                      │
│ [04/01/2023] [📅]                        │
│                                          │
│ Jangka Waktu (tahun) *                    │
│ [10] tahun                               │
│ Petunjuk: Aplikasi menghitung otomatis = 120 periode │
│                                          │
│ Waktu Notifikasi 1 *                    │
│ [10:00] [🕐]                             │
│                                          │
│ Waktu Notifikasi 2 *                    │
│ [19:00] [🕐]                             │
│                                          │
│ Jenis Bunga *                            │
│ ● Saldo Menurun                          │
│ ○ Suku Bunga Tetap untuk Seluruh Jangka Waktu│
│                                          │
│ [SELANJUTNYA] [BATAL]                    │
└─────────────────────────────────────────┘
```

---

### LOAN-02: Lihat Daftar Pinjaman dan Detail

**Tujuan**: Lihat ringkasan pinjaman, filter berdasarkan status, pencarian, dan detail setiap pinjaman.

**Langkah**:
1. Buka **Fungsi** → Pilih **Pinjaman Bank**
2. Lihat layar daftar dengan filter "Aktif" (default) dan "Selesai"
3. Beralih antar filter untuk melihat ringkasan yang berbeda
4. Gunakan bilah pencarian: Masukkan "Downtown"
5. Ketuk pada pinjaman untuk melihat detail
6. Lihat jadwal pembayaran dengan periode yang sudah dibayar, periode saat ini, dan periode masa depan
7. Gunakan bilah pencarian dalam jadwal pembayaran: Masukkan "9/2024"

**Hasil**: Daftar menampilkan dengan benar berdasarkan filter, detail pinjaman menampilkan informasi lengkap dan jadwal pembayaran.

**Wireframe - Daftar Pinjaman**

```text
┌─────────────────────────────────────────┐
│ <  Manajemen Pinjaman Bank              │
├─────────────────────────────────────────┤
│ [Aktif] [Selesai]                       │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Saldo Saat Ini: Rp2.467.500.000    │  │
│ │ Total Pinjaman Asli: Rp3.000.000.000│ │
│ │ Bunga Dibayar: Rp25.800.000        │  │
│ │ Aktif: 1 pinjaman                   │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Cari (nama pinjaman, bank)]         │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Bank of America  [Aktif]     │  │
│ │ Pinjaman Rumah - Apartemen Downtown│  │
│ │ Saldo: Rp2.467.500.000              │  │
│ │ Asli: Rp3.000.000.000               │  │
│ │ Progress: 8 / 120 periode          │  │
│ │ Tanggal Berakhir: 04/01/2033       │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Detail Pinjaman**

```text
┌─────────────────────────────────────────┐
│ <  Detail Pinjaman                      │
├─────────────────────────────────────────┤
│ [ICON] Bank of America          [Edit]  │
│ Pinjaman Rumah - Apartemen Downtown     │
│ [Aktif]                                 │
│                                          │
│ Pinjaman Asli: Rp3.000.000.000         │
│ Saldo Saat Ini: Rp2.467.500.000        │
│ Periode Dibayar: 8 / 120                │
│ Bunga Dibayar: Rp25.800.000            │
│ Suku Bunga Saat Ini: 9,0%/tahun        │
│                                          │
│ [Perbarui Bunga] [Hitung Pelunasan]    │
│                                          │
│ Jadwal Pembayaran                       │
│ [🔍 Cari periode (misalnya, "5/2025")] │
│                                          │
│ Periode 1 – 05/2023 [Dibayar]           │
│ Total: Rp32,25jt • Pokok: Rp15jt • Bunga: Rp17,25jt│
│                                          │
│ Periode 9 – 01/2024 [Belum Dibayar]     │
│ Pokok: Rp15.000.000                     │
│ Bunga: Rp17.250.000                     │
│ Total: Rp32.250.000                     │
│ Tanggal Jatuh Tempo: 01/15/2024         │
│ [Tandai sebagai Dibayar]                 │
│                                          │
│ Periode 10 – 02/2024 [Belum Jatuh Tempo]│
│ Total: Rp32,25jt • Pokok: Rp15jt • Bunga: Rp17,25jt│
└─────────────────────────────────────────┘
```

---

### LOAN-03: Tandai Periode Pembayaran sebagai Dibayar (Catat Pembayaran)

**Tujuan**: Tandai periode pembayaran sebagai "Dibayar" setelah melakukan pembayaran ke bank.

**Langkah**:
1. Buka detail pinjaman
2. Temukan periode saat ini (Periode 9) dengan badge "Belum Dibayar"
3. Ketuk **Tandai sebagai Dibayar**
4. Isi informasi:
   - Tanggal pembayaran aktual: 01/15/2024 (default = hari ini)
   - Bunga aktual dibayar: Rp17.250.000 (default = bunga yang direncanakan)
   - Catatan: (opsional)
5. Lihat total pembayaran aktual dihitung secara otomatis
6. Ketuk **Konfirmasi**

**Hasil**: Periode 9 diperbarui menjadi "Dibayar", saldo menurun, periode yang dibayar meningkat, saldo saat ini menurun.

**Wireframe - Dialog Tandai sebagai Dibayar**

```text
┌─────────────────────────────────────────┐
│ Tandai sebagai Dibayar                   │
├─────────────────────────────────────────┤
│ Periode 9 – 01/2024          [Belum Dibayar] │
│                                          │
│ Tanggal Jatuh Tempo (direncanakan): 01/15/2024│
│ Pokok (tetap): Rp15.000.000              │
│                                          │
│ Tanggal Pembayaran Aktual *              │
│ [01/15/2024] [📅]                        │
│                                          │
│ Bunga Aktual Dibayar *                   │
│ [Rp17.250.000]                           │
│ Petunjuk: Bunga yang direncanakan: Rp17.250.000│
│                                          │
│ Total Pembayaran Aktual =                │
│   Rp15.000.000 (Pokok)                  │
│ + Rp17.250.000 (Bunga Aktual)           │
│ ────────────────────────────────        │
│ = Rp32.250.000                           │
│                                          │
│ Catatan (opsional)                       │
│ [Dibayar Rp50.000 lebih rendah, mendapat pengurangan bunga...]│
│                                          │
│ [BATAL] [KONFIRMASI]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Perbarui Suku Bunga Saat Ini (Saat Bank Menyesuaikan Suku Bunga Mengambang)

**Tujuan**: Perbarui suku bunga baru saat bank mengumumkan penyesuaian suku bunga mengambang.

**Langkah**:
1. Buka detail pinjaman
2. Lihat "Suku Bunga Saat Ini: 9,0%/tahun"
3. Ketuk **Perbarui Suku Bunga Saat Ini** (hanya ditampilkan jika saat ini dalam periode suku bunga mengambang)
4. Isi informasi:
   - Suku bunga baru: 10,5%/tahun
   - Tanggal efektif: 01/15/2024 (default = awal periode saat ini)
   - Catatan: "Bank menyesuaikan suku bunga sesuai keputusan baru"
5. Ketuk **Simpan**

**Hasil**: Suku bunga saat ini diperbarui, periode yang belum dibayar dari periode saat ini seterusnya diperbarui dengan suku bunga baru.

**Wireframe - Dialog Perbarui Suku Bunga**

```text
┌─────────────────────────────────────────┐
│ Perbarui Suku Bunga Saat Ini            │
├─────────────────────────────────────────┤
│ [ICON] Bank of America                   │
│ Nama Pinjaman: Pinjaman Rumah - Apartemen Downtown│
│ Periode Saat Ini: Periode 9 – 01/2024   │
│ Status: [Aktif]                         │
│ Periode: Mengambang (setelah promosi)   │
│                                          │
│ Suku Bunga Saat Ini (yang berlaku):     │
│ [9,0] %/tahun (readonly)                 │
│                                          │
│ Suku Bunga Baru (%/tahun) *              │
│ [10,5] %/tahun                           │
│                                          │
│ Tanggal Efektif *                        │
│ [01/15/2024] [📅]                        │
│                                          │
│ Catatan (opsional)                       │
│ [Bank menyesuaikan suku bunga...]       │
│                                          │
│ • Suku bunga baru akan diterapkan ke    │
│   periode dari Periode Saat Ini seterusnya. │
│ • Periode yang sudah dibayar tidak berubah. │
│                                          │
│ [BATAL] [SIMPAN]                         │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Pelunasan Dini (Pembayaran Sebagian untuk Mengurangi Bunga)

**Tujuan**: Melunasi sebagian pinjaman lebih awal untuk mengurangi total bunga yang harus dibayar dan memperpendek jangka waktu pinjaman.

**Langkah**:
1. Buka detail pinjaman
2. Ketuk **Hitung Jumlah Pelunasan**
3. **Langkah 1 - Masukkan Informasi Pelunasan Dini:**
   - Pilih metode: "Pembayaran Sebagian"
   - Pilih tanggal pelunasan dini: 01/15/2024
   - Masukkan jumlah pelunasan dini: Rp1.200.000.000
   - Lihat denda dihitung secara otomatis: Rp24.000.000 (2,0%)
   - Ketuk **Selanjutnya**
4. **Langkah 2 - Bandingkan Opsi:**
   - Lihat perbandingan antara "Tidak Ada Pelunasan Dini" dan "Pelunasan Dini Rp1.200.000.000"
   - Lihat hasil: Hemat Rp450.000.000 bunga, kurangi 40 periode
   - Ketuk **Konfirmasi Pelunasan Dini**

**Hasil**: Saldo menurun, jadwal pembayaran dihitung ulang, jumlah periode menurun, tanggal berakhir lebih awal.

**Wireframe - Langkah 1: Masukkan Informasi Pelunasan Dini**

```text
┌─────────────────────────────────────────┐
│ <  Pelunasan Dini                       │
├─────────────────────────────────────────┤
│ [ICON] Bank of America                   │
│ Nama Pinjaman: Pinjaman Rumah - Apartemen Downtown│
│ Saldo Saat Ini: Rp3.000.000.000        │
│ Periode Saat Ini: Periode 9 – 01/2024   │
│                                          │
│ Bagaimana Anda ingin melunasi?          │
│ ● Pembayaran Sebagian                   │
│ ○ Pelunasan Penuh                       │
│                                          │
│ Tanggal Pelunasan Dini *                 │
│ [01/15/2024] [📅]                        │
│                                          │
│ Jumlah Pelunasan Dini *                  │
│ [Rp1.200.000.000]                       │
│                                          │
│ Tingkat Denda yang Diterapkan: 2,0%     │
│ Denda: Rp24.000.000                     │
│                                          │
│ [SELANJUTNYA]                            │
└─────────────────────────────────────────┘
```

**Wireframe - Langkah 2: Bandingkan Opsi**

```text
┌─────────────────────────────────────────┐
│ <  Bandingkan Opsi                      │
├─────────────────────────────────────────┤
│ OPSI A: Tidak Ada Pelunasan Dini        │
│ ────────────────────────────────────────│
│ Total Bunga Dibayar hingga Saat Ini:     │
│   Rp780.000.000                        │
│ Total Bunga Tersisa: Rp780.000.000      │
│ Periode Tersisa: 112 periode            │
│ Tanggal Berakhir: 04/01/2033            │
│                                          │
│ OPSI B: Pelunasan Dini Rp1.200.000.000  │
│ ────────────────────────────────────────│
│ Denda Pelunasan Dini: Rp24.000.000     │
│ Total Bunga Dibayar hingga Saat Ini:     │
│   Rp804.000.000                        │
│ Total Bunga Tersisa: Rp330.000.000      │
│ Periode Tersisa: 72 periode             │
│ Tanggal Berakhir: 04/01/2029            │
│                                          │
│ HASIL PERBANDINGAN:                     │
│ • Penghematan Bunga: Rp450.000.000     │
│ • Pengurangan Waktu: 40 periode (~3,5 tahun)│
│                                          │
│ [KONFIRMASI PELUNASAN DINI]             │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Edit Pinjaman (Edit Informasi Dasar)

**Tujuan**: Edit informasi dasar pinjaman (nama, bank, catatan) setelah memulai pembayaran.

**Langkah**:
1. Buka detail pinjaman
2. Ketuk **Edit** (hanya edit nama, catatan, bank)
3. Edit:
   - Nama Pinjaman: "Pinjaman Rumah - Apartemen Downtown - Unit A1-1201"
   - (Opsional) Ubah bank: Chase Bank
   - Catatan: "Dipindahkan ke bank baru"
4. Lihat field yang dinonaktifkan: Jumlah Pinjaman, Tanggal Pencairan, Jangka Waktu, Suku Bunga
5. Ketuk **Simpan**

**Hasil**: Informasi dasar diperbarui, informasi lain tidak berubah.

**Catatan**: Jika pinjaman belum ada pembayaran, dapat mengedit semua informasi (jumlah, jangka waktu, konfigurasi suku bunga).

## 6. Logika & Aturan

### 6.1 Suku Bunga Promosi/Mengambang

- Dapat memiliki periode promosi (suku bunga lebih rendah)
- Setelah periode promosi, suku bunga mengambang per periode
- Setiap periode dapat **Mengambang** (berbasis pasar) atau **Tetap**

### 6.2 Denda Keterlambatan Pembayaran

- Denda dihitung berdasarkan %/tahun
- Dapat dikonfigurasi berbeda untuk setiap periode
- Denda hanya berlaku ketika pembayaran terlambat

### 6.3 Jadwal Pembayaran

- Aplikasi secara otomatis membuat jadwal pembayaran berdasarkan:
  - Jumlah pinjaman
  - Suku bunga
  - Jangka waktu
- Setiap periode pembayaran mencakup: Pokok + Bunga

### 6.4 Pelunasan Dini

- Hitung jumlah tersisa (pokok + bunga + denda jika ada)
- Setelah pelunasan, pinjaman akan berubah ke status "Selesai"

### 6.5 Notifikasi

- Aplikasi mengirim notifikasi pengingat saat pembayaran jatuh tempo
- Waktu notifikasi dapat dikonfigurasi untuk setiap pinjaman (`notificationTime1`, `notificationTime2`, default 10:00 dan 19:00)

## 7. Catatan Penting

- **Suku Bunga Kompleks**: Modul ini mendukung suku bunga yang berubah per periode, memerlukan konfigurasi yang cermat
- **Tidak dapat dihapus saat jadwal pembayaran ada**: Jika jadwal pembayaran ada, Anda hanya dapat melunasi, tidak dapat menghapus
- **Pelunasan Dini**: Mungkin memerlukan biaya denda tambahan, tergantung kebijakan bank
- **Jadwal Pembayaran**: Jadwal pembayaran dihitung secara otomatis, Anda tidak dapat mengedit secara langsung

