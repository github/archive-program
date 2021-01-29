# GitHub Kod Kasası Kılavuzu

## Giriş

Bu arşiv, GitHub Kod Kasası, misyonu gelecek nesiller için açık kaynaklı yazılımı korumak olan GitHub Arşiv Programı tarafından oluşturuldu. Bunu bir yıl sonra veya bin yıl sonra okuyabilirsiniz, ancak her iki durumda da içeriğinin ve belki de açık kaynak kavramının sizin için yararlı olacağını umuyoruz.

Bu öncelikle bir yazılım arşividir. Yazılım, bir bilgisayarın eylemlerini kontrol etmek için kullanılan bir dizi komuttur. Bilgisayar, matematiksel fonksiyonları, bizim çok ötesinde güçlere sahip bir insan zihninden çok daha hızlı otomatik olarak gerçekleştirebilen bir cihazdır. Bilgisayarlarımız, evrenin sırlarını keşfetmeye yardımcı olmak, tüm insanlığı her yerde mevcut olan bir bilgi ağında birbirine bağlamak, sesleri iletmek ve ayrıntılı hareketli görüntüleri elektrikli ekranlara yansıtmak için yeterince hızlı sinyalleri değiştirmek ve çok uzaktaki muazzam güçlü makineleri kontrol etmek için kullanılır. insan emeğinin hem kapasitesini hem de hassasiyetini aşıyor.

Yazılımı olmayan bir bilgisayar bunların hiçbirini yapamaz. Bir bilgisayar olağanüstü ve harika bir şeydir, ancak yazılım olmadan bu gücü hiçbir işe yaramaz. Bu arşivin amacı, yazılım hakkında bildiklerimizi size iletmektir.

Yazılım, karmaşık ancak insan tarafından okunabilir komut dizileri olarak yazılır ve çeşitli tatları programlama dilleri olarak bilinir, çünkü eksiksiz bir yazılım birimine genellikle program denir. Bu programlar daha sonra bilgisayarlar tarafından kullanılan birlerin ve sıfırların ikili diline dönüştürülür. Bu işlem derleme olarak bilinir.

Derlenen yazılımın, kaynak kodu olarak da bilinen orijinal program formuna geri şifresini çözmek çok zor olduğundan, insanların bu orijinal formu gizli tutmaları ve üzerinde mülkiyet talep etmeleri mümkündür. Açık kaynaklı yazılım, farklı bir yazılım türü değil, farklı bir yaklaşımdır. Açık kaynak ahlakı, gizliliği ve sahipliği reddeder. Açık kaynak yazılım programları, onu kullanmak isteyen herkese ücretsiz olarak sunulur, böylece bu programları iyileştirebilir veya yeni ve daha iyi bir şey oluşturmak için kullanabilirler.

Açık kaynaklı bir proje, kendi kendini organize eden bir topluluğun kolektif çalışmasıdır ve sayısı binlerle ifade edilebilir. Burada arşivlenen tüm açık kaynak yazılım projelerinin birikimi, milyonlarca kişiden oluşan bir topluluğun eseridir. Belirli kişiler, herhangi bir projede, kaynak kodunun en son resmi sürümünde önerilen değişiklikleri onaylama veya reddetme gibi özel haklara sahip olsalar da, hiç kimse onun sahibi değildir. Herkes, herhangi bir açık kaynak projesinin tam bir kopyasını herhangi bir zamanda, hiçbir ücret ödemeden veya ceza almadan alma ve kullanma hakkına sahiptir. Bu, bir projenin çatallanması olarak bilinir.

Birçok kişi aynı anda kaynak kod üzerinde çalıştığında, tüm değişikliklerini takip etmek ve bütünleştirmek zordur. 'Git' olarak bilinen açık kaynaklı bir proje, bu sorunu çözmeye adanmıştır. Bir projeye yapılan tüm eklemelerin ve değişikliklerin eksiksiz bir geçmişini Git deposu olarak bilinen bir varlığa entegre eder. Bu arşiv, esasen bu tür depoların arşividir.

Bu arşiv, dünyanın her yerinden insanların yazdıkları yazılım programlarını depolamasına, bu programlardaki değişiklikleri takip etmesine ve bunları iyileştirmek ve genişletmek için başkalarıyla işbirliği yapmasına olanak tanıyan bir hizmet sunan 'GitHub' adlı bir şirket tarafından oluşturuldu. GitHub, hizmetlerini halka açık açık kaynak yazılım geliştiricilerine ücretsiz olarak sunar. On milyonlarca böyle kullanıcısı var.

Aşağıda, bu yazılım arşivinden en iyi şekilde yararlanmak için bilmeniz ve sahip olmanız gerektiğine inandığımız şeylerin bir açıklaması yer almaktadır. Bunların bir kısmını veya herhangi birini bilmiyor veya anlamıyorsanız, umutsuzluğa kapılmayın! Ayrıca bu gereksinimlerin nasıl yerine getirileceğine dair bir kılavuz da ekledik. Herhangi bir nedenle bunları kendiniz başaramazsanız, o zaman torunlarınız başarabilir.

## Arşivi Kullanmak için Elinizde Bulunması Gerekenler

Prensip olarak, bu arşivin içeriğine erişmek için ihtiyacınız olan tek şey bir aydınlatma kaynağı ve bir çeşit büyüteçtir. Bununla birlikte, verilerinin çoğu (hepsi olmasa da) kodlanmış ve sıkıştırılmış bir biçimde film makaralarına çok sıkı bir şekilde paketlenmiştir. Bu verilerin okunması, kodunun çözülmesi ve sıkıştırmasının açılması, hatırı sayılır bir hesaplama gerektirecektir. Teoride bilgisayar olmadan da yapılabilir ama çok sıkıcı ve zor olurdu.

Bizim beklentimiz, yazılım, bilgisayar ve diğer terimlerle ilgili tanımlarımıza ihtiyacınız olmamasıdır. Muhtemelen bizimkinden çok daha gelişmiş ve muhtemelen temelde farklı bir şekilde tasarlanmış, kendi bilgisayarlarınız olduğunu hayal ediyoruz. Aşağıdaki genel bakışı ve kılavuzu anladıktan sonra, tüm verilere kolayca erişebileceksiniz.

