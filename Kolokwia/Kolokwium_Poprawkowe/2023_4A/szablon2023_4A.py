# ====================================================================================================>
# Zadanie 4A, 2024-01-26
# Napis nazywamy wielokrotnym, jeżeli powstał przez 𝑛-krotne (𝑛 > 1) powtórzenie innego napisu o
# długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest
# tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
# ====================================================================================================>


def multi(T): ...


if __name__ == "__main__":
    from testy2023_4A import odpal_testy

    multi(list(input("Podaj T: ")))

    # odpal_testy()
