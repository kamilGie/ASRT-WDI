# ====================================================================================================>
# Zadanie 207
# Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
# Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ??bartek??leszek??marek??ola??zosia???????????????????????????????????????Proszęnapisaćstosowne
# definicjetypóworazfunkcjęwstawiającądolistynapiszzachowaniemzasadypoprzedzania.Dofunkcjinależy
# przekazaćwskaźnikdolistyorazwstawianynapis,funkcjapowinnazwrócićwartośćlogicznąwskazującą,czy
# udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo
# wstawiony element.
# ====================================================================================================>


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):  # wypisywanie
        return f"{self.val}" + (f" -> {self.next}" if self.next else "")


def Zadanie_207(head, new_string) -> bool:
    current = head
    while True:
        if current.val[-1] < new_string[0] and new_string[-1] < current.next.val[0]:  # czy nowy napis pasuje z 2 stron
            new_node = Node(new_string, current.next)
            current.next = new_node
            return True

        current = current.next

        if current == head:  # przeszlismy cykl
            return False


