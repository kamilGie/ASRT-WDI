<picture>
  <source srcset="../../srt/zbior_zadan/195.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_195.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_195.png" alt="zadanie 195">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_195(current):
    head = current = Node(None, current)  # wartownik
    bestlen = 0  # najdluzszy podciag
    start = end = None  # pierwszy i ostatni element lancycha najdluzszego podciagu

    while current and current.next:
        prev, current = current, current.next

        cnt = 1
        while current.next and current.val < current.next.val:  # rosnie
            cnt += 1
            current = current.next

        if cnt == bestlen:  # podciag ma byc unikalny
            start = end = None  # usuwam znaleziony podciag
        elif cnt > bestlen:
            bestlen = cnt
            start, end = prev, current.next

    if start:  # istnieje podciag
        start.next = end

    return head.next  # pozbywamy się wartownika
```

---
Jeśli repo się podoba, zostaw gwiazdkę ✨
