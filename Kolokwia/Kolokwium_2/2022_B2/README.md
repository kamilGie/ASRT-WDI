
![black_Zrzut ekranu 2024-12-14 o 22 13 21](https://github.com/user-attachments/assets/0d441cc8-2376-4fdd-993e-2cac506e9abb)

```python
def dwa_rozne_czyniki(iloczyn):
    res = 0
    dzielnik = 2
    while iloczyn > 1:
        if iloczyn % dzielnik == 0:
            res += 1
            while iloczyn % dzielnik == 0:
                iloczyn //= dzielnik

            # Jeśli znaleźliśmy 2 dzielniki, sprawdzamy, czy w pełni podzieliły liczbę
            if res == 2:
                return iloczyn == 1

        dzielnik += 1

    return False  # byl jeden dzielnik tylko


def square(T):
    n = len(T)
    for bok in range(1, n - 1):  # Od 2x2 do największego możliwego
        for wiersz in range(n - bok):
            for kolumna in range(n - bok):
                iloczyn = (
                    T[wiersz][kolumna]
                    * T[wiersz][kolumna + bok]
                    * T[wiersz + bok][kolumna]
                    * T[wiersz + bok][kolumna + bok]
                )
                if dwa_rozne_czyniki(iloczyn):
                    return bok + 1
    return 0
```

# Opis Rozwiązania

Jest to, jak zwykle, najprostsze rozwiązanie, choć nie najbardziej optymalne. Oczywistym usprawnieniem byłoby ulepszenie funkcji `dwa_rozne_czyniki`, aby działała szybciej, np. iterując co 2 lub nawet co 6.

Ciekawym ulepszeniem byłaby również zmiana każdego elementu tablicy na krotke jego rozkładu na czynniki pierwsze i wyszukiwanie tych kwadratów, które mają dokładnie 2 lub 1 czynnik, i  zbior 4 krotek zbudowanych przez boki musi zawierac 2 elementy


