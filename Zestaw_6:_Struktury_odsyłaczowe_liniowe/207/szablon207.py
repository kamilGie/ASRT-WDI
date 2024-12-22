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








def Zadanie_207(head, new_string) -> bool: ...






if __name__ == "__main__":
    from testy207 import odpal_testy


    Zadanie_207(Node(1, Node(2, Node(3))), int(input('Podaj new_string: ')))


    # odpal_testy()
