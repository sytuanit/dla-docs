# Laporan

## 1. Tujuan

Modul **Laporan** menyediakan laporan keuangan detail, membantu Anda:
- Melihat ringkasan keuangan bulan saat ini
- Menganalisis pendapatan dan pengeluaran
- Melacak kemajuan tabungan
- Memperkirakan pengeluaran akhir bulan
- Melihat laporan berdasarkan jenis (Pendapatan, Pengeluaran, Tabungan, Pinjaman)

## 2. Kapan Menggunakan

Gunakan modul ini ketika Anda ingin:
- Melihat ringkasan keuangan
- Menganalisis tren pengeluaran
- Memeriksa kemajuan tujuan tabungan
- Memperkirakan risiko melebihi anggaran
- Melihat laporan detail berdasarkan jenis

## 3. Layar Terkait

- Laporan ringkasan
- Laporan pendapatan
- Laporan pengeluaran
- Laporan tabungan
- Laporan pinjaman

## 4. Penggunaan Utama

### 4.1 Lihat Laporan Ringkasan

1. Buka tab **Laporan** di navigasi bawah
2. Lihat bagian **Kesehatan Keuangan**:
   - Tujuan tabungan dan tabungan aktual (dengan progress bar dan tingkat pencapaian)
   - Arus Kas Bersih dengan rumus detail
   - Sisa anggaran (jika anggaran telah dibuat)
   - Kecepatan pengeluaran dibandingkan dengan bulan sebelumnya (jika data tersedia)
   - Kewajiban pinjaman bulan ini (jika ada)
   - 5 kategori pengeluaran teratas berdasarkan persentase
3. Lihat bagian **Perkiraan Tren Masa Depan** (jika anggaran > 0):
   - Sisa yang diharapkan pada akhir bulan dengan rumus detail
   - Probabilitas pencapaian tujuan tabungan
   - Pembayaran pinjaman mendatang (jika ada)
4. Ketuk pada kartu untuk scroll ke laporan detail yang sesuai

### 4.2 Lihat Laporan Pendapatan

1. Dari layar Laporan, ketuk pada item menu **💵 Pendapatan** di bagian "Laporan Detail"
2. Lihat total pendapatan aktual bulan ini
3. Lihat bagian **Pendapatan Berkala**: Total, diterima, belum diterima, detail untuk setiap item
4. Lihat bagian **Pendapatan Tambahan** (jika ada): Total, detail untuk setiap item, % peningkatan/penurunan
5. Lihat **Tren Pendapatan 3 Bulan** (jika data cukup tersedia)
6. Lihat **Riwayat Pendapatan Bulanan**
7. Lihat **Analisis Pendapatan (Wawasan)**: Persentase, tingkat stabilitas, tren

### 4.3 Lihat Laporan Pengeluaran

1. Dari layar Laporan, ketuk pada item menu **🔥 Pengeluaran** di bagian "Laporan Detail"
2. Lihat total pengeluaran aktual bulan ini dengan % peningkatan/penurunan dibandingkan dengan bulan sebelumnya
3. Lihat bagian **Pengeluaran Berkala**: Total, dibayar, belum dibayar, detail untuk setiap item
4. Lihat bagian **Pengeluaran Harian berdasarkan Kategori**: Kategori teratas dengan jumlah dan persentase
5. Lihat bagian **Lonjakan Pengeluaran** (jika data bulan sebelumnya tersedia)
6. Lihat **Tren Pengeluaran 3 Bulan** (jika data cukup tersedia)
7. Lihat **Riwayat Pengeluaran Bulanan**

### 4.4 Lihat Laporan Anggaran

1. Dari layar Laporan, ketuk pada item menu **📉 Anggaran** di bagian "Laporan Detail" (hanya ditampilkan saat anggaran telah dibuat)
2. Lihat **Ringkasan Anggaran Bulan Ini**: Anggaran bulanan, dibelanjakan (dengan rincian), tersisa, progress bar
3. Ketuk pada "Anggaran Bulanan" untuk melihat **Dialog Detail Anggaran** dengan metode perhitungan
4. Lihat bagian **Varians dari Rencana**: Item pendapatan dan pengeluaran dengan varians, total varians
5. Lihat bagian **Pengeluaran berdasarkan Kategori**: Total, setiap kategori dengan jumlah, persentase, progress bar
6. Ketuk pada kategori untuk melihat daftar pengeluaran dalam kategori tersebut

