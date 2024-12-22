from minimalizm import minimalizm


def Krotki_node():
    return f"""class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class przesylaczowe_rm(minimalizm):
    def parsuj_zadanie(self):
        index_startu = 0
        while self.linie_prototypu[index_startu][0] == "#":
            index_startu += 1

        # usuwa klase node
        while "def __str__(self)" not in self.linie_prototypu[index_startu]:
            index_startu += 1
        index_startu += 3

        while self.linie_prototypu[index_startu] == "\n":
            index_startu += 1

        res = "```python\n"
        res += Krotki_node()
        res += "\n\n"
        for linia in self.linie_prototypu[index_startu:]:
            if "__main__" in linia:
                break
            res += linia

        res = res.rstrip("\n")
        res += "\n```"
        return res
