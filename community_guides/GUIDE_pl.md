# Przewodnik po GitHub Code Vault

## Wstęp

To archiwum, GitHub Code Vault, zostało założone przez GitHub Archive Program, którego misją jest zachowanie oprogramowania open source dla przyszłych pokoleń. Możesz czytać to za rok lub za tysiąc lat, ale tak czy inaczej mamy nadzieję, że uznasz jego treść, a może i samą koncepcję open source za przydatną.

To jest przede wszystkim archiwum oprogramowania. Oprogramowanie to seria poleceń używanych do kontrolowania działań komputera. Komputer jest urządzeniem, które może automatycznie wykonywać funkcje matematyczne tak szybko, że ma moc znacznie przewyższającą nasz umysł. Nasze komputery są używane do pomocy w odkrywaniu tajemnic wszechświata, do łączenia całej ludzkości we wszechobecną sieć informacji, do manipulowania sygnałami wystarczająco szybkimi, by transmitować dźwięki i wyświetlać na ekranach elektrycznych szczegółowe ruchome obrazy, oraz do sterowania niezwykle potężnymi maszynami, które znacznie przekraczają zarówno możliwości, jak i precyzję ludzkiej pracy.

Komputer bez oprogramowania nie może zrobić żadnej z tych rzeczy. Komputer jest niezwykłą i cudowną rzeczą, ale bez oprogramowania cała jego moc jest bezużyteczna. Celem tego archiwum jest przekazanie Wam tego, co wiemy o oprogramowaniu.

Oprogramowanie jest pisane jako złożone, ale czytelne dla człowieka sekwencje poleceń, których różne odmiany są znane jako języki programowania, ponieważ kompletna jednostka oprogramowania jest często nazywana programem. Programy te są następnie konwertowane na binarny język jedynek i zer używany przez komputery. Proces ten znany jest jako kompilacja.

Ponieważ skompilowane oprogramowanie jest bardzo trudne do rozszyfrowania z powrotem do swojej oryginalnej formy programowej, znanej również jako kod źródłowy, możliwe jest dla ludzi utrzymanie tej oryginalnej formy w tajemnicy i roszczenie sobie prawa własności do niej. Oprogramowanie z otwartym źródłem nie jest innym rodzajem oprogramowania, ale innym etosem. Etos otwartego oprogramowania odrzuca tajemnicę i własność. Programy z otwartym źródłem są udostępniane wszystkim, którzy chcą ich używać, bez żadnych kosztów, tak by mogli je ulepszać lub używać do budowania czegoś nowego i lepszego.

Projekt open source jest zbiorową pracą samoorganizującej się społeczności, która może liczyć tysiące osób. Nagromadzenie wszystkich zarchiwizowanych tu projektów oprogramowania open source jest dziełem wielomilionowej społeczności. Podczas gdy pewne osoby mogą mieć specjalne prawa w ramach danego projektu, takie jak możliwość zatwierdzania lub odrzucania sugerowanych zmian w najnowszej oficjalnej wersji jego kodu źródłowego, nikt nigdy nie jest jego właścicielem. Każda osoba ma prawo wziąć i używać kompletną kopię dowolnego projektu open source w dowolnym momencie, bez żadnych kosztów czy kar. Jest to znane jako forking projektu.

Kiedy wiele osób pracuje nad kodem źródłowym w tym samym czasie, trudno jest śledzić i łączyć wszystkie ich zmiany. Projekt open source znany jako 'Git' jest poświęcony rozwiązaniu tego problemu. Umożliwia on gromadzenie kompletnej historii wszystkich zmian w projekcie w postaci tak zwanego repozytorium Git. To archiwum jest w zasadzie zbiorem takich repozytoriów.

Archiwum to zostało stworzone przez firmę o nazwie „GitHub”, która oferuje usługę pozwalającą ludziom na całym świecie przechowywać napisane przez siebie programy, śledzić zmiany w tych programach i współpracować z innymi w celu ich ulepszania i rozszerzania. GitHub udostępnia swoje usługi za darmo twórcom publicznego oprogramowania open source. Ma dziesiątki milionów takich użytkowników.

Poniżej znajduje się opis tego, co naszym zdaniem należy wiedzieć i posiadać, aby jak najlepiej wykorzystać to archiwum oprogramowania. Jeśli nie wiesz lub nie rozumiesz niektórych z tych rzeczy, nie załamuj się! Zamieściliśmy również wskazówki, jak spełnić te wymagania. Jeśli z jakiegoś powodu nie będziecie mogli sami ich spełnić, to wasi potomkowie będą mogli.