Bununla birlikte, bizimkinden daha düşük bilgisayarlara sahip olmanız veya hatta hiç bilgisayarınız olmaması mümkündür. Böyle bir olasılık durumunda, Teknoloji Ağacı adını verdiğimiz sıkıştırılmamış, kodlanmamış, insan tarafından okunabilir bir veri makarası hazırladık. Teknoloji Ağacı, zamanla bu arşivdeki açık kaynak yazılımı kullanabilen bilgisayarları yeniden oluşturmak için bu bilgileri kullanabilmeniz umuduyla temel teknolojilerimiz, bilgisayarlarımız ve yazılımımız hakkında bilgiler içerir.

## İçinde Ne Var

Arşiv çok büyük - yaklaşık 21 trilyon bayt (aşağıda açıklanmıştır) - çünkü son derece kapsayıcı ve demokratiktir. Milyonlarca insan, yazdıkları yazılımı herkesin kullanımına sunar. Bu arşiv, GitHub kullanıcılarının aktif olarak geliştirmekte olduğu tüm genel yazılımların bir anlık görüntüsünü (tek bir zamanda tek bir kopyasını) içerir. Bu, milyonlarca ayrı depo içerdiği anlamına gelir. Umudumuz, bu geniş, demokratik yaklaşımın geleceğin tarihçilerinin ilgisini çekmesidir.

Bu arşive dahil edilen depolar yalnızca son işleme sürelerine, yani en son güncellendiği zamana ve yıldız sayısına göre belirlendi. (GitHub kullanıcıları, ilgilendiklerini veya kendileri için önemli olduklarını belirtmek için herkese açık depolara 'yıldız' atabilirler.) Anlık görüntü 02/02/2020 tarihinde, yani Şubat ayının ikinci gününde başlatıldı. Zamanı saydığımız için Miladi takvimin 2020 yılı. İçinde bulunan depolar şunlardır: önceki 80 gün içinde herhangi bir kaydetme içeren tüm depolar; önceki 365 gün içinde en az bir yıldız içeren tüm depolar; ve en son ne zaman güncellendiğine bakılmaksızın en az 250 yıldızlı tüm kod depoları.

Tabii ki, bu depoların hepsi etki ve bağımlılıkları açısından eşit derecede önemli değildir. Teknoloji Ağacı, arşivdeki en önemli depoların bir dizinini ve kısa bir açıklamasını ve hangilerinin en pratik olduğunu belirlemek için tüm bu milyonlarca depo arasında gezinmek zorunda kalmadan erişilebilmesi için her birinin hangi makarada bulunabileceğini listeler. işe yarar.

## Arşive Genel Bakış

Arşiv, 188 makara filmden oluşuyor: Teknoloji Ağacı adını verdiğimiz, insan tarafından okunabilir bilgi ve yol gösterici "kılavuz makarası" ve arşivlenmiş yazılım içerir 187 makara. Her makara 65.000 ayrı çerçeve içerir. Her makaranın başındaki çerçeveler ve kılavuz makaranın çerçeveleri, insan tarafından okunabilir metin ve resimler içerir. Diğer tüm film kareleri, QR kodları olarak bilinen görsel bir biçimde saklanan dijital verilerden oluşur.

Dijital veriler, nihayetinde ikili formatta, yani 0 ve 1 şeklinde depolanan veriler anlamına gelir, çünkü bilgisayarların kendileri ikili olup - 1 veya 0'a karşılık gelen "açık" veya "kapalı" elektrik sinyalleri tarafından kontrol edilir ve bu nedenle ikili veriler bilgisayarların anlaması diğerlerinden çok daha kolaydır.

Her makaranın başında depolanan, insan tarafından okunabilir meta veriler, filmin kendisi hakkında bilgi, kullanılan QR kodlaması için bir kılavuz, onu çözmek için bir yazılım programı ve bir indeks içerir. Dizin, o makarada depolanan her dosya için başlığı, başlangıç çerçeve numarasını ve sağlama toplamını listeler.

Dosya, tutarlı tek bir veri varlığıdır. Sağlama toplamı, karma işlevi olarak bilinen bir hesaplamanın benzersiz bir değeridir ve içeriğinin zarar görmediğinden veya bozulmadığından emin olmak için bir dosyanın tüm içeriği üzerinde çalışır; arşivde kullanılan hash işlevi 'SHA-1' olarak bilinir.

Her QR kodu, filmin neredeyse tüm karesini kaplayan küçük beyaz veya siyah karelerden oluşan bir alandan oluşur. QR kodlarını, insan tarafından okunabilir metinden çok daha kompakt ve sağlam oldukları için kullanıyoruz. Bir QR kodu ikili verilere, yani bir dizi bir ve sıfıra kod çözer.

Bu kod çözme, bu ikili verileri anlamlı bilgilere dönüştürmenin yalnızca ilk adımıdır. Sıkıştırılmış verilerdir, yani A harfini 128 kez yazmak yerine "128xA" yazılmasına benzer şekilde, yerden tasarruf etmek için sıkıştırılmıştır. Kodu çözüldükten sonra açılmalıdır.

Açıldıktan sonraki sonuç arşiv dosyası olarak bilinir: tek bir yazılım projesinin havuzunun tüm içeriğini içeren tek bir dosya. Depoların çoğu birçok dosya içerir, bu nedenle bu arşiv dosyası, birçok ayrı bölüm içeren bir kitap veya diğer birçok kutuyu içeren bir kutu gibidir. Arşiv dosyasını, erişmeden önce bileşen dosyalarına açmak, kesinlikle gerekli olmasa da genellikle avantajlıdır.

Son olarak, her bileşen dosyası kendi ikili veri kümesidir, yani birler ve sıfırlardır. Biçimini biliyorsanız, veriler anlam ifade edebilir. Örneğin, arşivdeki en yaygın format olan 'UTF-8' olarak bilinen formatta, birler ve sıfırlar bayt olarak bilinen sekizli gruplara bölünür, 01000001 baytı A harfini temsil eder; üç bayt 01101001 01101110 01110100 int kelimesini temsil eder; ve iki bayt 11000011 10000011, Ã (üstte tilde vurgulu A) harfini temsil eder.

