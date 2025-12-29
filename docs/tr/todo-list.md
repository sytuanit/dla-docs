# Yapılacaklar Listesi

## 1. Amaç

**Yapılacaklar Listesi** modülü, tekrarlayan görevleri yönetmenize ve tamamlanma ilerlemesini takip etmenize yardımcı olur:
- Zamana dayalı tekrarlayan görevler (günlük/haftalık/aylık/yıllık)
- Metrik tabanlı tekrarlayan görevler (mil/saat/kez...)
- Vadesi geldiğinde hatırlatıcılar
- Tamamlanma geçmişi takibi
- Gider kaydı (varsa)

Bu modül, araba bakımı, filtre değişimi, periyodik kontroller gibi önemli görevleri kaçırmamanıza yardımcı olur.

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Zamanlamaya göre tekrarlayan görevler (örn: Her 3 ayda bir su filtresini değiştir)
- Metriklere göre tekrarlayan görevler (örn: Her 3.000 milda bir araba yağı değiştir)
- Vadesi geldiğinde otomatik hatırlatıcılara ihtiyaç duyduğunuzda
- Tamamlanma geçmişini takip etmek istediğinizde
- İlişkili giderleri kaydetmek istediğinizde

## 3. İlgili Ekranlar

- Yapılacaklar listesi ekranı
- Görev türü seçme (Zamana dayalı / Metrik tabanlı)
- Yeni yapılacak ekleme
- Yapılacak düzenleme
- Metrik tabanlı görevi onaylama
- Yapılacak geçmişi
- Vadesi gelen görevler listesi (zil listesi)

## 4. Ana Kullanım

### 4.1 Zamana Dayalı Yapılacak Ekleme

1. **İşlevler** → **Yapılacaklar Listesi**'ni seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. **Zamana Dayalı Yapılacak**'ı seçin
4. Bilgileri doldurun:
   - **Görev Adı**: (gerekli, örn: "Su filtresini değiştir")
   - **Tekrar Döngüsü**: Sayı girin ve birim seçin (Gün/Hafta/Ay/Yıl)
   - **Sonraki Vade Tarihi**: Tarih seçin (yalnızca yarından itibaren seçmeye izin verir)
   - **Hatırlatıcı Saati**: Saat seçin (gerekli, örn: 08:00)
   - **Bu görev gider içerir**: (İsteğe bağlı) Gider varsa işaretleyin
     - İşaretlenirse: **Kategori** seçin (gerekli)
   - **Not**: Ek bilgiler (isteğe bağlı)
5. **Kaydet**'e dokunun

### 4.2 Metrik Tabanlı Yapılacak Ekleme

1. **İşlevler** → **Yapılacaklar Listesi**'ni seçin
2. **+** (FAB) düğmesine dokunun
3. **Metrik Tabanlı Yapılacak**'ı seçin
4. Bilgileri doldurun:
   - **Görev Adı**: (gerekli, örn: "Araba yağı değiştir")
   - **Döngü**: Sayı girin (örn: 3.000)
   - **Birim**: Birim girin (örn: "Mil")
   - **Son Tamamlanan Metrik Değeri**: Mevcut değeri girin (örn: 12.500)
   - **Bu görev gider içerir**: (İsteğe bağlı) Gider varsa işaretleyin
     - İşaretlenirse: **Kategori** seçin (gerekli)
   - **Not**: Ek bilgiler (isteğe bağlı)
5. **Kaydet**'e dokunun

### 4.3 Metrik Tabanlı Görevi Onaylama

1. Yapılacaklar listesine gidin
2. Onaylanacak metrik tabanlı görevi (METRIC türü) bulun
3. Karttaki **Onayla** düğmesine dokunun (yalnızca `isActive = true` olduğunda gösterilir)
4. Bilgileri doldurun:
   - **Mevcut Metrik Değeri**: Mevcut değeri girin (gerekli, ≥ son tamamlanan metrik değeri olmalı)
   - **Not**: (İsteğe bağlı)
5. Otomatik hesaplanan **Delta**'yı görüntüleyin (mevcut değer - son tamamlanan değer)
6. **Onaylandı**'ya dokunun
7. (Görev gider içeriyorsa) **Gider Ekle** veya **İptal**'i seçin

**Not**: Zamana dayalı görevler (CYCLE türü) kartta "Onayla" düğmesine sahip değildir. Onaylama yalnızca "Vadesi Gelen Görevler" (zil listesi) ekranında yapılır.

### 4.4 Liste ve Detayları Görüntüleme

