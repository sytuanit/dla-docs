# Ekstra Gelir

## 1. Amaç

**Ekstra Gelir** modülü şunlar gibi sabit döngüsü olmayan tekrarlanmayan geliri kaydetmenize yardımcı olur:
- Online Satışlar
- Serbest Çalışma
- İkramiyeler
- Nakit Hediye
- Diğer düzensiz gelirler

**Tekrarlanan Gelir**'den farklı olarak, ekstra gelirin otomatik döngüsü yoktur, her seferinde manuel olarak girmelisiniz.

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Rastgele, tekrarlanmayan geliri kaydetmek
- Bir zaman dilimindeki toplam geliri takip etmek
- Ekstra gelir eğilimlerini analiz etmek
- Aylık bütçeye hesaplamak

## 3. İlgili Ekranlar

- Ekstra gelir listesi
- Yeni gelir ekle
- Geliri düzenle

## 4. Ana Kullanım

### 4.1 Ekstra Gelir Ekle

1. **İşlevler** → **Ekstra Gelir** seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Kategori**: Seçin veya yeni kategori oluşturun
   - **Tutar**: Alınan tutarı girin
   - **Tarih**: Paranın alındığı tarihi seçin (varsayılan bugün)
   - **Not**: Detaylı açıklama (isteğe bağlı)
4. **Kaydet**'e dokunun

### 4.2 Gelir Listesini Görüntüle

1. **İşlevler** → **Ekstra Gelir** seçin
2. Liste yapılandırılan düzeninize göre görüntülenir (1, 2, 3 veya 4 sütun)
3. Kategori veya nota göre filtrelemek için **Ara** kullanın
4. **Zaman Filtresi** seçin: Bugün / Bu Hafta / Bu Ay / Geçen Ay / Özel

### 4.3 Geliri Düzenle

1. Ekstra gelir listesine gidin
2. Düzenlemek için öğeye uzun basın
3. Menüden **Düzenle** seçin
4. Bilgileri güncelleyin
5. **Kaydet**'e dokunun

### 4.4 Geliri Sil

1. Ekstra gelir listesine gidin
2. Silmek için öğeye uzun basın
3. Menüden **Sil** seçin
4. Silmeyi onaylayın

## 5. UI İllüstrasyonları (Wireframe)

### 5.1 Liste Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Ekstra Gelir                │
├─────────────────────────────────────────┤
│  [🔍 Ara...]                            │
│  [Bu Ay ▼] [Bu Hafta] [Bugün]          │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Online Satışlar                    │ │
│  │ ₺600                               │ │
│  │ 15/11/2024                         │ │
│  │                                    │ │
│  │ [Düzenle] [Sil]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Serbest Çalışma                    │ │
│  │ ₺1.200                             │ │
│  │ 14/11/2024                         │ │
│  │                                    │ │
│  │ [Düzenle] [Sil]                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Toplam: ₺1.800                        │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Ekle/Düzenle Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Ekstra Gelir Ekle            │
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Online Satışlar ▼]                     │
│                                         │
│  Tutar *                                 │
│  [₺600]                                 │
│                                         │
│  Tarih *                                 │
│  [15/11/2024]                           │
│                                         │
│  Not                                     │
│  [A Ürünü Satıldı]                       │
│                                         │
│  [Kaydet] [İptal]                       │
└─────────────────────────────────────────┘
```

## 6. Mantık ve Kurallar

### 6.1 Görüntüleme Düzeni

- Sütun sayısını yapılandırabilirsiniz: 1, 2, 3 veya 4 sütun
- Düzen ayarlarda kaydedilir ve tüm ekstra gelir listelerine uygulanır

### 6.2 Zaman Filtresi

- **Bugün**: Sadece bugünkü geliri gösterir
- **Bu Hafta**: Haftanın başından bugüne kadar
- **Bu Ay**: Ayın başından bugüne kadar
- **Geçen Ay**: Önceki ayın tamamı
- **Özel**: Özel zaman aralığı seçin

### 6.3 Arama

- **Kategori adı** ve **not** içinde arama yapar
- Büyük/küçük harf duyarlı değil
- Yazarken gerçek zamanlı arama

### 6.4 Bütçe Entegrasyonu

- Ekstra gelir bütçedeki "Ekstra Gelir"e hesaplanır
- Toplam aylık geliri takip etmenize yardımcı olur

## 7. Önemli Notlar

- **Döngü Yok**: Ekstra gelirin otomatik döngüsü yoktur, her seferinde manuel olarak girmelisiniz
- **Silinebilir**: Herhangi bir geliri silebilirsiniz
- **Bütçe Entegrasyonu**: Ekstra gelir otomatik olarak mevcut ayın bütçesine hesaplanır

