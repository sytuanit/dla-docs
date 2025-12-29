# Pengeluaran Berkala

## 1. Tujuan

Modul **Pengeluaran Berkala** membantu Anda mengelola pengeluaran berkala dengan siklus tetap seperti:
- Tagihan listrik, air, gas
- Internet, TV kabel
- Asuransi
- SPP
- Sewa
- Pengeluaran berkala lainnya

Modul ini secara otomatis membuat **kejadian** berdasarkan siklus yang Anda konfigurasi, dan mengingatkan Anda saat pembayaran jatuh tempo.

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda memiliki:
- Pengeluaran tetap dengan jadwal (mingguan, dua mingguan, atau bulanan)
- Perlu melacak dan mengonfirmasi kapan pembayaran dilakukan
- Ingin perhitungan otomatis ke anggaran bulanan

## 3. Layar Terkait

- Daftar pengeluaran berkala
- Tambah pengeluaran berkala baru
- Edit pengeluaran berkala
- Riwayat kejadian

## 4. Penggunaan Utama

### 4.1 Tambah Pengeluaran Berkala Baru

1. Buka **Fungsi** → Pilih **Pengeluaran Berkala**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Isi informasi:
   - **Kategori**: Pilih atau buat kategori baru
   - **Jumlah**: Masukkan jumlah pengeluaran (bisa dikosongkan, masukkan saat mengonfirmasi)
   - **Siklus**: Pilih Mingguan / Dua Mingguan / Bulanan
   - **Tanggal**: Pilih tanggal dalam siklus (misalnya, tanggal 15 setiap bulan)
   - **Tanggal Mulai**: (Hanya untuk siklus dua mingguan) Pilih tanggal mulai
   - **Catatan**: Informasi tambahan (opsional)
4. Ketuk **Simpan**

### 4.2 Konfirmasi Pembayaran Dilakukan

1. Buka daftar pengeluaran berkala
2. Temukan item dengan badge **"Menunggu Konfirmasi"** (kuning)
3. Ketuk item untuk membuka dialog konfirmasi
4. Isi:
   - **Jumlah Aktual**: (jika berbeda dari yang diharapkan)
   - **Catatan**: (opsional)
5. Ketuk **Konfirmasi**

### 4.3 Edit Pengeluaran Berkala

1. Buka daftar pengeluaran berkala
2. Ketuk item yang ingin diedit
3. Pilih **Edit** dari menu
4. Perbarui informasi
5. Ketuk **Simpan**

### 4.4 Lihat Riwayat

1. Buka daftar pengeluaran berkala
2. Ketuk item
3. Pilih **Riwayat** untuk melihat semua kejadian masa lalu

### 4.5 Nonaktifkan/Aktifkan Pengeluaran

1. Buka daftar pengeluaran berkala
2. Temukan item yang ingin dinonaktifkan/diaktifkan
3. Toggle switch **Aktif** di sisi kanan item

## 5. Contoh & Ilustrasi UI

### 5.1 Contoh 1: Buat Pengeluaran Berkala Bulanan (Tagihan Listrik)

**Skenario**: Anda ingin melacak tagihan listrik bulanan agar aplikasi secara otomatis mengingatkan Anda saat pembayaran jatuh tempo.

**Langkah**:
1. Buka layar Fungsi, pilih "Pengeluaran Berkala"
2. Ketuk tombol "➕ Tambah Baru" di kanan bawah
3. Pilih kategori "Utilitas" (atau buat baru jika tidak tersedia)
4. Masukkan jumlah: Rp300.000
5. Pilih siklus "Bulanan"
6. Pilih "Pilih hari dalam bulan", masukkan 15
7. Catatan otomatis terisi "Tagihan listrik bulanan" (dapat diedit)
8. Ketuk "Simpan"

**Hasil**: Aplikasi menampilkan pesan sukses dan kembali ke daftar. Item baru muncul dengan informasi lengkap, dan aplikasi akan secara otomatis mengingatkan Anda pada tanggal 15 setiap bulan.

