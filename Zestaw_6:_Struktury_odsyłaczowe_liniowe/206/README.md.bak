<picture>
  <source srcset="../../srt/zbior_zadan/206.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_206.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_206.png" alt="zadanie 206">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_206(p, q):
    head = tail = Node(0)
    while p or q:
        p_val = p.val if p else 0
        q_val = q.val if q else 0

        tail.next = Node(p_val - q_val)
        tail = tail.next

        if p: p = p.next
        if q: q = q.next

    return head.next
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
