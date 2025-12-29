# Tabungan

## 1. Tujuan

Modul **Tabungan** membantu Anda mengelola rekening tabungan bank, melacak saldo, suku bunga, dan jangka waktu. Modul ini mendukung:
- Mengelola beberapa rekening tabungan
- Melacak suku bunga dan jangka waktu
- Menghitung bunga secara otomatis saat jatuh tempo
- Penarikan dini (jika diperlukan)
- Perpanjangan rekening

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda memiliki:
- Rekening tabungan bank
- Perlu melacak saldo dan suku bunga
- Ingin pengingat saat jatuh tempo
- Perlu mengelola beberapa rekening tabungan

## 3. Layar Terkait

- Daftar rekening tabungan
- Tambah rekening baru
- Edit rekening
- Detail rekening
- Penarikan dini

## 4. Penggunaan Utama

### 4.1 Buat Rekening Tabungan Baru

1. Buka **Fungsi** → Pilih **Tabungan Bank**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Lihat "Saldo Saat Ini" (dapat diklik untuk melihat detail)
4. Pilih bank:
   - Jika ada: Pilih dari dropdown
   - Jika tidak: Ketuk tombol "+" untuk membuat bank baru
5. Masukkan jumlah setoran (harus ≤ Saldo Saat Ini)
6. Masukkan jangka waktu: 1-36 bulan
7. Masukkan suku bunga: %/tahun (1-100%)
8. Pilih tanggal mulai (default adalah hari ini, dapat dipilih dari bulan sebelumnya hingga sekarang)
9. Lihat tanggal jatuh tempo dihitung otomatis (dari tanggal mulai + jangka waktu)
10. Pilih rencana saat jatuh tempo:
    - Tarik pokok dan bunga (default)
    - Perpanjang POKOK (bunga ke rekening)
    - Perpanjang POKOK + BUNGA
11. (Opsional) Masukkan catatan
12. (Opsional) Pilih waktu notifikasi (default: 10:00 dan 19:00)
13. Ketuk **BUAT REKENING**

### 4.2 Lihat Daftar dan Detail Rekening

1. Buka **Fungsi** → Pilih **Tabungan Bank**
2. Lihat layar "Daftar Rekening Tabungan" dengan filter default "Aktif"
3. Lihat kartu ringkasan:
   - Filter "Aktif": Saldo saat ini, Uang dalam tabungan, Bunga yang diharapkan, Bunga bulan ini
   - Filter "Selesai": Total ditarik, Bunga diterima
4. (Opsional) Gunakan bilah pencarian untuk menemukan rekening berdasarkan nama bank atau kode
5. Beralih filter antara "Aktif" dan "Selesai"
6. Ketuk pada rekening tabungan untuk melihat detail:
   - Info rekening: Bank, Jangka waktu, Suku bunga, Jumlah setoran, Bunga yang diharapkan
   - Tanggal mulai dan tanggal jatuh tempo
   - Status: Aktif
   - Rencana saat jatuh tempo
   - (Jika ada) Riwayat perpanjangan
   - Tombol "TARIK" (jika aktif)

### 4.3 Tarik Rekening Tabungan

1. Buka daftar tabungan, temukan rekening yang telah mencapai atau melewati tanggal jatuh tempo
2. Ketuk tombol **TARIK** pada kartu (atau buka detail kemudian ketuk "TARIK")
3. Lihat dialog "TARIK REKENING TABUNGAN" dengan:
   - Info rekening: Bank, Jumlah setoran, Jangka waktu, Suku bunga
   - Tanggal penarikan (default = tanggal jatuh tempo, dapat dipilih tanggal berbeda)
   - Bunga diterima (default = bunga yang diharapkan, dapat diedit)
   - Total diterima (dihitung otomatis = pokok + bunga)
4. (Opsional) Edit tanggal penarikan atau bunga diterima
5. Ketuk **KONFIRMASI**

### 4.4 Perpanjang Rekening Tabungan

1. Buka daftar tabungan, temukan rekening yang telah mencapai tanggal jatuh tempo dengan rencana "Perpanjang POKOK" atau "Perpanjang POKOK + BUNGA"
2. Ketuk tombol **PERPANJANG** atau "Perpanjang sesuai rencana"
3. Lihat dialog "PERPANJANG REKENING TABUNGAN" dengan:
   - Info rekening: Bank, Jumlah pokok, Jangka waktu, Suku bunga
   - Bunga diterima (jika perpanjang POKOK, bunga masuk ke rekening)
