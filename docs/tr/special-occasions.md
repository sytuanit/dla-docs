# Özel Günler

## 1. Amaç

**Özel Günler** modülü, yıl boyunca özel günleri yönetmenize ve bunlara hazırlanmanıza yardımcı olur:
- Özel günleri yönetme (doğum günleri, tatiller, vb.)
- Yapılacaklar listesi oluşturma (hazırlık adımları)
- Her hazırlık adımına kontrol listesi ekleme
- Gün öncesi hatırlatıcılar
- Hazırlık ilerlemesini takip etme

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Yıl boyunca özel günleri yönetmek istediğinizde
- Önemli günlere hazırlanmak istediğinizde
- Yapılacaklar listesi oluşturmak istediğinizde
- Gün öncesi hatırlatıcılar almak istediğinizde

## 3. İlgili Ekranlar

- Özel günler listesi
- Yeni özel gün ekleme
- Gün detayları ve hazırlık adımları
- Hazırlık adımı ekleme
- Kontrol listesi seçme
- Yeni kontrol listesi oluşturma

## 4. Ana Kullanım

### 4.1 Özel Gün Ekleme

1. **İşlevler** → **Özel Günler**'i seçin
2. **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Gün Adı**: (örn: "Annemin Doğum Günü")
   - **Tarih**: Gün/ay seçin (DatePicker yalnızca gün/ay seçer, yıl yok)
   - **Ay Takvimi Kullan**: (İsteğe bağlı) Ay takvimi kullanmak istiyorsanız işaretleyin
     - İşaretlenirse: Ay günü ve ayını girin, uygulama en yakın güneş tarihini otomatik hesaplar
   - **Tekrar**: Yıllık / Sadece Bu Yıl
   - **Bildirim Göster**: Saat seçin (gerekli, örn: 07:00)
   - **Not**: Ek bilgiler (isteğe bağlı)
4. (İsteğe bağlı) Hazırlık adımları ekleyin (bkz. 4.2)
5. **Kaydet**'e dokunun

### 4.2 Hazırlık Adımı Ekleme

1. Yeni gün eklerken: "Hazırlık Adımları" bölümünde **+ Adım Ekle**'ye dokunun
2. Veya gün detaylarından: **+ Adım Ekle**'ye dokunun
3. Bilgileri doldurun:
   - **Ne Zaman?**: "X gün önce" veya "Gününde"
   - **Gün Sayısı**: ("X gün önce" seçilirse) Gün sayısını girin
   - **Bildirim Göster**: Saat seçin (gerekli)
   - **Tamamlanana Kadar Günlük Tekrar**: (İsteğe bağlı) Günlük hatırlatıcılar istiyorsanız işaretleyin
   - **İçerik**: Adım adı (gerekli, örn: "Hediye Al")
   - **Not**: (İsteğe bağlı)
   - **Kontrol Listesi Kullan**: (İsteğe bağlı) Alışveriş kontrol listesiyle bağlantı kurmak için işaretleyin
4. **Ekle**'ye (veya FAB "Uygula") dokunun

### 4.3 Kontrol Listesi Oluşturma

1. Hazırlık adımı eklerken, **Kontrol Listesi Kullan**'ı işaretleyin
2. "Alışveriş Kontrol Listesi Seç" ekranı otomatik açılır
3. FAB **+** ile yeni kontrol listesi oluşturun
4. Kontrol listesi adını girin
5. Öğeler ekleyin:
   - Öğe adını girin
   - Yeni öğe eklemek için **+**'ya dokunun
6. **Kaydet**'e dokunun
7. Yeni kontrol listesi otomatik seçilir ve "Hazırlık Adımı Ekle" ekranına döner

### 4.4 Adımı Tamamlandı Olarak İşaretleme

1. Özel gün detaylarına gidin
2. İşaretlenecek adımı bulun
3. Onay kutusuna [ ] dokunarak [✓] yapın
4. Kontrol listesi varsa, kontrol listesi adına dokunarak görüntüleyin ve öğeleri işaretleyin/işareti kaldırın

