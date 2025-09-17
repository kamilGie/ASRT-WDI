<picture>
  <source srcset="../../srt/zbior_zadan/107.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_107.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_107.png" alt="zadanie 107">
</picture>

```python
def same_cyfry_pierwsze(n):
    k = n
    primes = {2, 3, 5, 7}
    while k > 0:
        if (k % 10) not in primes:
            return False
        k = k // 10
    # end while
    return True


def Zadanie_107(tab):
    n = len(tab)

    for y in range(n):
        flag = False
        for x in range(n):

            if same_cyfry_pierwsze(tab[y][x]):
                flag = True
                break
            # end if

        # end for 2
        if not flag:
            return False

    # end for 1
    return True



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
