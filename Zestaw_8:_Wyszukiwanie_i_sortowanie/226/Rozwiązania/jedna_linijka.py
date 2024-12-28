def Zadanie_226(T):
    T.sort(key=lambda k: 0 if {k[k.index(2) - 1], k[(k.index(2) + 1) % 4]} == {1, 3} else 2 if {k[k.index(2) - 1], k[(k.index(2) + 1) % 4]} == {3, 4} else 1)
