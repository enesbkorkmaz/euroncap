# euroncap
Euro NCAP Veri Analizi ve Değerlendirmesi 
Ad Soyad: Enes Burak Korkmaz                                                       
Bölüm: Bilgisayar Mühendisliği                                                                                        
Öğrenci Numarası: 234210052 

Konu Özeti: 
Bu proje, Avrupa Yeni Otomobil Değerlendirme Programı (Euro NCAP) tarafından sağlanan 
veri setini analiz ederek farklı marka ve modellerdeki araçların güvenlik performansını 
incelemeyi amaçlamaktadır. Projede, araçların yetişkin yolcu güvenliği, çocuk yolcu güvenliği, 
yaya güvenliği ve güvenlik asistanı gibi farklı metriklere göre değerlendirildiği analizler 
gerçekleştirilmiştir. 

Veriler üzerinde aşağıdaki analizler yapılmıştır:
- Ülkelere göre araçların ortalama yıldız dereceleri,
- Yetişkin yolcu güvenliğine göre en yüksek performansa sahip 10 aracın analizi,
- Yıllara göre güvenlik puanlarının değişimi,
- Araç sınıflarına göre dağılım ve yıldız derecelerinin incelenmesi,
- Çarpışma güvenliği metrikleri arasındaki korelasyon analizi. 
Sonuç olarak, proje, otomobil güvenliği trendlerini değerlendirmek ve güvenlik performansı ile 
yıldız dereceleri arasındaki ilişkileri belirlemek için önemli veriler sağlamaktadır.

Veri Kaynağı ve Toplama Yöntemi: 
Veri seti, Euro NCAP tarafından gerçekleştirilen çarpışma testlerinin sonuçlarını içermektedir. 
Toplamda 1997-2024 yılları arasında test edilmiş 773 farklı araç modeline ait veriler 
bulunmaktadır. Veri seti, Euro NCAP resmi sitesi üzerinden WebScraper ile elde edilen veriler 
ile oluşturulan bir CSV dosyası formatında sağlanmıştır. Python programlama dili ve ilgili 
kütüphaneler (pandas, matplotlib, seaborn) kullanılarak veriler işlenmiş ve analiz edilmiştir. 

Veri Seti Hakkında Bilgi: 
- Toplam Değişken Sayısı: 10
- Origin: Ülke
- Make: Araç Markası
- Model: Araç Modeli
- Year: Üretim Yılı
- Adult Occupant: Yetişkin Yolcu Güvenliği (%)
- Child Occupant: Çocuk Yolcu Güvenliği (%) 
- Vulnerable Road Users: Yaya Güvenliği (%)
- Safety Assist: Güvenlik Asistanı Performansı (%)
- Class: Araç Sınıfı - Overall Rating: Genel Yıldız Derecesi (1-5)
  
Veri Türleri:
-  Sayısal: Yüzdelik skorlar ve yıldız dereceleri.
- Kategorik: Araç sınıfları,ülkeler.

Web Scraper Sitemap:
{"_id":"euroncap","startUrl":["https://www.euroncap.com/en/ratings-rewards/latest-safety-ratings/?selectedMake=7277&selectedMakeName=Audi&selectedModel=0&selectedModelName=All&nodeId=1306&allProtocols=true&selectedStar=&includeFullSafetyPackage=true&includeStandardSafetyPackage=true&selectedProtocols=51097,49446,45155,41776,40302,34803,30636,26061,24370,-1&selectedClasses=1202,1199,1201,1196,1205,1203,1198,1179,40250,1197,1204,1180,34736,44997&allClasses=true&allDriverAssistanceTechnologies=false&selectedDriverAssistanceTechnologies=&thirdRowFitment=false"],"selectors":[{"id":"car_select","parentSelectors":["_root"],"type":"SelectorLink","selector":".c9 a","multiple":false,"linkType":"linkFromHref"},{"id":"car_name","parentSelectors":["_root"],"type":"SelectorText","selector":"h1","multiple":false,"regex":""},{"id":"car_type","parentSelectors":["_root"],"type":"SelectorText","selector":"a.car-class","multiple":false,"regex":""},{"id":"car_year","parentSelectors":["_root"],"type":"SelectorText","selector":"div.year","multiple":false,"regex":""},{"id":"adult_occupant","parentSelectors":["_root"],"type":"SelectorText","selector":".adult-occupant div.value","multiple":false,"regex":""},{"id":"child_occupant","parentSelectors":["_root"],"type":"SelectorText","selector":".child-occupant div.value","multiple":false,"regex":""},{"id":"vulnerable_road_users","parentSelectors":["_root"],"type":"SelectorText","selector":".pedestrian div.value","multiple":false,"regex":""},{"id":"safety_assist","parentSelectors":["_root"],"type":"SelectorText","selector":".safety-assist div.value","multiple":false,"regex":""},{"id":"car_select2","parentSelectors":["_root"],"type":"SelectorLink","selector":"assessment-row a","multiple":false,"linkType":"linkFromHref"},{"id":"scroll","parentSelectors":["_root"],"type":"SelectorElementClick","clickActionType":"real","clickElementSelector":"#mCSB_7_container li:nth-of-type(n+3) span","clickElementUniquenessType":"uniqueText","clickType":"clickOnce","delay":2000,"discardInitialElements":"do-not-discard","multiple":true,"selector":"#mCSB_7_container li:nth-of-type(n+3) span"}]}
