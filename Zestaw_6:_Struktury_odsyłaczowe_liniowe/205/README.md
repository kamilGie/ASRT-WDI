<picture>
  <source srcset="../../srt/zbior_zadan/205.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_205.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_205.png" alt="zadanie 205">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_205(head, p, q) -> int:
    deleted_cnt = 0
    while head:
        if head.val > 0 and head.val % 2 == 0:
            p = Node(head.val, p)
        elif head.val < 0 and head.val % 2 == 1:
            q = Node(head.val, q)
        else:
            deleted_cnt += 1

        head = head.next

    return deleted_cnt
```