# Tekrarlanan Giderler

## 1. Amaç

**Tekrarlanan Giderler** modülü şunlar gibi sabit döngülerle periyodik giderleri yönetmenize yardımcı olur:
- Elektrik, su, gaz faturaları
- İnternet, kablolu TV
- Sigorta
- Öğrenim ücreti
- Kira
- Diğer tekrarlanan giderler

Bu modül, yapılandırdığınız döngüye göre otomatik olarak **olaylar** oluşturur ve ödeme zamanı geldiğinde size hatırlatır.

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Belirli bir programda sabit giderler (haftalık, iki haftada bir veya aylık)
- Ödemenin ne zaman yapıldığını takip etme ve onaylama ihtiyacı
- Aylık bütçeye otomatik hesaplama isteği

## 3. İlgili Ekranlar

- Tekrarlanan giderler listesi
- Yeni tekrarlanan gider ekle
- Tekrarlanan gideri düzenle
- Olay geçmişi

## 4. Ana Kullanım

### 4.1 Yeni Tekrarlanan Gider Ekle

1. **İşlevler** → **Tekrarlanan Giderler** seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Kategori**: Seçin veya yeni kategori oluşturun
   - **Tutar**: Gider tutarını girin (boş bırakılabilir, onaylarken girilebilir)
   - **Döngü**: Haftalık / İki Haftada Bir / Aylık seçin
   - **Tarih**: Döngüdeki tarihi seçin (örn. her ayın 15'i)
   - **Başlangıç Tarihi**: (Sadece iki haftada bir döngü için) Başlangıç tarihini seçin
   - **Not**: Ek bilgiler (isteğe bağlı)
4. **Kaydet**'e dokunun

### 4.2 Yapılan Ödemeyi Onayla

1. Tekrarlanan giderler listesine gidin
2. **"Onay Bekliyor"** rozeti (sarı) olan öğeyi bulun
3. Öğeye dokunarak onay iletişim kutusunu açın
4. Doldurun:
   - **Gerçek Tutar**: (beklenenden farklıysa)
   - **Not**: (isteğe bağlı)
5. **Onayla**'ya dokunun

### 4.3 Tekrarlanan Gideri Düzenle

1. Tekrarlanan giderler listesine gidin
2. Düzenlemek için öğeye dokunun
3. Menüden **Düzenle** seçin
4. Bilgileri güncelleyin
5. **Kaydet**'e dokunun

### 4.4 Geçmişi Görüntüle

1. Tekrarlanan giderler listesine gidin
2. Bir öğeye dokunun
3. Tüm geçmiş olayları görmek için **Geçmiş** seçin

### 4.5 Gideri Devre Dışı Bırak/Etkinleştir

1. Tekrarlanan giderler listesine gidin
2. Devre dışı bırakılacak/etkinleştirilecek öğeyi bulun
3. Öğenin sağ tarafındaki **Etkin** anahtarını değiştirin

## 5. Örnekler ve UI İllüstrasyonları

### 5.1 Örnek 1: Aylık Tekrarlanan Gider Oluştur (Elektrik Faturası)

**Senaryo**: Uygulamanın ödeme zamanı geldiğinde otomatik olarak hatırlatması için aylık elektrik faturasını takip etmek istiyorsunuz.

**Adımlar**:
1. İşlevler ekranına gidin, "Tekrarlanan Giderler" seçin
2. Sağ alt köşedeki "➕ Yeni Ekle" düğmesine dokunun
3. "Faturalar" kategorisini seçin (yoksa yeni oluşturun)
4. Tutar girin: ₺600
5. "Aylık" döngüsünü seçin
6. "Ayın gününü seç" seçin, 15 girin
7. Not otomatik doldurulur "Aylık elektrik faturası" (düzenlenebilir)
8. "Kaydet"e dokunun

**Sonuç**: Uygulama başarı mesajı gösterir ve listeye döner. Yeni öğe tüm bilgilerle görünür ve uygulama her ayın 15'inde otomatik olarak hatırlatır.

---

### 5.2 Örnek 2: Vadesi Gelen Gideri Onayla ve Gerçek Tutarı Güncelle

**Senaryo**: Su faturası ödeme günü (10'u), ancak ödenecek gerçek tutar belirlenen ₺240 yerine ₺210 (azaldı).

**Adımlar**:
1. Uygulamayı açın veya "Tekrarlanan Giderler" ekranına gidin
2. Uygulama otomatik olarak vadesi gelen olayı algılar ve onay iletişim kutusunu gösterir
3. İletişim kutusu varsayılan tutarı gösterir: ₺240
4. Gerçek tutarı ₺210 olarak güncelleyin
5. Not girin: "Bu ay su tasarrufu yapıldı" (isteğe bağlı)
6. "Ödendi Onayla"ya dokunun

**Sonuç**: Uygulama onaylanan olayı gerçek tutar ₺210 ile günceller, otomatik olarak bir sonraki olayı oluşturur ve mevcut finansal bakiyeyi günceller (₺210 çıkarır).

---

### 5.3 Örnek 3: Artık Geçerli Olmadığında Tekrarlanan Gideri Devre Dışı Bırak

**Senaryo**: 2 ay boyunca geçici olarak yer kiralamıyorsunuz, bu yüzden "Kira" giderini tamamen silmek yerine devre dışı bırakmak istiyorsunuz.

**Adımlar**:
1. "Tekrarlanan Giderler" ekranına gidin
2. Listede "Kira" öğesini bulun
3. Öğenin sağ tarafındaki "Etkin" anahtarını dokunun
4. Uygulama onay iletişim kutusunu gösterir: "Bu gideri devre dışı bırakmak istediğinizden emin misiniz?"
5. Onaylamak için "Devre Dışı Bırak" düğmesine dokunun

**Sonuç**: "Kira" kartı "Etkin Değil" durumuna (gri) değişir, anahtar "Etkin Değil" olur. Uygulama bu gider için artık yeni olaylar oluşturmaz. Anahtarı "Etkin Değil" → "Etkin" olarak değiştirerek yeniden etkinleştirebilirsiniz.

## 6. Mantık ve Kurallar

### 6.1 Döngü ve Tarih

- **Haftalık**: Haftanın gününü seçin (1=Pazartesi, 7=Pazar)
- **İki Haftada Bir**: Haftanın günü + belirli başlangıç tarihi
- **Aylık**: Ayın gününü seçin (1-31)

### 6.2 Otomatik Olay Oluşturma

- Uygulama şu durumlarda otomatik olarak **olay** oluşturur:
  - Yeni gider eklerken
  - Döngüdeki tarihe ulaşıldığında
  - Yeni ay başladığında

### 6.3 Olay Durumu

- **PENDING**: Onay bekliyor (sarı rozet gösterir)
- **COMPLETED**: Onaylandı (yeşil rozet gösterir)
- **CANCELLED**: İptal edildi (kırmızı rozet gösterir)

### 6.4 Bütçe Entegrasyonu

- Gideri onaylarken, uygulama otomatik olarak mevcut ayın bütçesini günceller (varsa)
- Gider bütçedeki "Tekrarlanan Giderler"e hesaplanır

### 6.5 Bildirimler

- Ödeme vadesi geldiğinde uygulama hatırlatma bildirimi gönderir
- Bildirim zamanı her öğe için yapılandırılabilir (`notificationTime1`, `notificationTime2`, varsayılan 16:00 ve 19:00)

## 7. Önemli Notlar

- **Tutar boş bırakılabilir**: Kesin tutarı bilmiyorsanız, boş bırakabilir ve onaylarken girebilirsiniz
- **Olay varsa silinemez**: Olaylar varsa, yalnızca devre dışı bırakabilirsiniz (isActive = false), silemezsiniz
- **Geç onaylama**: Geçmiş olayları onaylayabilirsiniz, uygulama otomatik olarak bütçeyi yeniden hesaplar
- **Döngü değiştirme**: Döngüyü düzenlerken, gelecekteki olaylar yeniden hesaplanacaktır

