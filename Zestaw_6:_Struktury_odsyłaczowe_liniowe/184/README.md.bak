<picture>
  <source srcset="../../srt/zbior_zadan/184.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_184.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_184.png" alt="zadanie 184">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_184(p, q):
    def reverse_list(node):
        "Funkcja pomocnicza do odwracania listy"
        prev, current = None, node
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        return prev

    p, q = reverse_list(p), reverse_list(q)
    current = head = Node(0)  # pomocnicze Node
    carry = 0

    while p or q or carry:
        p_val = p.val if p else 0
        q_val = q.val if q else 0

        total = p_val + q_val + carry
        carry, value = divmod(total, 10)

        current.next = Node(value)  # tworze nowy lancuch z wartoscia
        current = current.next

        if p:
            p = p.next
        if q:
            q = q.next

    return reverse_list(head.next)  # usuwam pomocniczy node
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
