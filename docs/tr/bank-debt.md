# Banka Kredileri

## 1. Amaç

**Banka Kredileri** modülü banka kredilerini yönetmenize yardımcı olur, şunları içerir:
- Kredi tutarını, faiz oranını, vadeyi takip etme
- Ödeme planını yönetme
- Döneme göre faiz hesaplama (uygulanabilirse)
- Geç ödeme cezalarını yönetme
- Erken kapatma (gerekirse)

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Banka kredileri
- Ödeme planını takip etme ihtiyacı
- Faiz ve cezaları hesaplama isteği
- Ödeme vadesi geldiğinde hatırlatma ihtiyacı

## 3. İlgili Ekranlar

- Kredi listesi
- Yeni kredi ekle (4 adım)
- Krediyi düzenle
- Kredi detayları ve ödeme planı
- Erken kapatma

## 4. Ana Kullanım

### 4.1 Yeni Kredi Ekle (4 Adım)

#### Adım 1: Temel Bilgiler

1. **İşlevler** → **Banka Kredileri** seçin
2. **+** (FAB) düğmesine dokunun
3. Bilgileri doldurun:
   - **Banka**: Seçin veya yeni banka oluşturun
   - **Kredi Adı**: (örn.: "Konut Kredisi")
   - **Kredi Tutarı**: Anapara tutarı
   - **Kullandırım Tarihi**: Paranın alındığı tarih
   - **Vade**: Yıl sayısı
   - **Faiz Türü**: Promosyonel/değişken oran veya Sabit oran
4. **İleri**'ye dokunun

#### Adım 2: Faiz Oranını Yapılandır

**"Promosyonel/Değişken Oran" seçerseniz:**
- **Promosyonel Oran Var**'ı etkinleştirin (uygulanabilirse)
- **Promosyonel Ay** ve **Promosyonel Oran** girin
- Değişken oran dönemleri ekleyin:
  - Yıl ve ay aralığı seçin
  - Faiz oranı girin (%/yıl)
  - **Değişken** veya **Sabit** seçin

**"Sabit Oran" seçerseniz:**
- **Sabit Oran** girin (%/yıl)

**İleri**'ye dokunun

#### Adım 3: Cezaları Yapılandır

1. **Geç Ödeme Cezası Var**'ı etkinleştirin (uygulanabilirse)
2. Ceza dönemleri ekleyin:
   - Yıl ve ay aralığı seçin
   - **Ceza Oranı** girin (%/yıl)
3. **İleri**'ye dokunun

#### Adım 4: Onayla ve Kaydet

1. Bilgileri gözden geçirin:
   - Ödenecek toplam tutar
   - Beklenen ödeme planı
2. **Kaydet**'e dokunun

### 4.2 Kredi Detaylarını Görüntüle

1. Kredi listesine gidin
2. Bir krediye dokunun
3. Bilgileri görüntüleyin:
   - Temel bilgiler
   - Ödeme planı
   - Ödenen tutar / Kalan
   - Faiz oranı ve cezalar

### 4.3 Ödeme Dönemini Ödendi Olarak İşaretle

1. Kredi detaylarına gidin
2. Vadesi gelen ödeme dönemini bulun (rozet "Ödenmedi")
3. **Ödendi Olarak İşaretle**'ye dokunun
4. Bilgileri doldurun:
   - **Gerçek Ödeme Tarihi**: Ödenen tarih (varsayılan = bugün)
   - **Gerçek Ödenen Faiz**: Gerçek ödenen faiz (varsayılan = planlanan faiz)
   - **Not**: (isteğe bağlı)
5. Otomatik hesaplanan **Toplam Gerçek Ödeme**'yi görüntüleyin (anapara + gerçek faiz)
6. **Onayla**'ya dokunun

### 4.4 Mevcut Faiz Oranını Güncelle

1. Kredi detaylarına gidin (yalnızca şu anda değişken oran dönemindeyse gösterilir)
2. **Mevcut Faiz Oranını Güncelle**'ye dokunun
3. Bilgileri doldurun:
   - **Yeni Faiz Oranı**: Yeni faiz oranı (%/yıl)
   - **Etkin Tarih**: Yeni oranı uygulamaya başlama tarihi (varsayılan = mevcut dönemin başlangıcı)
   - **Not**: (isteğe bağlı)
4. **Kaydet**'e dokunun
5. Mevcut dönemden itibaren ödenmemiş dönemler yeni faiz oranıyla güncellenecektir

### 4.5 Erken Kapatma

1. Kredi detaylarına gidin
2. **Kapatma Tutarını Hesapla**'ya dokunun
3. **Adım 1 - Erken Ödeme Bilgilerini Girin:**
   - Yöntem seçin: **Kısmi Ödeme** veya **Tam Kapatma**
   - Erken ödeme tarihini seçin (varsayılan = bugün)
   - Erken ödeme tutarını girin (kısmi ise)
   - Otomatik hesaplanan **Erken Ödeme Cezası**'nı görüntüleyin
