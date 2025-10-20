<picture>
  <source srcset="../../srt/zbior_zadan/136.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_136.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_136.png" alt="zadanie 136">
</picture>

```python
def if_jump_possible(T, y, x):
    if 0 <= y < len(T):
        if 0 <= x < len(T):
            return True
    # end if
    return False


def Zadanie_136(n):
    T = [[0 for _ in range(n)] for _ in range(n)]

    def rek(y, x, i):
        T[y][x] = i
        if i == len(T) ** 2:
            return True
        else:
            jumps = [
                (-1, -2),
                (-2, -1),
                (-2, 1),
                (-1, 2),
                (1, 2),
                (2, 1),
                (2, -1),
                (1, -2),
            ]
            for jump in jumps:
                if (
                    if_jump_possible(T, y + jump[0], x + jump[1])
                    and T[y + jump[0]][x + jump[1]] == 0
                ):
                    if rek(y + jump[0], x + jump[1], i + 1):
                        return True
            # end for
            T[y][x] = 0
            return False

    # end def rek

    rek(0, 0, 1)
    return T

```


