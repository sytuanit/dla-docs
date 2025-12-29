# Pendapatan Berkala

## 1. Tujuan

Modul **Pendapatan Berkala** membantu Anda mengelola sumber pendapatan rutin seperti:
- Gaji bulanan
- Pendapatan sewa
- Pensiun
- Dividen investasi
- Pendapatan berkala lainnya

Modul ini secara otomatis membuat **kejadian** berdasarkan siklus yang Anda konfigurasi, dan mengingatkan Anda saat waktunya menerima pembayaran.

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda memiliki:
- Pendapatan tetap dengan jadwal (mingguan, dua mingguan, atau bulanan)
- Perlu melacak dan mengonfirmasi kapan pembayaran diterima
- Ingin perhitungan otomatis ke anggaran bulanan

## 3. Layar Terkait

- Daftar pendapatan berkala
- Tambah pendapatan berkala baru
- Edit pendapatan berkala
- Riwayat kejadian

## 4. Penggunaan Utama

### 4.1 Tambah Pendapatan Berkala Baru

1. Buka **Fungsi** → Pilih **Pendapatan Berkala**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Isi informasi:
   - **Kategori**: Pilih atau buat kategori baru
   - **Jumlah**: Masukkan jumlah pendapatan (bisa dikosongkan, masukkan saat mengonfirmasi)
   - **Siklus**: Pilih Mingguan / Dua Mingguan / Bulanan
   - **Tanggal**: Pilih tanggal dalam siklus (misalnya, tanggal 15 setiap bulan)
   - **Tanggal Mulai**: (Hanya untuk siklus dua mingguan) Pilih tanggal mulai
   - **Catatan**: Informasi tambahan (opsional)
4. Ketuk **Simpan**

### 4.2 Konfirmasi Pembayaran Diterima

1. Buka daftar pendapatan berkala
2. Temukan item dengan badge **"Menunggu Konfirmasi"** (kuning)
3. Ketuk item untuk membuka dialog konfirmasi
4. Isi:
   - **Jumlah Aktual**: (jika berbeda dari yang diharapkan)
   - **Catatan**: (opsional)
5. Ketuk **Konfirmasi**

### 4.3 Edit Pendapatan Berkala

1. Buka daftar pendapatan berkala
2. Ketuk item yang ingin diedit
3. Pilih **Edit** dari menu
4. Perbarui informasi
5. Ketuk **Simpan**

### 4.4 Lihat Riwayat

1. Buka daftar pendapatan berkala
2. Ketuk item
3. Pilih **Riwayat** untuk melihat semua kejadian masa lalu

### 4.5 Nonaktifkan/Aktifkan Pendapatan

1. Buka daftar pendapatan berkala
2. Temukan item yang ingin dinonaktifkan/diaktifkan
3. Toggle switch **Aktif** di sisi kanan item

## 5. Contoh & Ilustrasi UI

### 5.1 Contoh 1: Buat Pendapatan Berkala Bulanan (Gaji)

**Skenario**: Anda ingin melacak gaji bulanan agar aplikasi secara otomatis mengingatkan Anda saat waktunya menerima pembayaran.

**Langkah**:
1. Buka layar Fungsi, pilih "Pendapatan Berkala"
2. Ketuk tombol "➕ Tambah Baru" di kanan bawah
3. Pilih kategori "Gaji" (atau buat baru jika tidak tersedia)
4. Masukkan jumlah: Rp60.000.000
5. Pilih siklus "Bulanan"
6. Pilih "Pilih hari dalam bulan", masukkan 5
7. Catatan otomatis terisi "Gaji bulanan" (dapat diedit)
8. Ketuk "Simpan"

**Hasil**: Aplikasi menampilkan pesan sukses dan kembali ke daftar. Item baru muncul dengan informasi lengkap, dan aplikasi akan secara otomatis mengingatkan Anda pada tanggal 5 setiap bulan.

