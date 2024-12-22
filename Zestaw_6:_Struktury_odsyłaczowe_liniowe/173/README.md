<picture>
  <source srcset="../../srt/zbior_zadan/173.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_173.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_173.png" alt="zadanie 173">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def wypis(p):  # z wykladu
    while p:
        print(p.val)
        p = p.next
```