<picture>
  <source srcset="../../srt/zbior_zadan/183.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_183.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_183.png" alt="zadanie 183">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_183(p):
    def reverse_list(node):
        "Funkcja pomocnicza do odwracania listy"
        prev, current = None, node
        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node
        return prev

    current = head = reverse_list(p)
    carry = 1

    while current and carry:
        # sprawdzam czy przeszlo dzielac przez 10
        carry, current.val = divmod(current.val + carry, 10)
        current = current.next

    # przywrócenie oryginalny porządku
    head = reverse_list(head)
    return head if not carry else Node(1, head)  # potrzeba zwieksznia cyfr liczby
```
# Opis Rozwiązania 

https://github.com/user-attachments/assets/97d538a0-9044-4ce3-9f33-dcbcfe88aea9



---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
