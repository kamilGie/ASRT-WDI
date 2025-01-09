# ====================================================================================================>
# Zadanie 64
# Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakoń-
# czonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
# ====================================================================================================>


def Zadanie_64():
    largest = [0] * 10

    while True:
        x = int(input())
        if x == 0: break

        for i in range(10):
            if x > largest[i]:
                j = 9
                while j > i:
                    largest[j] = largest[j - 1]
                    j -= 1
                largest[i] = x
                break

    print(largest[9])


