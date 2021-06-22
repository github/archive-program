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

## Pliki, katalogi, repozytoria i formaty danych

Przydatne może być omówienie, w jaki sposób archiwum jest logicznie podzielone. W szczególności pomocna może być dyskusja na temat plików, katalogów i formatów danych.

Plik jest zbiorem danych zgrupowanych w spójną całość o jednej nazwie: pomyśl o danych jak o piasku, a o pliku jak o pewnego rodzaju worku, który może pomieścić piasek i tylko piasek. Katalog jest zbiorem plików: pomyśl o nim jako o rodzaju worka, który może pomieścić tylko inne worki. Podążając za tą metaforą, każde repozytorium składa się z katalogu zewnętrznego, zwanego katalogiem głównym, który zawiera pewną liczbę plików i/lub pewną liczbę katalogów. Każdy katalog może z kolei zawierać zarówno pliki, jak i same katalogi.

Struktura ta jest korzystna, ponieważ pliki zorganizowane w grupy są znacznie łatwiejsze do pracy niż pojedynczy zbiór plików. Identyfikator konkretnego pliku w katalogu zewnętrznym składa się z nazw wszystkich katalogów składowych, poczynając od głównego, po czym następuje jego indywidualna nazwa, ze znakiem / pomiędzy każdą nazwą. Na przykład, plik o nazwie README.md w katalogu głównym będzie identyfikowany jako /README.md, a plik identyfikowany jako /public/www/index.html będzie plikiem index.html w katalogu 'www' wewnątrz katalogu 'public' wewnątrz katalogu głównego.

Każde repozytorium z kolei ma dwie nazwy, oddzielone separatorem, którym w archiwum jest _ lub podkreślnik. (Historycznie był to znak / lub ukośnik, ale jest on również używany do wskazywania katalogu, więc używamy _ dla jasności). Pierwsza nazwa to konto na GitHubie, które jest właścicielem tego repozytorium; druga to nazwa indywidualnego repozytorium. Kombinacja identyfikatorów repozytorium i pliku może być użyta do jednoznacznej identyfikacji pojedynczego pliku w archiwum. Na przykład plik 'package.json' w katalogu 'web' w repozytorium 'ykarma' w ramach konta GitHub 'rezendi' może być jednoznacznie zidentyfikowany jako /web/package.json w rezendi_ykarma w archiwum.

Różne rodzaje plików mają różne przeznaczenie. Archiwum GitHuba składa się w dużej mierze z plików tekstowych, czyli plików, których dane mają reprezentować język pisany. Większość oprogramowania jest pisana w plikach tekstowych zawierających wysoce ustrukturyzowany tekst zwany kodem źródłowym. Specjalny program znany jako kompilator przekształca ten czytelny dla człowieka kod źródłowy w czytelne dla komputera instrukcje znane jako kod skompilowany lub kod maszynowy.

Pliki, które nie są plikami tekstowymi, takie jak pliki, które reprezentują obrazy wizualne lub zawierają skompilowany kod, są często określane jako pliki binarne. Jest to niestety mylące określenie, ponieważ pliki tekstowe to w końcu także zera i jedynki. Pliki, które nie są plikami tekstowymi będziemy określać jako pliki nietekstowe.

Istnieje wiele sposobów reprezentowania języka pisanego przez człowieka za pomocą zer i jedynek. Z powodów historycznych, większość kodu źródłowego była pierwotnie napisana w tak zwanym alfabecie łacińskim. Alfabet łaciński ma 26 podstawowych znaków, które są używane do reprezentowania słów, z których każdy ma dwie formy, wielką i małą literę. Posiada również 10 cyfr do reprezentowania liczb. Alfabet łaciński, wraz z różnymi innymi symbolami używanymi do oznaczania struktury i innych pojęć, jest kodowany jako 1 i 0 w formacie znanym jako „ASCII”, który może reprezentować 128 różnych znaków i z powodów historycznych był dominujący w większości oprogramowania przez wiele lat.

Jednakże, alfabet łaciński jest tylko niewielkim podzbiorem wielu sposobów, w jakie ludzie wyrażają siebie w języku pisanym. Aby obsługiwać inne alfabety, a jednocześnie umożliwić wszystkim programom, które zostały napisane z myślą o używaniu ASCII, kontynuowanie pracy bez zmian (koncepcja znana jako kompatybilność wsteczna), wprowadzono inny format danych znany jako „UTF-8”.