### 4.5 Lihat Laporan Tabungan

1. Dari layar Laporan, ketuk pada item menu **💾 Tabungan** di bagian "Laporan Detail" (hanya ditampilkan saat rekening tabungan ada)
2. Lihat **Tabungan Aktual Bulan Ini** dengan rumus Arus Kas Bersih
3. Lihat bagian **Analisis Tabungan**: % dari pendapatan, perbandingan dengan bulan sebelumnya, perkiraan akhir bulan
4. Lihat bagian **Daftar Rekening Tabungan**: Semua rekening aktif, diurutkan berdasarkan tanggal jatuh tempo terdekat
5. Lihat **Grafik Pertumbuhan Tabungan 6 Bulan** (jika lebih dari 1 bulan data tersedia)

### 4.6 Lihat Laporan Pinjaman

1. Dari layar Laporan, ketuk pada item menu **💸 Pinjaman** di bagian "Laporan Detail" (hanya ditampilkan saat pinjaman ada)
2. Lihat **Ringkasan Pinjaman**: Saldo utang saat ini, biaya pinjaman bulan ini (dengan rincian pokok + bunga)
3. Lihat bagian **Pembayaran Terdekat**: Tanggal jatuh tempo, status, hari hingga pembayaran berikutnya
4. Lihat bagian **Jadwal Pembayaran Bulanan**: 3 bulan terakhir dengan jumlah dan status
5. Lihat bagian **Analisis Pinjaman (Wawasan)**: Total dibayar, tren saldo utang, suku bunga, risiko keterlambatan pembayaran
6. Lihat **Grafik Pengurangan Utang 6 Bulan** (jika lebih dari 1 bulan data tersedia)

## 5. Contoh & Ilustrasi UI

### 5.1 REPORT-01: Lihat Ringkasan Kesehatan Keuangan dan Perkiraan Tren

**Tujuan**: Lihat ringkasan keuangan bulan saat ini, termasuk kemajuan tabungan, arus kas bersih, sisa anggaran, dan perkiraan akhir bulan.

**Langkah**:
1. Buka tab **Laporan** di navigasi bawah
2. Lihat bagian **Kesehatan Keuangan**:
   - Tujuan tabungan: Rp9.000.000 (20% dari pendapatan)
   - Tabungan aktual: Rp6.300.000
   - Progress bar: 70% - TINGKAT PENCAPAIAN: SEDANG
   - Arus Kas Bersih: +Rp4.200.000 [POSITIF] dengan rumus detail
   - Sisa anggaran: Rp9.300.000 [STABIL] (62% anggaran ≈ 60% waktu)
   - Kecepatan pengeluaran: 12% lebih tinggi dari bulan sebelumnya
   - Kewajiban pinjaman: Rp6.300.000 [DIBAYAR]
   - 5 kategori teratas: Makanan (32%), Belanja (25%), Hiburan (18%), Transportasi (15%), Lainnya (10%)
3. Lihat bagian **Perkiraan Tren Masa Depan**:
   - Sisa yang diharapkan pada akhir bulan: +Rp3.450.000 [SURPLUS] dengan rumus detail
   - Probabilitas pencapaian tujuan: 82% [HAMPIR MENCAPAI]
   - Pembayaran pinjaman mendatang: Hari 25: Rp6.300.000 [DANA CUKUP]

