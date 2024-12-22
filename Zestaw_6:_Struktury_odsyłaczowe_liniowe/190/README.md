<picture>
  <source srcset="../../srt/zbior_zadan/190.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_190.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_190.png" alt="zadanie 190">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_even_fives_in_octal(value):
    is_even = True
    while value > 0:
        if value % 8 == 5:
            is_even = not is_even  # odwraca wartosci logiczna
        value //= 8
    return is_even


def Zadanie_190(p):
    head = prev = Node(0, p)  # Wartownik

    while prev.next:
        current = prev.next
        if is_even_fives_in_octal(current.val) and current != head.next:  # ignoruje 1 element bo jest z przodu
            prev.next = current.next
            current.next = head.next
            head.next = current
        else:
            prev = current

    return head.next  # pomijamy wartownika
```