4. (Opsional) Edit suku bunga baru atau jangka waktu baru (default = jangka waktu lama)
5. Ketuk **KONFIRMASI PERPANJANGAN**

### 4.5 Edit Rekening Tabungan

1. Buka detail rekening tabungan aktif
2. Ketuk tombol **Edit** di kanan atas
3. Edit informasi:
   - Bank (jika perlu)
   - Jumlah setoran (jika meningkat, harus ≤ Saldo Saat Ini)
   - Jangka waktu, Suku bunga
   - Tanggal mulai (jika perlu)
   - Rencana saat jatuh tempo
   - Catatan, Waktu notifikasi
4. Lihat tanggal jatuh tempo dihitung ulang secara otomatis (jika jangka waktu/tanggal mulai berubah)
5. Ketuk **SIMPAN PERUBAHAN**

### 4.6 Buat Bank Baru

1. Pada layar "Tambah Rekening Tabungan" atau "Edit Rekening Tabungan"
2. Ketuk pada field "Bank"
3. Ketuk tombol "+" di samping dropdown untuk membuat bank baru
4. Lihat dialog "TAMBAH BANK BARU"
5. Masukkan nama bank
6. Masukkan kode bank (maks 3-4 karakter, otomatis huruf besar)
7. Pilih warna ikon (dari color picker atau palette)
8. Lihat pratinjau ikon
9. Ketuk **BUAT**

## 5. Contoh & Ilustrasi UI

### SAVINGS-01: Buat Rekening Tabungan Baru

**Tujuan**: Buat rekening tabungan baru untuk melacak setoran bank, suku bunga, dan tanggal jatuh tempo.

**Langkah Utama**:
1. Buka Fungsi → Tabungan Bank
2. Ketuk tombol "+" (FAB)
3. Pilih bank (atau buat baru)
4. Masukkan jumlah setoran, jangka waktu, suku bunga
5. Pilih tanggal mulai (default hari ini)
6. Pilih rencana saat jatuh tempo
7. (Opsional) Masukkan catatan dan waktu notifikasi
8. Ketuk "BUAT REKENING"

**Wireframe - Layar Tambah Rekening Tabungan**:

```text
┌──────────────────────────────────────────────┐
│ <  Tambah Rekening Tabungan                  │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Card ]                                      │
│                                               │
│ Saldo Saat Ini                        [ > ]    │
│ Rp31.200.000                                  │
│                                               │
│ Bank *                                        │
│ [ Bank of America ▼ ]                 [ + ] │
│                                               │
│ Jumlah Setoran (IDR) *                       │
│ [ Rp60.000.000 ]                             │
│                                               │
│ Jangka Waktu *                                │
│ [ 6 ] bulan                                   │
│                                               │
│ Suku Bunga *                                  │
│ [ 4,8 ] %/tahun                               │
│                                               │
│ Tanggal Mulai *                               │
│ [ 12/20/2025 ]                    [📅]        │
│                                               │
│ Tanggal Jatuh Tempo (readonly)                │
│ [ 06/20/2026 ]                                 │
│                                               │
│ Rencana saat Jatuh Tempo                      │
│ (●) Tarik pokok dan bunga                    │
│ ( ) Perpanjang POKOK                          │
│ ( ) Perpanjang POKOK + BUNGA                  │
│                                               │
│ Catatan (opsional)                             │
│ [                                      ]      │
│                                               │
│ Waktu Notifikasi 1                            │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Waktu Notifikasi 2                             │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  BATAL  ]       [  BUAT REKENING  ]
```

---

### SAVINGS-02: Tarik Rekening Tabungan

**Tujuan**: Tarik rekening tabungan saat mencapai tanggal jatuh tempo untuk menerima pokok dan bunga.

**Langkah Utama**:
1. Buka daftar tabungan, temukan rekening yang telah mencapai atau melewati tanggal jatuh tempo
2. Ketuk tombol "TARIK"
3. Lihat dialog dengan info rekening, tanggal penarikan, bunga diterima
4. (Opsional) Edit tanggal penarikan atau bunga diterima
5. Ketuk "KONFIRMASI"

**Wireframe - Dialog Tarik**:

```text
┌─────────────────────────────────────────┐
│  TARIK REKENING TABUNGAN                │
├─────────────────────────────────────────┤
│  [ICON BANK]  Bank of America           │
│                                         │
│  Jangka Waktu & Suku Bunga: 6 bulan · 4,8%/tahun │
│  Jumlah Setoran: Rp60.000.000         │
│                                         │
│  Tanggal Penarikan:                    │
│  [ 12 / 20 / 2025 ]  [📅]               │
│                                         │
│  Bunga Diterima:                       │
│  [ Rp1.440.000 ]                       │
│                                         │
│  Total Diterima: Rp61.440.000         │
│                                         │
│  [  KONFIRMASI  ]                       │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: Lihat Daftar dan Detail Rekening

**Tujuan**: Lihat ringkasan rekening tabungan aktif dan selesai, serta detail setiap rekening.

**Langkah Utama**:
1. Buka Fungsi → Tabungan Bank
2. Lihat kartu ringkasan berdasarkan filter
3. Gunakan bilah pencarian (opsional)
4. Beralih filter antara "Aktif" dan "Selesai"
5. Ketuk pada rekening untuk melihat detail

**Wireframe - Layar Daftar**:

```text
┌──────────────────────────────────────────────┐
│ <  Manajemen Tabungan Bank                    │
│                  [ + [FAB] Tambah Rekening ]  │
└──────────────────────────────────────────────┘

[Chip] Filter
[ Aktif ]   [ Selesai ]