### 4.5 İlerlemeyi Görüntüleme

1. Özel gün detaylarına gidin
2. "Genel Bakış" bölümünü görüntüleyin:
   - Hazırlık Adımları: Toplam adım sayısı
   - Tamamlandı: İşaretlenen adımlar / Toplam adımlar
   - Durum: Başlamadı / Devam Ediyor / Tamamlandı

### 4.6 Özel Günü Düzenleme

1. Özel gün detaylarına gidin
2. Başlıktaki **Düzenle ›** bağlantısına dokunun
3. Bilgileri düzenleyin: Ad, tarih, tekrar, hatırlatıcı saati, not
4. **Kaydet**'e dokunun

### 4.7 Hazırlık Adımını Düzenleme

1. Özel gün detaylarına gidin
2. Düzenlemek için adıma dokunun (Sil simgesi hariç tüm öğeye tıklayın)
3. Bilgileri düzenleyin: Zaman, içerik, kontrol listesi
4. **Uygula**'ya (veya FAB) dokunun

## 5. Örnekler & Arayüz İllüstrasyonları

### OCCASION-01: Yeni Özel Gün Oluşturma (Hazırlık Adımlarıyla Doğum Günü)

**Amaç**: Uygulamanın gün gelmeden otomatik hatırlatması için hazırlık adımlarıyla yeni bir özel gün (doğum günü) oluşturun.

**Ana Adımlar**:
1. İşlevler → Özel Günler → "+" (FAB) düğmesine dokunun
2. Gün adını girin, tarih seçin (01/05), tekrar "Yıllık" seçin, hatırlatıcı saati seçin (07:00)
3. Hazırlık adımı 1 ekleyin: "7 gün önce – 08:00" - "Hediye Al"
4. Hazırlık adımı 2 ekleyin: "1 gün önce – 19:00" - "Pasta Sipariş Et"
5. "Kaydet"e dokunun

**Wireframe - Özel Gün Ekleme Ekranı**:

```text
┌──────────────────────────────────────────────┐
│ <  Özel Gün Ekle                             │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Gün Bilgileri                              │
│                                               │
│ Gün Adı *                                     │
│ [ An'ın Doğum Günü                    ]       │
│                                               │
│ Tarih                                         │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker yalnızca gün/ay seçer)          │
│                                               │
│ [ ] Ay Takvimi Kullan                         │
│                                               │
│ Tekrar                                        │
│ (•) Yıllık                                     │
│ ( ) Sadece Bu Yıl                             │
│                                               │
│ Bildirim Göster *                            │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Not (isteğe bağlı)                            │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Hazırlık Adımları          [ + Adım Ekle ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Hediye Al                   [Sil Simgesi] │ │
│ │     7 gün önce – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Pasta Sipariş Et                   [Sil Simgesi] │ │
│ │     1 gün önce – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ İptal ]                        [ Kaydet ]
```

---

### OCCASION-02: Ay Takvimi Kullanarak Özel Gün Oluşturma (Alışveriş Kontrol Listesiyle Anma Günü)

**Amaç**: Alışveriş kontrol listesiyle bağlantılı hazırlık adımlarıyla ay takvimi kullanarak özel gün (Anma Günü) oluşturarak sunum satın almayı takip edin.

**Ana Adımlar**:
1. İşlevler → Özel Günler → "+" (FAB) düğmesine dokunun
2. Gün adını girin "Annemin Anma Günü", "Ay Takvimi Kullan"ı işaretleyin
3. Ay tarihini girin: 15/11, uygulama otomatik güneş tarihini hesaplar: 12/15/2025
4. Adım 2'nin kontrol listesi bağlantısı "sunum satın al" olan 3 hazırlık adımı ekleyin
5. "Kaydet"e dokunun

**Wireframe - Ay Tarihi Seçme**:

