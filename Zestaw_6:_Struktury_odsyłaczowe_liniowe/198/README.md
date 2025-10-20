<picture>
  <source srcset="../../srt/zbior_zadan/198.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_198.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_198.png" alt="zadanie 198">
</picture>

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_198(head):
    slow = fast = head

    # Szukam punktu przecięcia w cyklu
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    before_cycle = 0
    while head != fast:  #  przechodze przez head az zostanie elemetem cyklu
        head = head.next
        before_cycle += 1

        fast = fast.next
        while fast != slow:  # przechodze przez cykl
            if fast == head:  # head jest w cyklu zwracam dlugosci
                return before_cycle
            fast = fast.next

    return before_cycle
```

