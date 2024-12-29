# ====================================================================================================>
# Zadanie 5, 20 stycznia 2022
# Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
# dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
# sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
# dokładnie z 3 liczbami czynnikowo-podobnymi.
# ====================================================================================================>


# https://github.com/pawlowiczf/WDI-2023/blob/main/WDI%20zestaw%207/Kolokwia/3_2022.py
def czynnikowo_podobne(a,b):
    n = 2
    counter = 0

    while a > 1:
        flag = False

        while a % n == 0:
            a = a // n
            flag = True 

        if flag and b % n == 0:
            counter += 1 
        #end if
        n += 1 
    #end while
    return counter == 1
#end def 


def three(T):

    result = 0

    for y in range(1, len(T) - 1):
        for x in range(1, len(T) - 1):
            tmp = 0

            if czynnikowo_podobne( T[y][x], T[y-1][x-1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y-1][x+1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y+1][x-1] ): tmp += 1
            if czynnikowo_podobne( T[y][x], T[y+1][x+1] ): tmp += 1

            if tmp == 3: result += 1
        #end for 2
    #end for 1
    return result 