**Wireframe**:
```text
┌──────────────────────┐  ┌──────────────────────┐
│ 🎯 Tujuan Tabungan    │  │ 💾 Tabungan Aktual  │
│ Rp9.000.000          │  │ Rp6.300.000         │
│ 20% dari pendapatan  │  │                      │
└──────────────────────┘  └──────────────────────┘

[██████████████----------------------] 70%
TINGKAT PENCAPAIAN: SEDANG

┌────────────────────────────────────────────────────────────┐
│ Arus Kas Bersih = Tabungan Aktual                        │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ +Rp4.200.000                      [POSITIF]           │ │
│ └────────────────────────────────────────────────────────┘ │
│ Arus Kas Bersih = Pendapatan (berkala + tambahan)         │
│                – Pengeluaran (berkala + harian + pinjaman)│
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 📉 Sisa Anggaran                                           │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ Rp9.300.000                      [STABIL]             │ │
│ └────────────────────────────────────────────────────────┘ │
│ • 62% anggaran ≈ 60% waktu → Pengeluaran dengan kecepatan yang sesuai│
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 💹 Sisa yang Diharapkan pada Akhir Bulan                  │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ Diharapkan: +Rp3.450.000             [SURPLUS]     │ │
│ └────────────────────────────────────────────────────────┘ │
│ • Pengeluaran yang Diharapkan = (Rata-rata Pengeluaran Harian × Hari Tersisa)│
│                + (Pengeluaran Tetap Tertunda)              │
└────────────────────────────────────────────────────────────┘
```

### 5.2 REPORT-02: Lihat Laporan Pendapatan

**Tujuan**: Lihat analisis detail pendapatan bulan ini, termasuk pendapatan berkala, pendapatan tambahan, tren dan wawasan.

**Langkah**:
1. Dari layar Laporan, ketuk pada item menu **💵 Pendapatan** di bagian "Laporan Detail"
2. Lihat **Total Pendapatan Aktual Bulan Ini**: Rp31.500.000
3. Lihat bagian **Pendapatan Berkala**: Total Rp22.500.000 (Diterima: Rp19.500.000, Belum diterima: Rp3.000.000), detail untuk setiap item
4. Lihat bagian **Pendapatan Tambahan**: Total Rp9.000.000 (Freelance: Rp4.500.000, Menjual barang: Rp1.500.000, Bonus kecil: Rp3.000.000), 5% peningkatan dari bulan sebelumnya
5. Lihat **Tren Pendapatan 3 Bulan** (grafik sparkline)
6. Lihat **Riwayat Pendapatan Bulanan**: Bulan ini, bulan sebelumnya, 2 bulan lalu
7. Lihat **Analisis Pendapatan (Wawasan)**: Persentase pendapatan berkala, penilaian stabilitas, % peningkatan/penurunan

**Wireframe**: Lihat `wf-bao-cao-thu-nhap.md`

### 5.3 REPORT-03: Lihat Laporan Pengeluaran

**Tujuan**: Lihat analisis detail pengeluaran bulan ini, termasuk pengeluaran berkala, pengeluaran harian berdasarkan kategori, tren dan kategori lonjakan pengeluaran.

**Langkah**:
1. Dari layar Laporan, ketuk pada item menu **🔥 Pengeluaran** di bagian "Laporan Detail"
2. Lihat **Total Pengeluaran Aktual Bulan Ini**: Rp27.300.000 (12% peningkatan dari bulan sebelumnya)
3. Lihat bagian **Pengeluaran Berkala**: Total Rp12.750.000 (Dibayar: Rp11.250.000, Belum dibayar: Rp1.500.000), detail untuk setiap item
4. Lihat bagian **Pengeluaran Harian berdasarkan Kategori**: Makanan Rp9.750.000 (36%), Belanja Rp4.500.000 (16%), Transportasi Rp3.150.000 (12%), Hiburan Rp2.100.000 (8%), Lainnya Rp1.500.000 (5%)
5. Lihat bagian **Lonjakan Pengeluaran**: Makanan (+Rp1.800.000, +22%), Belanja (+Rp1.200.000, +35%)
6. Lihat **Tren Pengeluaran 3 Bulan** (grafik sparkline)
7. Lihat **Riwayat Pengeluaran Bulanan**: Bulan ini, bulan sebelumnya, 2 bulan lalu

**Wireframe**: Lihat `wf-bao-cao-chi-tieu.md`

### 5.4 REPORT-04: Lihat Laporan Anggaran

