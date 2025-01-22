<picture>
  <source srcset="../../srt/zbior_zadan/2023_5A.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2023_5A.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2023_5A.png" alt="zadanie 2023_5A">
</picture>

```python
def distinct_octal(x):
    digits_appear = [False] * 8
    while x:
        x, d = divmod(x, 8)
        if digits_appear[d]:  # Jeśli cyfra już wystąpiła
            return False
        digits_appear[d] = True  # Zaznacz cyfrę jako używaną
    return True


def square(T):
    n = len(T)
    B = [[distinct_octal(T[i][j]) for j in range(n)] for i in range(n)]  # Tablica booli
    D = [[0] * n for _ in range(n)]  # Tablica przechowująca rozmiary kwadratów
    res = 0

    for i in range(n):
        for j in range(n):
            if B[i][j]:  # Jeśli liczba spełnia warunek
                if i == 0 or j == 0:
                    D[i][j] = 1  # Na brzegu wszystkie wartości mają bok 1
                else:
                    # Minimalna z trzech sąsiednich wartości plus 1
                    D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
                res = max(res, D[i][j])  # Aktualizacja maksymalnego boku
    return res
```

# Opis Rozwiązania

https://www.youtube.com/watch?v=nZAyRZC8tko
