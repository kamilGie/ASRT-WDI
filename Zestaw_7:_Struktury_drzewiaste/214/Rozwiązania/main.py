# ====================================================================================================>
# Zadanie 214
# Proszę napisać następujące funkcje:
# 1. Funkcja wypisującą zawartość drzewa.
# 2. Funkcja, która sprawdza czy dana liczba należy do drzewa.
# 3. Funkcja, która zwróci rozmiar drzewa (liczbę węzłów).
# 4. Funkcja, która zwróci wysokość drzewa (liczbę poziomów).
# 5. Funkcja, która zwróci liczbę liści drzewie.
# 6. Funkcja, która zwróci liczbę węzłów na n-tym poziomie.
# 7. Funkcja, która zwróci liczbę węzłów mających jednego potomka.
# Każdą funkcję proszę zrealizować jako funkcję rekurencyjną, a następnie jako funkcję bez użycia rekurencji.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return f"{str(self.left) + ' ' if self.left else ''}{self.val}{' ' + str(self.right) if self.right else ''}"


# 1. Funkcja wypisująca zawartość drzewa
def wypisz_rek(p):
    if p:
        print(p.val)
        wypisz_rek(p.left)
        wypisz_rek(p.right)


def wypisz_iter(p):
    stack = []
    current = p
    while stack or current:
        if current:
            print(current.val)
            stack.append(current.right)  # Zapamiętaj prawą gałąź
            current = current.left  # Idź w lewo
        else:
            current = stack.pop()  # Przejdź do zapisanej gałęzi


def wypisz_iter_morris(p):
    current = p
    while current:
        if not current.left:
            print(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                print(current.val)
                current = current.right


# 2. Funkcja sprawdzająca, czy dana liczba należy do drzewa
def czy_nalezy_rek(p, val):
    if not p:
        return False
    if p.val == val:
        return True
    return czy_nalezy_rek(p.left, val) or czy_nalezy_rek(p.right, val)


def czy_nalezy_iter(p, val):
    stack = [p]
    while stack:
        current = stack.pop()
        if current:
            if current.val == val:
                return True
            stack.append(current.right)
            stack.append(current.left)
    return False


# 3. Funkcja zwracająca rozmiar drzewa (liczbę węzłów)
def rozmiar_rek(p):
    if not p:
        return 0
    return 1 + rozmiar_rek(p.left) + rozmiar_rek(p.right)


def rozmiar_iter(p):
    stack = [p]
    count = 0
    while stack:
        current = stack.pop()
        if current:
            count += 1
            stack.append(current.left)
            stack.append(current.right)
    return count


# 4. Funkcja zwracająca wysokość drzewa (liczbę poziomów)
def wysokosc_rek(p):
    if not p:
        return 0
    return 1 + max(wysokosc_rek(p.left), wysokosc_rek(p.right))


def wysokosc_iter(p):
    if not p:
        return 0
    queue = [(p, 1)]  # Kolejka przechowuje węzeł i jego poziom
    max_height = 0
    while queue:
        current, level = queue.pop(0)
        max_height = max(max_height, level)
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))
    return max_height


# 5. Funkcja zwracająca liczbę liści w drzewie
def liczba_lisci_rek(p):
    if not p:
        return 0
    if not p.left and not p.right:
        return 1
    return liczba_lisci_rek(p.left) + liczba_lisci_rek(p.right)


def liczba_lisci_iter(p):
    stack = [p]
    count = 0
    while stack:
        current = stack.pop()
        if current:
            if not current.left and not current.right:
                count += 1
            stack.append(current.left)
            stack.append(current.right)
    return count


# 6. Funkcja zwracająca liczbę węzłów na n-tym poziomie
def wezly_na_poziomie_rek(p, n):
    if not p:
        return 0
    if n == 0:
        return 1
    return wezly_na_poziomie_rek(p.left, n - 1) + wezly_na_poziomie_rek(p.right, n - 1)


def wezly_na_poziomie_iter(p, n):
    if not p:
        return 0
    queue = [(p, 0)]  # Kolejka przechowuje węzeł i jego poziom
    count = 0
    while queue:
        current, level = queue.pop(0)
        if level == n:
            count += 1
        elif level < n:
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
    return count


# 7. Funkcja zwracająca liczbę węzłów mających jednego potomka
def wezly_z_jednym_potomkiem_rek(p):
    if not p:
        return 0
    count = 0
    if (not p.left and p.right) or (p.left and not p.right):
        count = 1
    return (
        count
        + wezly_z_jednym_potomkiem_rek(p.left)
        + wezly_z_jednym_potomkiem_rek(p.right)
    )


def wezly_z_jednym_potomkiem_iter(p):
    stack = [p]
    count = 0
    while stack:
        current = stack.pop()
        if current:
            if (not current.left and current.right) or (
                current.left and not current.right
            ):
                count += 1
            stack.append(current.left)
            stack.append(current.right)
    return count


