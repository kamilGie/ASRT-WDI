<picture>
  <source srcset="../../srt/zbior_zadan/203.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_203.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_203.png" alt="zadanie 203">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_203(p, q):
    dummy_p = Node(0, p)
    dummy_q = Node(0, q)

    prev_p, curr_p = dummy_p, p
    prev_q, curr_q = dummy_q, q

    removed_count = 0
    while curr_p and curr_q:

        if curr_p.val == curr_q.val:  # # Zachowujemy węzły w obu listach
            prev_p, curr_p = curr_p, curr_p.next
            prev_q, curr_q = curr_q, curr_q.next
        elif curr_p.val < curr_q.val:  # Usuń element z listy p
            prev_p.next = curr_p.next
            curr_p = curr_p.next
            removed_count += 1
        else:  # Usuń element z listy q
            prev_q.next = curr_q.next
            curr_q = curr_q.next
            removed_count += 1

    # Usuwanie pozostałych elementów z listy p
    prev_p.next = None
    while curr_p:
        removed_count += 1
        curr_p = curr_p.next

    # Usuwanie pozostałych elementów z listy q
    prev_q.next = None
    while curr_q:
        removed_count += 1
        curr_q = curr_q.next

    return removed_count
```

---
Jeśli repo się podoba, zostaw gwiazdkę 🤝
