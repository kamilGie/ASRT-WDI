<picture>
  <source srcset="../../srt/zbior_zadan/180.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_180.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_180.png" alt="zadanie 180">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def push_back(p, val) -> Node:
    head = p
    while p.next:
        p = p.next
    p.next = Node(val)
    return head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
