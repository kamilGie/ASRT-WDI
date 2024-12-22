<picture>
  <source srcset="../../srt/zbior_zadan/193.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_193.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_193.png" alt="zadanie 193">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_193(head):
    dummy = Node(0, head)
    current = dummy
    removed_count = 0

    while current.next and current.next.next:
        if current.next.val == current.next.next.val:
            duplicate_val = current.next.val
            while current.next and current.next.val == duplicate_val:
                current.next = current.next.next
                removed_count += 1
        else:
            current = current.next

    return removed_count
```