1. **İşlevler** → **Yapılacaklar Listesi**'ni seçin
2. Görev adına göre aramak için **Arama çubuğu**'nu kullanın
3. Filtrelemek için **Filtre çipleri**'ni kullanın:
   - **Tümü**: Tüm görevleri göster
   - **Zamana dayalı**: Yalnızca CYCLE türü görevleri göster
   - **Metrik tabanlı**: Yalnızca METRIC türü görevleri göster
4. Detayları görüntülemek ve düzenlemek için bir görev kartına dokunun

### 4.5 Yapılacak Düzenleme

1. Yapılacaklar listesine gidin
2. Düzenlemek için görev kartına dokunun
3. Bilgileri güncelleyin:
   - **Not**: Geçmiş varsa, **Döngü** (CYCLE) veya **Birim/Döngü** (METRIC) kilitlenir ve düzenlenemez
4. **Kaydet**'e dokunun

### 4.6 Geçmişi Görüntüleme

1. Yapılacaklar listesine gidin
2. Görüntülenecek görevin **Geçmişi Görüntüle ›** bağlantısına dokunun
3. Zamana göre filtrelemek için **Filtre çipleri**'ni kullanın:
   - **Tümü**: Tüm geçmişi göster
   - **Bu Ay**: Yalnızca mevcut aydan geçmişi göster
   - **Geçen Ay**: Yalnızca önceki aydan geçmişi göster
   - **Son 3 Ay**: Yalnızca son 3 aydan geçmişi göster

### 4.7 Görevi Devre Dışı Bırakma/Etkinleştirme

1. Yapılacaklar listesine gidin
2. Devre dışı bırakılacak/etkinleştirilecek görevi bulun
3. Kart alt bilgisindeki **Aktif** anahtarını açın/kapatın
4. Devre dışı bırakılan görevler **"Pasif"** rozeti (gri) gösterir

### 4.8 Yapılacak Silme

1. Yapılacaklar listesine gidin
2. Kart başlığındaki **Sil** simgesine (🗑️) dokunun
3. İletişim kutusunda silmeyi onaylayın
4. Görev ve tüm ilişkili geçmiş silinir

## 5. Örnekler & Arayüz İllüstrasyonları

### TODO-01: Zamana Dayalı Yapılacak Oluşturma (Su Filtresini Değiştir)

**Amaç**: Uygulamanın vadesi geldiğinde otomatik hatırlatması için zamana dayalı bir yapılacak oluşturun.

**Ana Adımlar**:
1. İşlevler → Yapılacaklar Listesi → "+" (FAB) düğmesine dokunun
2. "Zamana Dayalı Yapılacak"ı seçin
3. Görev adını girin: "Su filtresini değiştir"
4. Döngüyü girin: "3" ay
5. Sonraki vade tarihini seçin: 03/01/2026
6. Hatırlatıcı saati seçin: 08:00
7. "Bu görev gider içerir"i işaretleyin, kategori "Faturalar"ı seçin
8. Notu girin: "Filtre #1 ve #2'yi değiştir"
9. "Kaydet"e dokunun

**Wireframe - Zamana Dayalı Yapılacak Ekleme Ekranı**:

```text
┌──────────────────────────────────────────────┐
│ <  Zamana Dayalı Yapılacak Ekle             │
├──────────────────────────────────────────────┤

Görev Adı
[ Su filtresini değiştir            ]

Tekrar Döngüsü
Her [ 3 ] [ Ay ▼ ]
(Birim: Gün / Hafta / Ay / Yıl)

Sonraki Vade Tarihi
[ 03 / 01 / 2026    ▼ ]
İpucu: 
İlk kez vade tarihi.
Sonraki tarihler girilen döngüye göre otomatik hesaplanacaktır.

Hatırlatıcı Saati
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Bu görev gider içerir

┌─────────────────────────────────────┐
│ Kategori *                           │
│ [Faturalar ▼] [+ Yeni Oluştur]       │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Not (isteğe bağlı)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ İptal ]                         [ Kaydet ]
└──────────────────────────────────────────────┘
```

---

### TODO-02: Metrik Tabanlı Yapılacak Oluşturma (Araba Yağı Değiştir)

**Amaç**: Kilometreye göre araba bakımını takip etmek için metrik tabanlı bir yapılacak oluşturun.

**Ana Adımlar**:
1. İşlevler → Yapılacaklar Listesi → "+" (FAB) düğmesine dokunun
2. "Metrik Tabanlı Yapılacak"ı seçin
3. Görev adını girin: "Araba yağı değiştir"
4. Döngüyü girin: "3.000", birim: "Mil"
5. Son tamamlanan metrik değerini girin: "12.500"
6. "Bu görev gider içerir"i işaretleyin, kategori "Araba Bakımı"nı seçin
7. Notu girin: "Yağ + yağ filtresi değiştir"
8. "Kaydet"e dokunun

