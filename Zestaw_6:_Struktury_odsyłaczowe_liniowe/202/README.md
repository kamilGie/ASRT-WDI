<picture>
  <source srcset="../../srt/zbior_zadan/202.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_202.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_202.png" alt="zadanie 202">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_202(p, q):
    head_p, head_q = Node(None, p), Node(None, q)  # Wskaźniki z wartonikami

    prev_q, current_q = head_q, q
    cnt = 0  # Licznik usuniętych elementów
    while current_q:
        prev_p = head_p
        current_p = head_p.next

        # Zwiekszam current_p aż nie bedzię mniejszę od current_q bo q jest posortowane
        while current_p and current_p.val < current_q.val:
            prev_p = current_p
            current_p = current_p.next

        if current_p and current_p.val == current_q.val:  # wartość jest w obu listach
            prev_p.next = current_p.next  # usuwam z dwoch list
            prev_q.next = current_q.next
            cnt += 2
        else:  # prev_q sie zmienia bo nie usunelismy current_q
            prev_q = current_q

        current_q = current_q.next

    return cnt
```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
