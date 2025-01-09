<picture>
  <source srcset="../../srt/zbior_zadan/78.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_78.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_78.png" alt="zadanie 78">
</picture>

```python
def Zadanie_78(t):
    n = len(t)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + t[i]

    best = 0
    for i in range(n):
        for j in range(i, n):
            if j > i and t[j] <= t[j - 1]:
                break
            sub_sum = s[j + 1] - s[i]
            idx_sum = (j * (j + 1)) // 2 - (i * (i - 1)) // 2
            if sub_sum == idx_sum:
                best = max(best, j - i + 1)
    return best
```