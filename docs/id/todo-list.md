# Daftar Tugas

## 1. Tujuan

Modul **Daftar Tugas** membantu Anda mengelola tugas berulang dan melacak kemajuan penyelesaian, termasuk:
- Tugas berulang berbasis waktu (harian/mingguan/bulanan/tahunan)
- Tugas berulang berbasis metrik (mil/jam/kali...)
- Pengingat saat jatuh tempo
- Pelacakan riwayat penyelesaian
- Pencatatan pengeluaran (jika berlaku)

Modul ini membantu Anda tidak pernah melewatkan tugas penting seperti perawatan mobil, penggantian filter, pemeriksaan berkala, dll.

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda memiliki:
- Tugas yang berulang pada jadwal (misalnya, Ganti filter air setiap 3 bulan)
- Tugas yang berulang berdasarkan metrik (misalnya, Ganti oli mobil setiap 3.000 mil)
- Perlu pengingat otomatis saat jatuh tempo
- Ingin melacak riwayat penyelesaian
- Perlu mencatat pengeluaran terkait

## 3. Layar Terkait

- Layar daftar tugas
- Pilih jenis tugas (Berbasis Waktu / Berbasis Metrik)
- Tambah tugas baru
- Edit tugas
- Konfirmasi tugas berbasis metrik
- Riwayat tugas
- Daftar tugas jatuh tempo (daftar bel)

## 4. Penggunaan Utama

### 4.1 Tambah Tugas Berbasis Waktu

1. Buka **Fungsi** → Pilih **Daftar Tugas**
2. Ketuk tombol **+** (FAB) di kanan bawah
3. Pilih **Tugas Berbasis Waktu**
4. Isi informasi:
   - **Nama Tugas**: (wajib, misalnya, "Ganti filter air")
   - **Siklus Berulang**: Masukkan angka dan pilih unit (Hari/Minggu/Bulan/Tahun)
   - **Tanggal Jatuh Tempo Berikutnya**: Pilih tanggal (hanya memungkinkan memilih dari besok seterusnya)
   - **Waktu Pengingat**: Pilih waktu (wajib, misalnya, 08:00)
   - **Tugas ini menimbulkan pengeluaran**: (Opsional) Centang jika ada pengeluaran
     - Jika dicentang: Pilih **Kategori** (wajib)
   - **Catatan**: Informasi tambahan (opsional)
5. Ketuk **Simpan**

### 4.2 Tambah Tugas Berbasis Metrik

1. Buka **Fungsi** → Pilih **Daftar Tugas**
2. Ketuk tombol **+** (FAB)
3. Pilih **Tugas Berbasis Metrik**
4. Isi informasi:
   - **Nama Tugas**: (wajib, misalnya, "Ganti oli mobil")
   - **Siklus**: Masukkan angka (misalnya, 3.000)
   - **Unit**: Masukkan unit (misalnya, "Mil")
   - **Nilai Metrik Terakhir yang Diselesaikan**: Masukkan nilai saat ini (misalnya, 12.500)
   - **Tugas ini menimbulkan pengeluaran**: (Opsional) Centang jika ada pengeluaran
     - Jika dicentang: Pilih **Kategori** (wajib)
   - **Catatan**: Informasi tambahan (opsional)
5. Ketuk **Simpan**

### 4.3 Konfirmasi Tugas Berbasis Metrik

1. Buka daftar tugas
2. Temukan tugas berbasis metrik (tipe METRIC) untuk dikonfirmasi
3. Ketuk tombol **Konfirmasi** pada kartu (hanya ditampilkan saat `isActive = true`)
4. Isi informasi:
   - **Nilai Metrik Saat Ini**: Masukkan nilai saat ini (wajib, harus ≥ nilai metrik terakhir yang diselesaikan)
   - **Catatan**: (Opsional)
5. Lihat **Delta** dihitung secara otomatis (nilai saat ini - nilai terakhir yang diselesaikan)
6. Ketuk **Dikonfirmasi**
7. (Jika tugas memiliki pengeluaran) Pilih **Tambah Pengeluaran** atau **Batal**

**Catatan**: Tugas berbasis waktu (tipe CYCLE) tidak memiliki tombol "Konfirmasi" pada kartu. Konfirmasi hanya dilakukan di layar "Tugas Jatuh Tempo" (daftar bel).

### 4.4 Lihat Daftar dan Detail