**Wireframe - Metrik Tabanlı Yapılacak Ekleme Ekranı**:

```text
┌──────────────────────────────────────────────┐
│ <  Metrik Tabanlı Yapılacak Ekle             │
├──────────────────────────────────────────────┤

Görev Adı
[ Araba yağı değiştir                        ]

Döngü
Her [ 3,000 ] Birim [ Mil ]
(Birim: Mil / Saat / Kez / ...)

Son Tamamlanan Metrik Değeri
[ 12,500 ]

──────────────────────────────────────────────
[✓] Bu görev gider içerir

┌─────────────────────────────────────┐
│ Kategori *                           │
│ [Araba Bakımı ▼] [+ Yeni Oluştur] │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Not (isteğe bağlı)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ İptal ]                         [ Kaydet ]
└──────────────────────────────────────────────┘
```

---

### TODO-03: Liste ve Detayları Görüntüleme

**Amaç**: Yapılacakların genel bakışını görüntüleyin, türe göre filtreleyin, arayın ve her görevin detaylarını görüntüleyin.

**Ana Adımlar**:
1. İşlevler → Yapılacaklar Listesi'ne gidin
2. Arama çubuğu ve filtre çipleriyle listeyi görüntüleyin
3. Filtreleri kullanın: "Tümü", "Zamana dayalı", "Metrik tabanlı"
4. Görev adına göre aramak için arama çubuğunu kullanın
5. Detayları görüntülemek için bir görev kartına dokunun

**Wireframe - Yapılacaklar Listesi Ekranı**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Geri]  Yapılacaklar Listesi              [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Ara...                                                │
│                                                          │
│  [Tümü] [Zamana dayalı] [Metrik tabanlı]                │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Kart: Su filtresini değiştir                    │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Su filtresini değiştir    [Tamamlandı] [🗑️]   │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Döngü: Her 3 ay                           │ │    │
│  │ │ ✅ Son tamamlandı: 12/01/2025                │ │    │
│  │ │ 📅 Sonraki vade tarihi: 03/01/2026           │ │    │
│  │ │ ⏳ 76 gün kaldı                               │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Geçmişi Görüntüle ›                 [⚪ Aktif]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Kart: Araba yağı değiştir                       │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Araba yağı değiştir                 [🗑️]      │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Takip: Mil                                │ │    │
│  │ │ ✅ Son onaylandı: 12/02/2025                 │ │    │
│  │ │ 🔢 Son metrik değeri: 12.500 mil            │ │    │
│  │ │ 🎯 Sonraki vade: 14.500 mil                  │ │    │
│  │ │ ⏳ ~300 mil kaldı                             │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Onayla]                                    │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Geçmişi Görüntüle ›                 [⚪ Aktif]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-04: Metrik Tabanlı Görevi Onaylama (Araba Yağı Değiştir)

**Amaç**: Mevcut metrik değerini girerek metrik tabanlı bir görevin tamamlanmasını onaylayın.

**Ana Adımlar**:
1. Yapılacaklar listesine gidin
2. "Araba yağı değiştir" görevini (METRIC türü) bulun
3. "Onayla" düğmesine dokunun
4. Mevcut metrik değerini girin: "14.520"
5. Otomatik hesaplanan deltayı görüntüleyin: "+2.020 mil"
6. Notu girin: "Yağ + yağ filtresi değiştirildi"
7. "Onaylandı"ya dokunun

**Wireframe - Metrik Tabanlı Görevi Onaylama İletişim Kutusu**:

```text
┌──────────────────────────────────────────────┐
│  Metrik Tabanlı Görevi Onayla               │
├──────────────────────────────────────────────┤

Görev Adı:
Araba yağı değiştir   (salt okunur)

Takip:
Mil   (salt okunur)

Son Tamamlanan Metrik Değeri:
12.500 Mil   (salt okunur)

──────────────────────────────────────────────
Mevcut Metrik Değeri
[ 14,520 ] Mil

Delta:
+2,020 Mil   (otomatik)

──────────────────────────────────────────────
Not
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ Onaylanmadı ]    [ Onaylandı ]
└──────────────────────────────────────────────┘
```

---

### TODO-05: Yapılacak Düzenleme ve Geçmişi Görüntüleme

**Amaç**: Yapılacak bilgilerini düzenleyin ve tamamlanma geçmişini görüntüleyin.