ASCII pozostaje najbardziej rozpowszechnionym formatem kodu źródłowego. Każda szpula tego archiwum zawiera przewodnik po znakach ASCII. ASCII jest podzbiorem UTF-8, co oznacza, że wszystkie kodowania ASCII są również kodowaniami UTF-8. Szpula przewodnika zawiera dodatkowo specyfikację wszystkich znaków UTF-8. Prawie wszystkie pliki tekstowe w tym archiwum powinny być zakodowane jako UTF-8.

Pliki nietekstowe obejmują pliki przeznaczone do reprezentowania obrazów i sformatowanych dokumentów. Powszechnie stosowaną konwencją jest to, że nazwy plików kończą się znakiem „.”, po którym następuje przyrostek wskazujący typ pliku. Na przykład, nazwa pliku kończąca się na .jpg jest prawdopodobnie plikiem obrazu JPEG; nazwa kończąca się na .PNG jest prawdopodobnie plikiem obrazu Portable Network Graphic; a nazwa kończąca się na .pdf jest plikiem Portable Document Format.

Nie ma jednego sufiksu, który wskazuje na pliki tekstowe. W przypadku kodu źródłowego, przyrostek wskazuje raczej na język programowania lub język znaczników, w którym kod został napisany. Języki programowania i znaczników zostaną opisane bardziej szczegółowo poniżej.

## Jak rozpakować zawartość archiwum

W tym miejscu przedstawimy, jak rozpakować dane zarchiwizowane repozytorium do jego poszczególnych plików składowych. Ponownie, proces ten składa się z:

1. Określenia konkretnej szpuli i klatek, na których zarchiwizowane są dane repozytorium.

2. Dekodowania z kodów QR, pól czarnych, białych i szarych pikseli na tych klatkach, do pliku binarnego, czyli ciągu (co najmniej tysięcy, a często milionów) zer i jedynek.

3. Rozpakowania pliku binarnego do dłuższego, nieskompresowanego pliku archiwum.

4. Rozpakowania pliku archiwum do osobnych podplików, które zawiera. Należy jednak pamiętać, że dane archiwalne są na ogół zrozumiałe, choć nieprzejrzyste, nawet jeśli ten krok zostanie pominięty.

5. Wreszcie, konwersji każdego z tych podplików - samych sekwencji 1 i 0, które mogą być zarówno dość krótkie jak i bardzo długie - na znaki pisane, jeśli są to pliki tekstowe.

### Określenie konkretnej szpuli i klatek, na których zarchiwizowane są dane repozytorium

Każda szpula filmowa zaczyna się od pustej klatki, a następnie od referencyjnej klatki zerowej, która składa się z czarnego prostokąta w jednym rogu klatki. Następną klatką jest czytelna dla człowieka klatka kontrolna, zawierająca informacje o szpuli. Następnie znajduje się spis treści, który z kolei zawiera listę plików danych użytkownika.

Każde repozytorium na tej szpuli jest jednym z tych plików danych użytkownika. Lista zawiera unikalny identyfikator, identyfikator pliku i nazwę dla każdego z tych plików. Na przykład, repozytorium CPython konta Python może mieć identyfikator pliku 12345, a nazwę python_cpython.tar.

Po liście plików danych użytkownika znajduje się lista lokalizacji danych cyfrowych. Lista ta zawiera identyfikator pliku, klatkę początkową, bajt początkowy, klatkę końcową i bajt końcowy. Tak więc, używając hipotetycznego przykładu CPython, element na tej liście o identyfikatorze 12345 może mieć ramkę początkową 054321, bajt początkowy 03210321, ramkę końcową 054545 i bajt końcowy 12321232.

Oznacza to, że aby uzyskać dane CPython: Przejdź do klatki 54321 tej szpuli filmu. Zdekoduj wszystkie klatki od początkowej, 54321, do końcowej, 54545, na wartości binarne, w sposób opisany poniżej. W ten sposób otrzymasz 225 fragmentów danych ponumerowanych od 54321 do 54545, które rozpoczną się od zestawu pustych fragmentów bez danych. Odrzuć pierwsze 3210320 bajtów w pierwszym niepustym kawałku danych. Dołącz wszystkie "środkowe" fragmenty danych, w kolejności. Na koniec dołącz pierwsze 12321232 bajty z ostatniego fragmentu danych, 54545. Teraz masz zebrane kompletne repozytorium CPython, jako pojedynczy skompresowany plik archiwum.

### Dekodowanie kodów QR do pliku binarnego

