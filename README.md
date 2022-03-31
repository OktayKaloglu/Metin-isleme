# Metin-isleme

- Kullanıcı metni ve satır genişliğini girdikten sonra program, metni iki yana 'sola ve sağa' hizalanmış olarak ekranda gösterir. Eğer kullanıcı isterse işlem bittikten sonra satır genişliğini tekrar değiştirip farklı boyutlarda görebilir. Metinde yer alan kelimeler ve metindeki tekrar sayıları, hem kelimelere göre alfabetik hem de tekrar sayılarına göre azalan sırada 2 sütun halinde listelenir, yine kullanıcı isterse yeni bir metin girip deneyebilir. 

- Bir diğer adımda ise Türkçe’de kullanılan 29 harfin kelime içindeki konumlarına göre tekrar sayılarını tablo şeklinde listelenir.

- Kelime uzayı fonksiyonunda ise tüm paragraflarda yer alan kelimeler Türkçe'de kullanılan 29 büyük harf ile rastgele olarak oluşturulmuş olan bir harf uzayında ddoğu, batı, güney, kuzey, güneydoğu, kuzeydoğu, güneybatı ve kuzeybatı yönlerinde aranır ve her bulunduğu kelimenin harf uzayındaki başlangıç konumu ve yönü, ya da hiç bulunmadığını ifade eden bir algoritma sayesinde ekrana listelenmektedir.

#### Örnek paragraf girdisi:

Durağan bellek özelliğiyle tanımlanan değişkene programın yürütülmesi başlamadan önce bellekte yer atanır Programda değişkene ilk kez başvurulduğunda ana belleğe yüklenir ve programın yürütülmesi sona erinceye değin atanan yer saklanır Dışsal bir blokta yürütme sırasında ilk adımda bazı değişkenlerin başlangıç değerlerinin biliniyor olması için durağan olarak tanımlanmaları uygun bir yoldur İçsel bir prosedürde bir değişkenin durağan olarak tanımlanması içinse prosedürün ilk yürütmesinden son yürütmesine değin değişkenin değerinin değişmemesi gibi bir koşulun varlığı konu olabilir Her iki durumda içsel ve dışsal prosedürde durağan bellek özelliğiyle tanımlanan değişken bir başka prosedürde yeni bellek sınıfı gerektirecek biçimde tanımlandığı sürece durağan bellek sınıfı özelliğini korur ayrıca durağan bellek özelliği taşıyan değişkenler programın neresinde tanımlanırsa tanımlansınlar yürütmeden önce belleğe atanırlar

#### Çıktılar
Paragrafın girilmesi ve satır genişliğine göre hizalanması:
![image](https://user-images.githubusercontent.com/57726183/154367166-9723eae6-1b14-4fe3-a542-7a136ebc999d.png)
##### Kelimelerin hem alfabetik hem tekrar sayısına göre azalan sırada sıralanması:
![image](https://user-images.githubusercontent.com/57726183/154367229-fed6e07c-645d-4ff8-9361-52e6e8ea39e6.png)

##### Kelimelerin konumları:
![image](https://user-images.githubusercontent.com/57726183/154367336-f4607b1f-9946-4052-9bb7-1a0451b80d24.png)
##### Kelimelerin harf uzayında kontrolü ve varsa konumları:
![image](https://user-images.githubusercontent.com/57726183/154367389-81312cfb-37e9-4fd6-ab38-b1066cda6f09.png)
![image](https://user-images.githubusercontent.com/57726183/154367417-386e36b8-62b5-450f-97d7-cdddfc743d3a.png)

Yön matrisi:

![image](https://user-images.githubusercontent.com/57726183/154369937-8946ffc3-09d0-40f5-b40d-5da383affdad.png)