## Co jest potrzebne do korzystania z archiwum

W zasadzie wszystko, czego potrzebujesz, aby uzyskać dostęp do zawartości tego archiwum, to źródło światła i jakieś szkło powiększające. Jednakże większość danych (choć nie wszystkie) została bardzo ciasno upakowana na szpulach filmowych w zakodowanej i skompresowanej formie. Odczytanie, zdekodowanie i zdekompresowanie tych danych będzie wymagało znacznych nakładów obliczeniowych. Teoretycznie można by to zrobić bez użycia komputerów, ale byłoby to bardzo żmudne i skomplikowane.

Spodziewamy się, że nie będziesz potrzebował naszych definicji oprogramowania, komputera i innych terminów. Przypuszczamy, że macie swoje własne komputery, prawdopodobnie znacznie bardziej zaawansowane od naszych i być może całkowicie inaczej skonstruowane. Gdy zrozumiesz poniższy przegląd i przewodnik, będziesz w stanie bez problemu uzyskać dostęp do wszystkich danych.

Niemniej jednak, możliwe jest, że posiadacie komputery gorsze od naszych, lub nawet nie posiadacie ich wcale. Na wypadek takiej ewentualności, przygotowaliśmy nieskompresowany, niekodowany, zrozumiały dla człowieka zwój danych, który nazywamy Drzewem Technologicznym. Drzewo Technologii zawiera informacje o naszych podstawowych technologiach, naszych komputerach i naszym oprogramowaniu, w nadziei, że z czasem będziecie w stanie wykorzystać tę wiedzę do odtworzenia komputerów, które mogą korzystać z oprogramowania open source znajdującego się w tym archiwum.

## Co jest w środku

Archiwum jest tak duże - około 21 bilionów bajtów (wyjaśnione poniżej) - ponieważ jest niezwykle inkluzywne i demokratyczne. Wiele milionów ludzi udostępnia wszystkim napisane przez siebie oprogramowanie. To archiwum zawiera snapshot - to znaczy pojedynczą kopię, w jednym momencie w czasie - całego publicznego oprogramowania, które użytkownicy GitHuba aktywnie rozwijają. Oznacza to, że zawiera ono miliony oddzielnych repozytoriów. Mamy nadzieję, że to szerokie, demokratyczne podejście będzie interesujące dla przyszłych historyków.

Repozytoria zawarte w tym archiwum zostały określone wyłącznie na podstawie czasu ich ostatniego commitu, czyli ostatniej aktualizacji, oraz na podstawie ich liczby gwiazdek. (Wszyscy użytkownicy GitHuba mają możliwość „gwiazdkowania” publicznych repozytoriów, aby zaznaczyć, że są one dla nich interesujące lub ważne). Ten snapshot został zainicjowany 02.02.2020, czyli drugiego dnia lutego, w roku 2020 kalendarza gregoriańskiego, tak jak my liczymy czas. Repozytoria, które są w nim uwzględnione to: wszystkie repozytoria z jakimikolwiek commitami w ciągu ostatnich 80 dni; wszystkie repozytoria z przynajmniej jedną gwiazdką z jakimikolwiek commitami w ciągu ostatnich 365 dni; oraz wszystkie repozytoria z przynajmniej 250 gwiazdkami, niezależnie od tego kiedy były ostatnio aktualizowane.

Oczywiście, nie wszystkie z tych repozytoriów są równie ważne pod względem wpływu i zależności. Drzewo Technologiczne zawiera indeks i krótki opis najważniejszych repozytoriów w archiwum, a także listę, na której szpuli można znaleźć każde z nich, dzięki czemu można uzyskać do nich dostęp bez konieczności przedzierania się przez te wszystkie miliony repozytoriów, aby określić, które z nich są najbardziej przydatne.

## Przegląd archiwum

Archiwum składa się ze 188 szpul filmu: jednej „szpuli przewodnika”, zawierającej informacje i wskazówki czytelne dla człowieka, którą nazywamy Drzewem Technicznym, oraz 187 szpul zarchiwizowanego oprogramowania. Każda szpula zawiera 65 000 pojedynczych klatek. Klatki na początku każdej szpuli oraz klatki „szpuli przewodnika” zawierają czytelny dla człowieka tekst i obrazy. Wszystkie pozostałe klatki filmu składają się z danych cyfrowych przechowywanych w formie wizualnej znanej jako kody QR.