4. **İleri**'ye dokunun
5. **Adım 2 - Seçenekleri Karşılaştırın:**
   - "Erken Ödeme Yok" ve "Erken Ödeme" arasındaki karşılaştırmayı görüntüleyin
   - Sonuçları görüntüleyin: Faiz tasarrufu, süre azalması
6. **Erken Ödemeyi Onayla**'ya dokunun

### 4.6 Krediyi Düzenle

1. Kredi detaylarına gidin
2. **Düzenle**'ye dokunun (yalnızca ad, not, banka düzenlenir)
3. Düzenlenebilir bilgileri düzenleyin:
   - **Kredi Adı**: Düzenlenebilir
   - **Banka**: Değiştirilebilir
   - **Not**: Düzenlenebilir
   - **Kredi Tutarı, Kullandırım Tarihi, Vade, Faiz Oranı**: Henüz ödeme yapılmadıysa düzenlenebilir
4. **Kaydet**'e dokunun

## 5. Örnekler ve UI İllüstrasyonları

### LOAN-01: Yeni Kredi Oluştur (Promosyonel Faiz Oranlı Konut Kredisi)

**Amaç**: Konut kredisini, promosyonel faiz oranını ve aylık ödeme planını takip etmek için yeni kredi oluşturun.

**Adımlar**:
1. **İşlevler** → **Banka Kredileri** seçin
2. Yeni kredi eklemek için **+** (FAB) düğmesine dokunun
3. **Adım 1 - Temel Bilgiler:**
   - Banka seçin: Türkiye İş Bankası
   - Ad girin: "Konut Kredisi - Şehir Merkezi Dairesi"
   - Kredi tutarı girin: ₺6.000.000
   - Kullandırım tarihi seçin: 01/04/2023
   - Vade girin: 10 yıl (otomatik hesaplanır = 120 dönem)
   - Bildirim zamanlarını seçin: 10:00 ve 19:00
   - Faiz türü seçin: "Azalan Bakiye"
   - **İleri**'ye dokunun
4. **Adım 2 - Faiz Oranını Yapılandır:**
   - "Promosyonel Faiz Dönemi Var"ı etkinleştirin
   - Girin: İlk 6 ay @ %18,0/yıl
   - Sonraki dönemleri ekleyin:
     - Yıl 1 (aylar 7-12): %27,0/yıl, değişken
     - Yıl 2 (aylar 13-24): %28,5/yıl, değişken
     - Yıl 3 ve sonrası: %30,0/yıl, değişken
   - **İleri**'ye dokunun
5. **Adım 3 - Erken Ödeme Cezasını Yapılandır:**
   - "Erken Ödeme Cezası Uygula"yı etkinleştirin
   - Ceza girin: Yıl 1-3: %1,8, Yıl 4-5: %1,4, Yıl 6+: %0,9
   - **İleri**'ye dokunun
6. **Adım 4 - Onayla:**
   - Özet bilgileri gözden geçirin
   - **Kredi Oluştur**'a dokunun

**Sonuç**: Kredi başarıyla oluşturuldu, 120 dönemlik ödeme planı otomatik olarak oluşturuldu, bildirimler zamanlandı.

---

### LOAN-02: Kredi Listesi ve Detaylarını Görüntüle

**Amaç**: Kredilerin genel bakışını görüntüleyin, duruma göre filtreleyin, arayın ve her kredinin detaylarını görüntüleyin.

**Adımlar**:
1. **İşlevler** → **Banka Kredileri** seçin
2. Filtreler "Aktif" (varsayılan) ve "Tamamlandı" ile liste ekranını görüntüleyin
3. Farklı genel bakışları görmek için filtreler arasında geçiş yapın
4. Arama çubuğunu kullanın: "Merkez" girin
5. Detayları görmek için krediye dokunun
6. Ödenen dönemler, mevcut dönem ve gelecekteki dönemlerle ödeme planını görüntüleyin
7. Ödeme planındaki arama çubuğunu kullanın: "9/2024" girin

**Sonuç**: Liste filtrelere göre doğru görüntülenir, kredi detayları tüm bilgileri ve ödeme planını gösterir.

---

### LOAN-03: Ödeme Dönemini Ödendi Olarak İşaretle (Ödeme Kaydet)

**Amaç**: Bankaya ödeme yaptıktan sonra bir ödeme dönemini "Ödendi" olarak işaretleyin.

**Adımlar**:
1. Kredi detaylarına gidin
2. Rozet "Ödenmedi" olan mevcut dönemi (Dönem 9) bulun
3. **Ödendi Olarak İşaretle**'ye dokunun
4. Bilgileri doldurun:
   - Gerçek ödeme tarihi: 15/01/2024 (varsayılan = bugün)
   - Gerçek ödenen faiz: ₺31.050 (varsayılan = planlanan faiz)
   - Not: (isteğe bağlı)
5. Otomatik hesaplanan toplam gerçek ödemeyi görüntüleyin
6. **Onayla**'ya dokunun

**Sonuç**: Dönem 9 "Ödendi" olarak güncellenir, bakiye azalır, ödenen dönemler artar, mevcut bakiye azalır.

---

### LOAN-04: Mevcut Faiz Oranını Güncelle (Banka Değişken Oranı Ayarladığında)

