<picture>
  <source srcset="../../srt/zbior_zadan/208.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_208.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_208.png" alt="zadanie 208">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_208(p, k):
    current = p
    counter = {}
    while True:  # zliczam wystapienia kazdej wartosci
        counter[current.val] = counter.get(current.val, 0) + 1
        current = current.next
        if current == p:  # przeszedlem cykl
            break

    removed = False
    prev = Node(None, current)
    while True:  # jesli wartosci wystapila k razy to usuwam z listy
        if counter[current.val] == k:
            prev.next = current.next
            removed = True
        else:  # nie usunalem wiec mozna przesunac prev na current
            prev = current

        current = current.next

        if current == p:  # przeszedlem cykl
            return removed
```

