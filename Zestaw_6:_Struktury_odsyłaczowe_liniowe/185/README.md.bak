<picture>
  <source srcset="../../srt/zbior_zadan/185.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_185.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_185.png" alt="zadanie 185">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_185(p, key) -> Node:
    head = prev = Node(key, p)  # wartownik z key
    while p:
        if p.val == key:  # znaleziono
            prev.next = p.next  # usuwam
            return head.next  # bez wartownika
        prev, p = p, p.next

    return head  # nie znaleziono zwracam z wartownikiem
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