Szczegóły dotyczące sposobu dekodowania klatek filmu na dane binarne znajdują się w czytelnej dla człowieka informacji o reprezentacji, która znajduje się po spisie treści na początku każdej szpuli filmu w archiwum. Informacje te znajdują się na każdej szpuli, tak że nawet jeśli pojedyncza szpula zostanie odłączona od archiwum, nadal będzie można odszyfrować jej zawartość. Informacja o reprezentacji zawiera w kolejności:

1. Przewodnik po programie archiwum GitHub (ten dokument)

2. Indeks opisowy GitHuba, lista i krótki opis wszystkich repozytoriów na tej szpuli

3. Opis informacji o reprezentacji

4. Ochrona zasobów cyfrowych i sposoby pozyskiwania danych, przegląd szczegółów dotyczących pozyskiwania danych

5. Opis nośnika pamięci

6. Technologia odzyskiwania danych

7. Ogólne utrzymanie struktury szpuli (format szpuli)

8. Ogólny opis formatu klatki 4K

9. Opis rozpakowywania biblioteki (dla kodów QR)

10. Rozpakowywanie kodu źródłowego biblioteki

11. Specyfikacja formatu danych ASCII

12. Specyfikacja języka programowania C

13. Kod źródłowy pliku archiwum TAR

14. Kod źródłowy PDF

15. Specyfikacja formatu pliku XZ (dla kompresji / dekompresji, opisana poniżej)

Szósta z tych pozycji, dokument technologii odzyskiwania danych, opisuje wymagania i procesy wykorzystania skanera do przechwycenia danych zawartych w pojedynczej cyfrowo zakodowanej klatce filmu i przekształcenia ich w formę nadającą się do analizy komputerowej. Ósma z tych pozycji, opis formatu klatki 4K, zawiera informacje techniczne, w tym kod źródłowy, wymagane do tego, aby komputer mógł pobrać taki zeskanowany obraz i przekształcić go w dane binarne.

Teoretycznie jest to możliwe, aby przekonwertować repozytorium z danych zakodowanych w QR na dane binarne bez użycia komputera. Byłoby to jednak niezwykle trudne i prawdopodobnie wymagałoby znacznego wysiłku ze strony dobrze zorganizowanej społeczności przez wiele tygodni, jeśli nie miesięcy lub lat. Ponieważ zawartość repozytoriów to oprogramowanie przeznaczone do pracy na komputerze, ich wykorzystanie bez komputera byłoby, w najlepszym wypadku, minimalne.

W przypadku, gdyby spadkobiercy tego archiwum nie będą posiadali komputerów, powinni przechowywać archiwum w całości i bezpiecznie do czasu, aż je zdobędą. Jednym z celów Drzewa Technologii, które można odczytać przez człowieka, jest pomoc w przyspieszeniu rozwoju technologii i komputerów na wypadek takiej ewentualności. (Jego innym celem jest skodyfikowanie naszej technologii i jej rozwoju dla przyszłych historyków).

### Rozpakowanie pliku archiwum do poszczególnych podplików, które zawiera

Plik binarny dla każdego repozytorium jest w formacie znanym jako TAR, czyli Tape Archive. Plik TAR jest zasadniczo tworzony poprzez grupowanie pewnej liczby plików razem poprzez łączenie końca jednego z początkiem następnego, tak jak sklejanie pojedynczych kartek papieru w jeden zwój. Plik TAR może zawierać dowolną liczbę plików, o dowolnym rozmiarze, podzielonych na dowolną liczbę katalogów i podkatalogów.

Każdy podplik w pliku TAR jest poprzedzony 512-bajtowym rekordem nagłówkowym, który działa jak taśma w metaforze zwoju. Ten rekord nagłówkowy zawiera informacje o pliku, takie jak jego nazwa i rozmiar. Koniec archiwum jest wskazywany przez co najmniej dwa kolejne 512-bajtowe bloki.

Ponieważ pliki TAR są w zasadzie tylko zbiorami plików z rekordami tekstowymi pomiędzy nimi, jeżeli plik TAR zawiera wszystkie pliki tekstowe, może być traktowany jako plik tekstowy. Jeżeli zawiera on mieszaninę, może być traktowany jako plik tekstowy, który zawiera mieszaninę uporządkowanego, znaczącego tekstu (składowe pliki tekstowe) i niezrozumiałego bełkotu (składowe pliki nietekstowe).

