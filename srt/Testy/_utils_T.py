RAMKA = "# ====================================================================================================>\n"

NAGLOWEK = "class testy(unittest.TestCase):\n"

IMPORTY = "import unittest\nfrom contextlib import redirect_stdout\nimport io\n"

ODPAL_TESTY = "def odpal_testy():\n    suite = unittest.TestLoader().loadTestsFromTestCase(testy)\n    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)\n"


def stworz_podpowiedzi():
    podpowiedzi = []

    # Wymuszenie podania dokładnie trzech podpowiedzi
    for i in range(1, 4):
        podp = input(f"💡 Podaj podpowiedź nr {i}: ")
        podpowiedzi.append(podp)

    # Generowanie funkcji w formacie kodu Python
    podpowiedzi_code = ",\n        ".join(f'"{p}"' for p in podpowiedzi)
    return f"""def podpowiedz(nr: int):
    podpowiedzi = [
        {podpowiedzi_code}
    ]
    print(podpowiedzi[nr - 1])"""


KOMENDA = f"""
def komenda(k: str, *args, **kwargs):
    \"\"\"
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu


    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    \"\"\"
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
"""


def dynamiczny_import_funkcji(nr_zadania, funkcje):
    funkcjeStr = ", ".join(funkcja.__name__ for funkcja in funkcje)
    return f"from szablon{nr_zadania} import {funkcjeStr}\n"
