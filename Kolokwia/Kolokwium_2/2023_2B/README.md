
![black_Zrzut ekranu 2024-12-3 o 23 21 26](https://github.com/user-attachments/assets/a3a00dd6-7a9c-4010-8711-eeff35d3b53c)

```python
from math import isqrt


def a(n):
    res = 1
    if n == 1:
        return res
    for i in range(2, isqrt(n)):
        if n % i == 0:
            res += i
            res += n // i

    if isqrt(n) ** 2 == n:
        res += isqrt(n)
    return res


def b(n):
    a, b = 1, 1
    while a <= n:
        a, b = a + b, a
    return a


def c(n):
    # return n + int(str(n)[::-1])
    reverse = 0
    kopia = n
    while kopia > 0:
        kopia, d = divmod(kopia, 10)
        reverse = reverse * 10 + d
    return n + reverse


def cycle(x, n):
    def rek(l, i):
        if l == x and i < n:
            return n - i  # powrocila
        if i == 0:
            return 0
        # zwracam max dlugosci łańcucha jesli nie bedzie zadnego to max zwróci 0
        return max(rek(a(l), i - 1), rek(b(l), i - 1), rek(c(l), i - 1))

    return rek(x, n)


if __name__ == "__main__":
    from testy2023_2B import odpal_testy, komenda

    # cycle(int(input("Podaj x: ")), int(input("Podaj n: ")))

    odpal_testy()
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
