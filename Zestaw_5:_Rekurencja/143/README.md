<picture>
  <source srcset="../../srt/zbior_zadan/143.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_143.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_143.png" alt="zadanie 143">
</picture>

```python
def Zadanie_143(matrix):
    def calc_det_recur(matrix, y, il, poss, perm, inv):
        if y >= len(matrix):
            # print("-----\nend, il:", il)
            nonlocal su

            if inv % 2 == 0:
                modif = 1
            else:
                modif = -1

            su += modif * il
            # print("sum", su,"\n-------\n")
            return il

        for curr_i in poss:
            # print("y", y)
            # print("curr_i", curr_i, [i for i in poss if i != curr_i])

            inv_c = inv
            for perm_el in perm:
                if perm_el > curr_i:
                    inv_c += 1

            calc_det_recur(
                matrix,
                y + 1,
                il * matrix[y][curr_i],
                [i for i in poss if i != curr_i],
                perm + [curr_i],
                inv_c,
            )

    su = 0
    poss = [i for i in range(len(matrix))]
    for curr_i in range(len(matrix[0])):
        # print("y", 0)
        # print("curr_i", curr_i, [i for i in poss if i != curr_i])
        calc_det_recur(
            matrix, 1, matrix[0][curr_i], [i for i in poss if i != curr_i], [curr_i], 0
        )

    return su



```

---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
