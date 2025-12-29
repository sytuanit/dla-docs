# Acara Khusus

## 1. Tujuan

Modul **Acara Khusus** membantu Anda mengelola acara khusus sepanjang tahun dan mempersiapkannya, termasuk:
- Mengelola acara khusus (ulang tahun, liburan, dll.)
- Membuat daftar tugas (langkah persiapan)
- Melampirkan checklist ke setiap langkah persiapan
- Pengingat sebelum acara
- Melacak kemajuan persiapan

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Mengelola acara khusus sepanjang tahun
- Mempersiapkan acara penting
- Membuat daftar tugas
- Menerima pengingat sebelum acara

## 3. Layar Terkait

- Daftar acara khusus
- Tambah acara khusus baru
- Detail acara dan langkah persiapan
- Tambah langkah persiapan
- Pilih checklist
- Buat checklist baru

## 4. Penggunaan Utama

### 4.1 Tambah Acara Khusus

1. Buka **Fungsi** → Pilih **Acara Khusus**
2. Ketuk tombol **+** (FAB)
3. Isi informasi:
   - **Nama Acara**: (misalnya, "Ulang Tahun Ibu")
   - **Tanggal**: Pilih hari/bulan (DatePicker hanya memilih hari/bulan, tidak ada tahun)
   - **Gunakan Kalender Lunar**: (Opsional) Centang jika Anda ingin menggunakan kalender lunar
     - Jika dicentang: Masukkan hari dan bulan lunar, aplikasi secara otomatis menghitung tanggal solar terdekat
   - **Ulang**: Tahunan / Tahun Ini Saja
   - **Tampilkan Notifikasi Pada**: Pilih waktu (wajib, misalnya, 07:00)
   - **Catatan**: Informasi tambahan (opsional)
4. (Opsional) Tambah langkah persiapan (lihat 4.2)
5. Ketuk **Simpan**

### 4.2 Tambah Langkah Persiapan

1. Saat menambah acara baru: Ketuk **+ Tambah Langkah** di bagian "Langkah Persiapan"
2. Atau dari detail acara: Ketuk **+ Tambah Langkah**
3. Isi informasi:
   - **Kapan?**: "X hari sebelumnya" atau "Pada hari tersebut"
   - **Jumlah Hari**: (jika memilih "X hari sebelumnya") Masukkan jumlah hari sebelum acara
   - **Tampilkan Notifikasi Pada**: Pilih waktu (wajib)
   - **Ulang Harian hingga Selesai**: (Opsional) Centang jika Anda ingin pengingat harian
   - **Konten**: Nama langkah (wajib, misalnya, "Beli Hadiah")
   - **Catatan**: (Opsional)
   - **Gunakan Checklist**: (Opsional) Centang untuk menautkan dengan checklist belanja
4. Ketuk **Tambah** (atau FAB "Terapkan")

### 4.3 Buat Checklist

1. Saat menambah langkah persiapan, centang **Gunakan Checklist**
2. Layar "Pilih Checklist Belanja" secara otomatis terbuka
3. Ketuk FAB **+** untuk membuat checklist baru
4. Masukkan nama checklist
5. Tambah item:
   - Masukkan nama item
   - Ketuk **+** untuk menambah item baru
6. Ketuk **Simpan**
7. Checklist baru secara otomatis dipilih dan kembali ke layar "Tambah Langkah Persiapan"

### 4.4 Tandai Langkah sebagai Selesai

1. Buka detail acara khusus
2. Temukan langkah untuk ditandai
3. Ketuk checkbox [ ] untuk mengubah menjadi [✓]
4. Jika memiliki checklist, ketuk nama checklist untuk melihat dan centang/batal centang item

### 4.5 Lihat Kemajuan

1. Buka detail acara khusus
2. Lihat bagian "Ringkasan":
   - Langkah Persiapan: Jumlah total langkah
   - Selesai: Jumlah langkah yang ditandai / Total langkah
   - Status: Tidak Dimulai / Sedang Berjalan / Selesai

### 4.6 Edit Acara Khusus

1. Buka detail acara khusus
2. Ketuk hyperlink **Edit ›** di header
3. Edit informasi: Nama, tanggal, ulang, waktu pengingat, catatan
4. Ketuk **Simpan**

### 4.7 Edit Langkah Persiapan

1. Buka detail acara khusus
2. Ketuk pada langkah untuk mengedit (klik pada seluruh item, kecuali ikon Hapus)
3. Edit informasi: Waktu, konten, checklist
4. Ketuk **Terapkan** (atau FAB)

