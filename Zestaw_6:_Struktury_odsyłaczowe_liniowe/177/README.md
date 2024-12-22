<picture>
  <source srcset="../../srt/zbior_zadan/177.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_177.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_177.png" alt="zadanie 177">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def iteration(p, q):
    head = tail = Node(0)  # wartownik
    while p and q:
        if p.val < q.val:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    # Dodanie pozostałych elementów
    tail.next = p if p else q
    return head.next  # bez wartownika


def recursive(p, q):
    if not p:
        return q
    if not q:
        return p

    if p.val < q.val:
        p.next = recursive(p.next, q)
        return p
    else:
        q.next = recursive(p, q.next)
        return q
```