```text
│ │ │ Ay Tarihi                                   │ │ │
│ │ │ Gün (1-30)    Ay (1-12)                     │ │ │
│ │ │ [ 15 ]        [ 11 ]                         │ │ │
│ │ │                                               │ │ │
│ │ │ Güneş Tarihi (otomatik hesaplanan - yalnızca gösterim)  │ │ │
│ │ │ [ Metin: 12/15/2025                 ]         │ │ │
│ │ │ (Bu gelecekteki EN YAKIN güneş tarihidir)│ │ │
```

---

### OCCASION-03: Özel Günlerin Listesini ve Detaylarını Görüntüleme

**Amaç**: Özel günlerin genel bakışını görüntüleyin, zamana göre filtreleyin ve hazırlık ilerlemesiyle her günün detaylarını görüntüleyin.

**Ana Adımlar**:
1. İşlevler → Özel Günler'e gidin
2. "Tümü", "Yaklaşan", "Bu Ay" filtresiyle listeyi görüntüleyin
3. Gün kartına dokunarak detayları görüntüleyin
4. Genel bakışı görüntüleyin: Adım sayısı, Tamamlandı, Durum
5. Onay kutusunu işaretleyerek adımı tamamlandı olarak işaretleyin

**Wireframe - Özel Günler Listesi Ekranı**:

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Özel Günler Listesi                                     │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Gün Ekle ]                                        │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filtre: [ Tümü ]  [ Yaklaşan ]  [ Bu Ay ]          │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Annemin Anma Günü    [Devam Ediyor] [Sil Simgesi] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 12/15/2025 • 15/11 (Ay) • 10 gün kaldı          │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Gerekli Hazırlık Adımları:                        │ │ │
│ │ │   [✓] 3 gün önce – Sunumları listele               │ │ │
│ │ │   [ ] 1 gün önce – Sunumlar için alışverişe git   │ │ │
│ │ │   [ ] Gününde – Sunak / tören hazırla               │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Wireframe - Özel Gün Detayları Ekranı**:

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Özel Gün Detayları                                   │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Annemin Anma Günü                       [Düzenle ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 12/15/2025 (Güneş) • 15/11 (Ay Takvimi)          │ │ │
│ │ │ 10 gün kaldı • Tekrar: Yıllık                     │ │ │
│ │ │                                                      │ │ │
│ │ │ Not:                                             │ │ │
│ │ │ Küçük yemek, beyaz çiçekler, misafirleri sınırla.│ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Genel Bakış                                         │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Hazırlık Adımları: 3                              │ │ │
│ │ │ Tamamlandı: 1 / 3                                 │ │ │
│ │ │ Durum: [Devam Ediyor]                            │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Hazırlık Adımları                  [ + Adım Ekle ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] Sunumları listele                    [Sil Simgesi]           │ │ │
│ │ │     3 gün önce – 08:00                        │ │ │
│ │ │     09:15'te tamamlandı – 12/12/2025               │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Sunumlar için alışverişe git            [Sil Simgesi]            │ │ │
│ │ │     1 gün önce – 19:00                      │ │ │
│ │ │     Tamamlanana kadar günlük tekrar                  │ │ │
│ │ │     Alışveriş Kontrol Listesi: sunum satın al ›           │ │ │
│ │ │     [✓] 8 öğeden 3'ü tamamlandı                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### OCCASION-04: Alışveriş Kontrol Listesiyle Hazırlık Adımı Ekleme

**Amaç**: Özel gün için yeni hazırlık adımı ekleyin ve alışverişi takip etmek için alışveriş kontrol listesiyle bağlantı kurun.

**Ana Adımlar**:
1. Özel gün detaylarına gidin → "+ Adım Ekle"ye dokunun
2. "Ne Zaman?" seçin: "X gün önce", gün sayısını girin: 1
3. Hatırlatıcı saati seçin: 19:00
4. "Tamamlanana Kadar Günlük Tekrar"ı etkinleştirin
5. İçeriği girin: "Sunumlar için alışverişe git"
6. "Kontrol Listesi Kullan"ı işaretleyin → "sunum satın al" kontrol listesini seçin
7. "Ekle"ye dokunun

**Wireframe - Hazırlık Adımı Ekleme Ekranı**:

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Hazırlık Adımı Ekle                                       │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Hazırlık Zamanı                                      │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Ne Zaman? * (gerekli)                              │ │ │
│ │ │ [ X gün önce         ▼ ]                           │ │ │
│ │ │                                                      │ │ │
│ │ │ Gün Sayısı * (yalnızca "X gün önce" seçildiğinde gösterilir) │ │ │
│ │ │ [  1  ]  gün önce                                   │ │ │
│ │ │                                                      │ │ │
│ │ │ Bildirim Göster * (gerekli)                        │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Tamamlanana kadar günlük tekrar                  │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 İçerik                                               │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ İçerik * (gerekli)                                 │ │ │
│ │ │ [ Sunumlar için alışverişe git               ]        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 Alışveriş Kontrol Listesiyle Bağlantı Kur?          │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Kontrol Listesi Kullan                            │ │ │
│ │ │ Alışveriş Kontrol Listesi: sunum satın al ›    [Değiştir Simgesi]  │ │ │
│ │ │ (8 öğe)                                              │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ İptal ]                        [ Ekle ]             │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### OCCASION-05: Hazırlık Adımını Tamamlandı Olarak İşaretleme ve Kontrol Listesi İlerlemesini Görüntüleme