Możliwe jest zagnieżdżanie plików TAR w plikach TAR, jeden kontener w drugim, i w ten sposób przechowywana jest większość naszych zarchiwizowanych danych. Dla danego repozytorium, zewnętrzny plik TAR będzie zawierał co najmniej:

* pojedynczy, nieskompresowany plik metadanych o nazwie META, który zawiera nazwę repozytorium, nazwę konta, opis, język, liczbę gwiazdek i liczbę forków.
* skompresowany (patrz poniżej) plik o nazwie COMMITS, który zawiera log zmian dokonanych w repozytorium w czasie
* plik o nazwie repo.tar.xz, skompresowany plik TAR, który zawiera rzeczywistą zawartość repozytorium.

Inne metadane, takie jak wiki, gh-pages, issues i pull requests, mogą być również dołączone jako oddzielne skompresowane pliki.

Szczegółowe informacje o plikach TAR oraz oprogramowaniu do ich kodowania i dekodowania można znaleźć w informacjach o reprezentacji w każdej szpuli archiwum.

### Rozpakowywanie skompresowanych plików do czytelnych, nieskompresowanych plików

W celu włączenia jak największej liczby repozytoriów i jak największej ilości danych, większość danych została skompresowana. Kompresja oznacza użycie małej ilości danych do reprezentowania większej ilości, poprzez użycie wzorców i powtórzeń w tej większej ilości. Na przykład, zamiast pisać znak a dziewięć razy z rzędu, można po prostu napisać skompresowany tekst 9a, jeśli jest się pewnym, że czytelnik zrozumie, że 9a oznacza nieskompresowany tekst aaaaaaaaa.

Efektywne algorytmy kompresji są o wiele bardziej złożone, ale obowiązuje ta sama zasada. Niniejsze archiwum wykorzystuje program kompresujący znany jako „XZ”, który z kolei wykorzystuje algorytm znany jako „LZMA”. Drugi plik danych w każdej szpuli zawiera kod źródłowy i dokumentację do programu XZ w pojedynczym nieskompresowanym pliku archiwum TAR, opisanym poniżej. (Pierwszy plik danych zawiera Powszechną Deklarację Praw Człowieka we wszystkich dostępnych językach pisanych).

LZMA łączy w sobie tak zwany algorytm „LZ77” i „kodowanie zakresowe”. LZ77 zastępuje powtarzające się dane odniesieniami do poprzednich wystąpień tych danych. Na przykład, w dużym uproszczeniu, jeśli 80-bajtowa fraza pojawia się dwa razy, w odstępie 400 bajtów, za drugim razem algorytm zasadniczo zagęszcza dane mówiąc „powtórz 80 bajtów sprzed 400 bajtów”. Kodowanie zakresowe zasadniczo przekształca całą wiadomość w pojedynczą bardzo długą liczbę, która z kolei może być zakodowana.

Konkretne kroki algorytmu, który ma być użyty do dekompresji danych, są opisane w kodzie źródłowym XZ zawartym w drugim pliku danych w każdej szpuli. Choć teoretycznie możliwe jest ręczne zdekompresowanie danych, byłby to proces niezwykle czaso- i pracochłonny. W praktyce przydałby się działający komputer.

### Konwersja każdego pojedynczego pliku na znaki pisane

Przez tysiąclecia ludzkość używała wielu znaków pisanych. Kodowanie używane do reprezentowania tych znaków jako 1 i 0 w tym archiwum jest znane jako „UTF-8”. Pojedynczy znak UTF-8, tj. pojedynczy symbol pisany, może zajmować od 1 do 4 bajtów danych binarnych.

Z powodów historycznych, ponieważ były one najpowszechniej używane w czasach i regionach, w których i kiedy zaczęto tworzyć oprogramowanie, grupa znaków (i pojęć) znana jako „ASCII” jest kodowana najbardziej efektywnie, po 1 bajcie na znak. Wszystko, co nie jest ASCII, jest kodowane jako 2 lub więcej bajtów na znak. Większość plików tekstowych w tym archiwum jest ASCII, ale znaczna ich liczba nie jest. Wiele innych będzie w większości ASCII z okazjonalnymi znakami spoza ASCII.

Szczegółowa specyfikacja ASCII znajduje się w informacji o reprezentacji w każdej szpuli archiwum. Szczegółowa specyfikacja UTF-8 znajduje się na szpuli z przewodnikiem. Pierwszy plik danych na każdej szpuli archiwum będzie zawierał tekst Powszechnej Deklaracji Praw Człowieka we wszystkich dostępnych językach pisanych. Będzie on służył zarówno jako narzędzie do tłumaczenia, jak i jako przykład ASCII i UTF-8.

