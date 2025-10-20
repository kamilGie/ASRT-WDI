<picture>
  <source srcset="../../srt/zbior_zadan/84.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_84.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_84.png" alt="zadanie 84">
</picture>

```python
def multi(T):
    """
    Dla kazdego napisu iterujemy od połowy długości napisu w dół.
    W każdej iteracji tworzę podnapis od 0 do bieżącej pozycji iteracji,
    sprawdzam, czy powtarzając podnapis , otrzymam oryginalny napis.
    """
    res = 0
    for napis in T:
        n = len(napis)
        for i in range(n // 2, 0, -1):
            if n % i == 0 and napis[:i] * (n // i) == napis:
                res = max(res, i)
                break
    return res

```

---
Jeśli repo się podoba, zostaw gwiazdkę 👍
