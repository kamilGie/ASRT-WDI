![black_Zrzut ekranu 2024-12-6 o 11 17 57](https://github.com/user-attachments/assets/0f7f8dc4-7234-4497-b068-a64a40a563d0)

```python

from math import inf


def maximize_moves(x, y, forbidden, N, prev_move=None):
    """Zwroci maxymalna ilosci ruchow do konca lub -inf jak sie nie da dotrzec do konca"""
    # Sprawdzam czy jestem na legalnej pozycji
    if (x, y) in forbidden:  # Zajęte
        return -inf
    if not (0 <= x < N and 0 <= y < N):  # za granicami szachownicy
        return -inf

    if (x, y) == (N - 1, N - 1):
        return 0  # Cel osiągnięty

    res = -inf
    # Zeby krol wrocim tam gdzie byl musialby po ruchu w gore pojsc w dol lub na odwrot
    if prev_move != "up":  # czy moge w dol
        res = max(res, maximize_moves(x + 1, y, forbidden, N, "down") + 1)
    if prev_move != "down":  # czy moge w gore
        res = max(res, maximize_moves(x - 1, y, forbidden, N, "up") + 1)
    res = max(res, (maximize_moves(x, y + 1, forbidden, N)) + 1)  # W prawo

    # Zwracam maxymalna liczbe ruchow najlepszego ruchu
    return res


def king(N, L):
    result = maximize_moves(0, 0, L, N)
    return None if result == -inf else result
```



    
# Opis Rozwiązania
**interaktywny Algorytm** klikni aby uzyć:

[![Kliknij tutaj](https://github.com/user-attachments/assets/e3804eb4-a103-40eb-8f67-a0b01250e2f3)](https://gieras.pl/asrt/wdi/2022a3)


Ważne jest zauważenie że król cofnie się tylko wtedy, gdy po ruchu w górę wykona ruch w dół i odwrotnie.






---
Jeśli Ci się przydało, miło będzie za gwiazdkę 🤝