## Rodzaje plików

Istnieje wiele różnych rodzajów plików tekstowych, tworzonych z różnych powodów. Podstawowym rodzajem, dla którego istnieje to archiwum, jest kod źródłowy. Kod źródłowy jest bardzo gęstym, niezwykle uporządkowanym tekstem, w którym symbole takie jak '{' i ';' mają ogromne znaczenie.

Kluczową rzeczą w kodzie źródłowym jest to, że jest on napisany tak, by mógł być czytany przez kompilatory. Ponieważ kompilatory są oprogramowaniem, innym sposobem wyrażenia tego jest to, że kod źródłowy jest pisany po to, by był czytany przez komputery. Dobry kod jest również napisany tak, że inni ludzie, jeśli są wykwalifikowani i wykształceni w dziedzinie oprogramowania, mogą go zrozumieć; ale jest on poprawny tylko wtedy, gdy może go zrozumieć kompilator.

Kompilator ten z kolei, poprzez skomplikowane sekwencje opisane w drzewie technologicznym, przekształci kod źródłowy w sekwencje jedynek i zer, które spowodują, że komputer będzie wykonywał funkcje i czynności opisane w kodzie. Weźmy bardzo prosty przykład, linia kodu

    for (int i=0; i<5; i++) { }

zostanie przekształcona przez kompilator w serię instrukcji binarnych podawanych komputerowi, które spowodują, że niewielka część komputera, zwana rejestrem procesora, ustawi swoją wartość na 0, a następnie zwiększy tę wartość do 1, 2, 3, a potem 4. (Nie jest to przykład użytecznego kodu; jest to tylko zobrazowanie złożonego procesu przekształcania kodu źródłowego w działające oprogramowanie).

Inne rodzaje plików tekstowych, takie jak JSON, XML i HTML, są używane do przechowywania danych (w przeciwieństwie do poleceń) dla komputerów. Są one zazwyczaj również czytelne dla ludzi, chociaż ich ustrukturyzowane formaty sprawiają, że są trudniejsze do odczytania niż mniej ustrukturyzowany tekst opowiadający historię, taki jak ten plik.

Większość innych rodzajów plików tekstowych jest przeznaczona do ostatecznego odczytania przez człowieka. Niektóre z nich są prostym, najczęściej nieuporządkowanym tekstem, jak ten plik, który właśnie czytasz. Jednym z rodzajów plików, które można spotkać w archiwum, jest Markdown, oznaczany rozszerzeniem .md, który jest rodzajem formy pośredniej, przeznaczonej do odczytu przez ludzi w surowej postaci, a jednocześnie ustrukturyzowanej tak, by komputery mogły je sformatować w bardziej atrakcyjne wizualnie i użyteczne układy. Większość repozytoriów w tym archiwum posiada plik README.md w formacie Markdown, który ma być wstępem do repozytorium, opisującym czym jest, dlaczego istnieje i jak z niego korzystać.

Przydatny może być również krótki przegląd najbardziej powszechnych form plików nietekstowych. Skompilowany kod jest nietekstem. Pliki JPG i PNG kodują obrazy w formacie cyfrowym, a MP3 i WAV kodują dźwięk. Pliki PDF kodują dokumenty z precyzyjnym, doskonałym formatowaniem. A pliki ZIP i TAR, jak już wcześniej wspomniano, są kontenerami, które z kolei mogą zawierać jeden lub wiele innych plików.

## Języki ludzkie i języki programowania

### Języki ludzkie

Istnieją tysiące języków pisanych używanych obecnie przez ludzkość i jeszcze więcej języków mówionych. Większość z nich jest używana tylko przez stosunkowo niewielkie populacje, ale istnieje co najmniej dwadzieścia języków używanych jako pierwszy lub drugi język przez co najmniej 60 milionów ludzi.

Najpowszechniej używanymi językami na świecie są angielski i chiński. Z powodów historycznych, przez wiele lat większość rozwoju oprogramowania miała miejsce w krajach anglojęzycznych, więc przez pewien czas angielski stał się domyślnym językiem oprogramowania. Większość języków programowania używa w swojej składni angielskich słów. Jest to język, w którym po raz pierwszy napisano ten przewodnik po archiwum.

