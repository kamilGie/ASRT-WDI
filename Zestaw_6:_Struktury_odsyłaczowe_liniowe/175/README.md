<picture>
  <source srcset="../../srt/zbior_zadan/175.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_175.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_175.png" alt="zadanie 175">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def contains(head, value) -> bool:
    while head:
        if head.val == value:
            return True
        head = head.next
    return False


def insert(head, value) -> Node:
    return Node(value, head) if not contains(head, value) else head


def delete_node(head, value) -> Node:
    if head.val == value:  # wartość jest pierwsza
        return head.next

    prev, current = Node(0, head), head  # prev na wartowniku
    while current:
        if current.val == value:
            prev.next = current.next
            return head  # znaleziono usunieto
        prev = current
        current = current.next

    return head  # nie bylo value
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