Bu veri arşivleme süreci, önce sıkıştırılmış ve sonra QR ile kodlanmış arşiv dosyalarına paketlenmiş ikili dosyalar, basitçe insan tarafından okunabilir metin yazmakla karşılaştırıldığında açıkça karmaşıktır. Geçmeniz gereken arşivden çıkarma süreci - QR'den sıkıştırılmış ikiliye; sıkıştırılmamış olarak sıkıştırılmış; arşiv dosyasını birden çok dosyaya; metin dosyalarını insan tarafından okunabilir metne dönüştürmek - benzer şekilde karmaşıktır. Bunun nedeni, bu karmaşıklığın, normalde mümkün olandan çok daha fazla veriyi nispeten kolay bir şekilde bilgisayar tarafından okunabilir bir şekilde depolamamıza izin vermesidir.

Bu karmaşıklık sizin için zor ve maliyetliyse özür dileriz, ancak beklentimiz, bu durumda bu kılavuzun ve insan tarafından okunabilen Teknoloji Ağacının bu karmaşıklığı hafifleteceği ve belki de sizin için arşivden daha yararlı olabileceği yönündedir. içerikler, en azından bilgisayarlarınız arşiv verilerinin karmaşıklığıyla başa çıkmanın kolay olacağı kadar gelişene kadar.

## Dosyalar, Dizinler, Depolar ve Veri Biçimleri

Arşivin mantıksal olarak nasıl bölündüğünü tartışmak öğretici olabilir. Özellikle, dosyalar, dizinler ve veri formatları hakkında bir tartışma muhtemelen yardımcı olacaktır.

Bir dosya, tek bir ada sahip tutarlı bir varlık halinde gruplandırılmış bir veri koleksiyonudur: veriyi kum olarak düşünün ve bir dosyayı kum ve yalnızca kum tutabilen bir tür çanta olarak düşünün. Bir dizin, bir dosya koleksiyonudur: onu yalnızca diğer çantaları tutabilen bir tür çanta olarak düşünün. Bu metaforu takiben, her depo, bir dizi dosya ve / veya birkaç dizin içeren, kök dizin olarak bilinen bir dış dizinden oluşur. Her bir dizin sırayla hem dosyaları hem de dizinleri içerebilir.

Bu yapı tercih edilir çünkü gruplar halinde düzenlenmiş dosyalar, tek bir dosya koleksiyonuyla çalışmaktan çok daha kolaydır. Dış dizindeki belirli bir dosyanın tanımlayıcısı, kökten başlayarak, her adın arasında bir / karakteri olan kendi bireysel adıyla başlayan, onu kapsayan tüm dizinlerin adlarından oluşur. Örneğin, kök dizinde README.md adlı bir dosya /README.md olarak tanımlanacak ve /public/www/index.html olarak tanımlanan bir dosya, 'www' dizinindeki 'www' dizininde bulunan index.html olacaktır. kök dizinin içindeki public 'dizini.

Her bir arşivin, arşivde bir _ veya alt çizgi karakteri olan bir bölücü ile ayrılmış iki adı vardır. (Tarihsel olarak bir / veya bölü çizgisi idi, ancak bu aynı zamanda bir dizini belirtmek için de kullanıldı, bu nedenle netlik için _ kullanırız.) İlk ad, o depoya sahip olan GitHub hesabıdır; ikincisi, bireysel arşivin adıdır. Arşiv ve dosya tanımlayıcılarının kombinasyonu, arşivdeki tek bir dosyayı benzersiz şekilde tanımlamak için kullanılabilir. Örneğin, GitHub hesabı 'rezendi' içindeki 'ykarma' havuzundaki 'web' dizinindeki 'package.json' dosyası arşivdeki rezendi_ykarma'da /web/package.json olarak benzersiz bir şekilde tanımlanabilir.

Farklı türdeki dosyaların farklı amaçları vardır. GitHub arşivi büyük ölçüde metin dosyalarından, yani verilerinin yazılı dili temsil etmesi amaçlanan dosyalardan oluşur. Çoğu yazılım, kaynak kodu olarak bilinen yüksek düzeyde yapılandırılmış metin içeren metin dosyalarında yazılır. Derleyici olarak bilinen özel bir program, bu insan tarafından okunabilir kaynak kodunu, derlenmiş kod veya makine kodu olarak bilinen bilgisayarda okunabilir talimatlara dönüştürür.

Görsel görüntüleri temsil eden veya derlenmiş kod içeren dosyalar gibi metin dosyaları olmayan dosyalara genellikle ikili dosyalar denir. Metin dosyaları da sonuçta 1'ler ve 0'lar olduğu için bu maalesef yanıltıcı bir terimdir. Metin dosyası olmayan dosyalara metin olmayan dosyalar olarak atıfta bulunacağız.

Yazılı insan dilini 1'ler ve 0'ları kullanarak temsil etmenin birçok yolu vardır. Tarihsel nedenlerden ötürü, kaynak kodların çoğu orijinal olarak Latin alfabesi olarak bilinen şekilde yazılmıştır. Latin alfabesi, konuşulabilir kelimeleri temsil etmek için kullanılan 26 temel karaktere sahiptir ve bunların her biri iki biçime sahiptir, büyük harf ve küçük harf. Ayrıca sayıları temsil etmek için 10 hanesi vardır. Latin alfabesi, yapıyı ve diğer kavramları belirtmek için kullanılan çeşitli diğer ilişkili sembollerle birlikte, 128 farklı karakteri temsil edebilen ve tarihsel nedenlerle çoğu yazılımda uzun yıllar baskın olan 'ASCII' olarak bilinen bir formatta 1'ler ve 0'lara kodlanmıştır. .

Bununla birlikte, Latin alfabesi, insanların kendilerini yazılı dilde ifade ettikleri birçok yolun yalnızca küçük bir alt kümesidir. Diğer komut dosyalarını desteklemek ve ASCII'yi kullanmak üzere yazılmış olan tüm yazılımların değişiklik yapmadan çalışmaya devam etmesine izin verirken (geriye dönük uyumluluk olarak bilinen bir kavram), 'UTF-8' olarak bilinen başka bir veri formatı tanıtıldı.

