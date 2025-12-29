# Tekrarlanan Gelir

## 1. Amaç

**Tekrarlanan Gelir** modülü şunlar gibi düzenli gelir kaynaklarını yönetmenize yardımcı olur:
- Aylık maaş
- Kira geliri
- Emekli maaşı
- Yatırım temettüleri
- Diğer tekrarlanan gelirler

Bu modül, yapılandırdığınız döngüye göre otomatik olarak **olaylar** oluşturur ve ödeme alma zamanı geldiğinde size hatırlatır.

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Belirli bir programda sabit gelir (haftalık, iki haftada bir veya aylık)
- Ödemenin ne zaman alındığını takip etme ve onaylama ihtiyacı
- Aylık bütçeye otomatik hesaplama isteği

## 3. İlgili Ekranlar

- Tekrarlanan gelir listesi
- Yeni tekrarlanan gelir ekle
- Tekrarlanan geliri düzenle
- Olay geçmişi

## 4. Ana Kullanım

### 4.1 Yeni Tekrarlanan Gelir Ekle

1. **İşlevler** → **Tekrarlanan Gelir** seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Kategori**: Seçin veya yeni kategori oluşturun
   - **Tutar**: Gelir tutarını girin (boş bırakılabilir, onaylarken girilebilir)
   - **Döngü**: Haftalık / İki Haftada Bir / Aylık seçin
   - **Tarih**: Döngüdeki tarihi seçin (örn. her ayın 15'i)
   - **Başlangıç Tarihi**: (Sadece iki haftada bir döngü için) Başlangıç tarihini seçin
   - **Not**: Ek bilgiler (isteğe bağlı)
4. **Kaydet**'e dokunun

### 4.2 Alınan Ödemeyi Onayla

1. Tekrarlanan gelir listesine gidin
2. **"Onay Bekliyor"** rozeti (sarı) olan öğeyi bulun
3. Öğeye dokunarak onay iletişim kutusunu açın
4. Doldurun:
   - **Gerçek Tutar**: (beklenenden farklıysa)
   - **Not**: (isteğe bağlı)
5. **Onayla**'ya dokunun

### 4.3 Tekrarlanan Geliri Düzenle

1. Tekrarlanan gelir listesine gidin
2. Düzenlemek için öğeye dokunun
3. Menüden **Düzenle** seçin
4. Bilgileri güncelleyin
5. **Kaydet**'e dokunun

### 4.4 Geçmişi Görüntüle

1. Tekrarlanan gelir listesine gidin
2. Bir öğeye dokunun
3. Tüm geçmiş olayları görmek için **Geçmiş** seçin

### 4.5 Geliri Devre Dışı Bırak/Etkinleştir

1. Tekrarlanan gelir listesine gidin
2. Devre dışı bırakılacak/etkinleştirilecek öğeyi bulun
3. Öğenin sağ tarafındaki **Etkin** anahtarını değiştirin

## 5. Örnekler ve UI İllüstrasyonları

### 5.1 Örnek 1: Aylık Tekrarlanan Gelir Oluştur (Maaş)

**Senaryo**: Uygulamanın ödeme alma zamanı geldiğinde otomatik olarak hatırlatması için aylık maaşı takip etmek istiyorsunuz.

**Adımlar**:
1. İşlevler ekranına gidin, "Tekrarlanan Gelir" seçin
2. Sağ alt köşedeki "➕ Yeni Ekle" düğmesine dokunun
3. "Maaş" kategorisini seçin (yoksa yeni oluşturun)
4. Tutar girin: ₺120.000
5. "Aylık" döngüsünü seçin
6. "Ayın gününü seç" seçin, 5 girin
7. Not otomatik doldurulur "Aylık maaş" (düzenlenebilir)
8. "Kaydet"e dokunun

**Sonuç**: Uygulama başarı mesajı gösterir ve listeye döner. Yeni öğe tüm bilgilerle görünür ve uygulama her ayın 5'inde otomatik olarak hatırlatır.

---

### 5.2 Örnek 2: Vadesi Gelen Geliri Onayla ve Gerçek Tutarı Güncelle

**Senaryo**: Maaş günü (5'i), ancak belirlenen ₺120.000 yerine alınan gerçek tutar ₺126.000 (maaş artışı).

**Adımlar**:
1. Uygulamayı açın veya "Tekrarlanan Gelir" ekranına gidin
2. Uygulama otomatik olarak vadesi gelen olayı algılar ve onay iletişim kutusunu gösterir
3. İletişim kutusu varsayılan tutarı gösterir: ₺120.000
4. Gerçek tutarı ₺126.000 olarak güncelleyin
5. Not girin: "Bu ay ikramiye var" (isteğe bağlı)
6. "Alındı Onayla"ya dokunun

**Sonuç**: Uygulama onaylanan olayı gerçek tutar ₺126.000 ile günceller, otomatik olarak bir sonraki olayı oluşturur ve mevcut finansal bakiyeyi günceller.

---

### 5.3 Örnek 3: Ödeme Alınmadığında Gelir Olayını İptal Et

**Senaryo**: Kira ödeme günü (1'i), ancak kiracı para transfer etmediği için ödeme alınmadı.

**Adımlar**:
1. Uygulamayı açın veya "Tekrarlanan Gelir" ekranına gidin
2. Uygulama vadesi gelen olay için onay iletişim kutusunu gösterir
3. "İptal Et" düğmesine dokunun
4. Neden girin: "Kiracı para transfer etmedi" (zorunlu)
5. "İptali Onayla"ya dokunun

**Sonuç**: İptal edilen olay "İptal Edildi" durumuna değişir, iptal nedenini gösterir ve uygulama otomatik olarak bir sonraki olayı oluşturur. Finansal bakiye değişmez çünkü ödeme alınmadı.

## 6. Mantık ve Kurallar

### 6.1 Döngü ve Tarih

- **Haftalık**: Haftanın gününü seçin (1=Pazartesi, 7=Pazar)
- **İki Haftada Bir**: Haftanın günü + belirli başlangıç tarihi
- **Aylık**: Ayın gününü seçin (1-31)

### 6.2 Otomatik Olay Oluşturma

- Uygulama şu durumlarda otomatik olarak **olay** oluşturur:
  - Yeni gelir eklerken
  - Döngüdeki tarihe ulaşıldığında
  - Yeni ay başladığında

### 6.3 Olay Durumu

- **PENDING**: Onay bekliyor (sarı rozet gösterir)
- **COMPLETED**: Onaylandı (yeşil rozet gösterir)
- **CANCELLED**: İptal edildi (kırmızı rozet gösterir)

### 6.4 Bütçe Entegrasyonu

- Geliri onaylarken, uygulama otomatik olarak mevcut ayın bütçesini günceller (varsa)
- Gelir bütçedeki "Tekrarlanan Gelir"e hesaplanır

### 6.5 Bildirimler

- Ödeme vadesi geldiğinde uygulama hatırlatma bildirimi gönderir
- Bildirim zamanı her öğe için yapılandırılabilir (`notificationTime1`, `notificationTime2`, varsayılan 16:00 ve 19:00)

## 7. Önemli Notlar

- **Tutar boş bırakılabilir**: Kesin tutarı bilmiyorsanız, boş bırakabilir ve onaylarken girebilirsiniz
- **Olay varsa silinemez**: Olaylar varsa, yalnızca devre dışı bırakabilirsiniz (isActive = false), silemezsiniz
- **Geç onaylama**: Geçmiş olayları onaylayabilirsiniz, uygulama otomatik olarak bütçeyi yeniden hesaplar
- **Döngü değiştirme**: Döngüyü düzenlerken, gelecekteki olaylar yeniden hesaplanacaktır

