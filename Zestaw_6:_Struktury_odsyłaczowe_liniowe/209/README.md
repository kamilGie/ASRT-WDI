<picture>
  <source srcset="../../srt/zbior_zadan/209.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_209.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_209.png" alt="zadanie 209">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_repairable(head, step):
    """ sprawdza czy krokiem dostane sie do kazdego z lancuchow """
    current_val = head.val
    while head.next:
        current_val += step
        if current_val == head.next.val: # dostalem sie do lancucha ide do nastpnego
            head = head.next
        elif (step > 0 and current_val > head.next.val) or ( step < 0 and current_val < head.next.val): # przeszedlem
            return False
    return True


def repair(p):
    original_step = p.next.val - p.val

    divisor = 1 # ile kroków z pierwszego do drugiego elementu
    step = original_step
    while not is_repairable(p, step):  # szukam kroku który da ciag
        divisor += 1
        step = original_step / divisor

    inserted_count = 0
    while p.next:
        if p.val + step != p.next.val: # jesli krokiem nie dotarlem do nastpnego elemetu musze go dodac
            p.next = Node(p.val + step, p.next)
            inserted_count += 1
        p = p.next
    return inserted_count
```