ASCII, kaynak kodun en yaygın biçimi olmaya devam etmektedir. Bu arşivin her makarası, ASCII karakterleri için bir rehber içerir. ASCII, UTF-8'in bir alt kümesidir, yani tüm ASCII kodlamaları da UTF-8 kodlamalarıdır. Kılavuz makara ayrıca tüm UTF-8 karakterlerinin bir özelliğini içerir. Bu arşivdeki neredeyse tüm metin dosyaları UTF-8 olarak kodlanmalıdır.

Metin olmayan dosyalar, resimleri ve biçimlendirilmiş belgeleri temsil etmesi amaçlanan dosyaları içerir. Yaygın olarak kullanılan bir kural, dosya adlarının '.' İle bitmesidir. Bu karakterin ardından dosya türünü gösteren bir son ek gelir: örneğin, .jpg ile biten bir dosya adı muhtemelen bir JPEG resim dosyasıdır; .PNG ile biten dosya büyük olasılıkla Taşınabilir Ağ Grafiği resim dosyasıdır; ve .pdf ile biten bir Taşınabilir Belge Biçimi dosyası.

Metin dosyalarını gösteren tek bir son ek yoktur. Daha ziyade, kaynak kodu için sonek kodun hangi programlama veya biçimlendirme dilinde yazıldığını belirtme olasılığı daha yüksektir. Programlama ve biçimlendirme dilleri aşağıda daha ayrıntılı olarak açıklanacaktır.

## Arşiv İçeriğini Çıkarma

Burada, arşivlenmiş belirli bir havuzun çeşitli kurucu dosyalara nasıl açılacağına dair bir genel bakış sunacağız. Yine, bu süreç şunlardan oluşur:

1. Depo verilerinin arşivlendiği belirli makara ve çerçeveleri tanımlama.

2. QR kodlarından, bu çerçevelerdeki siyah, beyaz ve gri piksel alanlarından bir ikili dosyaya (en az binlerce ve genellikle milyonlarca) 1 ve 0'lık bir dizi kod çözme.

3. İkili dosyayı daha uzun, sıkıştırılmamış bir arşiv dosyasına açmak.

4. Arşiv dosyasını, içerdiği ayrı alt dosyalara açmak. Bununla birlikte, arşiv verilerinin, bu adım atlansa bile karmaşık olmasına rağmen genel olarak anlaşılabilir olduğunu unutmayın.

5. Son olarak, bu alt dosyaların her birini - oldukça kısadan çok uzuna değişebilen 1'ler ve 0'ların dizileri - metin dosyaları iseler yazılı karakterlere dönüştürmek.

### Depo verilerinin arşivlendiği belirli makarayı ve çerçeveleri tanımlama

Her bir film makarası boş bir filmin lideriyle başlar ve daha sonra boş bir çerçevenin bir köşesinde düz siyah bir dikdörtgenden oluşan Sıfır Referans Çerçevesi. İnsan tarafından okunabilen bir sonraki çerçeve, makara hakkında bilgi içeren Kontrol Çerçevesidir. Aşağıda, Kullanıcı Veri Dosyalarının bir listesini içeren İçindekiler Tablosu yer almaktadır.

Bu makaradaki her depo, bu Kullanıcı Veri Dosyalarından biridir. Liste, benzersiz bir kimlik, bir dosya kimliği ve bu dosyaların her biri için bir ad içerir. Örneğin, Python hesabının CPython deposu, 12345 olarak listelenen dosya kimliğine ve python_cpython.tar olarak listelenen ada sahip olabilir.

Kullanıcı Veri Dosyaları listesinin ardından, Dijital Veri Konumlarının bir listesi bulunmaktadır. Bu liste dosya kimliğini, bir başlangıç çerçevesini, bir başlangıç baytını, bir bitiş çerçevesini ve bir bitiş baytını içerir. Dolayısıyla, varsayımsal CPython örneğini kullanarak, bu listedeki 12345 kimliğine sahip öğenin başlangıç çerçevesi 054321, başlangıç baytı 03210321, bitiş çerçevesi 054545 ve bitiş baytı 12321232 olabilir.

Bunun anlamı, CPython verilerini almak için: Bu film makarasının 54321 karesine gidin. Başlangıç çerçevesi 54321'den bitiş çerçevesi 54545'e kadar tüm karelerin kodunu, aşağıda açıklanan yöntemlerle ikili değerlere çevirin. Bu size 54321'den 54545'e kadar numaralandırılmış 225 adet veri verecektir, bu veri içermeyen bir dizi boş parça ile başlayacaktır. İlk boş olmayan veri parçasındaki ilk 3210320 baytı atın. Sırayla tüm "ortadaki" veri parçalarını ekleyin. Son olarak, son veri parçası olan 54545'ten ilk 12321232 baytı ekleyin. Artık tüm CPython havuzunu tek bir sıkıştırılmış arşiv dosyası olarak bir araya getirdiniz.

### QR kodlarından ikili dosyaya kod çözme

Film karelerinin kodunun ikili verilere nasıl çözüleceğine ilişkin ayrıntılar, arşivdeki her film makarasının başlangıcında bulunan İçindekiler Tablosunun ardından bulunan insan tarafından okunabilir Temsili Bilgilerde bulunur. Bu bilgiler her makarada bulunur, böylece tek bir makara arşivden ayrılmış olsa bile içeriğini deşifre etmek mümkün olacaktır. Bu Temsil Bilgileri sırayla şunları içerir:

1. GitHub Arşiv Programı Rehberi (bu belge)

2. GitHub tanımlayıcı indeksi, bu makaradaki tüm depoların bir listesi ve kısa açıklaması

3. Temsil Bilgileri açıklaması

4. Dijital Koruma ve Veri Nasıl Alınır, veri alma ayrıntılarına genel bakış

5. Depolama Aracı açıklaması

6. Veri Erişim Teknolojisi

7. Genel Koruma Makarası Yapısı (makara biçimi)

8. Genel 4K Çerçeve formatı açıklaması

9. Kutudan çıkarma kitaplığı açıklaması (QR kodları için)

10. Kitaplık kaynak kodunu kutudan çıkarma

11. ASCII veri formatı spesifikasyonu

12. C programlama dili belirtimi

13. TAR arşiv dosyası kaynak kodu

14. PDF kaynak kodu

15. XZ dosya formatı spesifikasyonu (sıkıştırma / açma için, aşağıda açıklanmıştır)

