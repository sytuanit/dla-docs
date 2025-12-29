# Tasarruf

## 1. Amaç

**Tasarruf** modülü banka tasarruf hesaplarını yönetmenize, bakiyeleri, faiz oranlarını ve vadeleri takip etmenize yardımcı olur. Bu modül şunları destekler:
- Birden fazla tasarruf hesabını yönetme
- Faiz oranlarını ve vadeleri takip etme
- Vade sonunda faizi otomatik hesaplama
- Erken çekme (gerekirse)
- Hesap yenileme

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Banka tasarruf hesapları
- Bakiye ve faiz oranlarını takip etme ihtiyacı
- Vade sonunda hatırlatma isteği
- Birden fazla tasarruf hesabını yönetme ihtiyacı

## 3. İlgili Ekranlar

- Tasarruf hesapları listesi
- Yeni hesap ekle
- Hesabı düzenle
- Hesap detayları
- Erken çekme

## 4. Ana Kullanım

### 4.1 Yeni Tasarruf Hesabı Oluştur

1. **İşlevler** → **Banka Tasarrufu** seçin
2. Sağ alt köşedeki **+** (FAB) düğmesine dokunun
3. "Mevcut Bakiye"yi görüntüleyin (detayları görmek için tıklayabilirsiniz)
4. Banka seçin:
   - Varsa: Açılır menüden seçin
   - Yoksa: Yeni banka oluşturmak için "+" düğmesine dokunun
5. Mevduat tutarını girin (Mevcut Bakiyeden ≤ olmalı)
6. Vade girin: 1-36 ay
7. Faiz oranı girin: %/yıl (1-100%)
8. Başlangıç tarihini seçin (varsayılan bugün, önceki aydan bugüne kadar seçebilirsiniz)
9. Otomatik hesaplanan vade tarihini görüntüleyin (başlangıç tarihi + vade)
10. Vade sonunda plan seçin:
    - Anapara ve faizi çek (varsayılan)
    - ANAPARA'yı yenile (faiz hesaba)
    - ANAPARA + FAİZ'i yenile
11. (İsteğe bağlı) Not girin
12. (İsteğe bağlı) Bildirim zamanlarını seçin (varsayılan: 10:00 ve 19:00)
13. **HESAP OLUŞTUR**'a dokunun

### 4.2 Liste ve Hesap Detaylarını Görüntüle

1. **İşlevler** → **Banka Tasarrufu** seçin
2. Varsayılan filtre "Aktif" ile "Tasarruf Hesapları Listesi" ekranını görüntüleyin
3. Genel bakış kartını görüntüleyin:
   - Filtre "Aktif": Mevcut bakiye, Tasarruftaki para, Beklenen faiz, Bu ayın faizi
   - Filtre "Tamamlandı": Toplam çekilen, Alınan faiz
4. (İsteğe bağlı) Banka adı veya koduna göre hesapları bulmak için arama çubuğunu kullanın
5. Filtreyi "Aktif" ve "Tamamlandı" arasında değiştirin
6. Detayları görmek için bir tasarruf hesabına dokunun:
   - Hesap bilgileri: Banka, Vade, Faiz oranı, Mevduat tutarı, Tahmini faiz
   - Başlangıç tarihi ve vade tarihi
   - Durum: Aktif
   - Vade sonunda plan
   - (Varsa) Yenileme geçmişi
   - "ÇEK" düğmesi (aktifse)

### 4.3 Tasarruf Hesabını Çek

1. Tasarruf listesine gidin, vade tarihine ulaşan veya geçen hesabı bulun
2. Karttaki **ÇEK** düğmesine dokunun (veya detaylara gidin ve "ÇEK"e dokunun)
3. Şunlarla "TASARRUF HESABINI ÇEK" iletişim kutusunu görüntüleyin:
   - Hesap bilgileri: Banka, Mevduat tutarı, Vade, Faiz oranı
   - Çekme tarihi (varsayılan = vade tarihi, farklı tarih seçebilirsiniz)
   - Alınan faiz (varsayılan = tahmini faiz, düzenleyebilirsiniz)
   - Toplam alınan (otomatik hesaplanır = anapara + faiz)
4. (İsteğe bağlı) Çekme tarihini veya alınan faizi düzenleyin
5. **ONAYLA**'ya dokunun

### 4.4 Tasarruf Hesabını Yenile

