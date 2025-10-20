<picture>
  <source srcset="../../srt/zbior_zadan/189.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_189.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_189.png" alt="zadanie 189">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def czy_usunac(val):
    cnt = [0, 0, 0]
    while val:
        cnt[val % 3] += 1
        val //= 3
    return cnt[1] > cnt[2]


def Zadanie_189(head):
    head = p = Node(0, head)  # pomocniczy poczatek
    while p.next:
        if czy_usunac(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    return head.next  # usuwanie poczatku
```