┌──────────────────────────────────────────────┐
│  KARTU RINGKASAN                              │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Saldo        │  │ Bunga          │         │
│  │ Saat Ini     │  │ yang Diharapkan│         │
│  │ Rp31.200.000│  │ Rp3.285.000    │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Uang dalam   │  │ Bunga Bulan   │         │
│  │ Tabungan     │  │ Ini           │         │
│  │ Rp210.000.000│  │ Rp1.140.000   │         │
│  └──────────────┘  └──────────────┘         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Bilah Pencarian                           │
│  [ 🔍 Cari... ]                               │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Bank of America      [Icon Hapus] │
│                                              │
│ Rp60.000.000         |  6 bulan @ 4,8%     │
│                                              │
│ Bunga yang Diharapkan: Rp1.440.000         │
│ Jatuh Tempo: 12/20/2025   (5 hari tersisa)  │
│                    🔔 Segera Jatuh Tempo   │
│                                              │
│                    [ TARIK ]                │
└──────────────────────────────────────────────┘
```

**Wireframe - Layar Detail**:

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Bank of America          [ Edit ]│
│                                              │
│ Jangka Waktu & Suku Bunga: 6 bulan · 4,8%/tahun │
│ Jumlah Setoran: Rp60.000.000                 │
│ Bunga yang Diharapkan: Rp1.440.000         │
│                                              │
│ Tanggal Mulai: 06/20/2025                    │
│ Tanggal Jatuh Tempo: (5 hari tersisa) 12/20/2025 │
│                                              │
│ Status: Aktif                                 │
│                                              │
│ Rencana saat Jatuh Tempo:                    │
│ (●) Tarik pokok dan bunga                   │
│                                              │
│                    [  TARIK  ]               │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Perpanjang Rekening Tabungan

**Tujuan**: Perpanjang rekening tabungan sesuai rencana saat mencapai tanggal jatuh tempo.

**Langkah Utama**:
1. Temukan rekening yang telah mencapai tanggal jatuh tempo dengan rencana "Perpanjang POKOK" atau "Perpanjang POKOK + BUNGA"
2. Ketuk tombol "PERPANJANG"
3. Lihat dialog dengan info rekening dan bunga diterima
4. (Opsional) Edit suku bunga baru atau jangka waktu baru
5. Ketuk "KONFIRMASI PERPANJANGAN"

**Hasil**: Rekening lama diperbarui, rekening baru dibuat dengan `rootSavingId` tertaut ke rekening lama. Jika perpanjang POKOK, bunga ditambahkan ke saldo saat ini. Jika perpanjang POKOK + BUNGA, pokok dan bunga diperpanjang.

---

### SAVINGS-05: Buat Bank Baru

**Tujuan**: Buat bank baru untuk digunakan saat membuat rekening tabungan.

**Langkah Utama**:
1. Pada layar "Tambah Rekening Tabungan" atau "Edit Rekening Tabungan"
2. Ketuk tombol "+" di samping dropdown "Bank"
3. Masukkan nama bank, kode bank
4. Pilih warna ikon
5. Lihat pratinjau ikon
6. Ketuk "BUAT"

**Wireframe - Dialog Buat Bank**:

```text
┌─────────────────────────────────────────┐
│  TAMBAH BANK BARU                        │
├─────────────────────────────────────────┤
│  NAMA BANK                               │
│  [ ABC Bank ]                            │
│                                         │
│  KODE BANK                               │
│  [ ABC ]                                 │
│                                         │
│  WARNA IKON                              │
│  [ 🎨 ]  #FF5722                         │
│                                         │
│  PRATINJAU IKON                          │
│  ┌─────────┐                             │
│  │   ABC   │  (Latar: #FF5722)           │
│  └─────────┘                             │
│                                         │
│  [  BATAL  ]    [  BUAT  ]              │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Edit Rekening Tabungan

**Tujuan**: Edit informasi rekening tabungan aktif (bank, jumlah, jangka waktu, suku bunga, rencana jatuh tempo).

**Langkah Utama**:
1. Buka detail rekening tabungan aktif
2. Ketuk tombol "Edit"
3. Edit informasi yang diperlukan
4. Lihat tanggal jatuh tempo dihitung ulang secara otomatis (jika jangka waktu/tanggal mulai berubah)
5. Ketuk "SIMPAN PERUBAHAN"

**Hasil**: Info rekening diperbarui, bunga yang diharapkan dihitung ulang berdasarkan suku bunga baru. Jika jumlah berubah, saldo saat ini disesuaikan sesuai.

## 6. Logika & Aturan

### 6.1 Perhitungan Bunga

- Bunga dihitung dengan rumus: `Jumlah × Suku Bunga × (Jangka Waktu / 12)`
- Bunga dihitung saat jatuh tempo atau saat menarik dini

### 6.2 Status

- **Aktif (ACTIVE)**: Rekening tabungan aktif, belum mencapai tanggal jatuh tempo atau belum diproses
- **Selesai (COMPLETED)**: Rekening telah ditarik
- **Diperpanjang (ROLLED_OVER)**: Rekening telah diperpanjang, rekening baru dibuat

### 6.3 Penarikan dan Perpanjangan

- **Penarikan**: Saat menarik, pokok + bunga ditambahkan ke saldo saat ini, secara otomatis membuat "Pendapatan Tambahan" dengan kategori "Bunga Tabungan"
- **Penarikan Dini**: Dapat menarik sebelum tanggal jatuh tempo, bunga diterima mungkin lebih rendah dari bunga yang diharapkan
- **Perpanjang POKOK**: Bunga ditambahkan ke saldo saat ini, pokok diperpanjang dengan jangka waktu baru
- **Perpanjang POKOK + BUNGA**: Pokok dan bunga diperpanjang, saldo saat ini tidak berubah
- **Riwayat Perpanjangan**: Perpanjangan disimpan dan ditampilkan dalam detail rekening, tertaut via `rootSavingId`

### 6.4 Notifikasi

- Aplikasi mengirim notifikasi pengingat saat tanggal jatuh tempo tiba
- Waktu notifikasi dapat dikonfigurasi untuk setiap rekening (`notificationTime1`, `notificationTime2`, default 10:00 dan 19:00)

## 7. Catatan Penting

- **Modul Premium Diperlukan**: Fitur ini hanya untuk pengguna Premium
- **Suku Bunga**: Masukkan suku bunga per tahun (%/tahun), dari 1 hingga 100%
- **Jangka Waktu**: Dihitung dalam bulan, dari 1 hingga 36 bulan
- **Tanggal Jatuh Tempo**: Dihitung otomatis dari tanggal mulai + jangka waktu
- **Jumlah Setoran**: Harus ≤ Saldo Saat Ini, saat membuat rekening akan secara otomatis mengurangi saldo saat ini
- **Tanggal Mulai**: Hanya dapat dipilih dari awal bulan sebelumnya hingga sekarang
- **Notifikasi**: Notifikasi dikirim pada tanggal jatuh tempo pada 2 waktu (default 10:00 dan 19:00), dapat disesuaikan untuk setiap rekening
- **Badge "Segera Jatuh Tempo"**: Ditampilkan ketika ≤ 7 hari hingga tanggal jatuh tempo
- **Badge "Jatuh Tempo"**: Ditampilkan ketika tanggal jatuh tempo telah tiba
- **Hapus Rekening**: Saat menghapus rekening aktif, jumlah pokok ditambahkan kembali ke saldo saat ini. Menghapus rekening root akan menghapus seluruh rantai perpanjangan
- **Kartu Ringkasan**: Berubah berdasarkan filter, menampilkan informasi agregat untuk rekening aktif atau selesai