1. Buka **Fungsi** → Pilih **Daftar Tugas**
2. Gunakan **Bilah pencarian** untuk mencari berdasarkan nama tugas
3. Gunakan **Filter chip** untuk memfilter:
   - **Semua**: Tampilkan semua tugas
   - **Berbasis Waktu**: Hanya tampilkan tugas tipe CYCLE
   - **Berbasis Metrik**: Hanya tampilkan tugas tipe METRIC
4. Ketuk pada kartu tugas untuk melihat detail dan mengedit

### 4.5 Edit Tugas

1. Buka daftar tugas
2. Ketuk pada kartu tugas untuk mengedit
3. Perbarui informasi:
   - **Catatan**: Jika ada riwayat, **Siklus** (CYCLE) atau **Unit/Siklus** (METRIC) akan terkunci dan tidak dapat diedit
4. Ketuk **Simpan**

### 4.6 Lihat Riwayat

1. Buka daftar tugas
2. Ketuk pada tautan **Lihat Riwayat ›** dari tugas untuk melihat
3. Gunakan **Filter chip** untuk memfilter berdasarkan waktu:
   - **Semua**: Tampilkan semua riwayat
   - **Bulan Ini**: Hanya tampilkan riwayat dari bulan saat ini
   - **Bulan Lalu**: Hanya tampilkan riwayat dari bulan sebelumnya
   - **3 Bulan Terakhir**: Hanya tampilkan riwayat dari 3 bulan terakhir

### 4.7 Nonaktifkan/Aktifkan Tugas

1. Buka daftar tugas
2. Temukan tugas untuk dinonaktifkan/diaktifkan
3. Toggle switch **Aktif** di footer kartu
4. Tugas yang dinonaktifkan akan menampilkan badge **"Tidak Aktif"** (abu-abu)

### 4.8 Hapus Tugas

1. Buka daftar tugas
2. Ketuk ikon **Hapus** (🗑️) di header kartu
3. Konfirmasi penghapusan dalam dialog
4. Tugas dan semua riwayat terkait akan dihapus

## 5. Contoh & Ilustrasi UI

### TODO-01: Buat Tugas Berbasis Waktu (Ganti Filter Air)

**Tujuan**: Buat tugas berbasis waktu agar aplikasi secara otomatis mengingatkan Anda saat jatuh tempo.

**Langkah Utama**:
1. Buka Fungsi → Daftar Tugas → Ketuk tombol "+" (FAB)
2. Pilih "Tugas Berbasis Waktu"
3. Masukkan nama tugas: "Ganti filter air"
4. Masukkan siklus: "3" bulan
5. Pilih tanggal jatuh tempo berikutnya: 03/01/2026
6. Pilih waktu pengingat: 08:00
7. Centang "Tugas ini menimbulkan pengeluaran", pilih kategori "Utilitas"
8. Masukkan catatan: "Ganti filter #1 dan #2"
9. Ketuk "Simpan"

**Wireframe - Layar Tambah Tugas Berbasis Waktu**:

```text
┌──────────────────────────────────────────────┐
│ <  Tambah Tugas Berbasis Waktu              │
├──────────────────────────────────────────────┤

Nama Tugas
[ Ganti filter air            ]

Siklus Berulang
Setiap [ 3 ] [ Bulan ▼ ]
(Unit: Hari / Minggu / Bulan / Tahun)

Tanggal Jatuh Tempo Berikutnya
[ 03 / 01 / 2026    ▼ ]
Petunjuk: 
Tanggal jatuh tempo untuk pertama kali.
Tanggal selanjutnya akan dihitung secara otomatis berdasarkan siklus yang Anda masukkan.

Waktu Pengingat
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Tugas ini menimbulkan pengeluaran

┌─────────────────────────────────────┐
│ Kategori *                           │
│ [Utilitas ▼] [+ Buat Baru]         │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Catatan (opsional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Batal ]                         [ Simpan ]
└──────────────────────────────────────────────┘
```

---

### TODO-02: Buat Tugas Berbasis Metrik (Ganti Oli Mobil)

**Tujuan**: Buat tugas berbasis metrik untuk melacak perawatan mobil berdasarkan jarak tempuh.

**Langkah Utama**:
1. Buka Fungsi → Daftar Tugas → Ketuk tombol "+" (FAB)
2. Pilih "Tugas Berbasis Metrik"
3. Masukkan nama tugas: "Ganti oli mobil"
4. Masukkan siklus: "3.000", unit: "Mil"
5. Masukkan nilai metrik terakhir yang diselesaikan: "12.500"
6. Centang "Tugas ini menimbulkan pengeluaran", pilih kategori "Perawatan Mobil"
7. Masukkan catatan: "Ganti oli + filter oli"
8. Ketuk "Simpan"

