# Instagram Görsel İndirme Projesi

Bu proje, Selenium ve Python kullanarak belirli bir Instagram profilinin gönderilerindeki görselleri indirmenizi sağlar. Kullanıcı adı ve şifre girerek Instagram'a giriş yapar, ardından belirtilen profilin gönderilerinden görsel URL'lerini alır ve bu görselleri belirtilen bir klasöre kaydeder.

## Özellikler:
- Instagram giriş işlemi
- Profil sayfasına giderek gönderileri tarama
- Sayfa kaydırma işlemi ile daha fazla gönderi yükleme
- Gönderi görsellerini indirip, belirli bir klasöre kaydetme
- Görsellerin güvenli isimlerle kaydedilmesi

## Gereksinimler:
- Python 3.x
- Selenium
- webdriver_manager
- requests

## Kurulum:
1. Projeyi yerel bilgisayarınıza indirin.
2. Gerekli Python paketlerini yüklemek için aşağıdaki komutu kullanın:
   ```bash
   pip install selenium webdriver_manager requests
3. ChromeDriver'ı otomatik olarak yüklemek için webdriver_manager kullanılacaktır.

## Kullanım:
1. username ve password değişkenlerine Instagram hesabınızın giriş bilgilerini girin.
2. profile_name değişkenine indirmek istediğiniz Instagram profilinin kullanıcı adını yazın.
3. Python dosyasını çalıştırarak belirtilen profilin görsellerini indirebilirsiniz.
