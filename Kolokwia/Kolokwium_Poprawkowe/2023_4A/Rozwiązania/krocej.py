# ====================================================================================================>
# Zadanie 4A, 2024-01-26
# Napis nazywamy wielokrotnym, jeżeli powstał przez 𝑛-krotne (𝑛 > 1) powtórzenie innego napisu o
# długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest
# tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
# ====================================================================================================>


# mega fajne
def multi(T):
    return max(
        max(
            cykl
            for cykl in range(len(napis) // 2, 0, -1)
            if len(napis) % cykl == 0 and napis[:cykl] * (len(napis) // cykl) == napis
        )
        for napis in T
    )
