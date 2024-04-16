# Zynpbus: Otomatik Otobüs Kartı Bakiye Yükleyici
Bir arkadaşa hayır yapmak amacıyla geliştirilmiş olan bu selenium python otomasyonu, koda tanımlamış olduğunuz otobüs kartı id no verisi kullanarak her 1 dakika bir kontrol eder otobüs kartınız ile bir biniş yaptığınızda yani bakiyeniz değiştiğinde yine koda tanımlamış olduğunuz kredi veya banka kartı bilgilerini kullanarak kartınıza para yükler.

## Proje Yapısı

### kontrol.py
- Koda tanımlı olan kart idsini kullanarak bursa kartın sitesinden kullanıcının bakiyesini kontrol eder ve eğer bakiye değişirse para.py dosyasını çalıştırır.

### para.py
- Koda tanımlı olan kart id ve diğer gerekli bilgileri forma doldurur ve ödeme kısmına geçer, kredi kartı bilgilerini de doldurduktan sonra 3D secure doğrulama kısmına geçer.Bu doğrulama kodu alma kısmı şöyle gerçekleşiyor: Android telefonlarda MacroDroid isimli bir otomasyon uygulaması var, bu uygulamada ayarladıgımız makro telefona gelen her sms'i bizim 3d.php dosyamıza post isteği ile yolluyor, php kodu sadece doğrulama kodu olan kısmı ayırıyor ve bir txt dosyasına kaydediyor.Bilgisayarınızda çalışan python kodu bu txt dosyasına erişip kodu yazıyor ve hayırlı olsun ödeme tamamlandı.

### 3d.php
- MacroDroid uygulamamızdan gelen 3D secure doğrulama kodunu içeren post isteği alan ve kodu txt dosyasına kaydeden php kodu.

## Nasıl Kullanılır

**Adım 1:** Infinity Free sitesinden bir web sitesi oluşturun ve domaine bağlayın, sitenin ana dizine 3d.php dosyasını atın ve post_verileri.txt adlı bir dosya oluşturun.

**Adım 2:** Android telefonunuza MacroDroid uygulamasını yükleyip, sağ alttaki artı butonuna tıklayıp yeni makro ekleyelim.Tetikleyiciler kısmında herhangi bir kişiden sms gelmesi şeklinde eylemler kısmını ise en altta olan web etkileşimleri kısmından http olarak istek türünü post içerik gövdesini text plain olarak ayarlayıp sagdaki 3 noktaya basıyoruz, oradan sms mesajı yazıyoruz ve son olarak linki sizin domainize göre düzenleyip kaydediyoruz.

**Adım 3:** 2 python dosyamızda ki verileri (kredi kartı no, infinity freeden alıp txt dosyanini oluşturduğunuz link filan) kendimize göre düzenledikten sonra geriye çalıştırıp, arkamıza yaslayıp beklemek kalıyor.
