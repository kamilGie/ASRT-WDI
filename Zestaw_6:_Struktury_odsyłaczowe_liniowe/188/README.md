<picture>
  <source srcset="../../srt/zbior_zadan/188.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_188.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_188.png" alt="zadanie 188">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_188(head):
    while head.next and (head.val == 0 or head.next.val % head.val == 0):
        head = head.next
    if head.next:
        head.next = Zadanie_188(head.next)
    return head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