**Wireframe - Layar Tambah Tugas Berbasis Metrik**:

```text
┌──────────────────────────────────────────────┐
│ <  Tambah Tugas Berbasis Metrik              │
├──────────────────────────────────────────────┤

Nama Tugas
[ Ganti oli mobil                        ]

Siklus
Setiap [ 3.000 ] Unit [ Mil ]
(Unit: Mil / Jam / Kali / ...)

Nilai Metrik Terakhir yang Diselesaikan
[ 12.500 ]

──────────────────────────────────────────────
[✓] Tugas ini menimbulkan pengeluaran

┌─────────────────────────────────────┐
│ Kategori *                           │
│ [Perawatan Mobil ▼] [+ Buat Baru] │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Catatan (opsional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Batal ]                         [ Simpan ]
└──────────────────────────────────────────────┘
```

---

### TODO-03: Lihat Daftar dan Detail

**Tujuan**: Lihat ringkasan tugas, filter berdasarkan jenis, pencarian, dan detail setiap tugas.

**Langkah Utama**:
1. Buka Fungsi → Daftar Tugas
2. Lihat daftar dengan bilah pencarian dan filter chip
3. Gunakan filter: "Semua", "Berbasis Waktu", "Berbasis Metrik"
4. Gunakan bilah pencarian untuk mencari berdasarkan nama tugas
5. Ketuk pada kartu tugas untuk melihat detail

**Wireframe - Layar Daftar Tugas**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Kembali]  Daftar Tugas                    [🔔]      │
└─────────────────────────────────────────────────────────┘
│  🔍 Cari...                                             │
│                                                          │
│  [Semua] [Berbasis Waktu] [Berbasis Metrik]            │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Kartu: Ganti filter air                         │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Ganti filter air    [Selesai] [🗑️]          │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Siklus: Setiap 3 bulan                    │ │    │
│  │ │ ✅ Terakhir diselesaikan: 12/01/2025         │ │    │
│  │ │ 📅 Tanggal jatuh tempo berikutnya: 03/01/2026│ │    │
│  │ │ ⏳ 76 hari tersisa                            │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Lihat Riwayat ›                     [⚪ Aktif]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Kartu: Ganti oli mobil                          │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Ganti oli mobil                   [🗑️]      │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Lacak berdasarkan: Mil                      │ │    │
│  │ │ ✅ Terakhir dikonfirmasi: 12/02/2025        │ │    │
│  │ │ 🔢 Nilai metrik terakhir: 12.500 mil        │ │    │
│  │ │ 🎯 Jatuh tempo berikutnya: 14.500 mil        │ │    │
│  │ │ ⏳ ~300 mil tersisa                          │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Konfirmasi]                                │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Lihat Riwayat ›                     [⚪ Aktif]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04: Konfirmasi Tugas Berbasis Metrik (Ganti Oli Mobil)

**Tujuan**: Konfirmasi penyelesaian tugas berbasis metrik dengan memasukkan nilai metrik saat ini.

**Langkah Utama**:
1. Buka daftar tugas
2. Temukan tugas "Ganti oli mobil" (tipe METRIC)
3. Ketuk tombol "Konfirmasi"
4. Masukkan nilai metrik saat ini: "14.520"
5. Lihat delta yang dihitung secara otomatis: "+2.020 mil"
6. Masukkan catatan: "Ganti oli + filter oli"
7. Ketuk "Dikonfirmasi"

**Wireframe - Dialog Konfirmasi Tugas Berbasis Metrik**:

```text
┌──────────────────────────────────────────────┐
│  Konfirmasi Tugas Berbasis Metrik            │
├──────────────────────────────────────────────┤

Nama Tugas:
Ganti oli mobil   (readonly)

Lacak berdasarkan:
Mil   (readonly)

Nilai Metrik Terakhir yang Diselesaikan:
12.500 Mil   (readonly)

──────────────────────────────────────────────
Nilai Metrik Saat Ini
[ 14.520 ] Mil

Delta:
+2.020 Mil   (otomatis)

──────────────────────────────────────────────
Catatan
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Tidak Dikonfirmasi ]    [ Dikonfirmasi ]
└──────────────────────────────────────────────┘
```

---

### TODO-05: Edit Tugas dan Lihat Riwayat

**Tujuan**: Edit informasi tugas dan lihat riwayat penyelesaian.

