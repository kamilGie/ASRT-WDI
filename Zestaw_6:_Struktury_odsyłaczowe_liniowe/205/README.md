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
        next_node = head.next
        head.next = None # odlaczenie
        if head.val > 0 and head.val % 2 == 0:  # przypisanie p
            p.next = head
            p = p.next
        elif head.val < 0 and head.val % 2 == 1:  # przypisanie q
            q.next = head
            q = q.next
        else:  # usuwanie z pamieci
            deleted_cnt += 1

        head = next_node

    return deleted_cnt
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
