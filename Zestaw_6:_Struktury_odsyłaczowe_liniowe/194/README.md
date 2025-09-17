<picture>
  <source srcset="../../srt/zbior_zadan/194.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_194.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_194.png" alt="zadanie 194">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_194(head):
    p = head
    while p:
        prev, current = p, p.next

        while current:
            if current.val[0] <= p.val[1] and p.val[0] <= current.val[1]:  # przecinja sie zbiory
                p.val[0] = min(p.val[0], current.val[0])  # laczymy zbiory
                p.val[1] = max(p.val[1], current.val[1])
                prev.next = current.next  # Pominięcie węzła

            prev, current = current, current.next

        p = p.next

    return head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
