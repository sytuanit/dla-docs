# Yedekleme ve Geri Yükleme

## 1. Amaç

**Yedekleme ve Geri Yükleme** modülü şunlara yardımcı olur:
- Tüm uygulama verilerini dosyaya yedekleme
- Yedekleme dosyasından veri geri yükleme
- Cihaz hataları veya uygulama yeniden yüklemesi nedeniyle veri kaybından koruma

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Uygulamayı yeniden yüklemeden önce veri yedeklemek
- Verileri yeni cihaza aktarmak
- Veri kaybından sonra veri geri yüklemek
- Periyodik yedeklemeler oluşturmak

## 3. İlgili Ekranlar

- Yedekleme ekranı
- Geri yükleme ekranı

## 4. Ana Kullanım

### 4.1 Veri Yedekle

1. **Ayarlar** → **Yedekleme ve Veri** → **Yedekleme** gidin
2. Bilgileri görüntüleyin:
   - Yedeklenecek kayıt sayısı
   - Beklenen dosya boyutu
3. **Yedekle**'ye dokunun
4. Kayıt konumunu seçin (Dosya sistemi)
5. Yedekleme dosyası şu adla oluşturulacaktır: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Bu dosyayı güvenli bir yerde saklayın (bulut, bilgisayar, vb.)

### 4.2 Veri Geri Yükle

1. **Ayarlar** → **Yedekleme ve Veri** → **Geri Yükleme** gidin
2. Dosya sisteminden yedekleme dosyasını seçin
3. Dosya bilgilerini görüntüleyin:
   - Yedekleme oluşturma tarihi
   - Kayıt sayısı
   - Dosya boyutu
4. **Uyarı**: Geri yükleme mevcut tüm verilerin üzerine yazacaktır
5. **Geri Yükle**'ye dokunun
6. Geri yüklemeyi onaylayın
7. Geri yükleme işleminin tamamlanmasını bekleyin
8. Uygulama otomatik olarak yeniden yüklenecektir

## 5. UI İllüstrasyonları (Wireframe)

### 5.1 Yedekleme Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Veri Yedekle                  │
├─────────────────────────────────────────┤
│  Yedekleme Bilgileri                     │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Kayıt Sayısı                       │ │
│  │ 1.234 kayıt                        │ │
│  │                                    │ │
│  │ Beklenen Boyut                     │ │
│  │ ~2,5 MB                            │ │
│  │                                    │ │
│  │ Yedeklenecek veriler:              │ │
│  │ • Tekrarlanan Gelir                │ │
│  │ • Tekrarlanan Giderler             │ │
│  │ • Günlük Giderler                  │ │
│  │ • Bütçe                            │ │
│  │ • Tasarruf                         │ │
│  │ • Krediler                         │ │
│  │ • Özel Günler                      │ │
│  │ • Kategoriler                      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Yedekle]                              │
└─────────────────────────────────────────┘
```

### 5.2 Geri Yükleme Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Veri Geri Yükle             │
├─────────────────────────────────────────┤
│  Yedekleme Dosyası Seç                  │
│                                         │
│  [Dosya Seç...]                        │
│                                         │
│  Dosya Bilgileri                        │
│  ┌───────────────────────────────────┐ │
│  │ Dosya: dla-backup-2024-11-15.json│ │
│  │                                    │ │
│  │ Oluşturuldu: 15/11/2024 10:30     │ │
│  │                                    │ │
│  │ Kayıt Sayısı: 1.234               │ │
│  │                                    │ │
│  │ Boyut: 2,5 MB                      │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Uyarı                              │
│  Geri yükleme mevcut tüm verilerin     │
│  üzerine yazacaktır. Emin misiniz?     │
│                                         │
│  [Geri Yükle] [İptal]                  │
└─────────────────────────────────────────┘
```

## 6. Mantık ve Kurallar

### 6.1 Yedekleme Dosyası Formatı

- Yedekleme dosyası JSON formatındadır
- Dosya adı: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Tüm verileri içerir: kullanıcılar, kategoriler, işlemler, bütçeler, vb.

### 6.2 Yedeklenen Veriler

- Veritabanındaki tüm tablolar
- Hem sistem hem de kullanıcı verilerini içerir
- İçermez: uygulama ayarları, tercihler (dil, para birimi)

### 6.3 Geri Yükleme

- Geri yükleme mevcut tüm verileri silecektir
- Ardından yedekleme dosyasından veri içe aktaracaktır
- Geri yükleme tamamlandıktan sonra uygulama otomatik olarak yeniden yüklenecektir

### 6.4 Doğrulama

- Uygulama geri yüklemeden önce dosya formatını kontrol eder
- Sürüm uyumluluğunu kontrol eder (varsa)
- Dosya geçersizse hata gösterir

## 7. Önemli Notlar

- **Düzenli Yedekleme**: Periyodik olarak yedeklemelisiniz (haftalık veya aylık)
- **Birden Fazla Yerde Saklayın**: Yedekleme dosyasını birden fazla yerde saklayın (bulut, bilgisayar, USB)
- **Geri Yükleme Mevcut Verileri Kaybedecek**: Geri yüklemeden önce mevcut verileri yedeklediğinizden emin olun
- **Geri Alınamaz**: Geri yüklemeden sonra geri alınamaz