**Amaç**: Hazırlık adımlarını tamamlandı olarak işaretleyin ve alışveriş kontrol listesi ilerlemesini takip edin.

**Ana Adımlar**:
1. Özel gün detaylarına gidin
2. İlerleme gösteren kontrol listesiyle adımı görüntüleyin "8 öğeden 3'ü tamamlandı"
3. Detayları görüntülemek ve öğeleri işaretlemek/işareti kaldırmak için kontrol listesi adına dokunun
4. Adımı tamamlandı olarak işaretlemek için adım onay kutusunu işaretleyin
5. "Genel Bakış"ın gerçek zamanlı güncellendiğini görüntüleyin

---

### OCCASION-06: Özel Günü ve Hazırlık Adımlarını Düzenleme

**Amaç**: Oluşturduktan sonra özel gün bilgilerini ve hazırlık adımlarını düzenleyin.

**Ana Adımlar**:
1. Özel gün detaylarına gidin → "Düzenle ›"ye dokunun
2. Gün adını, notu düzenleyin
3. "Kaydet"e dokunun
4. Düzenlemek için adıma dokunun: Zamanı, içeriği değiştirin
5. Adımı silmek için Sil simgesine dokunun (onay iletişim kutusu var)

## 6. Mantık & Kurallar

### 6.1 Ay Takvimi Tarihleri

- Hem güneş hem de ay takvimi tarihlerini girebilirsiniz
- Uygulama ay tarihine karşılık gelen güneş tarihini otomatik hesaplar
- Ay takvimiyle yıllık tekrarı destekler

### 6.2 Tekrar

- **Yıllık**: Gün her yıl tekrarlanır (güneş veya ay takvimine göre)
  - Güneş takvimiyle: Her yıl solarDate'in (gün/ay) dayanarak nextOccurDate'i hesaplar
  - Ay takvimiyle: Her yıl ay tarihinden karşılık gelen güneş tarihine dönüştürür ve nextOccurDate'i günceller
- **Sadece Bu Yıl**: Gün yalnızca mevcut yılda geçerlidir, gelecek yıl tekrarlanmaz

### 6.3 Hazırlık Adımları

- **Ne Zaman?**: 2 seçeneği vardır:
  - **X gün önce**: Gün tarihinden X gün önce hatırlat (gün sayısını girmelisiniz)
  - **Gününde**: Gün tarihinde hatırlat (gün sayısı girmenize gerek yok)
