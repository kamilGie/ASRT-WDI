<picture>
  <source srcset="../../srt/zbior_zadan/199.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_199.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_199.png" alt="zadanie 199">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_199(head):
    slow = fast = head

    # Szukam punktu przecięcia w cyklu
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    before_cycle = None
    while head != fast:  #  przechodze przez head az zostanie elemetem cyklu
        before_cycle = head
        head = head.next

        fast = fast.next
        while fast != slow:  # przechodze przez cykl
            fast = fast.next
            if fast == head:  # head jest w cyklu zwracam ostatni element
                return before_cycle

    return before_cycle
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
