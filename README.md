# Gps-mqtt-data-register


Projemde GPS'ten alinan verileri MQTT haberleşme protokolü kullanarak yerel bir cihaza 
konum bilgilerinin (latitute, longitute) aktarımı ve bu bilgilerin bir dosyaya kaydedilmesinden bahsettim.

İlk olarak proje kullanılacak olan GPS sensörü ve Raspberry Pi 3B + bağlantıları yapıldı.
![image](https://user-images.githubusercontent.com/41265583/171617656-cdfd6639-bb46-44fa-b04b-87ac4cd84616.png)

Daha sonra Linux işletim sistemi üzerinden hem gelecek olan bilgilerin alınabilmesi ve kaydedilebilmesi için gerekli
kodlar yazıldı hem de Raspberry Pi 3B + uzaktan bağlantı sağlamak ve ekran görüntüsünü sağlamak amacıyla PUTTY ve VNC Viewer
programı kuruldu.

Ayrıca bu programların kullanımı ve seri haberleşme yapılabilmesi için Raspberry Pi üzerindeki gerekli ayarlamalarda yapıldı.
![image](https://user-images.githubusercontent.com/41265583/171618660-f937d778-d627-48e2-afe1-e41b988e7cf6.png)
![image](https://user-images.githubusercontent.com/41265583/171618665-035bd8f5-047e-479d-8942-3ba254e26e6a.png)

![image](https://user-images.githubusercontent.com/41265583/171618711-d30bc916-951f-4263-8635-3aae21117f14.png)
![image](https://user-images.githubusercontent.com/41265583/171618723-6e9bee0c-3cf9-405a-840f-ed60b6421b1a.png)

Artık başlamaya hazır durumdayız.

Buradan sonra MQTT protokolünün kullanılabilmesi için bu kütüphanenin sistemimizde yüklü olması gerekir.
NOT: Projemde Python kod kullanıldığı için MQTT'nin Python dili ile kullanılabilir olan kütüphanesi kullanılmalıdır.

Bunun için paho.mqtt yi yüklememiz gerekiyor.

Terminal ekranına kullanmakta olduğunuz pip versiyon bilgisine göre şu komutu yapıştırıp paho mqtt'yi yükleyebilirsiniz.
                    -pip install paho-mqtt
Ardından kodumuzu yazmaya başlayıp şu yöntem ile paho mqtt'yi kodumuza dahil edebiliriz.
                    from paho.mqtt import client as mqtt_client

!!!Önemli Bilgi: MQTT'nin koda dahil edilmesinden sonra ayarlanması gereken bazı özellikleri vardır. Bunlar MQTT-Publish.py adlı dosyada
gösterilmiştir. Burada önemli olan yayınlayacağımız mesajın ve dinleme yapacağımız kodun aynı MQTT Broker'a bağlı olması gerektiğidir.
(Port bilgisi unutulmamalıdır.)

MQTT bağlantısı kurulduktan sonra GPS sensöründen gelen bilgileri düzenlememiz gerekiyor. Gelen bu bilgiler NMEA 0183 standardına
uyumlu olarak gelecektir.

Bu projede gelen paketler(veriler) içerisinden GPGGA paketi kullanılmıştır. Lakin daha yaygın olan GPRMC paketide tercih edilebilir.

Burada kullanmakta olduğumuz paketin içindeki latitute ve longitute bilgilerini derece cinsine çeviriyoruz. Ardında bu bilgileri MQTT
aracılığıyla yayınlıyoruz.

Şuana kadar Raspberry Pi üzerinden aldığımız bilgileri MQTT kullanarak yayınladık. Şuandan itibaren kendi yerel cihazımızla 
(Linux Ubuntu 16.04 kurulu bir laptop) yayınlanan bu bilgiyi dinleyip bir .txt uzantılı dosyaya kaydeceğiz.

