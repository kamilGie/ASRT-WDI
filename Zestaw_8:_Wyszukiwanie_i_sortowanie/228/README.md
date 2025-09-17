<picture>
  <source srcset="../../srt/zbior_zadan/228.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_228.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_228.png" alt="zadanie 228">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


from math import inf


def remove_max(head):
    sentinel = Node(-inf, head)  # wartownik
    max_prev = current_prev = sentinel

    while current_prev.next:
        if current_prev.next.val > max_prev.next.val:
            max_prev = current_prev
        current_prev = current_prev.next

    # Usuwanie węzła z maksymalną wartością
    max_node = max_prev.next
    max_prev.next = max_node.next
    max_value = max_node.val

    return sentinel.next, max_value


def selection_sort(head) -> Node:
    sorted_head = None

    while head:
        head, max_value = remove_max(head)
        sorted_head = Node(max_value, sorted_head)

    return sorted_head
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