**Ana Adımlar**:
1. Yapılacaklar listesine gidin
2. "Su filtresini değiştir" görev kartına dokunun
3. Uyarıyı görüntüleyin: "⚠️ Geçmiş olduğu için döngü kilitli" (geçmiş varsa)
4. Sonraki vade tarihini, hatırlatıcı saatini, notu düzenleyin
5. "Kaydet"e dokunun
6. Filtrelerle geçmişi görüntülemek için "Geçmişi Görüntüle ›"ye dokunun

**Wireframe - Yapılacak Geçmişi Ekranı**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Geri]  Yapılacak Geçmişi - Su filtresini değiştir   │
└─────────────────────────────────────────────────────────┘
│  [Tümü] [Bu Ay] [Geçen Ay] [Son 3 Ay]                    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Su filtresini değiştir            [Tamamlandı]      │    │
│  │                                                  │    │
│  │ 📅 Döngü: Her 3 ay                                 │    │
│  │ ✅ Tamamlandı: 12/01/2025 – 09:10             │    │
│  │ 📝 Not: Filtre #1 ve #2'yi değiştir                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Su filtresini değiştir            [Tamamlandı]      │    │
│  │                                                  │    │
│  │ 📅 Döngü: Her 3 ay                                 │    │
│  │ ✅ Tamamlandı: 09/01/2025 – 08:45             │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### TODO-06: Yapılacak Devre Dışı Bırakma ve Silme

**Amaç**: Artık gerekmediğinde bir yapılacak görevi devre dışı bırakın veya silin.

**Ana Adımlar**:
1. Yapılacaklar listesine gidin
2. Devre dışı bırakılacak görevi bulun
3. "Aktif" anahtarını kapatmak için dokunun
4. "Pasif" rozetinin göründüğünü görüntüleyin
5. Tekrar etkinleştirmek için anahtarı tekrar dokunun
6. Görevi silmek için Sil simgesine (🗑️) dokunun
7. İletişim kutusunda silmeyi onaylayın

---

### TODO-07: Metrik Tabanlı Görevi Onaylama ve Gider Ekleme

**Amaç**: Metrik tabanlı bir görevi onaylayın ve ilişkili gideri otomatik olarak ekleyin.

**Ana Adımlar**:
1. Yapılacaklar listesine gidin
2. "Araba yağı değiştir" görevini bulun (METRIC türü, hasCost = true)
3. "Onayla" düğmesine dokunun
4. Mevcut metrik değerini girin: "14.520"
5. Notu girin: "Yağ + yağ filtresi değiştirildi"
6. "Onaylandı"ya dokunun
7. "Gider Oluştu mu?" iletişim kutusunun otomatik açıldığını görüntüleyin
8. "Gider Ekle"ye dokunun
9. Not ve kategori önceden doldurulmuş "Gider Ekle" ekranını görüntüleyin
10. Tutarı girin: 1.500 TRY
11. "Kaydet"e dokunun

**Wireframe - Gider Oluştu İletişim Kutusu**:

```text
┌──────────────────────────────────────────────┐
│  Gider Oluştu mu?                            │
├──────────────────────────────────────────────┤
Bu tamamlanma için bir gider eklemek
istiyor musunuz?

        [ İptal ]         [ Gider Ekle ]
└──────────────────────────────────────────────┘
```

## 6. Mantık & Kurallar

### 6.1 Yapılacak Türleri

- **Zamana dayalı (CYCLE türü)**:
  - Zamanlamaya göre tekrarlar (Gün/Hafta/Ay/Yıl)
  - Vadesi geldiğinde hatırlatıcı bildirimleri vardır
  - Onaylama yalnızca "Vadesi Gelen Görevler" (zil listesi) ekranında yapılır
  - Kartta "Onayla" düğmesi yoktur

- **Metrik tabanlı (METRIC türü)**:
  - Metrik kilometre taşlarına göre tekrarlar (Mil/Saat/Kez/Diğer)
  - Bildirim yok (MVP1)
  - Kartta "Onayla" düğmesi vardır (yalnızca `isActive = true` olduğunda gösterilir)
  - Mevcut metrik değerini girerek onaylama

### 6.2 Yapılacak Durumu

- **BEKLİYOR**: Yaklaşan (henüz vadesi gelmedi)
  - Rozet gösterilmez: `nextDueDate - bugün > 7 gün`
  - "Yaklaşan" rozeti göster (sarı): `0 < nextDueDate - bugün ≤ 7 gün`
