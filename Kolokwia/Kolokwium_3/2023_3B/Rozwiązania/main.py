# ====================================================================================================>
# Zadanie 3B, 2024-01-18
# Dana jest liczba odsyłaczowa, której elementy przechowują niepuste napisy składające się z małych
# liter alfabetu angielskiego. Proszę napisać funkcję make_order(p), która porządkuje elementy listy tak,
# aby na jej początku znalazły się napisy, w których kolejne litery są w porządku rosnącym, natomiast
# na końcu listy znalazły się napisy, w których litery są w porządku malejącym. Pomiędzy powstałymi
# grupami elementów należy wstawić elementy zawierające pusty napis. Do funkcji należy przekazać
# wskaźnik do pierwszego elementu listy, funkcja powinna zwrócić wskazanie do uporządkowanej listy.
# Na przykład lista: ala → ola → abel → ula → irys → ewa → sroka → gips
# Po uporządkowaniu może mieć postać: abel → gips → „” → irys → ala → ewa → „” → sroka → ola → ula
# Uwagi:
# • Czas na rozwiązanie zadania: 25 min.
# • Oceniane będą: czytelność (komentarze), poprawność, efektywność rozwiązań.
# Dodatkowe uwagi Garka podczas kolosa:
# • Nie można tworzyć nowych elementów poza wartownikiem (którego trzeba usunąć) i dwoma
# węzłami z pustymi stringami.
# • Można założyć, że mamy już zdefiniowane class Node.
# • Lista nie zawiera napisów składających się z jednej litery.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def check(s):  # 0 - rosnący, 1 - bez porządku, 2 - malejący
    l = len(s)
    if l == 1 or s[0] == s[1]:
        return 1  # edge cases: napis 1-literowy lub niemonotoniczny na początku
    lock = True if ord(s[0]) < ord(s[1]) else False
    for i in range(l - 1):
        if lock and s[i + 1] <= s[i]:
            return 1
        if not lock and s[i + 1] >= s[i]:
            return 1
    # dotarliśmy do końca bez zmiany monotoniczności
    if lock:
        return 0  # rosnący
    return 2  # malejący


def make_order(p) -> Node:
    seg1 = Node(None)
    seg1.next = Node(None)
    seg2 = seg1.next
    seg2.val = ""
    seg2.next = Node(None)
    seg3 = seg2.next
    seg3.val = ""  # przygotowana odpowiednio lista - wskaźniki na wszystkie 3 elementy, lista w formie: seg1 -> seg2 -> seg3 -> None
    while p != None:
        variant = check(p.val)
        if (
            variant == 0
        ):  # wskazujemy węzeł początkowy bloku, do którego dopinamy węzeł wskazany przez p
            q = seg1
        elif variant == 1:
            q = seg2
        else:
            q = seg3
        tmp = q.next
        q.next = p
        p.next, p = tmp, p.next  # ta zmiana musi nastąpić równocześnie
    return seg1.next  # pomijamy 1szy pusty węzeł - naszego "wartownika"