1. Tasarruf listesine gidin, planı "ANAPARA'yı Yenile" veya "ANAPARA + FAİZ'i Yenile" olan vade tarihine ulaşan hesabı bulun
2. **YENİLE** düğmesine veya "Planlandığı gibi yenile"ye dokunun
3. Şunlarla "TASARRUF HESABINI YENİLE" iletişim kutusunu görüntüleyin:
   - Hesap bilgileri: Banka, Anapara tutarı, Vade, Faiz oranı
   - Alınan faiz (ANAPARA'yı yenilerseniz, faiz hesaba gider)
4. (İsteğe bağlı) Yeni faiz oranını veya yeni vadeyi düzenleyin (varsayılan = eski vade)
5. **YENİLEMEYİ ONAYLA**'ya dokunun

### 4.5 Tasarruf Hesabını Düzenle

1. Aktif tasarruf hesabı detaylarına gidin
2. Sağ üst köşedeki **Düzenle** düğmesine dokunun
3. Bilgileri düzenleyin:
   - Banka (gerekirse)
   - Mevduat tutarı (artırırsanız, Mevcut Bakiyeden ≤ olmalı)
   - Vade, Faiz oranı
   - Başlangıç tarihi (gerekirse)
   - Vade sonunda plan
   - Not, Bildirim zamanları
4. Otomatik yeniden hesaplanan vade tarihini görüntüleyin (vade/başlangıç tarihi değişirse)
5. **DEĞİŞİKLİKLERİ KAYDET**'e dokunun

### 4.6 Yeni Banka Oluştur

1. "Tasarruf Hesabı Ekle" veya "Tasarruf Hesabını Düzenle" ekranında
2. "Banka" alanına dokunun
3. Yeni banka oluşturmak için açılır menünün yanındaki "+" düğmesine dokunun
4. "YENİ BANKA EKLE" iletişim kutusunu görüntüleyin
5. Banka adını girin
6. Banka kodunu girin (maks. 3-4 karakter, otomatik büyük harf)
7. Simge rengini seçin (renk seçiciden veya paletten)
8. Simge önizlemesini görüntüleyin
9. **OLUŞTUR**'a dokunun

## 5. Örnekler ve UI İllüstrasyonları

### SAVINGS-01: Yeni Tasarruf Hesabı Oluştur

**Amaç**: Banka mevduatını, faiz oranını ve vade tarihini takip etmek için yeni tasarruf hesabı oluşturun.

**Ana Adımlar**:
1. İşlevler → Banka Tasarrufu
2. "+" (FAB) düğmesine dokunun
3. Banka seçin (veya yeni oluşturun)
4. Mevduat tutarı, vade, faiz oranı girin
5. Başlangıç tarihini seçin (varsayılan bugün)
6. Vade sonunda plan seçin
7. (İsteğe bağlı) Not ve bildirim zamanlarını girin
8. "HESAP OLUŞTUR"a dokunun

---

### SAVINGS-02: Tasarruf Hesabını Çek

**Amaç**: Vade tarihine ulaştığında anapara ve faizi almak için tasarruf hesabını çekin.

**Ana Adımlar**:
1. Tasarruf listesine gidin, vade tarihine ulaşan veya geçen hesabı bulun
2. "ÇEK" düğmesine dokunun
3. Hesap bilgileri, çekme tarihi, alınan faiz ile iletişim kutusunu görüntüleyin
4. (İsteğe bağlı) Çekme tarihini veya alınan faizi düzenleyin
5. "ONAYLA"ya dokunun

---

### SAVINGS-03: Liste ve Hesap Detaylarını Görüntüle

**Amaç**: Aktif ve tamamlanmış tasarruf hesaplarının genel bakışını ve her hesabın detaylarını görüntüleyin.

**Ana Adımlar**:
1. İşlevler → Banka Tasarrufu
2. Filtreye göre genel bakış kartını görüntüleyin
3. Arama çubuğunu kullanın (isteğe bağlı)
4. Filtreyi "Aktif" ve "Tamamlandı" arasında değiştirin
5. Detayları görmek için hesaba dokunun

---

### SAVINGS-04: Tasarruf Hesabını Yenile

**Amaç**: Vade tarihine ulaştığında planlandığı gibi tasarruf hesabını yenileyin.

**Ana Adımlar**:
1. Planı "ANAPARA'yı Yenile" veya "ANAPARA + FAİZ'i Yenile" olan vade tarihine ulaşan hesabı bulun
2. "YENİLE" düğmesine dokunun
3. Hesap bilgileri ve alınan faiz ile iletişim kutusunu görüntüleyin
4. (İsteğe bağlı) Yeni faiz oranını veya yeni vadeyi düzenleyin
5. "YENİLEMEYİ ONAYLA"ya dokunun

**Sonuç**: Eski hesap güncellenir, yeni hesap eski hesaba rootSavingId ile bağlı olarak oluşturulur. ANAPARA'yı yenilerseniz, faiz mevcut bakiyeye eklenir. ANAPARA + FAİZ'i yenilerseniz, hem anapara hem de faiz yenilenir, mevcut bakiye değişmez.

---

### SAVINGS-05: Yeni Banka Oluştur

**Amaç**: Tasarruf hesapları oluştururken kullanmak için yeni banka oluşturun.

**Ana Adımlar**:
1. "Tasarruf Hesabı Ekle" veya "Tasarruf Hesabını Düzenle" ekranında
2. "Banka" açılır menüsünün yanındaki "+" düğmesine dokunun
3. Banka adı, banka kodu girin
4. Simge rengini seçin
5. Simge önizlemesini görüntüleyin
6. "OLUŞTUR"a dokunun

---

### SAVINGS-06: Tasarruf Hesabını Düzenle

**Amaç**: Aktif tasarruf hesabının bilgilerini düzenleyin (banka, tutar, vade, faiz oranı, vade planı).

**Ana Adımlar**:
1. Aktif tasarruf hesabı detaylarına gidin
2. "Düzenle" düğmesine dokunun
3. Gerekli bilgileri düzenleyin
4. Otomatik yeniden hesaplanan vade tarihini görüntüleyin (vade/başlangıç tarihi değişirse)
5. "DEĞİŞİKLİKLERİ KAYDET"e dokunun

**Sonuç**: Hesap bilgileri güncellenir, tahmini faiz yeni faiz oranına göre yeniden hesaplanır. Tutar değişirse, mevcut bakiye buna göre ayarlanır.

## 6. Mantık ve Kurallar

### 6.1 Faiz Hesaplama

- Faiz şu formülle hesaplanır: `Tutar × Faiz Oranı × (Vade / 12)`
- Faiz vade sonunda veya erken çekildiğinde hesaplanır

### 6.2 Durum

- **Aktif (ACTIVE)**: Tasarruf hesabı aktif, vade tarihine ulaşmadı veya işlenmedi
- **Tamamlandı (COMPLETED)**: Hesap çekildi
- **Yenilendi (ROLLED_OVER)**: Hesap yenilendi, yeni hesap oluşturuldu

### 6.3 Çekme ve Yenileme

- **Çekme**: Çekildiğinde, anapara + faiz mevcut bakiyeye eklenir, otomatik olarak "Ekstra Gelir" kategorisi "Tasarruf Faizi" ile oluşturulur
- **Erken Çekme**: Vade tarihinden önce çekebilirsiniz, alınan faiz tahmini faizden düşük olabilir
- **ANAPARA'yı Yenile**: Faiz mevcut bakiyeye eklenir, anapara yeni vade ile yenilenir
- **ANAPARA + FAİZ'i Yenile**: Hem anapara hem de faiz yenilenir, mevcut bakiye değişmez
- **Yenileme Geçmişi**: Yenilemeler kaydedilir ve hesap detaylarında gösterilir, `rootSavingId` ile bağlanır

### 6.4 Bildirimler

- Vade tarihi geldiğinde uygulama hatırlatma bildirimi gönderir
- Bildirim zamanı her hesap için yapılandırılabilir (`notificationTime1`, `notificationTime2`, varsayılan 10:00 ve 19:00)

## 7. Önemli Notlar

- **Premium Modül Gerekli**: Bu özellik yalnızca Premium kullanıcılar içindir
- **Faiz Oranı**: Yıllık faiz oranını girin (%/yıl), 1'den 100'e kadar
- **Vade**: Aylık hesaplanır, 1'den 36 aya kadar
- **Vade Tarihi**: Başlangıç tarihi + vade'den otomatik hesaplanır
- **Mevduat Tutarı**: Mevcut Bakiyeden ≤ olmalı, hesap oluştururken otomatik olarak mevcut bakiyeden çıkarılır
- **Başlangıç Tarihi**: Yalnızca önceki ayın başından bugüne kadar seçebilirsiniz
- **Bildirimler**: Bildirimler vade tarihinde 2 zaman (varsayılan 10:00 ve 19:00) gönderilir, her hesap için özelleştirilebilir
- **Rozet "Yakında Vadesi Geliyor"**: Vade tarihine ≤ 7 gün kaldığında gösterilir
- **Rozet "Vadesi Geldi"**: Vade tarihi geldiğinde gösterilir
- **Hesabı Sil**: Aktif hesabı silerken, anapara tutarı mevcut bakiyeye geri eklenir. Kök hesabı silmek tüm yenileme zincirini silecektir
- **Genel Bakış Kartı**: Filtreye göre değişir, aktif veya tamamlanmış hesaplar için toplu bilgileri gösterir

