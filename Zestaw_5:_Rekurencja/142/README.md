<picture>
  <source srcset="../../srt/zbior_zadan/142.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_142.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_142.png" alt="zadanie 142">
</picture>

```python
def waga2(li, n, res=[], p=0):
    if n == 0:
        return res
    if p == len(li):
        return False
    return (
        waga2(li, n - li[p], res + [li[p]], p + 1)
        or waga2(li, n, res, p + 1)
        or waga2(li, n + li[p], res + [-1 * li[p]], p + 1)
    )


def Zadanie_142(T, okreslona_masa):
    return waga2(T, okreslona_masa)



```

