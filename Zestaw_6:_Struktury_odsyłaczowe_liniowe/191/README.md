<picture>
  <source srcset="../../srt/zbior_zadan/191.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_191.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_191.png" alt="zadanie 191">
</picture>

```python
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        if next:
            next.prev = self
        if prev:
            prev.next = self


def even_ones_in_bin(val):
    even = True
    while val:
        if val % 2 == 1:
            even = not even
        val //= 2
    return even


def Zadanie_191(head):
    dummy = Node(0, head, None)  # wartownik
    current = head

    while current:
        if not even_ones_in_bin(current.val):
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        current = current.next

    return dummy.next
```
