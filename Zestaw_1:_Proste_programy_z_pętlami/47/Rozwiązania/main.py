# ====================================================================================================>
# Zadanie 47
# Wybieramy dodatnią liczbę całkowitą X. Z liczby X wykreślamy ostatnią cyfrę. Postępu-
# jemy tak,aż usuniemy wszystkie cyfry liczby X. Następnie sumujemy wszystkie powstałew w ten sposób liczby,
# włączając liczbę X. Naprzykład, jeżeli wybraliśmy X=1234 to w kolejnych krokach otrzymamy odpowiednio
# liczby 1234, 123, 12, 1. Ich suma to 1370. Mamy daną liczbę całkowitą dodatnią S. Proszę napisać program,
# który znajduje liczbę X taką, że powyżej opisana procedura daje sumę S. Można pokazać, że dla dowolnej
# dodatniej liczby S istnieje co najwyżej jedna taka wartość X. Jeżeli nie ma takiego X program powinien
# wypisać -1.
# ====================================================================================================>


def Zadanie_47(S):
    for X in range(1, S + 1):
        suma = 0
        kopia = X
        while kopia > 0:
            suma += kopia
            kopia //= 10
        if suma == S:
            return X
    return -1


