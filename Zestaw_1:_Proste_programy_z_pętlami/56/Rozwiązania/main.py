# ====================================================================================================>
# Zadanie 56
# „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych
# cyfr,gdzieM,N >=0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0 gdy taka liczba nie istnieje. Na
# przykład dla liczby 1202742516 spośród obciętych liczb pierwszych:2,5,7,251,2027 liczbą spełniającą warunek
# jest liczba 251.
# ====================================================================================================>


def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def has_unique_digits(x):
    """Maska bitowa aby uniknąć tablic"""
    digit_mask = 0
    while x > 0:
        digit = x % 10
        bit = 1 << digit  # Przesunięcie bitowe odpowiadające cyfrze
        if digit_mask & bit:  # Jeśli bit dla tej cyfry jest już ustawiony
            return False
        digit_mask |= bit  # Ustaw bit dla tej cyfry
        x //= 10
    return True


def remove_digits_from_start_and_end(K, M, N):
    num_digits = len_digits(K)
    divisor = 10 ** (num_digits - M)
    res = K % divisor  # Usuwamy cyfry z początku
    res //= 10**N  # Usuwamy cyfry z końca
    return res


def len_digits(K):
    count = 0
    while K > 0:
        K //= 10
        count += 1
    return count


def Zadanie_56(K):
    max_prime = 0
    num_digits = len_digits(K)

    for M in range(num_digits):  # Liczba cyfr do usunięcia z początku
        for N in range(num_digits - M):  # Liczba cyfr do usunięcia z końca
            fragment = remove_digits_from_start_and_end(K, M, N)
            if fragment > 0 and is_prime(fragment) and has_unique_digits(fragment):
                max_prime = max(max_prime, fragment)

    return max_prime


