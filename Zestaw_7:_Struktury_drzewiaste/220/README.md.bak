<picture>
  <source srcset="../../srt/zbior_zadan/220.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_220.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_220.png" alt="zadanie 220">
</picture>

```python
# to samo co 219
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def Zadanie_220(p, val=1):
    if not p:  # Pusty węzeł
        return val

    if p.right and p.left:  # Węzeł ma dwóch synów
        return max(Zadanie_219(p.left), Zadanie_219(p.right))

    if p.right:  # Węzeł ma tylko prawego syna
        return Zadanie_219(p.right, val + 1)

    if p.left:  # Węzeł ma tylko lewego syna
        return Zadanie_219(p.left, val + 1)

    return val  # Węzeł liścia
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
