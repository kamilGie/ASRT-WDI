<picture>
  <source srcset="../../srt/zbior_zadan/181.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_181.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_181.png" alt="zadanie 181">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_last(p) -> Node:
    head = p
    while p.next.next:
        p = p.next
    p.next = None
    return head
```