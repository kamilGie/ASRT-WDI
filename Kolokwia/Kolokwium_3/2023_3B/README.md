<picture>
  <source srcset="../../srt/zbior_zadan/2023_3B.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_2023_3B.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_2023_3B.png" alt="zadanie 2023_3B">
</picture>

```python
# Autor rozwiązania Piotr Polański
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def check(s):  # 0 - rosnący, 1 - bez porządku, 2 - malejący
    l = len(s)
    if l == 1 or s[0] == s[1]:
        return 1  # edge cases: napis 1-literowy lub niemonotoniczny na początku
    lock = True if ord(s[0]) < ord(s[1]) else False
    for i in range(l - 1):
        if lock and s[i + 1] <= s[i]:
            return 1
        if not lock and s[i + 1] >= s[i]:
            return 1
    # dotarliśmy do końca bez zmiany monotoniczności
    if lock:
        return 0  # rosnący
    return 2  # malejący


def make_order(p) -> Node:
    seg1 = Node(None)
    seg1.next = Node(None)
    seg2 = seg1.next
    seg2.val = ""
    seg2.next = Node(None)
    seg3 = seg2.next
    seg3.val = ""  # przygotowana odpowiednio lista - wskaźniki na wszystkie 3 elementy, lista w formie: seg1 -> seg2 -> seg3 -> None
    while p != None:
        variant = check(p.val)
        if (
            variant == 0
        ):  # wskazujemy węzeł początkowy bloku, do którego dopinamy węzeł wskazany przez p
            q = seg1
        elif variant == 1:
            q = seg2
        else:
            q = seg3
        tmp = q.next
        q.next = p
        p.next, p = tmp, p.next  # ta zmiana musi nastąpić równocześnie
    return seg1.next  # pomijamy 1szy pusty węzeł - naszego "wartownika"
```
