<picture>
  <source srcset="../../srt/zbior_zadan/182.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_182.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_182.png" alt="zadanie 182">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_182(p) -> Node:
    head = p
    while p and p.next:
        p.next = p.next.next
        p = p.next
    return head
```

---
Twoja gwiazdka pomaga w rozwoju repozytorium 🤝