**Langkah Utama**:
1. Buka daftar tugas
2. Ketuk pada kartu tugas "Ganti filter air"
3. Lihat peringatan: "⚠️ Siklus terkunci karena ada riwayat" (jika ada riwayat)
4. Edit tanggal jatuh tempo berikutnya, waktu pengingat, catatan
5. Ketuk "Simpan"
6. Ketuk "Lihat Riwayat ›" untuk melihat riwayat dengan filter

**Wireframe - Layar Riwayat Tugas**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Kembali]  Riwayat Tugas - Ganti filter air         │
└─────────────────────────────────────────────────────────┘
│  [Semua] [Bulan Ini] [Bulan Lalu] [3 Bulan Terakhir]  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Ganti filter air            [Selesai]           │    │
│  │                                                  │    │
│  │ 📅 Siklus: Setiap 3 bulan                        │    │
│  │ ✅ Diselesaikan pada: 12/01/2025 – 09:10       │    │
│  │ 📝 Catatan: Ganti filter #1 dan #2              │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Ganti filter air            [Selesai]           │    │
│  │                                                  │    │
│  │ 📅 Siklus: Setiap 3 bulan                        │    │
│  │ ✅ Diselesaikan pada: 09/01/2025 – 08:45       │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06: Nonaktifkan dan Hapus Tugas

**Tujuan**: Nonaktifkan atau hapus tugas ketika tidak lagi diperlukan.

**Langkah Utama**:
1. Buka daftar tugas
2. Temukan tugas untuk dinonaktifkan
3. Ketuk switch "Aktif" untuk mematikan
4. Lihat badge "Tidak Aktif" muncul
5. Ketuk switch lagi untuk mengaktifkan kembali
6. Ketuk ikon Hapus (🗑️) untuk menghapus tugas
7. Konfirmasi penghapusan dalam dialog

---

### TODO-07: Konfirmasi Tugas Berbasis Metrik dan Tambah Pengeluaran

**Tujuan**: Konfirmasi tugas berbasis metrik dan secara otomatis menambah pengeluaran terkait.

**Langkah Utama**:
1. Buka daftar tugas
2. Temukan tugas "Ganti oli mobil" (tipe METRIC, hasCost = true)
3. Ketuk tombol "Konfirmasi"
4. Masukkan nilai metrik saat ini: "14.520"
5. Masukkan catatan: "Ganti oli + filter oli"
6. Ketuk "Dikonfirmasi"
7. Lihat dialog "Menimbulkan Pengeluaran?" secara otomatis terbuka
8. Ketuk "Tambah Pengeluaran"
9. Lihat layar "Tambah Pengeluaran" dengan catatan dan kategori sudah terisi
10. Masukkan jumlah: Rp750.000
11. Ketuk "Simpan"

**Wireframe - Dialog Menimbulkan Pengeluaran**:

```text
┌──────────────────────────────────────────────┐
│  Menimbulkan Pengeluaran?                     │
├──────────────────────────────────────────────┤
Apakah Anda ingin menambah pengeluaran untuk
penyelesaian ini?

        [ Batal ]         [ Tambah Pengeluaran ]
└──────────────────────────────────────────────┘
```

## 6. Logika & Aturan

### 6.1 Jenis Tugas

- **Berbasis Waktu (tipe CYCLE)**:
  - Berulang pada jadwal (Hari/Minggu/Bulan/Tahun)
  - Memiliki notifikasi pengingat saat jatuh tempo
  - Konfirmasi hanya dilakukan di layar "Tugas Jatuh Tempo" (daftar bel)
  - Tidak ada tombol "Konfirmasi" pada kartu

- **Berbasis Metrik (tipe METRIC)**:
  - Berulang berdasarkan tonggak metrik (Mil/Jam/Kali/Lainnya)
  - Tidak ada notifikasi (MVP1)
  - Memiliki tombol "Konfirmasi" pada kartu (hanya ditampilkan saat `isActive = true`)
  - Konfirmasi dengan memasukkan nilai metrik saat ini

### 6.2 Status Tugas

- **PENDING**: Mendatang (belum jatuh tempo)
  - Tidak ada badge yang ditampilkan: `nextDueDate - today > 7 hari`
  - Tampilkan badge "Mendatang" (kuning): `0 < nextDueDate - today ≤ 7 hari`
- **OVERDUE**: Terlambat (merah) - `nextDueDate < today` dan belum dikonfirmasi
- **NOT_COMPLETED**: Tidak dilakukan (oranye) - Jatuh tempo tetapi belum dikonfirmasi
- **COMPLETED**: Selesai (hijau) - Dikonfirmasi
- **CANCELLED**: Dibatalkan (abu-abu) - Kejadian ini dibatalkan
- **INACTIVE**: Tidak Aktif (abu-abu) - `isActive = false`

