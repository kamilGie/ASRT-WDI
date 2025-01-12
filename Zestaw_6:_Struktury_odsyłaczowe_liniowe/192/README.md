<picture>
  <source srcset="../../srt/zbior_zadan/192.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_192.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_192.png" alt="zadanie 192">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def delete_key(p, key):
    dummy = Node(0, p)
    current = dummy
    while current.next:
        if current.next.val == key:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


def Zadanie_192(head):
    """Dla kazdej wartosci przechodze w przod i usuwam jej wystapienia"""
    current = head
    while current:
        current.next = delete_key(current.next, current.val)
        current = current.next

    return head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