## 5. Contoh & Ilustrasi UI

### OCCASION-01: Buat Acara Khusus Baru (Ulang Tahun dengan Langkah Persiapan)

**Tujuan**: Buat acara khusus baru (ulang tahun) dengan langkah persiapan agar aplikasi secara otomatis mengingatkan Anda sebelum acara terjadi.

**Langkah Utama**:
1. Buka Fungsi → Acara Khusus → Ketuk tombol "+" (FAB)
2. Masukkan nama acara, pilih tanggal (01/05), pilih ulang "Tahunan", pilih waktu pengingat (07:00)
3. Tambah langkah persiapan 1: "7 hari sebelumnya – 08:00" - "Beli Hadiah"
4. Tambah langkah persiapan 2: "1 hari sebelumnya – 19:00" - "Pesan Kue"
5. Ketuk "Simpan"

**Wireframe - Layar Tambah Acara Khusus**:

```text
┌──────────────────────────────────────────────┐
│ <  Tambah Acara Khusus                       │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Informasi Acara                            │
│                                               │
│ Nama Acara *                                   │
│ [ Ulang Tahun An                      ]       │
│                                               │
│ Tanggal                                        │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker hanya memilih hari/bulan)        │
│                                               │
│ [ ] Gunakan Kalender Lunar                    │
│                                               │
│ Ulang                                        │
│ (•) Tahunan                                     │
│ ( ) Tahun Ini Saja                            │
│                                               │
│ Tampilkan Notifikasi Pada *                  │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Catatan (opsional)                            │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Langkah Persiapan          [ + Tambah Langkah ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Beli Hadiah                   [Icon Hapus] │ │
│ │     7 hari sebelumnya – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Pesan Kue                     [Icon Hapus] │ │
│ │     1 hari sebelumnya – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ Batal ]                        [ Simpan ]
```

---

### OCCASION-02: Buat Acara Khusus Menggunakan Kalender Lunar (Hari Peringatan dengan Checklist Belanja)

**Tujuan**: Buat acara khusus menggunakan kalender lunar (Hari Peringatan) dengan langkah persiapan yang tertaut ke checklist belanja untuk melacak pembelian persembahan.

**Langkah Utama**:
1. Buka Fungsi → Acara Khusus → Ketuk tombol "+" (FAB)
2. Masukkan nama acara "Hari Peringatan Ibu", centang "Gunakan Kalender Lunar"
3. Masukkan tanggal lunar: 15/11, aplikasi secara otomatis menghitung tanggal solar: 12/15/2025
4. Tambah 3 langkah persiapan, di mana langkah 2 memiliki tautan checklist "beli persembahan"
5. Ketuk "Simpan"

**Wireframe - Pilih Tanggal Lunar**:

```text
│ │ │ Tanggal Lunar                                   │ │ │
│ │ │ Hari (1-30)    Bulan (1-12)                   │ │ │
│ │ │ [ 15 ]        [ 11 ]                           │ │ │
│ │ │                                               │ │ │
│ │ │ Tanggal Solar (dihitung otomatis - hanya tampilan)│ │ │
│ │ │ [ Teks: 12/15/2025                 ]         │ │ │
│ │ │ (Ini adalah tanggal solar TERDEKAT di masa depan)│ │ │
```

---

### OCCASION-03: Lihat Daftar dan Detail Acara Khusus

**Tujuan**: Lihat ringkasan acara khusus, filter berdasarkan waktu, dan detail setiap acara dengan kemajuan persiapan.

**Langkah Utama**:
1. Buka Fungsi → Acara Khusus
2. Lihat daftar dengan filter "Semua", "Mendatang", "Bulan Ini"
3. Ketuk pada kartu acara untuk melihat detail
4. Lihat ringkasan: Jumlah langkah, Selesai, Status
5. Tandai langkah sebagai selesai dengan mencentang checkbox

