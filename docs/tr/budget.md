# Bütçe

## 1. Amaç

**Bütçe** modülü aylık harcamaları planlamanıza ve takip etmenize yardımcı olur, belirlediğiniz bütçeyi aşmamanızı sağlar. Bu modül şunlara göre otomatik olarak hesaplar:
- Tekrarlanan geliriniz
- Tekrarlanan giderleriniz
- Gerçek günlük giderler

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Aylık harcamaları planlamak
- Bütçeyi aşmamayı kontrol etmek
- Tasarruf oranını takip etmek
- Kategoriye göre harcama analizini görüntülemek
- Aylar arası bütçeleri karşılaştırmak

## 3. İlgili Ekranlar

- Bütçe oluştur (ilk kez veya önceki aydan kopyala)
- Bütçe genel bakışını görüntüle
- Aya göre bütçe geçmişi
- Önceki aydan kopyalama önerisi

## 4. Ana Kullanım

### 4.1 İlk Kez Bütçe Oluştur (Durum A)

1. **İşlevler** → **Bütçe** seçin
2. Bütçe yoksa, uygulama otomatik olarak **Bütçe Oluştur** ekranını açar
3. Uygulama otomatik olarak hesaplar ve gösterir:
   - **Tekrarlanan Gelir**: Tüm aktif tekrarlanan gelirden toplam (salt okunur, detaylı döküm gösterir)
   - **Tekrarlanan Giderler**: Tüm aktif tekrarlanan giderlerden toplam (salt okunur, detaylı döküm gösterir)
   - **Toplam Bütçe (tasarruftan önce)**: Otomatik hesaplanır = Tekrarlanan Gelir - Tekrarlanan Giderler
4. **Tasarruf Oranı** girin: % tasarruf (0-100%, zorunlu)
5. **Tasarruf Tutarı** ve **Harcama Bütçesi** otomatik hesaplanmış olarak görüntüleyin
6. **Bütçeyi Kaydet**'e dokunun

### 4.2 Önceki Aydan Bütçe Kopyala (Durum C)

1. **İşlevler** → **Bütçe** seçin
2. Mevcut ayın bütçesi yoksa ancak önceki ayın varsa, uygulama **Bütçe Kopyalama Önerisi** ekranını gösterir
3. Seçeneklerden birini seçin:
   - **Önceki ayın bütçesini tamamen kopyala**: Uygulama otomatik olarak tasarruf oranını kopyalar, mevcut verilerden tekrarlanan gelir/giderleri yeniden hesaplar ve bütçeyi hemen oluşturur
   - **Kopyala ve Ayarla**: Uygulama tasarruf oranı önceki aydan önceden doldurulmuş olarak bütçe oluşturma ekranına gider, kaydetmeden önce ayarlayabilirsiniz
   - **Yeni Bütçe Oluştur**: Sıfırdan bütçe oluşturma akışını çalıştır (Durum A)
4. "Kopyala ve Ayarla" seçerseniz, gerekirse tasarruf oranını ayarlayın
5. **Bütçeyi Kaydet**'e dokunun

**Not**: Kopyalarken, Tekrarlanan Gelir ve Tekrarlanan Giderler mevcut tekrarlanan verilerden yeniden hesaplanır (önceki aydan kopyalanmaz), yalnızca tasarruf oranı kopyalanır.

### 4.3 Bütçe Genel Bakışını Görüntüle (Durum B)

1. **İşlevler** → **Bütçe** seçin
2. Mevcut ayın bütçesi varsa, uygulama **Genel Bakış** ekranını açar
3. Bilgileri görüntüleyin:
   - **Harcama Bütçesi**: Belirlenen harcama limiti
   - **Kullanılan**: Harcanan tutar (günlük giderler ve gelir/gider varyansları dahil)
   - **Kalan**: Bütçedeki kalan tutar
   - **Kullanım Oranı**: Kullanılan % bütçe (uyarı renkleriyle)
   - **Plandan Gelir ve Gider Varyansları**: Orijinal plandan varyanslar
   - **Kategoriye Göre Günlük Giderler**: Kategoriye göre detaylı harcama analizi

