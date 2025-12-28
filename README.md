# Creatine Water Reminder

iOS için BeeWare (Briefcase + Toga) kullanılarak geliştirilmiş su içme hatırlatıcısı ve antrenman planı uygulaması.

## Özellikler

1. **Su İçme Hatırlatıcısı**
   - Varsayılan olarak her 2 saatte bir local notification gönderir
   - Bildirim metni: "Creatine alıyorsun, su içmeyi unutma 💧"
   - Kullanıcı bildirimleri açıp kapatabilir

2. **Okul Modu**
   - "Okuldayım" switch'i ile bildirimler geçici olarak durdurulur
   - Switch kapatıldığında bildirimler kaldığı yerden devam eder

3. **Antrenman Planı**
   - Haftalık antrenman planı gösterilir
   - Bugünün antrenmanı otomatik olarak listelenir
   - Çarşamba (PUSH), Cumartesi (PULL), Pazar (LEGS), Pazartesi (Evde PUSH), Çarşamba (Evde PULL + Core)

4. **Basit ve Sade UI**
   - Ana ekranda bildirim ve okul modu switch'leri
   - Bugünün antrenmanı listesi

## Proje Yapısı

```
.
├── pyproject.toml          # Briefcase yapılandırması
├── src/
│   └── creatine/
│       ├── __init__.py
│       ├── app.py          # Ana uygulama (Toga UI)
│       ├── notifications.py # iOS bildirim yönetimi
│       ├── workouts.py      # Antrenman planı verileri
│       └── storage.py       # Kullanıcı ayarları (JSON)
├── ios/
│   └── CreatineWaterReminder/
│       └── NotificationBridge.swift  # iOS native notification bridge
└── .github/
    └── workflows/
        └── ios.yml         # GitHub Actions build workflow
```

## Geliştirme Ortamı (Windows)

### Gereksinimler

- Python 3.11+
- Briefcase
- Git

### Kurulum

1. **Python'u yükleyin** (eğer yoksa)
   - [Python.org](https://www.python.org/downloads/) adresinden indirin

2. **Briefcase'i yükleyin**
   ```bash
   pip install briefcase
   ```

3. **Projeyi klonlayın veya indirin**
   ```bash
   git clone <repo-url>
   cd creatine-water-reminder
   ```

4. **Bağımlılıkları yükleyin**
   ```bash
   pip install toga-iOS
   ```

### Yerel Test (Windows)

Windows'ta iOS uygulamasını doğrudan test edemezsiniz, ancak Python kodunu test edebilirsiniz:

```bash
# Uygulamayı çalıştır (simülatör için)
python -m src.creatine.app
```

## IPA Dosyasını Alma (Windows)

Windows'ta iOS uygulamasını derleyemezsiniz. IPA dosyasını almak için GitHub Actions kullanın:

### Yöntem 1: GitHub Actions (Önerilen)

1. **Kodu GitHub'a push edin**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **GitHub Actions'ı tetikleyin**
   - GitHub repository'nize gidin
   - "Actions" sekmesine tıklayın
   - "Build iOS IPA" workflow'unu seçin
   - "Run workflow" butonuna tıklayın (veya otomatik olarak push sonrası çalışır)

3. **IPA dosyasını indirin**
   - Workflow tamamlandıktan sonra (yaklaşık 10-15 dakika)
   - "Artifacts" bölümünden "creatine-water-reminder-ipa" dosyasını indirin
   - ZIP dosyasını açın, içindeki `.ipa` dosyasını kullanın

### Yöntem 2: Manuel Build (macOS Gerekli)

Eğer macOS erişiminiz varsa:

```bash
# iOS app oluştur
briefcase create iOS

# Build et
briefcase build iOS

# IPA paketle (imzasız)
briefcase package iOS --unsign

# IPA dosyası iOS klasöründe olacak
```

## IPA'yı Yükleme

### İmzasız IPA'yı Yükleme

1. **AltStore veya Sideloadly kullanın**
   - [AltStore](https://altstore.io/) (ücretsiz, kendi sunucunuz gerekir)
   - [Sideloadly](https://sideloadly.io/) (ücretsiz)

2. **Sideloadly ile yükleme:**
   - Sideloadly'yi indirin ve kurun
   - iPhone'unuzu USB ile bağlayın
   - `.ipa` dosyasını seçin
   - Apple ID'nizi girin
   - "Start" butonuna tıklayın

3. **Cihazda güven ayarları:**
   - Ayarlar > Genel > VPN ve Cihaz Yönetimi
   - Apple ID'nizi seçin ve "Güven" butonuna tıklayın

## Teknik Detaylar

### Bildirimler

- iOS `UNUserNotificationCenter` kullanılır
- Her 2 saatte bir tekrarlayan local notification
- Okul modu açıldığında bildirimler geçici olarak durdurulur

### Veri Saklama

- Kullanıcı ayarları JSON formatında `Documents/creatine_settings.json` dosyasında saklanır
- Ayarlar: `notifications_enabled`, `school_mode`

### Antrenman Planı

- Statik veri olarak `workouts.py` içinde tanımlı
- Gün bazlı otomatik gösterim
- Haftalık plan: Çarşamba, Cumartesi, Pazar, Pazartesi

## Sorun Giderme

### Bildirimler çalışmıyor

- iOS Ayarlar > Bildirimler > Creatine Water Reminder'dan izinleri kontrol edin
- Uygulamayı yeniden başlatın

### IPA build hatası

- GitHub Actions loglarını kontrol edin
- Python ve Briefcase versiyonlarını kontrol edin
- `pyproject.toml` dosyasındaki yapılandırmayı kontrol edin

## Lisans

MIT

## Geliştirici

Onur

