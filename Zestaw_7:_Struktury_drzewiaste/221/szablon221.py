# ====================================================================================================>
# Zadanie 221
# W kodzie Morse’a litery kodowane są za pomocą popularnie zwanych kropką i kreską, np.
# ’A’: ’.-’, ’B’: ’-...’, ’C’: ’-.-.’, itd. Proszę napisać funkcję, która tworzy drzewo binarne (na lewo kropka na
# prawo kreska) pozwalające dekodować znak poprzez schodzenie w drzewie od korzenia do odpowiedniego
# węzła. Następnie proszę napisać funkcję dekodującą napis złożony ze znaków kropek i kresek.
# ====================================================================================================>


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:  # wypisywanie
        return f"{str(self.left) if self.left else ''}{self.val}{str(self.right) if self.right else ''}"


def zbuduj_drzewo_morse() -> Node: ...


def dekoduj_morse(kod) -> str: ...


if __name__ == "__main__":
    from testy221 import odpal_testy

    # dekoduj_morse("... --- ...")  # return SOS

    odpal_testy()