**Wireframe - Layar Daftar Acara Khusus**:

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Daftar Acara Khusus                                      │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Tambah Acara ]                                       │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filter: [ Semua ]  [ Mendatang ]  [ Bulan Ini ]      │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Hari Peringatan Ibu    [Sedang Berjalan] [Icon Hapus] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 12/15/2025 • 15/11 (Lunar) • 10 hari tersisa  │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Langkah Persiapan yang Diperlukan:              │ │ │
│ │ │   [✓] 3 hari sebelumnya – Daftar persembahan        │ │ │
│ │ │   [ ] 1 hari sebelumnya – Belanja persembahan      │ │ │
│ │ │   [ ] Pada hari tersebut – Siapkan altar / upacara │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Wireframe - Layar Detail Acara Khusus**:

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Detail Acara Khusus                                   │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Hari Peringatan Ibu                       [Edit ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 12/15/2025 (Solar) • 15/11 (Kalender Lunar)      │ │ │
│ │ │ 10 hari tersisa • Ulang: Tahunan                │ │ │
│ │ │                                                      │ │ │
│ │ │ Catatan:                                           │ │ │
│ │ │ Makan kecil, bunga putih, batasi tamu.           │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Ringkasan                                          │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Langkah Persiapan: 3                              │ │ │
│ │ │ Selesai: 1 / 3                                    │ │ │
│ │ │ Status: [Sedang Berjalan]                         │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Langkah Persiapan                  [ + Tambah Langkah ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] Daftar persembahan                [Icon Hapus]           │ │ │
│ │ │     3 hari sebelumnya – 08:00                    │ │ │
│ │ │     Selesai pada 09:15 – 12/12/2025             │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Belanja persembahan                [Icon Hapus]            │ │ │
│ │ │     1 hari sebelumnya – 19:00                      │ │ │
│ │ │     Ulang harian hingga selesai                    │ │ │
│ │ │     Checklist Belanja: beli persembahan ›          │ │ │
│ │ │     [✓] Selesai 3 / 8 item                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### OCCASION-04: Tambah Langkah Persiapan dengan Checklist Belanja

**Tujuan**: Tambah langkah persiapan baru untuk acara khusus dan menautkan dengan checklist belanja untuk melacak belanja.

**Langkah Utama**:
1. Buka detail acara khusus → Ketuk "+ Tambah Langkah"
2. Pilih "Kapan?": "X hari sebelumnya", masukkan jumlah hari: 1
3. Pilih waktu pengingat: 19:00
4. Aktifkan "Ulang Harian hingga Selesai"
5. Masukkan konten: "Belanja persembahan"
6. Centang "Gunakan Checklist" → Pilih checklist "beli persembahan"
7. Ketuk "Tambah"

**Wireframe - Layar Tambah Langkah Persiapan**:

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Tambah Langkah Persiapan                                  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Waktu Persiapan                                      │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Kapan? * (wajib)                                  │ │ │
│ │ │ [ X hari sebelumnya         ▼ ]                   │ │ │
│ │ │                                                      │ │ │
│ │ │ Jumlah Hari * (hanya ditampilkan saat "X hari sebelumnya")│ │ │
│ │ │ [  1  ]  hari sebelumnya                           │ │ │
│ │ │                                                      │ │ │
│ │ │ Tampilkan Notifikasi Pada * (wajib)                │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Ulang harian hingga selesai                     │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Konten                                              │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Konten * (wajib)                                  │ │ │
│ │ │ [ Belanja persembahan               ]              │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 Tautkan dengan Checklist Belanja?                   │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Gunakan Checklist                                │ │ │
│ │ │ Checklist Belanja: beli persembahan ›    [Icon Tukar]  │ │ │
│ │ │ (8 item)                                          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ Batal ]                        [ Tambah ]           │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### OCCASION-05: Tandai Langkah Persiapan sebagai Selesai dan Lihat Kemajuan Checklist

**Tujuan**: Tandai langkah persiapan sebagai selesai dan melacak kemajuan checklist belanja.

**Langkah Utama**:
1. Buka detail acara khusus
2. Lihat langkah dengan checklist menampilkan kemajuan "Selesai 3 / 8 item"
3. Ketuk nama checklist untuk melihat detail dan centang/batal centang item
4. Centang checkbox langkah untuk menandai sebagai selesai
5. Lihat "Ringkasan" diperbarui secara real-time

---

### OCCASION-06: Edit Acara Khusus dan Langkah Persiapan

**Tujuan**: Edit informasi acara khusus dan langkah persiapan setelah dibuat.

**Langkah Utama**:
1. Buka detail acara khusus → Ketuk "Edit ›"
2. Edit nama acara, catatan
3. Ketuk "Simpan"
4. Ketuk pada langkah untuk mengedit: Ubah waktu, konten
5. Ketuk ikon Hapus untuk menghapus langkah (memiliki dialog konfirmasi)

## 6. Logika & Aturan

### 6.1 Tanggal Kalender Lunar

- Anda dapat memasukkan tanggal solar dan lunar
- Aplikasi secara otomatis menghitung tanggal solar yang sesuai dengan tanggal lunar
- Mendukung pengulangan tahunan berdasarkan kalender lunar

### 6.2 Ulang

