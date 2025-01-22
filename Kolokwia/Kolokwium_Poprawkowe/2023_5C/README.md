<picture>
  <source srcset="../../srt/zbior_zadan/2023_5C.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2023_5C.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2023_5C.png" alt="zadanie 2023_5C">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


from math import isqrt


def is_prime(val):
    if val < 2:
        return False
    if val < 4:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    for i in range(5, isqrt(val) + 1, 6):
        if val % i == 0 or val % (i + 2) == 0:
            return False
    return True


def odczepic(val):
    for i in range(2, isqrt(val) + 1):
        # jesli liczba jest pierwsza oraz wartosci jest podzielna przez jej kwadrat
        if is_prime(i) and val % (i * i) == 0:
            return val / (i * i) > 1 # sprawdzam czy jest wielokrotny wiecej niz 2 
    return False


def divide(p):
    q_head = q_tail = Node(0) # do odczepiania lista
    p_head = Node(0, p) # dodaje wartownika

    prev, curr = p_head, p
    while curr:
        if odczepic(curr.val):
            prev.next = curr.next
            q_tail.next, q_tail = curr, curr
        else:
            prev = curr
        curr = curr.next

    q_tail.next = None # aby nie wskazywal na nic ostatni
    return p_head.next, q_head.next # bez wartownikow
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
- [Rosnotes-WDI](https://github.com/kamilGie/Rosnotes-WDI) - Premiera wkrótce
- [ASRT-ASD](https://github.com/kamilGie/Rosnotes-Dyskretna) - Premiera wkrótce