Dane cyfrowe oznaczają dane ostatecznie przechowywane w formacie binarnym, tj. jako 0 i 1, ponieważ komputery same są binarne - sterowane przez sygnały elektryczne, które są albo „włączone” albo „wyłączone”, co odpowiada 1 lub 0 - i dlatego dane binarne są znacznie łatwiejsze do zrozumienia przez komputery niż jakiekolwiek inne.

Metadane czytelne dla człowieka, zapisane na początku każdej szpuli, zawierają informacje o samym filmie, przewodnik po zastosowanym kodowaniu QR, program do jego dekodowania oraz indeks. Indeks zawiera tytuł, numer początkowy klatki i sumę kontrolną każdego pliku zapisanego na danej szpuli.

Plik jest pojedynczą spójną jednostką danych. Suma kontrolna jest unikalną wartością uzyskaną z obliczeń, znana jako funkcja haszująca, która jest wykonywana na całej zawartości pliku w celu zapewnienia, że jego zawartość nie została uszkodzona lub zniszczona; funkcja haszująca używana w archiwum jest znana jako „SHA-1”.

Każdy kod QR składa się z pola maleńkich białych lub czarnych kwadracików, które zajmują prawie całą klatkę filmu. Używamy kodów QR, ponieważ są one znacznie bardziej kompaktowe i wytrzymałe niż tekst odczytywany przez człowieka. Kod QR dekoduje się na dane binarne, tj. serię jedynek i zer.

Dekodowanie jest tylko pierwszym krokiem w przekształcaniu danych binarnych w znaczące informacje. Są to dane skompresowane, co oznacza, że zostały one zagęszczone w celu zaoszczędzenia miejsca, podobnie jak w przypadku zapisu „128xA”, zamiast 128-krotnego zapisu litery A. Po zdekodowaniu, dane muszą zostać zdekompresowane.

Wynik po dekompresji jest znany jako plik archiwum: pojedynczy plik zawierający całą zawartość repozytorium jednego projektu oprogramowania. Większość repozytoriów zawiera wiele plików, więc taki plik archiwum jest jak książka, która zawiera wiele oddzielnych rozdziałów, albo pudełko, które zawiera wiele innych pudełek. Zazwyczaj korzystne jest, choć nie jest to absolutnie konieczne, rozpakowanie pliku archiwum na jego pliki składowe przed uzyskaniem do nich dostępu.

Wreszcie, każdy plik składowy jest własnym zestawem danych binarnych, czyli jedynek i zer. Dane można zrozumieć, jeśli zna się ich format. Na przykład, w formacie znanym jako „UTF-8”, najczęściej spotykanym w archiwach, jedynki i zera są podzielone na grupy po osiem, zwane bajtami, bajt 01000001 reprezentuje literę A; trzy bajty 01101001 01101110 01110100 reprezentują słowo int; a dwa bajty 11000011 10000011 reprezentują literę Ã (A z akcentem tyldy na górze).

Ten proces archiwizacji danych, pliki binarne pakowane do plików archiwalnych, które zostały najpierw skompresowane, a następnie zakodowane w QR, jest oczywiście skomplikowany w porównaniu z prostym zapisem tekstu czytelnego dla człowieka. Proces odarchiwizowania danych, przez który trzeba będzie przejść – od QR do skompresowanych plików binarnych; skompresowane do nieskompresowanych; plik archiwalny do wielu plików; pliki tekstowe do tekstu czytelnego dla człowieka - jest podobnie złożony. Dzieje się tak dlatego, że ta złożoność pozwala nam przechowywać znacznie więcej danych, niż byłoby to możliwe w innym przypadku, w sposób stosunkowo łatwy do odczytania przez komputer.

Jeśli ta złożoność jest dla Was trudna i kosztowna, przepraszamy, ale przypuszczamy, że w takim przypadku niniejszy przewodnik i czytelne dla człowieka drzewo technologiczne złagodzą tę złożoność i być może będą dla Was bardziej użyteczne niż zawartość archiwum, przynajmniej do czasu, gdy wasze komputery będą na tyle zaawansowane, że łatwo będzie poradzić sobie ze złożonością danych zawartych w archiwum.
