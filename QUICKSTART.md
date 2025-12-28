# Hızlı Başlangıç Kılavuzu

## Windows'tan IPA Alma (3 Adım)

### 1. Kodu GitHub'a Yükle
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### 2. GitHub Actions'ı Çalıştır
- GitHub repository'nize gidin
- "Actions" sekmesine tıklayın
- "Build iOS IPA" workflow'unu seçin
- "Run workflow" butonuna tıklayın
- 10-15 dakika bekleyin

### 3. IPA'yı İndir
- Workflow tamamlandıktan sonra
- "Artifacts" bölümünden "creatine-water-reminder-ipa" dosyasını indirin
- ZIP'i açın, `.ipa` dosyasını alın

## IPA'yı iPhone'a Yükleme

### Sideloadly Kullanarak (Önerilen)
1. [Sideloadly](https://sideloadly.io/) indirin
2. iPhone'unuzu USB ile bağlayın
3. `.ipa` dosyasını seçin
4. Apple ID'nizi girin
5. "Start" butonuna tıklayın
6. Cihazda: Ayarlar > Genel > VPN ve Cihaz Yönetimi > Apple ID'nizi seçin > "Güven"

## Yerel Test (Windows)

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Python kodunu test et (UI olmadan)
python -m src.creatine.app
```

Not: Windows'ta iOS uygulamasını tam olarak test edemezsiniz, sadece Python kodunu test edebilirsiniz.

## Proje Yapısı Özeti

```
src/creatine/
├── app.py          # Ana UI (Toga)
├── notifications.py # iOS bildirim yönetimi
├── workouts.py     # Antrenman planı
└── storage.py      # Ayarlar (JSON)

ios/CreatineWaterReminder/
└── NotificationBridge.swift  # iOS native kod (opsiyonel)

.github/workflows/
└── ios.yml         # GitHub Actions build
```

## Önemli Notlar

- IPA imzasız export edilir (sideloading için)
- Bildirimler iOS'ta çalışır (Windows'ta test edilemez)
- Ayarlar JSON dosyasında saklanır
- Antrenman planı statik veridir

