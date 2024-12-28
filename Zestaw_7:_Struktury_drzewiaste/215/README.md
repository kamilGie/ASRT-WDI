<picture>
  <source srcset="../../srt/zbior_zadan/215.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_215.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_215.png" alt="zadanie 215">
</picture>

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def usun_wszystkie_wezly(p):
    if not p:
        return None
    p.left = usun_wszystkie_wezly(p.left)
    p.right = usun_wszystkie_wezly(p.right)
    return None  # Usuwam bieżący węzeł


def usun_wezly_powyzej_poziomu(p, n) -> Node:
    if not p:
        return None
    p.left = usun_wezly_powyzej_poziomu(p.left, n - 1)
    p.right = usun_wezly_powyzej_poziomu(p.right, n - 1)
    return None if n <= 0 else p  # jak powyzej n to usuwam


def usun_liscie(p) -> Node:
    if not p:
        return None
    if not p.left and not p.right:  # Czy liści
        return None
    p.left = usun_liscie(p.left)
    p.right = usun_liscie(p.right)
    return p
```