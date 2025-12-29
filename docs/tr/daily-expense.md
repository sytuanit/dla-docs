# Günlük Giderler

## 1. Amaç

**Günlük Giderler** modülü şunlar gibi düzenli, sabit olmayan giderleri kaydetmenize yardımcı olur:
- Yemek ve Restoran
- Alışveriş
- Ulaşım
- Eğlence
- Diğer esnek giderler

**Tekrarlanan Giderler**'den farklı olarak, günlük giderler genellikle tutar ve sıklık açısından değişir ve sabit döngüsü yoktur.

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Rastgele, tekrarlanmayan giderleri kaydetmek
- Bütçeyi kontrol etmek için günlük harcamaları takip etmek
- Kategoriye göre harcama eğilimlerini analiz etmek
- Bir zaman dilimindeki toplam harcamayı görüntülemek

## 3. İlgili Ekranlar

- Günlük giderler listesi
- Yeni gider ekle
- Gideri düzenle

## 4. Ana Kullanım

### 4.1 Günlük Gider Ekle

1. **İşlevler** → **Günlük Giderler** seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Kategori**: Kategori seçin (veya varsayılan kategori yapılandırıldıysa kullanın)
   - **Tutar**: Harcanan tutarı girin
   - **Tarih**: Gider tarihini seçin (varsayılan bugün)
   - **Not**: Detaylı açıklama (isteğe bağlı)
4. **Kaydet**'e dokunun

### 4.2 Gider Listesini Görüntüle

1. **İşlevler** → **Günlük Giderler** seçin
2. Liste yapılandırılan düzeninize göre görüntülenir (2, 3 veya 4 sütun)
3. Kategori veya nota göre filtrelemek için **Ara** kullanın
4. **Zaman Filtresi** seçin: Bugün / Bu Hafta / Bu Ay / Geçen Ay / Özel

### 4.3 Gideri Düzenle

1. Günlük giderler listesine gidin
2. Düzenlemek için öğeye uzun basın
3. Menüden **Düzenle** seçin
4. Bilgileri güncelleyin
5. **Kaydet**'e dokunun

### 4.4 Gideri Sil

1. Günlük giderler listesine gidin
2. Silmek için öğeye uzun basın
3. Menüden **Sil** seçin
4. Silmeyi onaylayın

### 4.5 Varsayılan Kategori Ayarla

1. **Ayarlar** → **Kategoriler** → **Günlük Gider Kategorileri** gidin
2. Varsayılan olarak ayarlamak istediğiniz kategoriye dokunun
3. **Varsayılan Olarak Ayarla** seçin
4. Yeni gider eklerken, bu kategori otomatik olarak seçilir

## 5. UI İllüstrasyonları (Wireframe)

### 5.1 Liste Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Günlük Giderler              │
├─────────────────────────────────────────┤
│  [🔍 Ara...]                            │
│  [Bugün ▼] [Bu Hafta] [Bu Ay]          │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐           │
│  │ Yemek│ │ Alışv│ │ Taksi│           │
│  │ Dışarı│ │ eriş │ │      │           │
│  │      │ │      │ │      │           │
│  │ ₺60  │ │ ₺240 │ │ ₺30  │           │
│  │      │ │      │ │      │           │
│  │ 15/11│ │ 15/11│ │ 14/11│           │
│  └──────┘ └──────┘ └──────┘           │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐           │
│  │ Kahve│ │ Diğer│ │      │           │
│  │      │ │      │ │      │           │
│  │      │ │      │ │      │           │
│  │ ₺30  │ │ ₺120 │ │      │           │
│  │      │ │      │ │      │           │
│  │ 13/11│ │ 12/11│ │      │           │
│  └──────┘ └──────┘ └──────┘           │
│                                         │
│  Toplam: ₺480                          │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Ekle/Düzenle Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Günlük Gider Ekle            │
├─────────────────────────────────────────┤
│  Kategori *                              │
│  [Yemek Dışarı ▼]                        │
│                                         │
│  Tutar *                                 │
│  [₺60]                                  │
│                                         │
│  Tarih *                                 │
│  [15/11/2024]                           │
│                                         │
│  Not                                     │
│  [Arkadaşla öğle yemeği]                │
│                                         │
│  [Kaydet] [İptal]                       │
└─────────────────────────────────────────┘
```

## 6. Mantık ve Kurallar

### 6.1 Görüntüleme Düzeni

- Sütun sayısını yapılandırabilirsiniz: 2, 3 veya 4 sütun
- Düzen ayarlarda kaydedilir ve tüm gider listelerine uygulanır

### 6.2 Zaman Filtresi

- **Bugün**: Sadece bugünkü giderleri gösterir
- **Bu Hafta**: Haftanın başından bugüne kadar
- **Bu Ay**: Ayın başından bugüne kadar
- **Geçen Ay**: Önceki ayın tamamı
- **Özel**: Özel zaman aralığı seçin

### 6.3 Arama

- **Kategori adı** ve **not** içinde arama yapar
- Büyük/küçük harf duyarlı değil
- Yazarken gerçek zamanlı arama

### 6.4 Varsayılan Kategori

- Varsayılan kategori ayarladıysanız, ekleme ekranını açtığınızda bu kategori otomatik olarak seçilir
- Not da kategoriye göre otomatik doldurulabilir (yapılandırıldıysa)

### 6.5 Toplam Giderler

- Toplam giderler şu anda seçili zaman filtresine göre hesaplanır
- Listenin altında gösterilir

## 7. Önemli Notlar

- **Döngü Yok**: Günlük giderlerin otomatik döngüsü yoktur, her seferinde manuel olarak girmelisiniz
- **Silinebilir**: Herhangi bir gideri silebilirsiniz (tekrarlanan giderlerden farklı olarak)
- **Bütçe Entegrasyonu Yok**: Günlük giderler otomatik olarak bütçeye hesaplanmaz (kendiniz takip etmelisiniz)
- **Özel Kategoriler**: Ayarlarda yeni kategoriler oluşturabilirsiniz

