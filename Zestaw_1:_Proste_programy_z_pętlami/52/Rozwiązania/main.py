# ====================================================================================================>
# Zadanie 52
# Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze. Na przykład: 85=5∗17, 8+5=5+1+7. Proszę napisać program
# wypisujący liczby Smitha mniejsze od 10^6.
# ====================================================================================================>
# print(liczba_smitha)
# i tak dla wszystkich do miliona


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(n**0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_prime_factors(n):
    total = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            total += sum_digits(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1:
        total += sum_digits(n)
    return total


def Zadanie_52():
    for num in range(2, 10**6):
        if not is_prime(num):
            s_num = sum_digits(num)
            s_factors = sum_prime_factors(num)
            if s_num == s_factors:
                print(num)