**Tujuan**: Lihat ringkasan anggaran bulan ini, termasuk anggaran yang dibelanjakan, tersisa, varians dari rencana, dan pengeluaran berdasarkan kategori.

**Langkah**:
1. Dari layar Laporan, ketuk pada item menu **📉 Anggaran** di bagian "Laporan Detail"
2. Lihat **Ringkasan Anggaran Bulan Ini**:
   - Anggaran bulanan: Rp15.000.000 (ketuk untuk melihat detail perhitungan)
   - Dibelanjakan: Rp5.700.000 (Pengeluaran harian: Rp3.750.000, Varians pengeluaran: +Rp750.000, Varians pendapatan: -Rp300.000)
   - Tersisa: Rp9.300.000
   - Progress bar: 38,0% dengan teks petunjuk dinamis
3. Ketuk pada "Anggaran Bulanan" untuk melihat **Dialog Detail Anggaran** dengan rumus: Anggaran = Pendapatan - Pengeluaran
4. Lihat bagian **Varians dari Rencana**: Setiap item pendapatan/pengeluaran dengan varians, total varians
5. Lihat bagian **Pengeluaran berdasarkan Kategori**: Total, setiap kategori dengan jumlah, persentase, progress bar
6. Ketuk pada kategori untuk melihat daftar pengeluaran dalam kategori tersebut

**Wireframe**: Lihat `wf-bao-cao-ngan-sach.md`

### 5.5 REPORT-05: Lihat Laporan Tabungan

**Tujuan**: Lihat analisis detail tabungan bulan ini, termasuk tabungan aktual, analisis tabungan, daftar rekening tabungan, dan tren.

**Langkah**:
1. Dari layar Laporan, ketuk pada item menu **💾 Tabungan** di bagian "Laporan Detail"
2. Lihat **Tabungan Aktual Bulan Ini**: Rp6.300.000 dengan rumus Arus Kas Bersih detail
3. Lihat bagian **Analisis Tabungan**: Rekening tabungan untuk 20% dari pendapatan, 12% peningkatan dari bulan sebelumnya, perkiraan akhir bulan: Rp7.650.000 (≈85% dari tujuan)
4. Lihat bagian **Daftar Rekening Tabungan**: 3 rekening (Rp60.000.000, Rp7.500.000, Rp30.000.000), diurutkan berdasarkan tanggal jatuh tempo terdekat
5. Lihat **Grafik Pertumbuhan Tabungan 6 Bulan** (grafik garis)

**Wireframe**: Lihat `wf-bao-cao-tiet-kiem.md`

### 5.6 REPORT-06: Lihat Laporan Pinjaman

**Tujuan**: Lihat analisis detail pinjaman, termasuk saldo utang saat ini, biaya pinjaman bulan ini, jadwal pembayaran, wawasan dan tren.

**Langkah**:
1. Dari layar Laporan, ketuk pada item menu **💸 Pinjaman** di bagian "Laporan Detail"
2. Lihat **Ringkasan Pinjaman**: Saldo utang saat ini Rp975.000.000, Biaya pinjaman bulan ini Rp6.300.000 (Pokok: Rp5.250.000 + Bunga: Rp1.050.000)
3. Lihat bagian **Pembayaran Terdekat**: Hari 25 → DIBAYAR, Pembayaran berikutnya dalam 14 hari
4. Lihat bagian **Jadwal Pembayaran Bulanan**: 3 bulan terakhir dengan jumlah dan status
5. Lihat bagian **Analisis Pinjaman (Wawasan)**: Dibayar dalam 3 bulan terakhir: Rp18.900.000, Tren saldo utang menurun stabil, Bunga menyumbang 17% dari pembayaran, Risiko keterlambatan pembayaran: RENDAH
6. Lihat **Grafik Pengurangan Utang 6 Bulan** (grafik garis)

**Wireframe**: Lihat `wf-bao-cao-khoan-vay.md`

### 5.7 REPORT-07: Analisis Pengeluaran berdasarkan Kategori dari Laporan Ringkasan

