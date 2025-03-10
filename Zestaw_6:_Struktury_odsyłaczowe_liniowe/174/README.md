<picture>
  <source srcset="../../srt/zbior_zadan/174.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_174.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_174.png" alt="zadanie 174">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def policz(p: Node | None) -> int:
    count = 0
    while p is not None:
        count += 1
        p = p.next
    return count
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