- **Bildirim Göster**: Hatırlatıcı saati (gerekli, format HH:mm)
- **Tamamlanana Kadar Günlük Tekrar**: Etkinleştirilirse, kullanıcı adımı tamamlandı olarak işaretleyene kadar bildirim günlük tekrarlanır
- **Kontrol Listesi Bağlantısı**: Her adım alışveriş ilerlemesini takip etmek için bir alışveriş kontrol listesi ekleyebilir

### 6.4 Kontrol Listesi

- Kontrol listesi birden fazla adım için yeniden kullanılabilir
- Tamamlanan öğe sayısı / Toplam öğe sayısını takip edin (örn: "8 öğeden 3'ü tamamlandı")
- Detayları görüntülemek için "kontrol listesi adı ›" bağlantısıyla adım detaylarında gösterilir
- İlerlemeyi güncellemek için kontrol listesindeki öğeleri işaretleyebilir/işareti kaldırabilirsiniz
- Kontrol listesi tamamen tamamlanmamış olsa bile hazırlık adımı tamamlandı olarak işaretlenebilir

### 6.5 Bildirimler

- **Ana Gün Bildirimi**: `nextOccurDate + reminder_time`'da oluşturulur
  - YILLIK günle: Uygulama başladığında bildirim yeniden oluşturulur (yeni hesaplanan nextOccurDate'e dayanarak)
  - BİR KEZ günle: Bildirim yalnızca mevcut nextOccurDate için bir kez oluşturulur
- **Hazırlık Adımı Bildirimi**: Şunlara dayanarak hatırlatıcı tarihini hesaplayın:
  - Özel günün `nextOccurDate`'i
  - `reminderType` ve `daysBefore` (varsa)
  - `reminderTime`
- **Tekrar Bildirimi**: `repeatDailyUntilComplete = true` ise:
  - Günlük tekrarlayan bildirim oluştur
  - Tekrar bildirimlerini gruplamak için `notificationGroupKey` kullan
  - Kullanıcı adımı tamamlandı olarak işaretlediğinde otomatik iptal et

## 7. Önemli Notlar

- **Ay Takvimi Tarihleri**: 
  - Uygulama görüntüleme için otomatik olarak güneş takvimine dönüştürür
  - Mevcut tarihe kıyasla "gelecekteki EN YAKIN güneş tarihini" bulur
  - Gelecek yıllar: Sistem her yıl için (lunar_day, lunar_month)'dan karşılık gelen güneş tarihini her zaman yeniden hesaplar
  - O yıl aynı ayın hem normal hem de artık ayı varsa: Sistem kaçırmayı önlemek için 2 hatırlatıcı oluşturabilir
- **Yıllık Tekrar**: 
  - Gün gelecek yıl otomatik olarak nextOccurDate'i yeniden hesaplar
  - Ay takvimiyle: Her yıl ay tarihinden karşılık gelen güneş tarihine dönüştürür
- **Hatırlatıcı Saati**: 
  - Bir değere sahip olmalıdır (boş olamaz)
  - Doğru formatta olmalıdır HH:mm (00:00 - 23:59)
- **Kontrol Listesi**: 
  - Silinen kontrol listesi adımda hala görüntülenir (ancak düzenlenemez)
  - Kontrol listesi tamamen tamamlanmamış olsa bile adım tamamlandı olarak işaretlenebilir
- **Bildirimler**: 
  - Hatırlatıcıları almak için Ayarlar'da bildirimleri etkinleştirmeniz gerekir
  - Tekrar bildirimleri adımı tamamlandı olarak işaretlediğinizde otomatik iptal edilir
- **Gün Durumu**:
  - **Başlamadı**: Tüm adımlar tamamlanmadı (gri)
  - **Devam Ediyor**: En az 1 adım tamamlandı ancak hepsi değil (mavi)
  - **Tamamlandı**: Tüm adımlar tamamlandı (koyu yeşil)
  - Günün hazırlık adımı yoksa: Durum tarihe göre hesaplanır (Başlamadı / Devam Ediyor / Tamamlandı)

