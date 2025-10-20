<picture>
  <source srcset="../../srt/zbior_zadan/200.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_200.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_200.png" alt="zadanie 200">
</picture>

```python
# Zawieranie wartościowe
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def are_subsequences_equal(node1, sublist):
    while node1 and sublist: # Póki jedno sie nie skończy
        if node1.val != sublist.val: # Różnią się
            return False
        node1 = node1.next
        sublist = sublist.next
    return sublist is None  # Jeśli sublist się skończy, to była podlistą.


def contains_sublist(p, sublist):
    while p:
        if are_subsequences_equal(p, sublist):  # Czy sublist zaczyna się w p
            return True
        p = p.next
    return False


def Zadanie_200(p, q):
    return contains_sublist(p, q) or contains_sublist(q, p)
```


---
Twoja gwiazdka pomaga w rozwoju repozytorium 👍