**Tujuan**: Dari laporan ringkasan, ketuk pada bagian "Pengeluaran berdasarkan Kategori" untuk melihat laporan pengeluaran detail dan analisis lebih dalam.

**Langkah**:
1. Dari layar Laporan ringkasan, scroll ke bagian **Pengeluaran berdasarkan Kategori**
2. Lihat 5 kategori teratas dengan persentase tertinggi
3. Ketuk pada kartu "Pengeluaran berdasarkan Kategori" (dengan ikon chevron-right)
4. Aplikasi secara otomatis scroll ke bagian **Laporan Pengeluaran** di layar yang sama
5. Lihat detail lengkap: Total pengeluaran, pengeluaran berkala, pengeluaran harian berdasarkan kategori (lebih dari 5 teratas), lonjakan pengeluaran, tren dan riwayat

**Wireframe**: Lihat `wf-bao-cao.md` - bagian "Pengeluaran berdasarkan Kategori"

### 5.8 REPORT-08: Lihat Laporan Saat Data Tidak Cukup (Bulan Pertama)

**Tujuan**: Pengguna aplikasi baru melihat laporan di bulan pertama, ketika tidak ada data yang cukup untuk perbandingan dan analisis tren.

**Langkah**:
1. Buka tab **Laporan**
2. Lihat bagian **Kesehatan Keuangan**:
   - Tujuan tabungan dan tabungan aktual (jika anggaran ada)
   - Arus Kas Bersih dengan rumus
   - Sisa anggaran (jika ada)
   - **TIDAK** ditampilkan: "Kecepatan Pengeluaran" (tidak ada data bulan sebelumnya)
3. Lihat bagian **Perkiraan Tren Masa Depan** (jika anggaran > 0)
4. Ketuk pada **Laporan Pendapatan**: Total pendapatan bulan ini, pendapatan berkala dan tambahan, **TIDAK** ditampilkan "Tren 3 Bulan", **HANYA** ditampilkan "Bulan Ini" dalam riwayat
5. Ketuk pada **Laporan Pengeluaran**: Total pengeluaran bulan ini, pengeluaran berkala dan harian, **TIDAK** ditampilkan "Lonjakan Pengeluaran", "Tren 3 Bulan", **HANYA** ditampilkan "Bulan Ini" dalam riwayat

**Wireframe**: Lihat `wf-bao-cao.md` - kartu dengan tampilan kondisional

## 6. Logika & Aturan

### 6.1 Perhitungan Arus Kas Bersih

**Rumus**:
```
Arus Kas Bersih_bulan = 
  (Pendapatan berkala yang benar-benar diterima dalam bulan + Pendapatan tambahan dalam bulan)
  - (Pengeluaran berkala yang benar-benar dibayar dalam bulan + Pengeluaran harian dalam bulan + Pembayaran pinjaman aktual dalam bulan)
```

