<picture>
  <source srcset="../../srt/zbior_zadan/20.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_20.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_20.png" alt="zadanie 20">
</picture>

```python
def An1(A):
    return (A % 2) * (3 * A + 1) + (1 - A % 2) * A / 2


def Zadanie_20(N):
    eps = 1e-10

    # Przechodzimy przez kolejne liczby początkowe
    for i in range(2, 10000 + 1):  # Zakładamy przedział od 2 do 10000
        A = i
        cnt = 0

        # Obliczamy liczbę kroków do osiągnięcia wartości 1
        while abs(A - 1) > eps:
            A = An1(A)
            cnt += 1

        # Jeśli liczba kroków równa się N, zwracamy wyraz początkowy
        if cnt == N:
            return i

    # Jeśli nie znaleziono wyrazu początkowego, zwracamy informację
    return None
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
