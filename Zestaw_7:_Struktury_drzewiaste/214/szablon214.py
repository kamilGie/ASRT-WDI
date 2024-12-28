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






# 1. Funkcja wypisującą zawartość drzewa.
def wypisz_rek(p): ...



def wypisz_iter(p): ...


# bez rekurencji i stosu
def wypisz_iter_morris(p): ...



# 2. Funkcja, która sprawdza czy dana liczba należy do drzewa.
def czy_nalezy_rek(p, val): ...



def czy_nalezy_iter(p, val): ...



# 3. Funkcja, która zwróci rozmiar drzewa (liczbę węzłów).
def rozmiar_rek(p): ...



def rozmiar_iter(p): ...



# 4. Funkcja, która zwróci wysokość drzewa (liczbę poziomów).
def wysokosc_rek(p): ...



def wysokosc_iter(p): ...



# 5. Funkcja, która zwróci liczbę liści drzewie.
def liczba_lisci_rek(p): ...



def liczba_lisci_iter(p): ...



# 6. Funkcja, która zwróci liczbę węzłów na n-tym poziomie.
# poziom liczony od 0
def wezly_na_poziomie_rek(p, n): ...



def wezly_na_poziomie_iter(p, n): ...


# # 7. Funkcja, która zwróci liczbę węzłów mających jednego potomka.
def wezly_z_jednym_potomkiem_rek(p): ...



def wezly_z_jednym_potomkiem_iter(p): ...






if __name__ == "__main__":
    from testy214 import odpal_testy


    wypisz_rek(Node(1, Node(2),Node(3)))


    wypisz_iter(Node(1, Node(2),Node(3)))


    wypisz_iter_morris(Node(1, Node(2),Node(3)))


    czy_nalezy_rek(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    czy_nalezy_iter(Node(1, Node(2),Node(3)), int(input('Podaj val: ')))


    rozmiar_rek(Node(1, Node(2),Node(3)))


    rozmiar_iter(Node(1, Node(2),Node(3)))


    wysokosc_rek(Node(1, Node(2),Node(3)))


    wysokosc_iter(Node(1, Node(2),Node(3)))


    liczba_lisci_rek(Node(1, Node(2),Node(3)))


    liczba_lisci_iter(Node(1, Node(2),Node(3)))


    wezly_na_poziomie_rek(Node(1, Node(2),Node(3)), int(input('Podaj n: ')))


    wezly_na_poziomie_iter(Node(1, Node(2),Node(3)), int(input('Podaj n: ')))


    wezly_z_jednym_potomkiem_rek(Node(1, Node(2),Node(3)))


    wezly_z_jednym_potomkiem_iter(Node(1, Node(2),Node(3)))


    # odpal_testy()
