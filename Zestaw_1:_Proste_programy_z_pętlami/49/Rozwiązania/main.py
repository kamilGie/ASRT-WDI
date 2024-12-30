# ====================================================================================================>
# Zadanie 49
# Proszę znaleźć najmniejszą liczbę pierwszą, której suma cyfr wynosi 101, a cyfry są w
# porządku nierosnącym
# ====================================================================================================>


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    p = 3
    r = int(x**0.5)
    while p <= r:
        if x % p == 0:
            return False
        p += 2
    return True


found = False  # globalny "znacznik", gdy znajdziemy liczbę pierwszą


def dfs(pos, n, s, last_digit, num_str):
    global found
    if found:
        return
    if pos == n:
        if s == 101:
            val = int(num_str)
            if is_prime(val):
                print(val)
                found = True
        return
    start = 0
    if pos == 0:
        start = 1  # nie dopuszczamy 0 na wiodącej cyfrze
    for d in range(start, last_digit + 1):
        if s + d <= 101:
            dfs(pos + 1, n, s + d, d, num_str + str(d))
        if found:
            break


def Zadanie_49():
    global found
    # minimalna liczba cyfr to 12, bo 11 cyfr 9 to 99 (za mało by osiągnąć sumę 101)
    # maksymalnie 101 cyfr, jeśli same '1'
    for length in range(12, 102):
        dfs(0, length, 0, 9, "")
        if found:
            break


