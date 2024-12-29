from Bazowa import Bazowa

from _utils_S import podpowiedz, przykladowe_odpalenie, main, parsuj_prototyp


class main_s(Bazowa):
    def __str__(self) -> str:
        res = parsuj_prototyp(self.linie_prototypu, self.funkcje)

        cialo_maina = "\n"
        for funkcja in self.funkcje:
            cialo_maina += przykladowe_odpalenie(funkcja)
        cialo_maina += "\n\n"
        cialo_maina += podpowiedz()
        res += main(self.nr_zadania, cialo_maina)
        return res
