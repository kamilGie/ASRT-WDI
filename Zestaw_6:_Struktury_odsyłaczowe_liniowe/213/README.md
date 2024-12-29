<picture>
  <source srcset="../../srt/zbior_zadan/213.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_213.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_213.png" alt="zadanie 213">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def NWD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def arithmetic_difference(p):
    value_nwd = 1
    r = p.next.val - p.val

    while p.next:
        value_nwd = NWD(r, (p.next.val - p.val))
        p = p.next
    return value_nwd


def repair(p):
    step = arithmetic_difference(p)

    inserted_count = 0
    while p.next:
        if ( p.val + step != p.next.val):  # jesli krokiem nie dotarlem do nastpnego elemetu musze go dodac
            p.next = Node(p.val + step, p.next)
            inserted_count += 1
        p = p.next
    return inserted_count
```
