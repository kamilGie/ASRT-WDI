# ====================================================================================================>
# Zadanie 37
# Mamy dane dwa ciągi A,B o następujących zależnościach:
# A: a0=0,  a1=1,  an=a(n-1)−b*a(n-2)
# B: b0=2,  bn=b(n-1)+2∗a(n-1)
# Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
# kolejnymi wyrazami ciągu A (tj. a1 ,a2 ,a3 , ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu
# B (tj. b0 ,b1 ,b2 , ...).
# ====================================================================================================>


def Zadanie_37():
    a0, a1 = 0, 1
    b0 = 2
    b1 = b0 + 2 * a0

    if int(input()) == a0:
        print("b", b0)
    else:
        exit()

    while int(input()) == a1:
        print("b", b1)

        a0, a1 = a1, a1 - b1 * a0
        b0, b1 = b1, b1 + 2 * a0


