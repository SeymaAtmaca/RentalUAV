# UAV Rental Projesi ✈️✈️✈️

UAV Rental, Django ve Bootstrap kullanılarak geliştirilmiş bir web uygulamasıdır. Bu uygulama, kullanıcıların dronları kiralayabileceği ve yönetebileceği bir platform sağlar.
<br><br>
## ✈️ Özellikler 

- Kullanıcılar, dronları listeleyebilir, detaylarını görebilir, oluşturabilir, güncelleyebilir ve silebilir.
- Kullanıcılar, kiralama işlemlerini listeleyebilir, detaylarını görebilir, oluşturabilir, güncelleyebilir ve silebilir.
- Admin kullanıcıları, tüm dronları yönetebilir.
<br><br>
## ✈️ Kurulum

1.Projeyi klonlayın:

```bash
git clone https://github.com/SeymaAtmaca/RentalUAV.git
```

2.Proje dizinine gidin:
```bash
cd uav-rental
```

3.Sanal bir ortam oluşturun (isteğe bağlı):
```bash
python -m venv env
```

4.Sanal ortamı etkinleştirin (Windows):
```bash
env\Scripts\activate
```

5.Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

6.Veritabanını oluşturun:
```bash
python manage.py migrate
```

7.Admin kullanıcı oluşturun:
```bash
python manage.py createsuperuser
```

8.Sunucuyu başlatın:
```bash
python manage.py runserver
```

9.Tarayıcınızda http://localhost:8000 adresine gidin. Uygulamanız kullanıma hazır olacaktır. :))


<br><br>
## ✈️ Kullanım
* Uygulama ilk başlatıldığında bir giriş ekranı ile karşılaşılacaktır. Giriş sayfasında bir kullanıcı oluşturabilir ya da mevcut kullanıcınız ile giriş yaparak devam edebilirsiniz.
  
![1](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/1.png)

* Kullanıcılar arasında admin ve normal kullanıcılar olmak üzere yetkilendirme yapılmıştır. İlk olarak admin kullanıcı üzeridnen devam edersek profil sayfası admin için aşağıdaki gibidir. Burada daha önceden test edebilmek için bazı veriler eklenmiştir. UAV' lere ait Güncelleme / Silme eylemleri Admin kullanıcı yetkisine bağlıdır. 

![2](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/2.png)


* Admin UAV güncelleme eylemi için mevcut UAV' nin bilgilerini içeren form ekranı açılır. Admin kullancıı bu ekranda değerleri değiştirebilir ve Save aksiyonu alarak UAV bilgilerini günceller, profil sayfasına yönlendirilir.

![3](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/3.png)


* Silme aksiyonu alınmak istendiğinde ise Admin kullanıcısının tekrar onay vermesi istenir. Eğer "Onayla" butonuna tıklarsa mevcut öğe silinir. Öğe silindikten sonra veya "İptal" butonuna basıldıktan sonra tekrar profil sayfasına yönlendirilir.

![4](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/4.png)


* Profil sayfasının ikinci bölümünde yer alan kiralama alanında ise "Güncelleme","İptal", "UAV Kirala" eylemleri yer almaktadır. Eğer kullanıcı "Güncelle" aksiyonu alırsa mevcut kiralamaya ait bilgilerin yer aldığı Kiralama Formu açılır. Kullanıcı bu alanda bilgilerini güncelleyip Kaydet aksiyonu alabilir.

![5](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/5.png)

* Eğer kullanıcı "İptal" aksiyonu alırsa bir onay sayfasına yönlendirilir. Aynı şekilde bu alanda kulalnıcının silme işlemini onaylaması beklenir ve tekrar profil sayfasına yönlendirilir.

 ![6](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/6.png)

 * Yeni bir kiralama işlemi açılmak istenirse kulalnıcı "Kiralama Formu" ekranına yönlendirilir ve istenen bilgileri girmesi beklenir.

 ![8](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/8.png)


 <br><br><br>
 * Normal kullanıcı yetkileri ile profil ekranı aşağıdaki gibi görünmektedir. her kullanıcı kendi kiralamalarını görmekte ve bunlar için işlem yapabilmektedir.

 ![7](https://github.com/SeymaAtmaca/RentalUAV/blob/main/img/7.png)

 <br><br><br>
 ## ✈️ Teknolojiler : 
 * Python
 * Django
 * Bootstrap
 * SQLite
 * HTML / CSS