- **Tahunan**: Acara berulang setiap tahun (berdasarkan kalender solar atau lunar)
  - Dengan kalender solar: Setiap tahun menghitung nextOccurDate berdasarkan (hari/bulan) dari solarDate
  - Dengan kalender lunar: Setiap tahun mengonversi dari tanggal lunar ke tanggal solar yang sesuai dan memperbarui nextOccurDate
- **Tahun Ini Saja**: Acara hanya berlaku pada tahun saat ini, tidak berulang tahun depan

### 6.3 Langkah Persiapan

- **Kapan?**: Memiliki 2 opsi:
  - **X hari sebelumnya**: Ingatkan X hari sebelum tanggal acara (harus memasukkan jumlah hari)
  - **Pada hari tersebut**: Ingatkan pada tanggal acara (tidak perlu memasukkan jumlah hari)
- **Tampilkan Notifikasi Pada**: Waktu pengingat (wajib, format HH:mm)
- **Ulang Harian hingga Selesai**: Jika diaktifkan, notifikasi akan berulang setiap hari hingga pengguna menandai langkah sebagai selesai
- **Tautan Checklist**: Setiap langkah dapat melampirkan checklist belanja untuk melacak kemajuan belanja

### 6.4 Checklist

- Checklist dapat digunakan kembali untuk beberapa langkah
- Melacak jumlah item yang selesai / Total item (misalnya, "Selesai 3 / 8 item")
- Ditampilkan dalam detail langkah dengan tautan "nama checklist ›" untuk melihat detail
- Dapat centang/batal centang item dalam checklist untuk memperbarui kemajuan
- Langkah persiapan dapat ditandai selesai meskipun checklist belum sepenuhnya selesai

### 6.5 Notifikasi

- **Notifikasi Acara Utama**: Dibuat pada `nextOccurDate + reminder_time`
  - Dengan acara TAHUNAN: notifikasi akan dibangun kembali saat aplikasi dimulai (berdasarkan nextOccurDate yang baru dihitung)
  - Dengan acara SEKALI: notifikasi hanya dibuat sekali untuk nextOccurDate saat ini
- **Notifikasi Langkah Persiapan**: Hitung tanggal pengingat berdasarkan:
  - `nextOccurDate` dari acara khusus
  - `reminderType` dan `daysBefore` (jika ada)
  - `reminderTime`
- **Notifikasi Berulang**: Jika `repeatDailyUntilComplete = true`:
  - Buat notifikasi berulang harian
  - Gunakan `notificationGroupKey` untuk mengelompokkan notifikasi berulang
  - Secara otomatis dibatalkan saat pengguna menandai langkah sebagai selesai

## 7. Catatan Penting

- **Tanggal Kalender Lunar**: 
  - Aplikasi secara otomatis mengonversi ke kalender solar untuk ditampilkan
  - Mencari "tanggal solar TERDEKAT di masa depan" dibandingkan dengan tanggal saat ini
  - Tahun-tahun mendatang: Sistem selalu menghitung ulang tanggal solar yang sesuai dari (lunar_day, lunar_month) untuk setiap tahun
  - Jika tahun itu memiliki bulan reguler dan bulan kabisat dari bulan yang sama: Sistem dapat membuat 2 pengingat untuk menghindari terlewat
- **Ulang Tahunan**: 
  - Acara akan secara otomatis menghitung ulang nextOccurDate tahun depan
  - Dengan kalender lunar: Setiap tahun mengonversi dari tanggal lunar ke tanggal solar yang sesuai
- **Waktu Pengingat**: 
  - Harus memiliki nilai (tidak boleh kosong)
  - Harus format yang benar HH:mm (00:00 - 23:59)
- **Checklist**: 
  - Checklist yang dihapus masih ditampilkan dalam langkah (tetapi tidak dapat diedit)
  - Dapat menandai langkah sebagai selesai meskipun checklist belum sepenuhnya selesai
- **Notifikasi**: 
  - Perlu mengaktifkan notifikasi di Pengaturan untuk menerima pengingat
  - Notifikasi berulang akan secara otomatis dibatalkan saat menandai langkah sebagai selesai
- **Status Acara**:
  - **Tidak Dimulai**: Semua langkah belum selesai (abu-abu)
  - **Sedang Berjalan**: Setidaknya 1 langkah selesai tetapi tidak semua (biru)
  - **Selesai**: Semua langkah selesai (hijau gelap)
  - Jika acara tidak memiliki langkah persiapan: Status dihitung berdasarkan tanggal (Tidak Dimulai / Sedang Berjalan / Selesai)