**Detail**:
- **Pendapatan**: SUM(recurring_income_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date dalam bulan + SUM(extra_income.amount) WHERE occurred_at dalam bulan
- **Pengeluaran**: SUM(recurring_expense_occurrence.amount_snapshot) WHERE status = 'COMPLETED' AND due_date dalam bulan + SUM(daily_expense.amount) WHERE occurred_at dalam bulan + SUM(bank_debt_payment.total_amount) WHERE due_date dalam bulan AND status != 'CANCELLED'
- **Tabungan Aktual**: max(ArusKasBersih_bulan, 0) - Jika Arus Kas Bersih positif: Tabungan = Arus Kas Bersih, Jika Arus Kas Bersih negatif: Tabungan = 0 (pengeluaran berlebih)

### 6.2 Tingkat Pencapaian Tujuan Tabungan

**Rumus**:
```
ratio = Tabungan_bulan / budget.savings_amount
progress% = round(ratio × 100)
```

**Ambang Batas**:
- **BAIK**: progress% ≥ 90
- **SEDANG**: 70 ≤ progress% < 90
- **BURUK**: progress% < 70

### 6.3 Sisa Anggaran

**Rumus**:
- % Sisa Anggaran = (Sisa Anggaran / Total Anggaran) × 100
- % Waktu Tersisa = (Hari Tersisa / Total Hari dalam Bulan) × 100

**Kesimpulan**:
- Jika % anggaran ≈ % waktu: Kecepatan pengeluaran **WARAS**
- Jika % anggaran < % waktu: Pengeluaran **LEBIH CEPAT** dari kecepatan
- Jika % anggaran > % waktu: Pengeluaran **LEBIH LAMBAT** dari kecepatan

**Catatan**: Kartu ini hanya ditampilkan saat anggaran telah dibuat untuk bulan ini.

### 6.4 Perkiraan Akhir Bulan

**Pengeluaran yang Diharapkan**:
```
Pengeluaran_yang_Diharapkan = 
  (Rata-rata_Pengeluaran_Harian × Hari_Tersisa_dalam_Bulan)
  + Total_Pengeluaran_Berkala_Tertunda_Sisa_Bulan
  + Total_Pembayaran_Pinjaman_Bank_Tertunda_dalam_Bulan
```

**Detail**:
- Rata-rata_Pengeluaran_Harian = (Total daily_expense.amount dari awal bulan hingga hari ini) / Hari_Terlalu_dalam_Bulan
- Total_Pengeluaran_Berkala_Tertunda = SUM(recurring_expense_occurrence.amount_snapshot) WHERE status = 'PENDING' AND due_date antara besok hingga akhir bulan
- Total_Pembayaran_Pinjaman_Bank_Tertunda = SUM(bank_debt_payment.total_amount) WHERE due_date antara besok hingga akhir bulan AND status = 'PENDING'

**Sisa yang Diharapkan pada Akhir Bulan**:
```
Sisa_yang_Diharapkan_Akhir_Bulan = ArusKasBersih_bulan - Pengeluaran_yang_Diharapkan
```

**Probabilitas Pencapaian Tujuan Tabungan**:
```
ratio = Sisa_yang_Diharapkan_Akhir_Bulan / budget.savings_amount
progress% = round(ratio × 100)
```

**Label**:
- ≥ 90% → **AKAN MENCAPAI**
- 70–89% → **HAMPIR MENCAPAI**
- < 70% → **SULIT MENCAPAI**

**Catatan**: Perkiraan hanya ditampilkan saat anggaran > 0.

### 6.5 Data Aktual vs Rencana

- **Semua data laporan menggunakan data AKTUAL**:
  - Pendapatan: Kejadian COMPLETED + extra_income
  - Pengeluaran: Kejadian COMPLETED + daily_expense
  - Pembayaran pinjaman: bank_debt_payment dengan due_date dalam bulan (terlepas dari apakah dibayar atau tidak)
- **TIDAK menggunakan data rencana** (kejadian PENDING yang belum jatuh tempo)

## 7. Catatan Penting

- **Data Bulan Saat Ini Saja**: Laporan hanya menampilkan data bulan saat ini
- **Kondisi Tampilan**:
  - Kartu "Sisa Anggaran" hanya ditampilkan saat anggaran telah dibuat untuk bulan ini
  - Kartu "Kecepatan Pengeluaran" hanya ditampilkan saat data bulan sebelumnya tersedia untuk perbandingan
  - Kartu "Kewajiban Pinjaman" hanya ditampilkan saat pinjaman ada
  - Item menu "Anggaran" hanya ditampilkan saat anggaran telah dibuat
  - Item menu "Tabungan" hanya ditampilkan saat rekening tabungan ada
  - Item menu "Pinjaman" hanya ditampilkan saat pinjaman ada
  - Bagian "Perkiraan Tren Masa Depan" hanya ditampilkan saat anggaran > 0
- **Perkiraan Hanya untuk Referensi**: Berdasarkan tren saat ini dan item PENDING
- **Bulan Pertama**: Beberapa kartu/bagian tidak ditampilkan karena kurangnya data perbandingan (misalnya, "Kecepatan Pengeluaran", "Tren 3 Bulan", "Lonjakan Pengeluaran")
- **Kartu Dapat Diketuk**: Mengetuk kartu akan scroll ke laporan detail yang sesuai di layar yang sama

