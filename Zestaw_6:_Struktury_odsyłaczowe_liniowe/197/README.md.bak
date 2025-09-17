<picture>
  <source srcset="../../srt/zbior_zadan/197.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_197.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_197.png" alt="zadanie 197">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def cycle_length(head):
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # Cykl wykryty
            length = 1
            current = slow.next
            while current != slow:  # licze po ilu przejsciach `slow` dotrze do `fast`
                current = current.next
                length += 1
            return length
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
