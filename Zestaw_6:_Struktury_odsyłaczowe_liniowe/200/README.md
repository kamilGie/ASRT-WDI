<picture>
  <source srcset="../../srt/zbior_zadan/200.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_200.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_200.png" alt="zadanie 200">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def contain(p, element):
    while p:
        if p == element:
            return True
        p = p.next
    return False


def Zadanie_200(p, q):
    """Aby sie zawieral jeden w drugim to jeden musi wskazywac na poczatek pierwszego"""
    return contain(p, q) or contain(q, p)
```