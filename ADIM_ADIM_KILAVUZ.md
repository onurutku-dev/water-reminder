# 📱 ADIM ADIM KILAVUZ - Mala Anlatır Gibi

## 🎯 AMAÇ: iPhone'a uygulamayı yüklemek

Windows'ta olduğun için iOS uygulamasını kendin derleyemezsin. Bu yüzden GitHub Actions kullanacağız (ücretsiz, otomatik).

---

## ✅ ADIM 1: Git Kurulumu (Eğer yoksa)

### Git yüklü mü kontrol et:
1. Windows tuşuna bas
2. "cmd" yaz ve Enter'a bas
3. Şunu yaz: `git --version`
4. Eğer "git is not recognized" hatası alırsan → Git yüklü değil

### Git yükle (yoksa):
1. https://git-scm.com/download/win adresine git
2. "Download for Windows" butonuna tıkla
3. İndirilen dosyayı çalıştır
4. Hep "Next" de, kurulumu bitir

---

## ✅ ADIM 2: GitHub Hesabı Oluştur (Yoksa)

1. https://github.com adresine git
2. Sağ üstte "Sign up" butonuna tıkla
3. Email, şifre gir, hesap oluştur
4. Email'ini doğrula (gelen kutuna bak)

---

## ✅ ADIM 3: Kodu GitHub'a Yükle

### 3.1. Proje klasöründe Git başlat:

1. Proje klasörüne git: `C:\Users\admin\Desktop\New folder (5)`
2. Klasördeyken sağ tıkla → "Git Bash Here" seç (veya PowerShell aç)
3. Şu komutları sırayla yaz:

```bash
git init
git add .
git commit -m "İlk commit"
```

### 3.2. GitHub'da yeni repository oluştur:

1. GitHub.com'a git, giriş yap
2. Sağ üstte "+" işaretine tıkla → "New repository"
3. Repository adı: `creatine-water-reminder` (veya istediğin isim)
4. **Public** seç (ücretsiz için)
5. **"Initialize this repository with a README" işaretini KALDIR** (boş olsun)
6. "Create repository" butonuna tıkla

### 3.3. Kodu GitHub'a gönder:

GitHub'da oluşturduğun repository sayfasında, "Quick setup" bölümünde komutlar göreceksin. Şunları kullan:

**Eğer HTTPS kullanıyorsan:**
```bash
git remote add origin https://github.com/KULLANICI_ADIN/creatine-water-reminder.git
git branch -M main
git push -u origin main
```

**Not:** `KULLANICI_ADIN` yerine kendi GitHub kullanıcı adını yaz!

**Eğer GitHub kullanıcı adı/şifre isterse:**
- Kullanıcı adı: GitHub kullanıcı adın
- Şifre: GitHub şifren (veya Personal Access Token - aşağıda anlatıyorum)

**Personal Access Token oluştur (şifre çalışmazsa):**
1. GitHub → Sağ üst profil → Settings
2. Sol menüden "Developer settings"
3. "Personal access tokens" → "Tokens (classic)"
4. "Generate new token" → "Generate new token (classic)"
5. Note: "creatine-app" yaz
6. "repo" kutusunu işaretle
7. "Generate token" butonuna tıkla
8. Çıkan token'ı kopyala (bir daha gösterilmez!)
9. Git push yaparken şifre yerine bu token'ı kullan

---

## ✅ ADIM 4: GitHub Actions'ı Çalıştır

### 4.1. Repository'ne git:
1. GitHub.com'da repository'ne git
2. Üstte "Actions" sekmesine tıkla

### 4.2. Workflow'u çalıştır:
1. Sol menüden "Build iOS IPA" workflow'unu seç
2. Sağ üstte "Run workflow" butonuna tıkla
3. "Run workflow" butonuna tekrar tıkla
4. **10-15 dakika bekle** (macOS'ta build yapıyor)

### 4.3. İlerlemeyi takip et:
- Sarı nokta = Çalışıyor
- Yeşil tik = Başarılı ✅
- Kırmızı X = Hata ❌ (loglara bak)

---

## ✅ ADIM 5: IPA Dosyasını İndir

1. Workflow tamamlandıktan sonra (yeşil tik görünce)
2. "Artifacts" bölümüne git
3. "creatine-water-reminder-ipa" linkine tıkla
4. ZIP dosyası inecek
5. ZIP'i aç, içindeki `.ipa` dosyasını bir yere kopyala

---

## ✅ ADIM 6: iPhone'a Yükle (Sideloadly ile)

### 6.1. Sideloadly'yi indir:
1. https://sideloadly.io/ adresine git
2. "Download for Windows" butonuna tıkla
3. İndirilen dosyayı çalıştır ve kur

### 6.2. iPhone'u bağla:
1. iPhone'u USB kablosuyla bilgisayara bağla
2. iPhone'da "Bu bilgisayara güven" mesajına "Güven" de
3. Sideloadly'yi aç

### 6.3. IPA'yı yükle:
1. Sideloadly'de:
   - "iOS Device" seçili olsun
   - iPhone'un görünüyor mu kontrol et
2. "IPA" butonuna tıkla → `.ipa` dosyasını seç
3. "Apple ID" kısmına Apple ID email'ini gir
4. "Password" kısmına Apple ID şifreni gir
5. **"Start" butonuna tıkla**
6. 2-3 dakika bekle (yükleme sırasında)

### 6.4. iPhone'da güven ayarı:
1. iPhone'da: Ayarlar → Genel → VPN ve Cihaz Yönetimi
2. Apple ID'ni seç (email adresin görünecek)
3. "Güven" butonuna tıkla
4. "Güven" de tekrar

### 6.5. Uygulamayı aç:
1. iPhone ana ekranında "Creatine Water Reminder" uygulamasını bul
2. Aç (ilk açılışta biraz yavaş olabilir)
3. Bildirim izni isteyecek → "İzin Ver" de

---

## 🎉 TAMAMLANDI!

Artık uygulaman iPhone'unda! Her 2 saatte bir su içme hatırlatıcısı gelecek.

---

## ❓ SORUN GİDERME

### "Git is not recognized" hatası:
→ Git yüklü değil, ADIM 1'i yap

### "Permission denied" hatası:
→ Personal Access Token kullan (ADIM 3.3'te anlattım)

### GitHub Actions başarısız:
→ "Actions" sekmesinde workflow'a tıkla, logları kontrol et
→ Genelde Python versiyonu veya bağımlılık hatası olur

### Sideloadly "Device not found":
→ iPhone'un USB ile bağlı mı kontrol et
→ iPhone'da "Bu bilgisayara güven" dedin mi?

### Uygulama açılmıyor:
→ Ayarlar → Genel → VPN ve Cihaz Yönetimi → Apple ID → "Güven" yaptın mı?

### Bildirimler gelmiyor:
→ iPhone Ayarlar → Bildirimler → Creatine Water Reminder → İzinleri aç
→ Uygulamada "Su Bildirimleri" switch'ini aç

---

## 📞 YARDIM LAZIMSA

Hangi adımda takıldığını söyle, o adımı daha detaylı anlatayım!