### 6.3 Kunci Siklus/Unit

- Jika ada riwayat (catatan riwayat):
  - **Tipe CYCLE**: Siklus terkunci, tidak dapat diedit
  - **Tipe METRIC**: Unit dan siklus terkunci, tidak dapat diedit
- Tampilkan peringatan: "⚠️ Siklus terkunci karena ada riwayat" atau "⚠️ Unit terkunci karena ada riwayat"

### 6.4 Konfirmasi Tugas Berbasis Metrik

- **Validasi**:
  - Nilai metrik saat ini harus ≥ nilai metrik terakhir yang diselesaikan
  - Jika tidak valid: Tampilkan error "Nilai metrik saat ini harus ≥ nilai metrik terakhir yang diselesaikan"
- **Perbarui Otomatis**:
  - `lastMetricValue` = nilai saat ini
  - `nextMetricValue` = nilai saat ini + siklus
  - `lastCompletedDate` = hari ini
- **Pengeluaran**:
  - Jika `hasCost = true`: Tampilkan dialog "Menimbulkan Pengeluaran?" setelah konfirmasi berhasil
  - Navigasi ke layar "Tambah Pengeluaran" dengan `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Notifikasi

- **Tipe CYCLE**: 
  - Notifikasi dijadwalkan saat membuat/mengedit tugas
  - Notifikasi dibatalkan saat menonaktifkan atau menghapus tugas
  - Notifikasi dijadwalkan ulang saat mengaktifkan kembali (jika `nextDueDate >= today`)
- **Tipe METRIC**: Tidak ada notifikasi (MVP1)

### 6.6 Hitung Tanggal Jatuh Tempo Berikutnya

- **Tipe CYCLE**: 
  - Tanggal jatuh tempo berikutnya dihitung secara otomatis berdasarkan siklus setelah konfirmasi
  - Contoh: Siklus 3 bulan, tanggal jatuh tempo 03/01/2026 → Setelah konfirmasi, tanggal jatuh tempo berikutnya = 06/01/2026
- **Tipe METRIC**: 
  - Jatuh tempo berikutnya = nilai saat ini + siklus
  - Contoh: Nilai saat ini 14.520 mil, siklus 3.000 mil → Jatuh tempo berikutnya = 17.520 mil

## 7. Catatan Penting

1. **Tombol Konfirmasi**:
   - **Tugas berbasis waktu (CYCLE)**: Tidak ada tombol "Konfirmasi" pada kartu. Konfirmasi hanya dilakukan di layar "Tugas Jatuh Tempo" (daftar bel).
   - **Tugas berbasis metrik (METRIC)**: Memiliki tombol "Konfirmasi" pada kartu (hanya ditampilkan saat `isActive = true`).

2. **Ikon Bel**: Ikon bel di header menavigasi ke layar "Tugas Jatuh Tempo" (daftar bel) di mana pengguna dapat mengonfirmasi tugas jatuh tempo (hanya untuk tipe CYCLE).

3. **Kunci Siklus/Unit**: Jika ada riwayat, siklus (CYCLE) atau unit/siklus (METRIC) akan terkunci dan tidak dapat diedit untuk memastikan konsistensi data.

4. **Validasi Metrik**: Saat mengonfirmasi tugas berbasis metrik, nilai metrik saat ini harus ≥ nilai metrik terakhir yang diselesaikan. Jika tidak, aplikasi akan menampilkan error dan mencegah konfirmasi.

5. **Pengeluaran yang Ditimbulkan**: Jika tugas memiliki pengeluaran (`hasCost = true`), setelah konfirmasi berhasil, aplikasi akan bertanya apakah Anda ingin menambah pengeluaran. Jika Anda memilih "Tambah Pengeluaran", aplikasi akan secara otomatis mengisi catatan dan kategori.

6. **Hapus Tugas**: Saat menghapus tugas, semua riwayat terkait juga akan dihapus (cascade delete). Notifikasi juga akan dibatalkan.

7. **Nonaktifkan**: Saat menonaktifkan tugas tipe CYCLE, notifikasi akan dibatalkan. Saat mengaktifkan kembali, notifikasi akan dijadwalkan ulang (jika `nextDueDate >= today`).

8. **Akses Premium**: Modul ini memerlukan Akses Premium. Jika Anda tidak memiliki Premium, aplikasi akan menampilkan dialog meminta upgrade.

