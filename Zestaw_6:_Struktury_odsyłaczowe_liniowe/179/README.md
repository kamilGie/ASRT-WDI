<picture>
  <source srcset="../../srt/zbior_zadan/179.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_179.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_179.png" alt="zadanie 179">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_179(head) -> Node:

    heads = []
    tails = []
    for _ in range(10):  # 10 par podlist do przechowywania lancuchow
        sentinel = Node(0)  # węzeł-wartownik
        heads.append(sentinel)
        tails.append(sentinel)

    while head:
        last_digit = abs(head.val) % 10
        # Odcinamy węzeł od reszty listy i dołączamy do odpowiedniej podlisty
        next_node = head.next
        head.next = None
        tails[last_digit].next = head
        tails[last_digit] = head

        head = next_node

    result_tail = result_sentinel = Node(0)  # wartownik
    for i in range(10):
        if heads[i].next is not None:
            result_tail.next = heads[i].next
            result_tail = tails[i]

    return result_sentinel.next
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
