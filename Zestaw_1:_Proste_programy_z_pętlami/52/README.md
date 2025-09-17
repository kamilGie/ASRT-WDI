<picture>
  <source srcset="../../srt/zbior_zadan/52.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_52.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_52.png" alt="zadanie 52">
</picture>

```python
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(n**0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_prime_factors(n):
    total = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            total += sum_digits(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        total += sum_digits(n)
    return total


def Zadanie_52():
    for num in range(2, 10**6):
        if not is_prime(num):
            s_num = sum_digits(num)
            s_factors = sum_prime_factors(num)
            if s_num == s_factors:
                print(num)
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