**Layar Tambah Pengeluaran Berkala**:

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Tambah Pengeluaran Berkala│
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Utilitas ▼] [+ Tambah Baru]           │
│                                         │
│  Jumlah (IDR) *                          │
│  [Rp300.000]                             │
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
│  │ Hari dalam bulan: [15]            │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Catatan                                 │
│  ┌───────────────────────────────────┐ │
│  │ Tagihan listrik bulanan            │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Batal]                  [Simpan]     │
└─────────────────────────────────────────┘
```

---

### 5.2 Contoh 2: Konfirmasi Pengeluaran Jatuh Tempo dan Perbarui Jumlah Aktual

**Skenario**: Hari pembayaran tagihan air (tanggal 10), tetapi jumlah aktual yang harus dibayar adalah Rp105.000 (turun) bukan Rp120.000 yang ditetapkan.

**Langkah**:
1. Buka aplikasi atau buka layar "Pengeluaran Berkala"
2. Aplikasi secara otomatis mendeteksi kejadian jatuh tempo dan menampilkan dialog konfirmasi
3. Dialog menampilkan jumlah default: Rp120.000
4. Perbarui jumlah aktual menjadi Rp105.000
5. Masukkan catatan: "Bulan ini hemat air" (opsional)
6. Ketuk "Konfirmasi Dibayar"

**Hasil**: Aplikasi memperbarui kejadian yang dikonfirmasi dengan jumlah aktual Rp105.000, secara otomatis membuat kejadian berikutnya, dan memperbarui saldo keuangan saat ini (mengurangi Rp105.000).

**Dialog Konfirmasi Pengeluaran**:

```text
┌─────────────────────────────────────────┐
│  Konfirmasi Dibayar                      │
├─────────────────────────────────────────┤
│  Tagihan Air                             │
│  Bulanan (tanggal 10)                    │
│  Tanggal Jatuh Tempo: Hari Ini           │
│                                         │
│  Jumlah Aktual *                         │
│  [Rp105.000]                             │
│                                         │
│  Catatan                                 │
│  [Bulan ini hemat air]                  │
│                                         │
│  [Batalkan Ini]    [Konfirmasi Dibayar] │
└─────────────────────────────────────────┘
```

---

### 5.3 Contoh 3: Nonaktifkan Pengeluaran Berkala Saat Tidak Lagi Berlaku

**Skenario**: Anda sementara tidak menyewa tempat selama 2 bulan, jadi Anda ingin menonaktifkan pengeluaran "Sewa" daripada menghapusnya sepenuhnya.

**Langkah**:
1. Buka layar "Pengeluaran Berkala"
2. Temukan item "Sewa" dalam daftar
3. Ketuk switch "Aktif" di sisi kanan item
4. Aplikasi menampilkan dialog konfirmasi: "Apakah Anda yakin ingin menonaktifkan pengeluaran ini?"
5. Ketuk tombol "Nonaktifkan" untuk mengonfirmasi

**Hasil**: Card "Sewa" berubah menjadi status "Tidak Aktif" (abu-abu), switch berubah menjadi "Tidak Aktif". Aplikasi tidak lagi membuat kejadian baru untuk pengeluaran ini. Anda dapat mengaktifkan kembali dengan mengetuk switch "Tidak Aktif" → "Aktif".

**Layar Daftar dengan Switch**:

```text
┌─────────────────────────────────────────┐
│  ← Kembali    Pengeluaran Berkala       │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Sewa              [⚪ Tidak Aktif] │ │
│  │ Rp18.000.000                       │
│  │ Bulanan - tanggal 1                │
│  │ (Dinonaktifkan)                    │
│  │                                    │
│  │ [Edit] [Riwayat] [Hapus]           │
│  └───────────────────────────────────┘ │
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
  - Menambah pengeluaran baru
  - Mencapai tanggal dalam siklus
  - Bulan baru dimulai

### 6.3 Status Kejadian

- **PENDING**: Menunggu konfirmasi (menampilkan badge kuning)
- **COMPLETED**: Dikonfirmasi (menampilkan badge hijau)
- **CANCELLED**: Dibatalkan (menampilkan badge merah)

### 6.4 Integrasi Anggaran

- Saat mengonfirmasi pengeluaran, aplikasi secara otomatis memperbarui anggaran bulan saat ini (jika ada)
- Pengeluaran dihitung ke "Pengeluaran Berkala" dalam anggaran

### 6.5 Notifikasi

- Aplikasi mengirim notifikasi pengingat saat pembayaran jatuh tempo
- Waktu notifikasi dapat dikonfigurasi untuk setiap item (`notificationTime1`, `notificationTime2`, default 16:00 dan 19:00)

## 7. Catatan Penting

- **Jumlah bisa dikosongkan**: Jika Anda tidak tahu jumlah pastinya, Anda bisa mengosongkannya dan memasukkan saat mengonfirmasi
- **Tidak bisa dihapus saat ada kejadian**: Jika ada kejadian, Anda hanya bisa menonaktifkan (isActive = false), tidak bisa menghapus
- **Konfirmasi terlambat**: Anda bisa mengonfirmasi kejadian masa lalu, aplikasi akan secara otomatis menghitung ulang anggaran
- **Ubah siklus**: Saat mengedit siklus, kejadian masa depan akan dihitung ulang

