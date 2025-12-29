# Ayarlar

## 1. Amaç

**Ayarlar** modülü, uygulamayı kişisel ihtiyaçlarınıza göre yapılandırmanıza olanak tanır, şunları içerir:
- Dil ve para birimi
- Bildirimler
- Kategoriler
- Veri yedekleme ve geri yükleme
- Güvenlik (şifre, Face ID)

## 2. Ne Zaman Kullanılır

Şu durumlarda bu modülü kullanın:
- Dil veya para birimini değiştirmek
- Bildirimleri etkinleştirmek/devre dışı bırakmak
- Kategorileri yönetmek (ekle, düzenle, sil, varsayılan ayarla)
- Veri yedeklemek veya geri yüklemek
- Şifreyi değiştirmek veya Face ID'yi etkinleştirmek

## 3. İlgili Ekranlar

- Ana ayarlar ekranı
- Temel ayarlar
- Dil seç
- Para birimi seç
- Kategorileri yönet
- Veri yedekle
- Veri geri yükle
- Şifre değiştir
- Face ID / Parmak İzi etkinleştir

## 4. Ana Kullanım

### 4.1 Dili Değiştir

1. **Ayarlar** → **Görüntüleme ve Dil** → **Dil** gidin
2. İstediğiniz dili seçin
3. Uygulama yeni dille otomatik olarak yeniden yüklenecektir

### 4.2 Para Birimini Değiştir

1. **Ayarlar** → **Görüntüleme ve Dil** → **Para Birimi** gidin
2. Para birimi türünü seçin
3. Tüm tutarlar yeni birimde görüntülenecektir

### 4.3 Bildirimleri Etkinleştir/Devre Dışı Bırak

1. **Ayarlar** → **Bildirimler** gidin
2. **Bildirimler** anahtarını değiştirin
3. Etkinleştirilirse, şunlar hakkında hatırlatmalar alırsınız:
   - Vadesi gelen tekrarlanan gelir
   - Vadesi gelen tekrarlanan giderler
   - Vadesi gelen tasarruf hesapları
   - Yaklaşan özel günler

### 4.4 Kategorileri Yönet

1. **Ayarlar** → **Kategoriler** gidin
2. Yönetilecek kategori türünü seçin:
   - Tekrarlanan Gelir
   - Ekstra Gelir
   - Tekrarlanan Giderler
   - Günlük Giderler
3. Kategorileri Ekle/Düzenle/Sil
4. Varsayılan kategori ayarla (günlük giderler için)

### 4.5 Veri Yedekle

1. **Ayarlar** → **Yedekleme ve Veri** → **Yedekleme** gidin
2. Kayıt konumunu seçin (Dosya sistemi)
3. **Yedekle**'ye dokunun
4. Yedekleme dosyası oluşturulacaktır

### 4.6 Veri Geri Yükle

1. **Ayarlar** → **Yedekleme ve Veri** → **Geri Yükleme** gidin
2. Yedekleme dosyasını seçin
3. Geri yüklemeyi onaylayın
4. **Not**: Geri yükleme mevcut tüm verilerin üzerine yazacaktır

## 5. UI İllüstrasyonları (Wireframe)

### 5.1 Ana Ayarlar Ekranı

```text
┌─────────────────────────────────────────┐
│  ← Geri    Ayarlar                      │
├─────────────────────────────────────────┤
│  Görüntüleme ve Dil                      │
│  ┌───────────────────────────────────┐ │
│  │ Dil                                │ │
│  │ Türkçe                      →     │ │
│  │                                    │ │
│  │ Para Birimi                         │ │
│  │ TRY (₺)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Bildirimler                             │
│  ┌───────────────────────────────────┐ │
│  │ Bildirimler                [AÇIK] │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Yedekleme ve Veri                       │
│  ┌───────────────────────────────────┐ │
│  │ Yedekleme                    →    │ │
│  │                                    │ │
│  │ Geri Yükleme                  →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Kategoriler                             │
│  ┌───────────────────────────────────┐ │
│  │ Kategorileri Yönet              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Güvenlik                                │
│  ┌───────────────────────────────────┐ │
│  │ Şifre                         →    │ │
│  │                                    │ │
│  │ Face ID / Parmak İzi          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Mantık ve Kurallar

### 6.1 Dil

- Desteklenen: Türkçe, İngilizce, Tiếng Việt, 日本語
- Dili değiştirmek tüm uygulamayı yeniden yükler
- Sistem kategorileri otomatik olarak yeni dile çevrilir

### 6.2 Para Birimi

- Her dilin varsayılan para birimi vardır (örn. TRY Türkçe için)
- Farklı para birimi seçebilirsiniz
- Tüm tutarlar seçilen para birimine göre biçimlendirilir

### 6.3 Bildirimler

- Bildirimler yalnızca uygulama izne sahip olduğunda çalışır
- Bildirim zamanı her işleve bağlıdır ve yapılandırılabilir:
  - Tekrarlanan Gelir/Giderler: `notificationTime1`, `notificationTime2` (varsayılan 16:00 ve 19:00)
  - Tasarruf Hesapları ve Krediler: `notificationTime1`, `notificationTime2` (varsayılan 10:00 ve 19:00)
  - Özel Günler ve Hazırlık Adımları: girdiğiniz `reminderTime`'a göre
  - Her tür için bildirimleri ayrı ayrı devre dışı bırakabilirsiniz (gelecekte)

### 6.4 Kategoriler

- Sistem kategorileri silinemez, yalnızca devre dışı bırakılabilir
- Kullanıcı kategorileri silinebilir (kullanılmıyorsa)
- Her kategori türü bağımsızdır (tekrarlanan gelir, günlük giderler, vb.)

## 7. Önemli Notlar

- **Düzenli Yedekleme**: Veri kaybını önlemek için verileri periyodik olarak yedeklemelisiniz
- **Geri Yükleme Üzerine Yazacak**: Geri yükleme mevcut tüm verilerin yerini alacaktır
- **Şifre**: Şifreyi unutursanız, sıfırlayabilirsiniz (verileri silecektir)

