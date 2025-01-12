<picture>
  <source srcset="../../srt/zbior_zadan/219.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_219.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_219.png" alt="zadanie 219">
</picture>

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def Zadanie_219(p, val=1):
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
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
