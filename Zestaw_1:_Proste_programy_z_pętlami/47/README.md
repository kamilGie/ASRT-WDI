<picture>
  <source srcset="../../srt/zbior_zadan/47.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_47.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_47.png" alt="zadanie 47">
</picture>

```python
def Zadanie_47(S):
    for X in range(1, S + 1):
        suma = 0
        kopia = X
        while kopia > 0:
            suma += kopia
            kopia //= 10
        if suma == S:
            return X
    return -1
```