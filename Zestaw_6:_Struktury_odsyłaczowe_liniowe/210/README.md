<picture>
  <source srcset="../../srt/zbior_zadan/210.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_210.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_210.png" alt="zadanie 210">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def iloczyn(z1, z2, z3):
    head = tail = Node(0)  # Wartownik
    while z1 and z2 and z3:
        if z1.val == z2.val == z3.val:  # Istnieje przecięcie wszystkich trzech zbiorów
            tail.next = tail = Node(z1.val)
            z1, z2, z3 = z1.next, z2.next, z3.next
        else:  # Brak przecięcia, najmniejsza wartość zostaje odrzucona
            min_val = min(z1.val, z2.val, z3.val)
            if z1.val == min_val: z1 = z1.next
            if z2.val == min_val: z2 = z2.next
            if z3.val == min_val: z3 = z3.next

    return head.next
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
