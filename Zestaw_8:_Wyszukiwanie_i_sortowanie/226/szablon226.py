# ====================================================================================================>
# Zadanie 226
# Dany jest ciąg kwadratowych klocków. Każdy klocek ma kształt kwadratu pokolorowa-
# nego 4 kolorami. Klocki w ciągu mogą być dowolnie ustawione (przekręcone), a nawet odwrócone. Proszę
# napisać funkcję porządkującą klocki, tak aby identyczne klocki występowały obok siebie. Ciąg klocków jest
# reprezentowany jako tablica krotek, np. T = [(2,3,1,4), (3,2,4,1), (1,2,3,4), ...]
# ====================================================================================================>
# nic nie zwracać edytowac tablice in place

def Zadanie_226(T)->None: ...


if __name__ == "__main__":
    from testy226 import odpal_testy

    Zadanie_226(list(input("Podaj T: ")))

    # odpal_testy()