**Layar Tambah Pendapatan Berkala**:

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Tambah Pendapatan Berkala │
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Gaji ▼] [+ Tambah Baru]               │
│                                         │
│  Jumlah (IDR) *                          │
│  [Rp60.000.000]                          │
│                                         │
│  Siklus *                                │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Minggu│ │Dua Ming│ │Bulan  │        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Tanggal Pembayaran dalam Siklus        │
│  ⚪ Akhir bulan                          │
│  ⚫ Pilih hari dalam bulan              │
│  ┌───────────────────────────────────┐ │
│  │ Hari dalam bulan: [5]             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Catatan                                 │
│  ┌───────────────────────────────────┐ │
│  │ Gaji bulanan                        │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Batal]                  [Simpan]     │
└─────────────────────────────────────────┘
```

---

### 5.2 Contoh 2: Konfirmasi Pendapatan Jatuh Tempo dan Perbarui Jumlah Aktual

**Skenario**: Hari gajian (tanggal 5), tetapi jumlah aktual yang diterima adalah Rp63.000.000 (kenaikan gaji) bukan Rp60.000.000 yang ditetapkan.

**Langkah**:
1. Buka aplikasi atau buka layar "Pendapatan Berkala"
2. Aplikasi secara otomatis mendeteksi kejadian jatuh tempo dan menampilkan dialog konfirmasi
3. Dialog menampilkan jumlah default: Rp60.000.000
4. Perbarui jumlah aktual menjadi Rp63.000.000
5. Masukkan catatan: "Bulan ini ada bonus" (opsional)
6. Ketuk "Konfirmasi Diterima"

**Hasil**: Aplikasi memperbarui kejadian yang dikonfirmasi dengan jumlah aktual Rp63.000.000, secara otomatis membuat kejadian berikutnya, dan memperbarui saldo keuangan saat ini.

**Dialog Konfirmasi Pendapatan**:

```text
┌─────────────────────────────────────────┐
│  Konfirmasi Diterima                     │
├─────────────────────────────────────────┤
│  Gaji                                    │
│  Bulanan (tanggal 5)                     │
│  Tanggal Jatuh Tempo: Hari Ini          │
│                                         │
│  Jumlah Aktual *                         │
│  [Rp63.000.000]                          │
│                                         │
│  Catatan                                 │
│  [Bulan ini ada bonus]                  │
│                                         │
│  [Batalkan Ini]    [Konfirmasi Diterima]│
└─────────────────────────────────────────┘
```

---

### 5.3 Contoh 3: Batalkan Kejadian Pendapatan Saat Pembayaran Tidak Diterima

**Skenario**: Hari pembayaran sewa (tanggal 1), tetapi penyewa belum mentransfer uang sehingga pembayaran tidak diterima.

**Langkah**:
1. Buka aplikasi atau buka layar "Pendapatan Berkala"
2. Aplikasi menampilkan dialog konfirmasi untuk kejadian jatuh tempo
3. Ketuk tombol "Batalkan Ini"
4. Masukkan alasan: "Penyewa belum mentransfer uang" (wajib)
5. Ketuk "Konfirmasi Batal"

**Hasil**: Kejadian yang dibatalkan berubah menjadi status "Dibatalkan", menampilkan alasan pembatalan, dan aplikasi secara otomatis membuat kejadian berikutnya. Saldo keuangan tidak berubah karena tidak ada pembayaran yang diterima.

**Dialog Batalkan Kejadian Pendapatan**:

```text
┌─────────────────────────────────────────┐
│  Batalkan Ini                            │
├─────────────────────────────────────────┤
│  Pendapatan Sewa                         │
│  Bulanan (tanggal 1)                     │
│  Tanggal Jatuh Tempo: Hari Ini           │
│                                         │
│  Alasan Pembatalan *                     │
│  ┌───────────────────────────────────┐ │
│  │ Penyewa belum mentransfer uang     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Kembali]        [Konfirmasi Batal]    │
└─────────────────────────────────────────┘
```

---

## 6. Logika & Aturan

### 6.1 Siklus dan Tanggal

- **Mingguan**: Pilih hari dalam minggu (1=Senin, 7=Minggu)
- **Dua Mingguan**: Pilih hari dalam minggu + tanggal mulai spesifik
- **Bulanan**: Pilih hari dalam bulan (1-31)

### 6.2 Buat Kejadian Otomatis

- Aplikasi secara otomatis membuat **kejadian** ketika:
  - Menambah pendapatan baru
  - Mencapai tanggal dalam siklus
  - Bulan baru dimulai

### 6.3 Status Kejadian

- **PENDING**: Menunggu konfirmasi (menampilkan badge kuning)
- **COMPLETED**: Dikonfirmasi (menampilkan badge hijau)
- **CANCELLED**: Dibatalkan (menampilkan badge merah)

### 6.4 Integrasi Anggaran

- Saat mengonfirmasi pendapatan, aplikasi secara otomatis memperbarui anggaran bulan saat ini (jika ada)
- Pendapatan dihitung ke "Pendapatan Berkala" dalam anggaran

### 6.5 Notifikasi

- Aplikasi mengirim notifikasi pengingat saat pembayaran jatuh tempo
- Waktu notifikasi dapat dikonfigurasi untuk setiap item (`notificationTime1`, `notificationTime2`, default 16:00 dan 19:00)

## 7. Catatan Penting

- **Jumlah bisa dikosongkan**: Jika Anda tidak tahu jumlah pastinya, Anda bisa mengosongkannya dan memasukkan saat mengonfirmasi
- **Tidak bisa dihapus saat ada kejadian**: Jika ada kejadian, Anda hanya bisa menonaktifkan (isActive = false), tidak bisa menghapus
- **Konfirmasi terlambat**: Anda bisa mengonfirmasi kejadian masa lalu, aplikasi akan secara otomatis menghitung ulang anggaran
- **Ubah siklus**: Saat mengedit siklus, kejadian masa depan akan dihitung ulang

