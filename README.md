# ASRT-WDI 
## Automatyczne Szablony, Rozwiązania i Testy do WDI na AGH
### 🔧 Używanie Projektu

Każdy folder z zadaniem składa się z czterech składników:

1. **`README.md`** – zawiera treść zadania, **główne rozwiązanie** oraz, okazjonalnie, opis rozwiązania.
2. **`Rozwiązania`** – folder zawierający gotowe rozwiązania zadania.
3. **`szablon.py`** – szablon do wypełnienia własnym rozwiązaniem, który okazjonalnie zawiera **podpowiedzi** lub wyjaśnienia treści."
4. **`testy.py`** – plik z testami jednostkowymi.


### 🧪 Jak testować swoje rozwiązania?

Wypełnij plik `szablon.py` i uruchom go, odkomentowując funkcję `odpal_testy()`

https://github.com/user-attachments/assets/ad6d166e-bda7-4eca-a8cc-86d984913e0f

### 🌐 Wizualizacje Rozwiązań
Niektóre zadania zawierają wizualne wyjaśnienia algorytmów, które są hostowane w chmurze na stronie internetowej lub zrealizowane w Pygame, na przykład [Kolokwium 2022 A3](https://github.com/kamilGie/ASRT-WDI/tree/main/Kolokwia/Kolokwium_2/2022_A3), [160](https://github.com/kamilGie/ASRT-WDI/tree/main/Zestaw_5%3A_Rekurencja/160) czy [112](https://github.com/kamilGie/ASRT-WDI/tree/main/Zestaw_3%3A_Tablice_o_większej_liczbie_wymiarów/112) 

### 💡 Podpowiedzi

Niektóre zadania mają w `szablon` trzy ***podpowiedzi***: 1 Lekko nakieruje,  2 Wyjaśni,  3 Poprowadzi przez zadanie.  Aby je wyświetlić w terminalu, wystarczy odkomentować funkcję, na przykład [226](https://github.com/kamilGie/ASRT-WDI/blob/main/Zestaw_8%3A_Wyszukiwanie_i_sortowanie/226/szablon226.py) czy [Kolokwium 2021 6](https://github.com/kamilGie/ASRT-WDI/blob/main/Kolokwia/Kolokwium_3/2021_6/szablon2021_6.py)

### 🌑 Czarny Motyw Zestawu
Każdy zestaw oraz każde zadanie zawiera plik `README` z opisem zadań. Jeśli masz ustawiony czarny motyw na GitHubie, zestaw ten będzie wyświetlany w ciemnej wersji.


### 🐛 Zgłaszanie Błędów
Błędy w rozwiązaniach, testach lub treściach zgłaszaj na <a href="https://github.com/kamilgie/ASRT-WDI/issues/new?labels=bug">****Issues****</a> lub <a href="https://gieras.pl/">****prywatnie****</a>.


### 🧱 Prototypy
Nierozwiązane zadania znajdują się w plikach `prototyp.py` i czekają na rozwiązanie. Po rozwiązaniu zadania można stworzyć pełne zadanie, automatycznie generując wszystkie pliki.


<details>
   
   <summary> Tworzenie Zadań na prototypie </summary>

1. Po rozwiązaniu zadania na `prototyp.py` można stworzyć pełne zadanie, odkomentowując funkcję `stworz_zadanie` i przekazując w tablicy funkcje, które mają być objęte testami.
2. Funkcja `stworz_zadanie` automatycznie przygotuje testy na podstawie przekazanych funkcji. Poprosi również o podanie argumentów testowych, które Twoim zdaniem mogą być interesujące lub problematyczne.
3. Następnie utworzy folder zadania zawierający pliki: `rozwiazanie.py` oraz `szablon.py` na podstawie `prototyp.py`, a także `testy.py` na podstawie wcześniej wygenerowanych testów.

https://github.com/user-attachments/assets/f3316918-a5e9-457f-8c2e-b4a5e5f0f27c



</details>


 
---

## Źródła rozwiązań 📚

Część rozwiązań została zaczerpnięta (*bezczelnie podkradziona*) z poniższych repozytoriów.  
Jestem ogromnie wdzięczny ich autorom za świetne prace, które bardzo pomogły! 

- 🌟 [WDI-2023](https://github.com/pawlowiczf/WDI-2023) - [Filip Pawłowicz](https://github.com/pawlowiczf)
- 🌟 [WDI2020](https://github.com/Wisien999/WDI2020) - [Wisien999](https://github.com/Wisien999)  




### 🗿 Najwięksi współtwórcy:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://github.com/kamilGie/ASRT-WDI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kamilGie/ASRT-WDI" alt="Najwięksi współtwórcy" />
</a>




# Szczegóły Projektu

<details>
  <summary> 🤝 Jak pomóc i zostać współtwórcą? </summary>

## 🤝 Jak pomóc i zostać współtwórcą?


- Zalecam [***utworzenie forka***](https://github.com/kamilGie/WDI/fork) i zgłaszanie swoich zmian za pomocą pull requestów.

### 💡 Możliwe Ulepszenia
- ✏️ Stworzenie Zadania
- 🛠️ Poprawienie treści zadania, jeśli jest niejasna lub brakuje np. znaków potęgowania.
- 🔧 Ulepszanie testow poprzez komendy lub stworzeniej własnej [Szczegóły](#komendy)
- 🧠 Tworzenie Strategi Tworzenia Zadań [Szczegóły](#strategie)
  
ASRT opiera się na **rozszerzaniu funkcjonalności**. Dzięki temu możesz dodawać nowe funkcje i strategie bez modyfikacji istniejącego kodu, co ułatwia wdrożenie bez potrzeby wiedzy o całym systemie i unika konfliktów.
### 🐛 Zgłaszanie błędów

- Błędy w rozwiązaniach, testach lub treściach można zgłaszać <a href="https://github.com/kamilgie/ASRT-WDI/issues/new?labels=bug"> ****tutaj**** </a>

### 💬 Feedback

- Sam feedback na temat tego, jak się pracuje, w jakim kierunku można pójść oraz czego brakuje, również będzie mile widziany. [kontakt](http://www.gieras.pl).


</details>



<details>
  <summary> 🧪 Testowanie Zadania </summary>

## Testowanie Zadania
Przykładowy `szablon.py` wygląda tak: 
```python
# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>
# print(a,b,c)

def Zadanie_1(n): ...


if __name__ == "__main__":
    from testy01 import odpal_testy

    Zadanie_1(input('Podaj n: '))

    # odpal_testy()
```
### Na górze znajduje się opis zadania, funkcja do wypełnienia i przygotowany main.
Wypełniasz funkcję kodem, o który prosi opis zadania. Wyniki można zwracać lub wypisywać. Jeśli to nie będzie oczywiste, pod opisem zadania powinna być wskazówka od autora testów, jakiego sposobu zwracania wyników oczekuje. W tym przypadku widać, że boki trójkąta powinny być wypisywane kolejno, bez żadnych dodatkowych napisów.

Po tym, jak zrobisz zadanie i będziesz pewny jego poprawności, możesz odkomentować funkcję `odpal_testy()` i uruchomić program normalnie:
```python
# ====================================================================================================>
# Zadanie 1
# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej
# jest mniejsza od liczby N wprowadzonej z klawiatury.
# ====================================================================================================>
# print(a,b,c)

def Zadanie_1(n):
    for a in range(1, n):
        for b in range(a, n):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and c <= n:
                print(a, b, c)

if __name__ == "__main__":
     from testy01 import odpal_testy

     odpal_testy()
```
### wynik takiego programu dalby taki wynik
<img width="1504" alt="Zrzut ekranu 2024-10-24 o 22 26 09" src="https://github.com/user-attachments/assets/666313c3-15ec-4697-955c-1e5de81e23d7">
  
Wynik testu wskazuje na błąd: widzimy komunikat `AssertionError: '3 4 5' not found in [''].` Oznacza to, że test oczekiwał pustego stringa `''`, a otrzymał `'3 4 5'`, co sugeruje, że wynik dla c = 5 został niepotrzebnie wypisany.

Po chwili namysłu i ponownym przeczytaniu treści zadania, można zauważyć, że warunek mówi o długości przekątnej mniejszej, niż liczba **N**. Kod należy poprawić i ponownie uruchomić testy z nową nadzieją.

### Czasami można spotkać się z takim przypadkiem:
 <img width="1165" alt="Zrzut ekranu 2024-10-24 o 22 57 49" src="https://github.com/user-attachments/assets/4fe66d52-766c-417a-87ab-738a38271137">
Widzimy, że mimo poprawnego wyniku mamy błędny test, ponieważ wypisujemy wynik w innym typie lub kolejności. W takim przypadku możemy:

- Cieszyć się poprawnym rozwiązaniem i pójść dalej.
- Zmienić typ lub format wyjścia na taki, jaki jest oczekiwany w teście.
- Zainteresować się pomocą w rozwijaniu projektu i za pomocą komendy dodać swoją funkcję wraz z jej rozwiązaniem do listy poprawnych odpowiedzi, aby inni użytkownicy mieli dobre testy dla takich samych wyników jak twój.

Często też zadania mają kilka poprawnych odpowiedzi, więc na każdy test trzeba być czujnym i analizować jego poprawność. W takich przypadkach również nalegam, by zgłaszać mi takie zadania, ponieważ będą dodawane inne warianty poprawnej odpowiedzi.

Więcej o tym, jak działa cały projekt w 


---
</details>

<details>
  <summary> ✏️  Tworzenie Zadania z prototypu  </summary>

## Tworzenie Zadania
### `stworz_zadanie()` 
Każdy prototyp zawiera funkcję `stworz_zadanie`, importowaną z pliku `Develop`. Funkcja `stworz_zadanie` przesyła funkcje, które chcemy by obejmowały testy oraz wchodziły w skład szablonu do wypelnienia. Wiec przykładowo wypełniony `prototyp` powinnien wygladać tak:
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży 2 liczby
# ====================================================================================================>

def dodaj(a, b):
    return a + b

def mnoż(a, b):
    return a * b

if __name__ == "__main__":
    from Develop import stworz_zadanie

    # stworz_zadanie([dodaj, mnoż])
```

Funkcja `stworz_zadanie` działa podobnie jak funkcja `print`. Można ją uruchomić bez dodatkowych parametrów, aby wygenerować domyślną strukturę plików: `README.md`, `testy.py`  `szablon.py` oraz folder `Rozwiązania`. 

### Modyfikacje 

Można modyfikować sposób, w jaki generowane są pliki, ustawiając argumenty nazw plików. Modyfikacje są podawane jako stringi, które określają  strategie, z jaką wygenerują się pliki. Dla podstawowego użycia projektu przydatne będą trzy modyfikacje:

```python
# Stworzy testy, których wyniki będą zaokrąglone.
# Przydatne w zadaniach zwracających wartości typu `float`, gdzie wyniki mogą się różnić od ustawionego epsilonu.
stworz_zadanie([dodaj, mnoż], testy="float")
```

```python
# Stworzy testy, których wyniki będą w typie `set`.
#  Przydatne w zadaniach, w których kolejność lub częstotliwość występowania wyników nie ma znaczenia.
stworz_zadanie([dodaj, mnoż], testy="bez_kolejnosci")
```
```python
#  Nie stworzy pliku.
#  Przydatne w zadaniach abstrakcyjnych, które nie są możliwe do przetestowania.
stworz_zadanie([dodaj, mnoż], testy="brak", szablon="brak")
```

```python
# Stworzy zadanie które polega na listach przesyłaczowych
stworz_zadanie([dodaj, mnoż], testy="przesylaczowe_t", szablon="przesylaczowe_s", README="przesylaczowe_rm")
```


Dokładniej o modyfikacjach jest w sekcji [strategie](#Strategie)

<details>
   <summary> Domyślna konfiguracja plików </summary>

### `README.md` 
1. Dodaje kod do wyświetlania treści zależnych od motywu.
2. Dodaje linię, aby README formatowało się jak Python.
3. Z szablonu usuwa treści i zaczyna od pierwszej niezkomentowanej linijki.
4. Po napotkaniu `main` przestaje pisać.
5. Kończy formatowanie Pythonowe.


### `rozwiazanie.py` 
1. przepisuje prototyp do napotkania linijki main
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży dwie liczby
# ====================================================================================================>

def dodaj(a, b):
    return a + b

def mnoż(a, b):
    return a * b

```
### `szablon.py` 
1. Przepisuje pierwsze linie, które są komentarzami, aby zostawić opis zadania wraz z ewentualnymi komentarzami twórcy zadania.
2. Następnie usuwa wszystkie linijki poza linijką zaczynającą się od `def FunkcjaKtoraTestujemy(`. Tę linijkę pozostawia i dopisuje trzy kropki, aby użytkownik wiedział, że te funkcje są do napisania.
3. Usuwa wszystkie linie do momentu napotkania bloku `if __name__ == "__main__":`.
4. Zapisuje import funkcji `odpal_testy`. oraz `podpowiedz`
5. Prosi użytkownika o wprowadzenie argumentów, które pojawią się w szablonie wraz z jego zakomentowanym wynikiem.
6. zakomentwane funkcje podpowiedz
7. Zakomentowana metoda `odpal_testy()`, która będzie uruchamiać testy.
   
```python
# ====================================================================================================>
# Zadanie 0
# Stworz 2 funkcje jedna dodaje 2 liczby druga mnoży dwie liczby
# ====================================================================================================>

def dodaj(a, b): ...

def mnoż(a, b): ...

if __name__ == "__main__":
    from testy01 import odpal_testy, podpowiedz

    dodaj(2, 3) # return 5
    mnoż(2,2)  # return 4

    # podpowiedz(1)
    # podpowiedz(2)
    # podpowiedz(3)

    # odpal_testy()
```

### `testy.py` 
1. Napisze  importy, funkcje oraz  nagłówek klasy `Testy`
2. Następnie dla każdej funkcji przekazanej do testowania:
3. Sprawdza liczbę argumentów, jaką funkcja przyjmuje.
4. Jeśli liczba argumentów nie wynosi zero, prosi użytkownika o wpisanie argumentów testowych.
5. Przetwarza input użytkownika, zmieniając go na argumenty według algorytmów.
6. Uruchamia funkcję z argumentami testowymi, monitorując jednocześnie wartości wypisywane przez `print` oraz wartości zwracane przez funkcję.
7. Jeśli funkcja nic nie zwróci, wynikiem zostanie to, co zostało przechwycone przez `print`. Jeśli funkcja zwróci inną wartość, to ona będzie wynikiem, a dane wypisane przez `print` zostaną zignorowane.
8. Z argumentów i wyniku napisze metodę testową o nazwie `test_numerTestu_funkcjaTestowalna`.
```python
    def test_Nr1_dodaj(self):
        self.assertIn( dodaj(2, 2), 4)
```
9. Będzie powtarzać proces od punktów 3–8, aż do napotkania argumentu `stop` od użytkownika, który zakończy testy.


</details>

---

## Pisanie Testów


Po uruchomieniu funkcji `stworz_testy`, jeśli liczba argumentów przekazanych do testowania funkcji jest większa niż zero, program poprosi użytkownika o podanie argumentów testowych. Argumenty należy wpisywać w tej samej formie, jak w wywołaniu funkcji w Pythonie.

Najpierw program poprosi o wpisanie argumentów do szablonu, aby użytkownik mógł zobaczyć przykładowe wywołanie w szablonie wraz z wynikiem.

<img width="1000" alt="Zrzut ekranu 2024-12-29 o 20 19 47" src="https://github.com/user-attachments/assets/5a342afc-c949-4573-a3d6-4706f3623f1b" />

Następnie program poprosi o wpisywanie argumentów testowych, które posłużą do testowania funkcji w pliku `testy.py`.

<img width="999" alt="Zrzut ekranu 2024-12-29 o 20 18 33" src="https://github.com/user-attachments/assets/570a5893-090e-45a2-b758-89ff0cca42a8" />


Po stworzeniu odpowiedniej ilości testów, można zakończyć proces tworzenia testów, podając argument `stop`, co zakończy Twój wkład w tworzenie testów.

Na sam koniec program poprosi o podanie trzech podpowiedzi dla użytkownika.
<img width="1000" alt="Zrzut ekranu 2024-12-29 o 20 23 14" src="https://github.com/user-attachments/assets/80f5396c-1088-4db8-8b07-e6d0691ca9d7" />

###  Finalizacja

Po stworzeniu trzech plików funkcja utworzy plik `prototypBackup.py`, aby bezpiecznie móc usunąć prototyp. Plik `prototypBackup.py` jest ignorowany przez `.gitignore`, więc nie będzie dodawany do głównego repozytorium. Został stworzony, aby w przypadku błędnego stworzenia zadania z różnych powodów móc utworzyć zadanie na nowo. Funkcja `stworz_zadanie` dba o to, by nie usunąć pliku `prototypBackup`, dzięki czemu można tworzyć zadania do momentu zadowolenia z efektu końcowego.

Na tym kończy się funkcja `stworz_zadanie`. Jeśli jednak komuś nie podoba się sposób w jaki pliki `README.py`, `szablon.py`, `testy.py` lub folder `Rozwiazania` są tworzone, chciałby dodać jakąś funkcjonalność lub inaczej tworzyć testy zawsze może stworzyć własną Strategię!

---
</details>

<details>
  <summary>🧠 Strategie</summary>

## Strategie
Strategie definiują sposób, w jaki będziemy tworzyć nasze pliki w projekcie. Aktualna lista strategii znajduje się w folderach o odpowiednich nazwach: [srt/README](srt/README) [srt/Szablon](srt/Szablon), [srt/Rozwiazania](srt/Rozwiazania), [srt/Testy](srt/Testy). Każda z nich jest klasą z krótkim komentarzem opisującym jej przeznaczenie i jest dostępna do użycia przez każdego twórcę zadania. 

Taki układ projektu pozwala na prosty rozwój i umożliwia rozwijanie go przez każdego, bez potrzeby znajomości całego systemu. Każdy może napisać własną klasę domyślną, która będzie następnie testowana w użyciu. Po tym, jak stanie się powszechniejsza, szybsza lub lepsza, zostanie ustawiona jako domyślna. Można również dodać klasę dodatkową, która obsługuje testy dla określonej puli zadań, dla których domyślne tworzenie zadania nie jest wystarczające.


### Podstawy Pisania Strategii

Stworzymy kilka przykładowych klas strategii:

- **`Data`** – Jest to strategia szablonu, która działa jak domyślna, z tą różnicą, że na górze pliku zostanie dodana data rozwiązania.
  
W folderze [srt/Szablon](srt/Szablon), tworzymy nowy plik z klasa o takiej samej nazwie. Klasa dziedziczy po jednej z klas w jej folderze albo po klasie bazowej. Klasa [srt/Bazowa.py](srt/Bazowa.py) jest abstrakcyjną klasą, z której będą pochodzić wszystkie klasy pochodne.

Klasa bazowa ma abstrakcyjną metodę `__str__`, w której musimy zwrócić wynik w postaci stringa, który później znajdzie się w pliku szablonu. Dla naszego pomysłu ta klasa będzie wyglądać tak:

```python
# srt/Szablon/data.py

#  Dziedzicze po klasie z pliku szablonów do której metody __str__  mógłbym coś dodać
from domyslne_s import domyslne_s 
from datetime import date

class data(domyslne_s):
""" na górze pliku zostanie dodana data rozwiązania. """
    def __str__(self):
        res = str(date.today().day)
        res += "\n"
        res += super().__str__()
        return res
```

Aby dostosować sposób generowania pliku, można skorzystać z atrybutów klasy bazowej, które są dostępne w klasach pochodnych:

- **`linie_prototypu`** – lista stringów reprezentujących linie prototypu.
- **`nr_zadania`** – numer zadania, które rozwiązujemy.
- **`funkcje`** – funkcje przekazane do testów szablonu oraz inne pomocnicze funkcje.
- **`sciezka`** – ścieżka folderu, w którym znajduje się tworzone zadanie.
- **`nazwa_pliku`** – domyślna nazwa pliku, która pochodzi od nazwy folderu zawierającego klasę. Na przykład, w folderze *Rozwiazanie*, klasy dziedziczące mają atrybut ustawiony na "rozwiazanie{`nr_zadania`}.py".

Te atrybuty mogą być wykorzystywane w klasach pochodnych od klasy bazowej, a poniżej przedstawiamy przykład użycia jednego z nich.

```python
# srt/Rozwiazanie/meritum.py

from bazowa import bazowa
import inspect

class meritum(bazowa):
    """rozwiazania  która koncentruje się wyłącznie na samym rozwiązaniu, pomijając opis zadania oraz sekcję `main`"""

    def __str__(self):
        res = ""
        for funkcja in self.funkcje:
            res += inspect.getsource(funkcja)
        return res
```

Tak stworzoną klasę możemy już używać w funkcji `stworz_zadanie`, podając argument `rozwiazanie="meritum"`.

---

- **`float`**  strategia testów, która będzie zaokrąglać wyniki.

Strategie testów będą najtrudniejszych do napisania. Najczęściej będą nadpisywały metody już istniejących strategii i modyfikować sposób sprawdzania wyników testów.

Aby skutecznie zaimplementować taką strategię, będziemy musieli nadpisać dwie specjalnie wyodrębnione metody klasy `prime`:

```python
from prime import prime

DOKLADNOSCI = int(input("podaj dokładność, z jaką testy mogą zaokrąglać: "))


class float(prime):
    """testy beda zaaokroglac oczekiwany wynik"""

    def metoda_zwracajaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""

    def metoda_nasluchujaca_testow_bez_kolejnosci(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            self.assertAlmostEqual(wynik, { wynikWywolania }, places={DOKLADNOSCI})\n"""
```
Klasa `prime` ma wiele metod specjalnie wyodrębnionych do nadpisywania.

---

> Strategie nie mogą od siebie zależeć i muszą być niezależne. Można je odpalić w dowolnej konfiguracji.


Ograniczeniem strategii jest to, że nie przyjmuje argumentów innych niż `input` i jest to ustalenie stałe. Jednak, jeśli chcemy utworzyć zadanie, dodając pewne zmienne, możemy skorzystać z **komend**

</details>

<details>
  <summary> 💻 Komendy</summary>

## Komendy

<details>
   <summary> Działanie </summary>
   
W folderze [srt/Komendy](srt/Komendy) znajdują się pliki Python z komendami. Każdy plik zawiera **funkcje** o takiej samej nazwie, które wykonują odpowiednią komendę.

 przykładowa komenda wyglada tak. 
 ```python
# srt/Komendy/hello_name.py
def hello_name(imie):
    print("hello", imie)
```

Takiej komendy możemy użyć w `szablon.py`, importując z `testy` funkcję `komenda` i przekazując w pierwszym argumencie nazwę komendy, a następnie kolejne argumenty.
```python
# ====================================================================================================>
# Zadanie 1
# Wypisac swoje imie
# ====================================================================================================>

def Zadanie_1(): ...

if __name__ == "__main__":
    from testy01 import odpal_testy, komenda

    komenda("hello_name", "kamil")

    # Zadanie_1()
    # odpal_testy()
```
- w pliku `prototyp.py` importujemy z `Develop` funkcje komenda

Wynik odpalenia takiego programu będzie: `hello kamil`

Taka funkcjonalność pozwala w prosty sposób rozszerzać projekt o nowe komendy, umożliwiając ulepszanie testów, na przykład poprzez dodawanie dodatkowych testów lub wariacji poprawnego wyniku, a także wprowadzanie własnych preferencji, takich jak dodatkowe zachowanie po przejsciu testów na szablonie.

</details>

<details  >
  <summary><strong> SPIS KOMEND </strong> </summary>

### Legenda 
- `nazwaKomendy`, `mozliiwy do uzycia skrot`
- w budowie oznacza, że nie chce mi sie jej robić
- lokalna oznacza, że jej działanie nie moze wyjść poza lokalne repozytorium. By uniknąć przypadkow, że ktos nie spodziwal ze mu poleci [najlepsza  domyslna piosenka zwycieska](https://www.youtube.com/watch?v=CpeJiGDVMGo) po napisaniu szablonu
- Zapis `link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo` oznacza ze zmienna `link_do_muzyki` jest opcjonalna i domyslnie uzyjemy `https://www.youtube.com/watch?v=CpeJiGDVMGo`



### Spis 
  - `zmien_testy`
    ```python
    # tworzy na nowo zadanie na bazie szablonu jako prototyp
    komenda("zmien_testy", [funkcje], testy="domyslna", rozwiazanie="domyslna", szablon="domyslna")
     ```

  
  - `dodaj_testy`, `dt` - w budowie
    ```python
    # dodaje  dodatkowe testy 
    komenda("dodaj_testy", funkcja, ilosci_dodatkowych_testow)
     ```
     
  - `dodaj_wariancje`, `dw` - w budowie
    ```python
    # Do istniejacych juz wynikow testow funkcji dodaje kolejne mozliwe warienty na podstawie funkcji przeslanej
    komenda("dodaj_wariancje", funkcja)
     ```
  - `zwycieska_muzyka`,`zm` - w budowie, lokalna
    ```python
    # Do testow danego zadania dodaje muzyka po zaliczeniu testow w szablonie
    # imo must have 
    komenda("zwycieska_muzyka", link_do_muzyki="https://www.youtube.com/watch?v=CpeJiGDVMGo" )
     ```
 - `funkcja_input`,`fi` - w budowie
    ```python
    # szybkie testowanie funkcji na parametrach
    # dopoki nie przerwiesz bedziesz wpisywac input a komenda uzyje jej na funkcji i wypisze output
    komenda("szybka_funkcja", funkcja )
     ```
    
  - `StworzStruktureWDI`
    ```python
    # Nie bedzie wiecej uzywana i nawet nie da sie jej odpalic z poziomu plikow zadań - Takie zabezpieczenie
    # Ale dodaje jako taka ciekawostka oraz na przyszlosci do tworzenia struktur innych zadan
    komenda("StworzStruktureWDI")
     ```

</details>

<details  >
  <summary> Ogólne </summary>
   
### Argumenty
Funkcja `komenda` przyjmuje `"nazwaKomendy"`, `*args` oraz `**kwargs`, co pozwala na przesyłanie dowolnych argumentów zarówno w postaci argumentów pozycyjnych, jak i nazwanych. Aby ułatwić korzystanie, dodatkowo są dodawane dwa argumenty, jeśli komenda ich wymaga. Nie ma obowiązku ich podawania podczas wywołania komendy, są to: 
  - `nr_zadania`
  - `sciezka`
Więc komenda:
 ```python
# srt/Komendy/hello_zadanie.py
def hello_zadanie(nr_zadania, sciezka):# trzeba pamietac by nazwac te argumenty dokladnie tak 
    print("hello", nr_zadania, "from ", sciezka)
```
Może być wywołana w następujący sposób:
 ```python
# prototyp01.py
komenda("hello_zadanie")
```
Wynik takiej komendy to:

`hello 01 from  /Users/user/Desktop/projekty/WDI-RST/Zestaw_1:_Proste_programy_z_pętlami/prototyp01.py`



### skroty 

   Jesli komenda jest czesto używana może miec swój skrót w pliku `_skroty.py`, który tylko importuje komendę i ją odpala.
  ```python
  def hz(nr_zadania, sciezka):
    from hello_zadanie import hello_zadanie

    hello_zadanie(nr_zadania, sciezka)
   ```

### Zasady komend

- Każda ma mieć swój plik i ograniczać sie tylko do niego nawet jakby plik miałby mieć 20 linijek lub 100000 linijek.
- Każda komenda musi być w pełni niezależna i działać poprawnie samodzielnie, ale może wywoływać inne komendy w ramach swoich działań [zgodnie z wzorcem łańcucha zobowiązań]( https://refactoring.guru/pl/design-patterns/chain-of-responsibility)

</details>
</details>
