<picture>
  <source srcset="../../srt/zbior_zadan/187.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_187.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_187.png" alt="zadanie 187">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_187(head):
    current = head
    while current.next:
        if current.next.val < current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
