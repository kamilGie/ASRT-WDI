<picture>
  <source srcset="../../srt/zbior_zadan/153.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_153.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_153.png" alt="zadanie 153">
</picture>

```python
def get_first_digit(num):
    while num > 9:
        num //= 10

    return num


def rek(x, y, board, history=[], been=set()):
    been.add((x, y))

    if x == 7 and y == 7 or x == 0 and y == 7 or x == 0 and y == 0 or x == 7 and y == 0:
        return history

    for i, cord in enumerate(
        (
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y - 1),
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
        )
    ):
        x_n, y_n = cord
        try:
            if not (x_n, y_n) in been:
                cand = get_first_digit(board[y_n][x_n])
                if cand > board[y][x] % 10:
                    return rek(x_n, y_n, board, [*history, i], been)
        except IndexError:
            pass

    return False


def Zadanie_153(x, y, board):
    return rek(x, y, board)



```

