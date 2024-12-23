<picture>
  <source srcset="../../srt/zbior_zadan/204.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_204.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_204.png" alt="zadanie 204">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


from math import inf


def Zadanie_204(p, q):
    # Wskaźnik z wartonikiem -inf by kazde elemetny q mniejsze od pierwszego p mogly sie wpisac po -inf
    head_p = Node(-inf, p)
    current_q = q

    while current_q:
        prev_p, current_p = head_p, head_p.next

        # Zwiekszam current_p aż nie bedzię wieksze od current_q bo p jest posortowane
        while current_p and current_p.val <= current_q.val:
            prev_p = current_p
            current_p = current_p.next

        if prev_p.val < current_q.val:  # moge wpisac
            prev_p.next = Node(current_q.val, prev_p.next)

        current_q = current_q.next

    return head_p.next
```