- **VADESİ GEÇMİŞ**: Vadesi geçmiş (kırmızı) - `nextDueDate < bugün` ve onaylanmadı
- **TAMAMLANMADI**: Yapılmadı (turuncu) - Vadesi geldi ancak onaylanmadı
- **TAMAMLANDI**: Tamamlandı (yeşil) - Onaylandı
- **İPTAL EDİLDİ**: İptal edildi (gri) - Bu oluşum iptal edildi
- **PASİF**: Pasif (gri) - `isActive = false`

### 6.3 Döngü/Birim Kilitleme

- Geçmiş varsa (geçmiş kayıtları):
  - **CYCLE türü**: Döngü kilitli, düzenlenemez
  - **METRIC türü**: Birim ve döngü kilitli, düzenlenemez
- Uyarı göster: "⚠️ Geçmiş olduğu için döngü kilitli" veya "⚠️ Geçmiş olduğu için birim kilitli"

### 6.4 Metrik Tabanlı Görevi Onaylama

- **Doğrulama**:
  - Mevcut metrik değeri ≥ son tamamlanan metrik değeri olmalıdır
  - Geçersizse: Hata göster "Mevcut metrik değeri ≥ son tamamlanan metrik değeri olmalıdır"
- **Otomatik Güncelleme**:
  - `lastMetricValue` = mevcut değer
  - `nextMetricValue` = mevcut değer + döngü
  - `lastCompletedDate` = bugün
- **Giderler**:
  - `hasCost = true` ise: Başarılı onaylamadan sonra "Gider Oluştu mu?" iletişim kutusunu göster
  - `initialNote`, `initialCategoryId`, `todoHistoryId` ile "Gider Ekle" ekranına git

### 6.5 Bildirimler

- **CYCLE türü**: 
  - Bildirimler görev oluşturulurken/düzenlenirken zamanlanır
  - Bildirimler görev devre dışı bırakılırken veya silinirken iptal edilir
  - Bildirimler yeniden etkinleştirilirken yeniden zamanlanır (`nextDueDate >= bugün` ise)
- **METRIC türü**: Bildirim yok (MVP1)

### 6.6 Sonraki Vade Tarihini Hesaplama

- **CYCLE türü**: 
  - Sonraki vade tarihi onaylamadan sonra döngüye göre otomatik hesaplanır
  - Örnek: Döngü 3 ay, vade tarihi 03/01/2026 → Onaylamadan sonra, sonraki vade tarihi = 06/01/2026
- **METRIC türü**: 
  - Sonraki vade = mevcut değer + döngü
  - Örnek: Mevcut değer 14.520 mil, döngü 3.000 mil → Sonraki vade = 17.520 mil

## 7. Önemli Notlar

1. **Onayla Düğmesi**:
   - **Zamana dayalı görevler (CYCLE)**: Kartta "Onayla" düğmesi yoktur. Onaylama yalnızca "Vadesi Gelen Görevler" (zil listesi) ekranında yapılır.
   - **Metrik tabanlı görevler (METRIC)**: Kartta "Onayla" düğmesi vardır (yalnızca `isActive = true` olduğunda gösterilir).

2. **Zil Simgesi**: Başlıktaki zil simgesi, kullanıcıların vadesi gelen görevleri onaylayabileceği "Vadesi Gelen Görevler" (zil listesi) ekranına gider (yalnızca CYCLE türü için).

3. **Döngü/Birim Kilitleme**: Geçmiş varsa, döngü (CYCLE) veya birim/döngü (METRIC) kilitlenir ve veri tutarlılığını sağlamak için düzenlenemez.

4. **Metrik Doğrulama**: Metrik tabanlı bir görevi onaylarken, mevcut metrik değeri ≥ son tamamlanan metrik değeri olmalıdır. Değilse, uygulama bir hata gösterir ve onaylamayı engeller.

5. **Oluşan Giderler**: Bir görev gider içeriyorsa (`hasCost = true`), başarılı onaylamadan sonra uygulama bir gider eklemek isteyip istemediğinizi sorar. "Gider Ekle"yi seçerseniz, uygulama otomatik olarak notu ve kategoriyi önceden doldurur.

6. **Görev Silme**: Bir görevi silerken, tüm ilişkili geçmiş de silinir (kademeli silme). Bildirimler de iptal edilir.

7. **Devre Dışı Bırakma**: Bir CYCLE türü görevi devre dışı bırakırken, bildirimler iptal edilir. Yeniden etkinleştirirken, bildirimler yeniden zamanlanır (`nextDueDate >= bugün` ise).

8. **Premium Erişim**: Bu modül Premium Erişim gerektirir. Premium'unuz yoksa, uygulama yükseltme isteyen bir iletişim kutusu gösterir.