Bu öğelerin altıncı bölümü olan Veri Erişim Teknolojisi belgesi, dijital olarak kodlanmış tek bir film karesindeki verileri yakalamak ve onu bilgisayar analizine uygun bir forma dönüştürmek için bir tarayıcı kullanmak için gereksinimleri ve süreçleri açıklar. Bunlardan sekizincisi, Generic 4K Frame format açıklaması, bir bilgisayarın böyle taranmış bir görüntüyü alıp ikili veriye dönüştürmesi için gerekli olan kaynak kodu dahil teknik bilgileri sağlar.

Prensip olarak, bir depoyu QR kodlu verilerden ikili verilere bilgisayar kullanmadan dönüştürmek teorik olarak mümkündür. Bununla birlikte, çok zor olacak ve muhtemelen iyi organize olmuş bir topluluktan aylar veya yıllar olmasa da haftalarca büyük bir çaba gerektirecektir. Depoların içerikleri bir bilgisayarda çalıştırılmak üzere tasarlanmış yazılımlar olduğundan, bir bilgisayarın yokluğunda kullanımları en iyi ihtimalle minimum olacaktır.

Bu arşivin mirasçılarının bilgisayarları olmaması durumunda, sahip oldukları kadar arşivi bütün ve güvenli bir şekilde saklamaları gerekmektedir. İnsan tarafından okunabilir Teknoloji Ağacının bir amacı, bu olasılık durumunda teknolojilerin ve bilgisayarların gelişimini hızlandırmaya yardımcı olmaktır. (Diğer amacı, teknolojimizi ve gelişimini gelecekteki tarihçiler için kodlamaktır.)

### Arşiv dosyasını içerdiği ayrı alt dosyalara açmak

Her depo için ikili dosya, Teyp ARşivi'nin kısaltılmışı TAR olarak bilinen bir formattadır. Bir TAR dosyası, tek tek kağıt parçalarını tek bir kaydırmada birbirine bantlamak gibi, bir dizi dosyanın bir ucunu diğerinin başına bağlayarak bir araya getirilmesiyle oluşturulur. Bir TAR dosyası, herhangi bir sayıda dizine ve alt dizine bölünmüş, herhangi bir boyutta herhangi bir sayıda dosya içerebilir.

Bir TAR dosyasındaki her alt dosyanın önünde, kaydırma metaforundaki bant gibi davranan 512 baytlık bir başlık kaydı bulunur. Bu üstbilgi kaydı dosya hakkında adı ve boyutu gibi bilgileri içerir. Arşivin sonu en az iki ardışık 512 baytlık blokla belirtilir.

TAR dosyaları aslında aralarında metin kayıtları bulunan dosyaların koleksiyonları olduğundan, bir TAR dosyası tüm metin dosyalarını içeriyorsa, kendisi bir metin dosyası olarak değerlendirilebilir. Bir karışım içeriyorsa, yapılandırılmış, anlamlı metin (kurucu metin dosyaları) ve anlaşılmaz anlamsız sözler (metin olmayan kurucu dosyalar) karışımını içeren bir metin dosyası olarak kabul edilebilir.

TAR dosyalarını, bir kapsayıcı diğerinin içinde olacak şekilde TAR dosyalarının içine yerleştirmek mümkündür ve arşivlenmiş verilerimizin çoğu bu şekilde depolanır. Verilen herhangi bir depo için, dış TAR dosyası en azından şunları içerecektir:

* depo adı, hesap adı, açıklama, dil, yıldız sayısı ve çatal sayısını içeren META adlı sıkıştırılmamış tek bir meta veri dosyası
* zaman içinde depoda yapılan değişikliklerin günlüğünü içeren COMMITS adlı sıkıştırılmış (aşağıya bakın) bir dosya
* repo.tar.xz adlı bir dosya, gerçek depo içeriğini içeren sıkıştırılmış bir TAR dosyası

Wiki'ler, gh-pages sayfaları, sorunlar ve çeki istemleri gibi diğer meta veriler de ayrı sıkıştırılmış dosyalar olarak eklenebilir.

TAR dosyalarının belirli ayrıntıları ve bunları kodlamak ve çözmek için kullanılan yazılım, arşivin her makarasındaki Temsil Bilgilerinde bulunabilir.

### Sıkıştırılmış dosyaları okunabilir, sıkıştırılmamış dosyalar halinde açma

Mümkün olduğu kadar çok depoyu ve mümkün olduğunca çok veriyi dahil etmek için, verilerin çoğu sıkıştırılmıştır. Sıkıştırma, daha büyük bir miktarı temsil etmek için küçük miktarda veriyi, bu büyük miktarda kalıplar ve tekrarlar kullanarak kullanmak anlamına gelir. Örneğin, karakteri arka arkaya dokuz kez yazmak yerine, okuyucu 9a'nın sıkıştırılmamış metin aaaaaaaaa olduğunu anlayacağından emin olsaydı, sıkıştırılmış metni 9a yazabilirdi.

