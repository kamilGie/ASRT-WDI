<picture>
  <source srcset="../../srt/zbior_zadan/196.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_196.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_196.png" alt="zadanie 196">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_196(head):
    """Floyd's Cycle Detection"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # Przesunięcie o 1 krok
        fast = fast.next.next  # Przesunięcie o 2 kroki

        if slow == fast:  # Jeśli wskaźniki się spotykają, cykl istnieje
            return True

    return False  # Jeśli fast osiągnie None, brak cyklu
```