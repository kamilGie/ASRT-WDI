<picture>
  <source srcset="../../srt/zbior_zadan/186.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_186.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_186.png" alt="zadanie 186">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_186(head, word) -> bool:
    current = Node("", head)  # Węzeł pomocniczy na początku listy

    while current.next and current.next.val < word:
        current = current.next

    if current.next and current.next.val == word:
        return False  # istnieje w zbiorze

    # Wstawianie nowego węzła z napisem
    current.next = Node(word, current.next)
    return True
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
