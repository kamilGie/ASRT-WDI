<picture>
  <source srcset="../../srt/zbior_zadan/14.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_14.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_14.png" alt="zadanie 14">
</picture>

```python
def dzielniki(n):
    i = 2
    suma = 1
    while i * i < n:
        if n % i == 0:
            suma += i + (n // i)
        i += 1

    if i * i == n:
        suma += i

    return suma


def Zadanie_14():
    for num in range(2, 1000001):
        sum_divisors_num = dzielniki(num)

        if dzielniki(sum_divisors_num) == num and num > sum_divisors_num:
            print(num, sum_divisors_num)



```

---
Jeśli kod był pomocny, zostaw gwiazdkę ✨
