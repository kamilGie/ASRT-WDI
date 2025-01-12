<picture>
  <source srcset="../../srt/zbior_zadan/207.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_207.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_207.png" alt="zadanie 207">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_207(head, new_string) -> bool:
    current = head
    while True:
        if current.val[-1] < new_string[0] and new_string[-1] < current.next.val[0]:  # czy nowy napis pasuje z 2 stron
            new_node = Node(new_string, current.next)
            current.next = new_node
            return True

        current = current.next

        if current == head:  # przeszlismy cykl
            return False
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