Etkili sıkıştırma algoritmaları bundan çok daha karmaşıktır, ancak aynı ilke geçerlidir. Bu arşiv, "XZ" olarak bilinen ve daha sonra "LZMA" olarak bilinen bir algoritma kullanan bir sıkıştırma programı kullanır. Her makaradaki ikinci veri dosyası, aşağıda açıklanan tek bir sıkıştırılmamış TAR arşiv dosyasında XZ için kaynak kodunu ve dokümantasyonu içerir. (İlk veri dosyası, mevcut her yazılı insan dilinde İnsan Hakları Evrensel Beyannamesi'ni içerir.)

LZMA, 'LZ77' algoritması ve "aralık kodlaması" olarak bilinenleri birleştirir. LZ77, tekrarlanan verileri, bu verilerin önceki görünümlerine referanslarla değiştirir. Örneğin, büyük ölçüde basitleştirmek için, 80 baytlık bir cümle ikinci kez 400 bayt arayla iki kez görünürse, algoritma esasen verileri "400 bayt öncesinden 80 baytı tekrarla" diyerek sıkıştırır. Menzil kodlama, esas olarak tüm bir mesajı çok uzun tek bir sayıya dönüştürür ve bu da kodlanabilir.

Verileri açmak için kullanılacak algoritmanın belirli adımları, her makaradaki ikinci veri dosyasında bulunan XZ kaynak koduyla açıklanır. El ile açmak teorik olarak mümkün olsa da, bu olağanüstü derecede zaman ve emek-yoğun bir süreç olacaktır. Uygulamada, çalışan bir bilgisayar istenir.

### Her bir dosyayı tek tek yazılı karakterlere dönüştürme

İnsanlık, binlerce yıldır birçok yazılı karakter kullandı. Bu arşivde bu karakterleri 1'ler ve 0'lar olarak temsil etmek için kullanılan kodlama 'UTF-8' olarak bilinir. Tek bir UTF-8 karakteri, yani tek bir yazılı sembol, 1 ila 4 baytlık ikili veriyi işgal edebilir.

Tarihsel nedenlerden dolayı, yazılım geliştirmenin başladığı zaman ve bölgede en yaygın olarak kullanıldıkları için, 'ASCII' olarak bilinen bir grup karakter (ve kavram) karakter başına 1 bayt ile en verimli şekilde kodlanır. ASCII olmayan herhangi bir şey, karakter başına 2 veya daha fazla bayt olarak kodlanır. Bu arşivdeki metin dosyalarının çoğu ASCII'dir, ancak önemli bir kısmı değildir. Daha pek çoğu, ara sıra ASCII olmayan karakterler içeren çoğunlukla ASCII olacaktır.

ASCII'nin ayrıntılı özellikleri, arşivin her makarasındaki Temsil Bilgilerinde bulunabilir. UTF-8'in ayrıntılı özellikleri kılavuz makarada bulunabilir. Arşivin her makarasındaki ilk veri dosyası, mevcut her yazılı insan dilinde İnsan Hakları Evrensel Beyannamesi metnini içerecektir. Bu, hem bir çeviri aracı hem de ASCII ve UTF-8'in bir örneği olarak hizmet edecektir.

## Dosya Türleri

Farklı nedenlerle oluşturulmuş birçok farklı türde metin dosyası vardır. Buradaki birincil tür, bu arşivin var olma nedeni kaynak koddur. Kaynak kodu, '{' ve ';' gibi sembollerin bulunduğu çok yoğun, son derece yapılandırılmış bir metindir. çok önemlidir.

Kaynak kodla ilgili en önemli şey, derleyiciler tarafından okunmak üzere yazılmasıdır. Derleyiciler yazılım olduklarından, bunu ifade etmenin başka bir yolu da kaynak kodun bilgisayarlar tarafından okunmak üzere yazılmasıdır. Yazılım alanında yetenekli ve eğitimli olan diğer insanların anlayabilmesi için iyi kod da yazılır; ancak bu yalnızca bir derleyici anlayabilirse doğrudur.

Bu derleyici, sırayla, Teknoloji Ağacında açıklanan karmaşık diziler yoluyla, kaynak kodunu, bilgisayarın kod tarafından açıklanan işlevleri ve etkinlikleri gerçekleştirmesine neden olacak birler ve sıfırlar dizisine dönüştürecektir. Çok basit bir örnek vermek gerekirse, kod satırı

    _for (int i = 0; i <5; i ++) {} _

derleyici tarafından bilgisayara beslenen bir dizi ikili talimata dönüştürülür, bu da bilgisayarın kayıt adı verilen küçük bir kısmının değerini 0'a ayarlamasına ve ardından bu değeri 1, 2, 3'e yükseltmesine neden olur. ve sonra 4. (Bu, yararlı bir kod örneği olarak tasarlanmamıştır; yalnızca kaynak kodunu çalışan yazılıma dönüştürmenin çok katmanlı sürecinin bir örneğidir.)

JSON, XML ve HTML gibi diğer metin dosyaları türleri, bilgisayarlar için verileri (komutların aksine) depolamak için kullanılır. Yapılandırılmış formatları, bu dosya gibi daha az yapılandırılmış hikaye anlatımı metinlerine göre okumayı zorlaştırsa da, genellikle insanlar tarafından da okunabilir.

Diğer türdeki metin dosyalarının çoğu, sonunda insanlar tarafından okunmak üzere tasarlanmıştır. Şu anda okumakta olduğunuz bu dosya gibi bazıları basit, çoğunlukla yapılandırılmamış metindir. Arşivde yaygın olarak karşılaşacağınız bir tür Markdown, bir dosyaya .md uzantısı ile ifade edilen, bir tür ara form olan ve insanlar tarafından ham haliyle okunabilir ve aynı zamanda öyle yapılandırılmış bilgisayarlar bunları görsel olarak daha çekici ve kullanışlı düzenler halinde biçimlendirebilir. Bu arşivdeki çoğu depoda bir README.md Markdown dosyası bulunur ve bu dosya genellikle depoya ilk giriş olarak tasarlanmıştır, ne olduğunu, neden var olduğunu ve nasıl kullanılacağını açıklar.

Metin olmayan dosyaların en yaygın biçimlerine kısa bir genel bakış da yararlı olabilir. Derlenen kod metin değildir. JPG ve PNG dosyaları, görüntüleri dijital formatta, MP3 ve WAV ise sesi kodlar. PDF dosyaları belgeleri hassas, mükemmel biçimlendirmeyle kodlar. ZIP ve TAR dosyaları, daha önce belirtildiği gibi, sırayla bir veya daha fazla dosya içerebilen konteyner dosyalarıdır.

## İnsan Dilleri ve Programlama Dilleri

### İnsan Dilleri

Bugün insanlığın kullandığı binlerce yazılı dil ve daha da fazla konuşulan dil var. Bunların çoğu yalnızca nispeten küçük nüfus tarafından kullanılmaktadır, ancak en az 60 milyon kişi tarafından birinci veya ikinci dil olarak kullanılan en az yirmi dil vardır.

Dünyada en çok kullanılan diller İngilizce ve Çincedir. Tarihsel nedenlerden dolayı, uzun yıllar boyunca çoğu yazılım geliştirme İngilizce konuşan ülkelerde gerçekleşti, bu nedenle bir süre için İngilizce, yazılımın varsayılan dili haline geldi. Çoğu programlama dili sözdizimlerinde İngilizce kelimeleri kullanır. Bu arşiv kılavuzunun ilk yazıldığı dildir.

Bu arşivin mirasçılarının İngilizce bileceği garanti edilemese de, özellikle sonsuza dek sürecek bir dil gibi görünmektedir. Diğer dillere yönelik bazı rehberliklerin yararlı olması durumunda, İnsan Hakları Evrensel Beyannamesi'nin 500'den fazla mevcut çevirisini sıkıştırılmamış UTF-8 dosyası olarak her makaranın başına ve ayrıca Teknoloji Ağacına dahil ediyoruz. Bu deklarasyon, çağımızdaki her bir insanın hak ve özgürlüklerinin bir listesidir ve asla elinden alınmamalıdır.

### Programlama dilleri

Programlama dilleri, insanlar tarafından talimatları bilgisayarlara iletmek için kullanılan dillerdir. Yazılımın ifade edildiği dillerdir. Diğer (eğitimli) insanlar da programlama dillerinde yazılmış yazılımı okuyabilmelidir, ancak bu ikincil bir hedeftir.

Bir programlama dili, bir bilgisayara belirtilen eylemi belirtilen şekilde gerçekleştirmesi talimatını vermek için yapılandırılmış bir şekilde düzenlenebilen, çoğu kelimeler olan önceden tanımlanmış öğeler kümesidir. Bu tür talimatlardan oluşan bir koleksiyon, bir program veya kaynak kodu olarak bilinir. Kaynak kodu, esasen dondurulmuş, yazılı bir biçimde bir yazılımdır.

Programlar genellikle ifadeler olarak bilinen ayrı adımlara bölünür ve bunlar da işlevler olarak bilinen koleksiyonlar halinde birlikte gruplanır. Bir programın tamamı tek bir dosyada bulunabilir veya binlerce kişiye yayılmış olabilir.

Birçok farklı form, yaklaşım ve felsefeye yayılmış yüzlerce farklı programlama dili vardır. Bazıları daha sonra çalıştırılan ayrı ikili dosyalar halinde derlenir; "yorumlanmış" diller olarak bilinen bazıları, etkili bir şekilde derlenir ve ara aşama olmaksızın tek seferde çalıştırılır. Çoğu modern programlama dili, önceden yazılmış işlevlerin kitaplıklarını içerir ve bu tür kitaplıklar çok hacimli ve ayrıntılı olabilir. Günümüzün en popüler programlama dillerinden bazıları şunlardır:

* C, en eski ve en hızlı, en evrensel ve en güçlü dillerden biri, bazı yönlerden basit, bazılarında oldukça sınırlı ve her zaman sezgisel değil, okunması kolay veya öğrenmesi kolay.

* C++, C'nin daha karmaşık, soyut ve güçlü bir türevi.

* C#, ikili makine koduna değil, yorumlanmış bir "çalışma zamanına" derlenen başka bir türevi.

* C# 'a benzeyen (ancak daha önceleri ortaya çıkan) Java, belki de günümüzün en yaygın kullanılan dilidir.

* Addaki benzerliğine rağmen Java'dan oldukça farklı olan ve 'ECMAScript' olarak da bilinen JavaScript, başlangıçta tamamen bir web tarayıcısı içinde kullanılan bir dildir, yani İnternet olarak bilinen uzak bir bilgisayardan veri alan, yorumlayan ve görüntüleyen bir program sunucu; bugün ise bu sunucularda da yaygın olarak kullanılmaktadır.

* Daha katı kurallara sahip bir JavaScript biçimi olan TypeScript, böylelikle hatalar olarak da bilinen hataların programlara girme olasılığını azaltır.

* Python, bilim adamları arasında popüler olan, hem güçlü hem de iyi bir ilk dil olan zarif bir dildir.

* Ruby, ifadeleri neredeyse yazılı İngilizce gibi okunan sezgisel bir dil.

* Go, özellikle paralelleştirilmiş programlarda, yani birden çok işlevin aynı anda bağımsız olarak çalışacağı şekilde yazılan programlarda üstün olan basit, güçlü bir dildir.

* Swift, bir milyar insan tarafından kullanılan telefonlar ve diğer cihazlar için yazmak için kullanılan yeni bir dil.

* Rust, C'nin yerini alması amaçlanmıştır ve tehlikeli böcekleri çok daha az olası kılar.

* PHP, İnternet sunucuları için kullanılan basit bir dildir.

* Lisp, programlamaya temelde farklı, fonksiyon öncelikli yaklaşımı olan çok eski bir dildir.

* SQL, veritabanları olarak bilinen yapılandırılmış ve yüksek verimli veri depolarından veri almak için kullanılan çok farklı bir dil türüdür.

* Assembler (veya assembly), çok karışık, sınırlı, ancak hızlı ve güçlü bir dil ailesi olup, burada dil yapıları ile söz konusu bilgisayarın makine kodu arasında doğrudan bir ilişki vardır; yarı derlenmiş kod olarak kabul edilebilir.

## Geliştirme, Bağımlılıklar ve Açık Kaynak

### Geliştirme

Tek, basit bir kaynak kodu dosyasını alıp bir bilgisayardaki elektriksel vuruşlara dönüştürme süreci son derece karmaşıktır. Soyutlama katmanlarını kullanarak bu karmaşıklığı ele alıyoruz. Komut kümesi olarak bilinen bir soyutlama, tek bir derleyiciden gelen makine kodu çıktısının birçok farklı türde bilgisayarda kullanılmasına izin verir. Bir kaynak kodu yazarının, genellikle o kodu çalıştırmak için ne tür bir bilgisayarın, hatta hangi komut setinin kullanılacağını bilmesi veya umursaması gerekmez; bu derleyici tarafından soyutlanmıştır.

Modern yazılım, sırayla, tek bir bilgisayar için tek bir program üzerinde çalışan tek bir yazardan çok daha karmaşıktır. Tek bir proje içinde birçok dosya üzerinde aynı anda ve genellikle birden çok programlama dili kullanarak çalışan birçok yazardan oluşur. Dahası, her proje, araçlar ve / veya bileşenler olarak diğer, ayrı, kendi kendine yeten projelere bağlıdır ve bu projeler aktif olarak üzerinde çalışılır ve yine diğer projelere bağımlıdır. Tüm bu hareketli parçaların birlikte zarif ve verimli bir şekilde çalışmasını sağlamak, modern yazılım geliştirmenin zorluğudur.

Yazılım geliştiricileri olarak da bilinen birden çok kaynak kodu yazarı tek bir proje üzerinde çalışırken, her birinin kendi bilgisayarı ve tüm projenin bilgisayarında bir kopyası olur. Her biri değişiklik yaparsa, her biri aynı projenin farklı bir sürümüne sahip olur. Bir projenin birden çok sürümünü uzlaştırma süreci, sürüm kontrolü olarak bilinir. Sürüm kontrol yazılımı tarafından yönetilir; Bu arşivde, GitHub'ın adını aldığı Git adlı yazılım tarafından. Bu arşivdeki her depo bir Git deposudur.

Git, yazılımın farklı sürümlerini minimum insan müdahalesi gerektiren tek bir tutarlı formda otomatik olarak birleştirebilir. Git ayrıca, gerektiğinde ve gerektiğinde önceki bir sürüme geri dönmenizi sağlayan eksiksiz bir geçmiş tutar. Ancak, yer kazanmak için bu arşivin depoları genellikle Git geçmişlerini içermez.

Birden çok geliştirici, bir projeyi aynı anda birden çok farklı yoldan aldığında, bu, bir projeyi dallara ayırmak olarak bilinir ve bu yollar dallar olarak bilinir. Bir projenin üzerinde mutabık kalınan ana dal ana dal veya ana dal olarak bilinir. Git, tesis geliştiricilerin iki dal arasındaki farkları özetlemek ve onlarınkini diğerlerininkiyle birleştirmeyi önermek için kullanabilecekleri bir tesis sağlar. Bu, çekme isteği olarak bilinir. Modern yazılım geliştirme, büyük ölçüde bir projeyi dallara ayırmaktan, yazılımı şubenizde yazmaktan veya düzenlemekten ve bittiğinde çalışmanızın ana şubeye yeniden dahil edilmesi için bir çekme talebi göndermekten oluşur.

### Bağımlılıklar

Esasen her programlama dili, başkalarının çalışmaları üzerine inşa etmeyi destekler. Başkalarının çalışmalarını yeniden kullanmadan, her proje çok daha zor ve çok daha yavaş olacak ve kaybolan çok az proje gerçek dünyada gerçek kullanım görebilecektir.

A projesinin, A'nın işini yapabilmesi için B projesini içermesi gerekiyorsa, A projesine B'ye bağımlı olarak bilinir ve B, A projesinin bağımlılığı olarak bilinir. A, her biri birçok bağımlılığa sahip olabilen birçok bağımlılığa sahip olabilir. kendi bağımlılıkları vb. Ayrıca, her bağımlılık, belirli bir projenin belirli bir sürümü veya sürüm aralığı içindir. Bir projenin tüm çoklu bağımlılık katmanlarının tam maddeleştirilmesi, bağımlılık ağacı olarak bilinir.

Genel olarak, bağımlılıklar kaynak kodu dosyalarının içinde, genellikle en üstte maddeler halinde sıralanır ve derleyici veya yorumlayıcı bir bağımlılık bulduğunda, onu önceden tanımlanmış bir dizi dizinde arar. Bir projenin bağımlılık ağacı çok karmaşık olabileceğinden, bazen paket listesi olarak bilinen bir proje içindeki tek bir dosyada bütünüyle maddeler halinde sıralanır. Örneğin, Ruby projelerinde bu amaç için bir Gemfile olabilir ve JavaScript projelerinde bir package.json dosyası olabilir. Bu, paket yönetimi yazılımı olarak bilinen bir tür aracın bir proje için tüm bağımlılıkları bir veya daha fazla İnternet sunucusundan aynı anda almasına izin verir.

Bu arşiv durumunda, herhangi bir proje için bağımlılıkların arşivin başka bir yerinde bulunması muhtemeldir. Arşivde bir bağımlılık bulmak için öncelikle kaynak kodda veya paket listesinde, tam ayrıntıları dile ve çerçeveye göre değişen bağımlılığın adını keşfetmeli ve ardından kılavuz makaradaki ana indeksi kullanmalı, veya yokluğunda, söz konusu havuzun hangi makara ve çerçevelerde bulunabileceğini belirlemek için her bir makaranın önündeki indeksler.

### Açık kaynak

Bir programı bilgisayarda çalıştırmak sadece derlenmiş makine kodunu gerektirdiğinden, kaynak kodu gizli tutulurken bunu dağıtmak mümkündür. Bu, kapalı kaynak modeli olarak bilinir. Bilgi işlemin ilk günlerinde, kaynak kodu genellikle makine koduyla birlikte dağıtıldı, ancak daha sonra yazılım karlı bir endüstri haline geldikçe, kapalı kaynak modeli daha yaygın hale geldi.

O zamandan beri, kaynak kodunu herkese açık hale getirmenin, herkesin kopyalayabileceği, dallandırabileceği ve geliştirebileceği, yazılım geliştirmeye çok daha etkili bir yaklaşım olduğu öğrenildi. Bir projenin kaynak kodunu okuyabilen daha fazla kişi, olası ihtiyaçları ve faydalı yeni özellikleri belirleyecek daha fazla insan, projeye katkıda bulunacak kadar daha fazla insan, hataları tespit edip düzeltmeler gönderebilecek daha fazla kişi ve test edip doğrulayacak daha fazla kişi anlamına gelir. bu yeni kod çalışıyor.

Genel olarak, kapalı kaynak, yeni ve daha iyi fikirler bulmak ve benimsemek için mücadele eden daha küçük, dar görüşlü, parçalanmış topluluklara yol açar. Açık kaynak, birbirlerinin projelerinin büyümesine, gelişmesine ve başarılı olmasına yardımcı olan, birbirlerinin çalışmalarını bağımlılık olarak kullanan ve / veya kodlarını yeniden kullanan ve birbirlerinden öğrenen büyük, birbirine bağlı topluluklara yol açar. Açık kaynaklı yazılım, tüm insanlığın toplu kullanımı için bir araç setidir ve ne kadar çok ve daha iyi araçlara sahip olursak, bir tür olarak o kadar hızlı ve daha iyi ilerleyebiliriz.