### 4.4 Mevcut Ayın Bütçesini Düzenle

1. **Bütçe Genel Bakış** ekranında, **"Bütçeyi Düzenle"** düğmesine dokunun
2. Uygulama şunlarla düzenleme ekranını gösterir:
   - **Tekrarlanan Gelir** ve **Tekrarlanan Giderler**: Eski değerleri koru (salt okunur)
   - **Tasarruf Oranı**: Mevcut bütçeden önceden doldurulmuş (düzenlenebilir)
3. Gerekirse tasarruf oranını değiştirin
4. Tasarruf tutarı ve harcama bütçesinin otomatik güncellendiğini görüntüleyin
5. **"Bütçeyi Kaydet"**'e dokunun

**Not**: Düzenlerken, Tekrarlanan Gelir ve Tekrarlanan Giderler yeniden hesaplanmaz (eski snapshot'ı korur), yalnızca tasarruf oranı ve harcama bütçesi güncellenir.

### 4.5 Bütçe Geçmişini Görüntüle

1. **İşlevler** → **Bütçe** seçin
2. Menüden **Geçmiş** seçin
3. Geçmiş aylar için bütçe listesini görüntüleyin
4. Detayları görmek için bir aya dokunun

### 4.6 Kategoriye Göre Gider Detaylarını Görüntüle

1. **Bütçe Genel Bakış** ekranına gidin
2. **Kategoriye Göre Analiz** bölümüne kaydırın
3. Bir kategoriye dokunun
4. O kategorideki gider listesini görüntüleyin

## 5. Örnekler ve UI İllüstrasyonları

### 5.1 BUDGET-01: Mevcut Ay İçin İlk Kez Bütçe Oluştur

**Amaç**: Uygulamanın gelir ve tekrarlanan giderlere göre aylık harcamaları otomatik olarak hesaplaması ve takip etmesi için ilk kez bütçe oluşturun.

**Adımlar**:
1. İşlevler ekranına gidin, "Bütçe Yönetimi" seçin
2. Uygulama otomatik olarak bütçe olmadığını algılar ve "Bütçe Oluştur" ekranını gösterir
3. Otomatik hesaplanan bilgileri görüntüleyin: Tekrarlanan Gelir, Tekrarlanan Giderler, Toplam Bütçe (tasarruftan önce)
4. Tasarruf oranı girin: 20
5. Tasarruf tutarı ve harcama bütçesinin otomatik hesaplandığını görüntüleyin
6. "Bütçeyi Kaydet" düğmesine dokunun

**Sonuç**: Mevcut ay için bütçe kaydedildi, otomatik olarak "Bütçe Genel Bakış" ekranına gider.

---

### 5.2 BUDGET-02: Mevcut Ayın Bütçe Genel Bakışını Görüntüle

**Amaç**: Belirlenen bütçeye göre harcama durumunu görüntüleyin, kullanılan tutarlar, kalan ve kategoriye göre analiz dahil.

**Adımlar**:
1. İşlevler ekranına gidin, "Bütçe Yönetimi" seçin
2. Uygulama otomatik olarak bütçe olduğunu algılar ve "Bütçe Genel Bakış" ekranını gösterir
3. Kart 1 - Aylık Bütçe'yi görüntüleyin: Harcama Bütçesi, Kullanılan, Kalan, Kullanım Oranı
4. Kart 2 - Plandan Gelir ve Gider Varyansları'nı görüntüleyin
5. Kart 3 - Kategoriye Göre Günlük Giderler'i görüntüleyin
6. (İsteğe bağlı) Bütçe hesaplamasını açıklayan detaylı iletişim kutusunu görmek için "Harcama Bütçesi ›" üzerine tıklayın

**Sonuç**: İlerleme çubuğu ve uygun renklerle mevcut ayın tam bütçe bilgilerini gösterir.

---

### 5.3 BUDGET-03: Mevcut Ayın Bütçesini Düzenle

**Amaç**: Mevcut ay için harcama bütçesini değiştirmek için tasarruf oranını ayarlayın.

**Adımlar**:
1. "Bütçe Genel Bakış" ekranında, "Bütçeyi Düzenle" düğmesine dokunun
2. Uygulama düzenleme ekranını gösterir (bütçe oluşturma ekranına benzer)
3. Mevcut bilgileri görüntüleyin: Tekrarlanan Gelir, Tekrarlanan Giderler (eski değerleri koru)
4. Tasarruf oranını 25 olarak değiştirin
5. Tasarruf tutarı ve harcama bütçesinin otomatik güncellendiğini görüntüleyin
6. "Bütçeyi Kaydet" düğmesine dokunun

**Sonuç**: Bütçe güncellendi, yeni değerlerle "Bütçe Genel Bakış" ekranına döner.

---

### 5.4 BUDGET-04: Yeni Ay Başlarken Önceki Aydan Bütçe Kopyala

**Amaç**: Gerekirse ayarlama seçeneğiyle yeni bütçe oluşturma zamanından tasarruf etmek için önceki ayın bütçesini yeniden kullanın.

**Adımlar**:
1. İşlevler ekranına gidin, "Bütçe Yönetimi" seçin
2. Uygulama otomatik olarak mevcut ayın bütçesi olmadığını ancak önceki ayın olduğunu algılar, "Bütçe Kopyalama Önerisi" ekranını gösterir
3. "Kopyala ve Ayarla" seçin
4. Uygulama tasarruf oranı önceki aydan önceden doldurulmuş olarak bütçe oluşturma ekranına gider
5. (İsteğe bağlı) Gerekirse tasarruf oranını ayarlayın
6. "Bütçeyi Kaydet" düğmesine dokunun

**Sonuç**: Mevcut ay için yeni bütçe oluşturuldu, otomatik olarak "Bütçe Genel Bakış" ekranına gider.

## 6. Mantık ve Kurallar

### 6.1 Durumlar

- **Durum A**: İlk kez bütçe oluştur (hiçbir ay için bütçe yok)
- **Durum B**: Mevcut ayın bütçesi var → Genel bakışı görüntüle
- **Durum C**: Mevcut ayın yok, ancak önceki ayın var → Kopyalama önerisi

### 6.2 Otomatik Hesaplama

- **Tekrarlanan Gelir**: Tüm aktif `recurring_income`'dan toplam
- **Tekrarlanan Giderler**: Tüm aktif `recurring_expense`'den toplam
- **Günlük Giderler**: Aydaki `daily_expense`'den toplam
- **Toplam Bütçe**: Tekrarlanan Gelir + Ekstra Gelir
- **Tasarruf**: Toplam Bütçe × Tasarruf Oranı

### 6.3 Diğer Modüllerle Entegrasyon

- Tekrarlanan geliri onaylarken → Otomatik olarak bütçeyi güncelle
- Tekrarlanan gideri onaylarken → Otomatik olarak bütçeyi güncelle
- Günlük giderler otomatik olarak bütçeye hesaplanır

### 6.4 Bütçe Aşımı Uyarısı

- Harcama bütçeyi aştığında uygulama uyarı gösterecektir
- Uyarı Ana ekranda ve bildirimlerde gösterilir

### 6.5 Snapshot

- Bütçe oluştururken, uygulama o zamanki durumu kaydetmek için gelir/gider öğelerinin snapshot'ını oluşturur
- Snapshot karşılaştırma ve analiz için kullanılır

## 7. Önemli Notlar

- **Ayda bir bütçe**: Her ay için bütçe oluşturmanız gerekir
- **Bütçeyi düzenle**: Tasarruf oranını değiştirerek mevcut ayın bütçesini düzenleyebilirsiniz. Tekrarlanan Gelir ve Tekrarlanan Giderler değişmeden kalacaktır (snapshot) doğruluğu sağlamak için
- **Otomatik güncelleme**: Gelir/giderleri onaylarken bütçe otomatik olarak güncellenir
- **Önceki aydan kopyala**: Kopyalama özelliği bütçe oluşturma zamanından tasarruf etmenize yardımcı olur