**Amaç**: Banka değişken oran ayarlaması duyurduğunda yeni faiz oranını güncelleyin.

**Adımlar**:
1. Kredi detaylarına gidin
2. "Mevcut Faiz Oranı: %27,0/yıl" görüntüleyin
3. **Mevcut Faiz Oranını Güncelle**'ye dokunun (yalnızca şu anda değişken oran dönemindeyse gösterilir)
4. Bilgileri doldurun:
   - Yeni faiz oranı: %31,5/yıl
   - Etkin tarih: 15/01/2024 (varsayılan = mevcut dönemin başlangıcı)
   - Not: "Banka yeni karara göre faiz oranını ayarladı"
5. **Kaydet**'e dokunun

**Sonuç**: Mevcut faiz oranı güncellendi, mevcut dönemden itibaren ödenmemiş dönemler yeni faiz oranıyla güncellendi.

---

### LOAN-05: Erken Kapatma (Faizi Azaltmak İçin Kısmi Ödeme)

**Amaç**: Toplam ödenecek faizi azaltmak ve kredi vadesini kısaltmak için kredinin bir kısmını erken kapatın.

**Adımlar**:
1. Kredi detaylarına gidin
2. **Kapatma Tutarını Hesapla**'ya dokunun
3. **Adım 1 - Erken Ödeme Bilgilerini Girin:**
   - Yöntem seçin: "Kısmi Ödeme"
   - Erken ödeme tarihi seçin: 15/01/2024
   - Erken ödeme tutarı girin: ₺2.400.000
   - Otomatik hesaplanan cezayı görüntüleyin: ₺43.200 (%1,8)
   - **İleri**'ye dokunun
4. **Adım 2 - Seçenekleri Karşılaştırın:**
   - "Erken Ödeme Yok" ve "Erken Ödeme ₺2.400.000" arasındaki karşılaştırmayı görüntüleyin
   - Sonuçları görüntüleyin: ₺900.000 faiz tasarrufu, 40 dönem azalma
   - **Erken Ödemeyi Onayla**'ya dokunun

**Sonuç**: Bakiye azalır, ödeme planı yeniden hesaplanır, dönem sayısı azalır, bitiş tarihi daha erken olur.

---

### LOAN-06: Krediyi Düzenle (Temel Bilgileri Düzenle)

**Amaç**: Ödemelere başladıktan sonra kredinin temel bilgilerini düzenleyin (ad, banka, not).

**Adımlar**:
1. Kredi detaylarına gidin
2. **Düzenle**'ye dokunun (yalnızca ad, not, banka düzenlenir)
3. Düzenleyin:
   - Kredi Adı: "Konut Kredisi - Şehir Merkezi Dairesi - Birim A1-1201"
   - (İsteğe bağlı) Banka değiştirin: Ziraat Bankası
   - Not: "Yeni bankaya transfer edildi"
4. Devre dışı bırakılmış alanları görüntüleyin: Kredi Tutarı, Kullandırım Tarihi, Vade, Faiz Oranı
5. **Kaydet**'e dokunun

**Sonuç**: Temel bilgiler güncellendi, diğer bilgiler değişmedi.

**Not**: Kredide henüz ödeme yapılmadıysa, tüm bilgileri düzenleyebilirsiniz (tutar, vade, faiz yapılandırması).

## 6. Mantık ve Kurallar

### 6.1 Promosyonel/Değişken Oran

- Promosyonel dönem olabilir (düşük faiz oranı)
- Promosyonel dönemden sonra, faiz oranı döneme göre değişir
- Her dönem **Değişken** (piyasa tabanlı) veya **Sabit** olabilir

### 6.2 Geç Ödeme Cezaları

- Ceza %/yıl olarak hesaplanır
- Her dönem için farklı yapılandırılabilir
- Ceza yalnızca ödeme geciktiğinde uygulanır

### 6.3 Ödeme Planı

- Uygulama şunlara göre otomatik olarak ödeme planı oluşturur:
  - Kredi tutarı
  - Faiz oranı
  - Vade
- Her ödeme dönemi şunları içerir: Anapara + Faiz

### 6.4 Erken Kapatma

- Kalan tutarı hesapla (anapara + faiz + varsa cezalar)
- Kapatmadan sonra, kredi "Tamamlandı" durumuna değişir

### 6.5 Bildirimler

- Ödeme vadesi geldiğinde uygulama hatırlatma bildirimi gönderir
- Bildirim zamanı her kredi için yapılandırılabilir (`notificationTime1`, `notificationTime2`, varsayılan 10:00 ve 19:00)

## 7. Önemli Notlar

- **Karmaşık Faiz Oranları**: Bu modül döneme göre değişen faiz oranlarını destekler, dikkatli yapılandırma gerektirir
- **Ödeme planı varsa silinemez**: Ödeme planı varsa, yalnızca kapatabilirsiniz, silemezsiniz
- **Erken Kapatma**: Ek ceza ücretleri gerektirebilir, banka politikasına bağlıdır
- **Ödeme Planı**: Ödeme planı otomatik olarak hesaplanır, doğrudan düzenleyemezsiniz