Nie ma gwarancji, że spadkobiercy tego archiwum będą znali angielski, choć wydaje się, że jest to szczególnie prawdopodobny język, który przetrwa w nieskończoność. Na wypadek, gdyby przydały się wskazówki dotyczące innych języków, dołączamy ponad 500 dostępnych tłumaczeń Powszechnej Deklaracji Praw Człowieka w postaci nieskompresowanego pliku UTF-8 na początku każdego zwoju, a także w drzewie technologicznym. Deklaracja ta jest listą praw i wolności każdego człowieka naszej ery, które nigdy nie mogą zostać odebrane.

### Języki programowania

Języki programowania to języki używane przez ludzi do przekazywania instrukcji komputerom. Są to języki, w których wyrażane jest oprogramowanie. Inni (przeszkoleni) ludzie powinni również być w stanie czytać oprogramowanie napisane w językach programowania, ale to jest drugorzędny cel.

Język programowania jest zbiorem predefiniowanych elementów, z których większość stanowią słowa, które mogą być ułożone w uporządkowany sposób w celu poinstruowania komputera, aby wykonał określoną czynność w określony sposób. Zbiór takich instrukcji znany jest jako program lub kod źródłowy. Kod źródłowy to zasadniczo oprogramowanie w utrwalonej, pisemnej formie.

Programy są zazwyczaj podzielone na poszczególne kroki, znane jako instrukcje, które z kolei są pogrupowane w zbiory znane jako funkcje. Cały program może być zawarty w jednym pliku, lub może być rozłożony na tysiące.

Istnieją setki różnych języków programowania, rozproszonych w wielu różnych formach, podejściach i filozofiach. Niektóre z nich są kompilowane do oddzielnych plików binarnych, które są następnie wykonywane; niektóre, znane jako języki „interpretowane”, są efektywnie kompilowane i uruchamiane za jednym razem, bez żadnego etapu pośredniego. Większość nowoczesnych języków programowania zawiera biblioteki wstępnie napisanych funkcji, a biblioteki te mogą być bardzo obszerne i rozbudowane. Niektóre z najpopularniejszych obecnie języków programowania obejmują:

* C, jeden z najstarszych i najszybszych, najbardziej uniwersalnych i najpotężniejszych języków, prosty w niektórych aspektach, ale dość ograniczony w innych, i nie zawsze intuicyjny, łatwy do odczytania lub łatwy do nauczenia.

* C++, bardziej złożone, abstrakcyjne i potężniejsze rozwinięcie języka C.

* C#, dalsze rozwinięcie kompilacji nie do binarnego kodu maszynowego, ale interpretowanego „runtime”.

* Java, która jest podobna do (ale poprzedzająca) C#, jest prawdopodobnie najczęściej używanym obecnie językiem.

* JavaScript, w odróżnieniu od Javy, mimo podobieństwa w nazwie, znany również jako "ECMAScript", jest językiem początkowo używanym wyłącznie w przeglądarce internetowej, tj. programie, który pobierał, interpretował i wyświetlał dane ze zdalnego komputera zwanego serwerem internetowym; obecnie jest jednak powszechnie używany również na tych serwerach.

* TypeScript, forma JavaScriptu z bardziej rygorystycznymi zasadami, dzięki którym błędy, znane również jako bugi, mają mniejsze szanse na przedostanie się do programów.

* Python, elegancki język popularny wśród naukowców, zarówno potężny, jak i dobry jako pierwszy język.

* Ruby, intuicyjny język, którego składnię często czyta się prawie jak pisany angielski.

* Go, prosty, potężny język, który szczególnie dobrze radzi sobie z programami paralelizowanymi, tzn. programami napisanymi tak, aby wiele funkcji działało niezależnie w tym samym czasie.

* Swift, nowy język używany do pisania aplikacji na telefony i innych urządzeń używanych przez miliard ludzi.

* Rust, przeznaczony jako zamiennik dla C, taki, w którym prawdopodobieństwo wystąpienia niebezpiecznych błędów jest znacznie mniejsze.

* PHP, prosty język używany do obsługi serwerów internetowych.

* Lisp, bardzo stary język z fundamentalnie odmiennym, funkcyjnym podejściem do programowania.

* SQL, bardzo różny rodzaj języka używany do pobierania danych z ustrukturyzowanych i wysoce wydajnych magazynów danych znanych jako bazy danych.

* Assembler (lub assembly), bardzo enigmatyczna, ograniczona, ale szybka i potężna rodzina języków, w której istnieje bezpośredni związek między konstrukcjami językowymi a kodem maszynowym danego komputera; może być uważany za kod w połowie skompilowany.
