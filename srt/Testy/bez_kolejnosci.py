from prime import prime


class bez_kolejnosci(prime):
    """testy beda porownywac set wiec ani kolejnosci ani liczba wystapien nie bedzie miala znaczenia"""

    def metoda_zwracajaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
                wynik = {NazwaTestu}({', '.join(map(str, zmienne))})
                wynik = set(tuple(x) if isinstance(x, list) else x for x in wynik)
                oczekiwany_wynik = set(tuple(x) if isinstance(x, list) else x for x in { wynikWywolania })
                self.assertTrue(wynik == oczekiwany_wynik)
                \n"""

    def metoda_nasluchujaca_testow(
        self, NazwaTestu, numerTestu, zmienne, wynikWywolania, zmienne_nazwa
    ):
        oczekiwany_wynik = set(
            wynikWywolania.replace("'", "").replace("\\n", " ").split()
        )

        return f"""    def test_Nr{numerTestu:02}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
            f = io.StringIO()
            with redirect_stdout(f):
                {NazwaTestu}({', '.join(map(str, zmienne))})
            wynik = f.getvalue().strip()

            self.assertTrue(set(wynik.split()) == {oczekiwany_wynik})  # Porównanie z użyciem set
            \n"""
