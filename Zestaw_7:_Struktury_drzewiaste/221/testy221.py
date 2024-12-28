import unittest

from szablon221 import dekoduj_morse, zbuduj_drzewo_morse


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu


    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    import os
    import sys
    import importlib

    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):
    def test_Nr001_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.left.val, "I")

    def test_Nr002_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.left.left.left.val, "H")

    def test_Nr003_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.right.left.val, "R")

    def test_Nr004_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.right.right.val, "W")

    def test_Nr005_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.right.right.left.val, "P")

    def test_Nr006_zbuduj_drzewo_morse(self):
        p = zbuduj_drzewo_morse()
        self.assertEqual(p.left.left.left.left.left.val, "5")

    def test_Nr02_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- .- -.-"), "JAK")

    def test_Nr03_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --- -."), "ON")

    def test_Nr04_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-- .-"), "MA")

    def test_Nr05_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--. --- -.-. --.. . -.- .- .---"), "POCZEKAJ")

    def test_Nr06_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- .- -.-"), "JAK")

    def test_Nr07_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--- -."), "ON")

    def test_Nr08_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-- .-"), "MA")

    def test_Nr09_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -- --- -. .-. .-"), "AMONRA")

    def test_Nr10_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" - .- -.- .."), "TAKI")

    def test_Nr11_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--. --- ... -.-."), "GOSC")

    def test_Nr12_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... .-.. ..- -.-. .... .- .---"), "SLUCHAJ")

    def test_Nr13_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -- --- -. .-. .-"), "AMONRA")

    def test_Nr14_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... .. . -.. --.. .. ... --.."), "SIEDZISZ")

    def test_Nr15_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... ."), "SE")

    def test_Nr16_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --.. "), "Z")

    def test_Nr17_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse("-.. --.. .. . .-- -.-. --.. -.-- -. .- "), "DZIEWCZYNA"
        )

    def test_Nr18_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -- --- -. .-. .-"), "AMONRA")

    def test_Nr19_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... .. . -.. --.. .. ... --.."), "SIEDZISZ")

    def test_Nr20_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... .. . "), "SIE")

    def test_Nr21_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--.."), "Z")

    def test_Nr22_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse("-.. --.. .. . .-- -.-. --.. -.-- -. .-"), "DZIEWCZYNA"
        )

    def test_Nr23_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .--"), "W")

    def test_Nr24_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-.. --- -.- .- .-.. ..- "), "LOKALU")

    def test_Nr25_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -- --- -. .-. .- "), "AMONRA")

    def test_Nr26_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -- --- -. .-. .-"), "AMONRA")

    def test_Nr27_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- ..- - .- ... .-. .-"), "KUTASRA")

    def test_Nr28_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" ... .-. .- .-. .- .-. .- "), "SRARARA")

    def test_Nr29_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-. .. . "), "NIE")

    def test_Nr30_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-- .. . -- "), "WIEM")

    def test_Nr31_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .-- .. . ... .. . -.-"), "WIESIEK")

    def test_Nr32_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --.. -... .. --. -. .. . .--"), "ZBIGNIEW")

    def test_Nr33_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- .- .-. --- .-.."), "KAROL")

    def test_Nr34_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- ..- .-. -.. . "), "KURDE")

    def test_Nr35_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-. .. ."), "NIE")

    def test_Nr36_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-- .. . -- "), "WIEM")

    def test_Nr37_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- -. -.. .-. --.. . .---"), "ANDRZEJ")

    def test_Nr38_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" ... .. . -.. --.. .. ... --.."), "SIEDZISZ")

    def test_Nr39_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... ."), "SE")

    def test_Nr40_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--"), "W")

    def test_Nr41_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-.. --- -.- .- .-.. ..-"), "LOKALU")

    def test_Nr42_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --.. "), "Z")

    def test_Nr43_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse("-.. --.. .. . .-- -.-. --.. -.-- -. .-"), "DZIEWCZYNA"
        )

    def test_Nr44_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".."), "I")

    def test_Nr45_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--.. "), "Z")

    def test_Nr46_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".---- -----"), "10")

    def test_Nr47_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("..--- -----"), "20")

    def test_Nr48_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- .-.. . --. .- -- .."), "KOLEGAMI")

    def test_Nr49_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse(".--. --- -.. -.-. .... --- -.. --.. .. "), "PODCHODZI"
        )

    def test_Nr50_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--. --- ... -.-. "), "GOSC")

    def test_Nr51_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.. ---"), "DO")

    def test_Nr52_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. .. . -... .. . "), "CIEBIE")

    def test_Nr53_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--- -.. .--. .. -. .- "), "ODPINA")

    def test_Nr54_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... --- -... .. ."), "SOBIE")

    def test_Nr55_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- ... --.. ..- .-.. ."), "KOSZULE")

    def test_Nr56_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- . -."), "TEN")

    def test_Nr57_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-... .-.. ..- --.. -.- ."), "BLUZKE")

    def test_Nr58_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .--. --- -.- .- --.. ..- .--- ."), "POKAZUJE")

    def test_Nr59_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--"), "W")

    def test_Nr60_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse("-.- --- ... --.. ..- .-.. . -.-. -.-. . "), "KOSZULECCE"
        )

    def test_Nr61_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- . -."), "TEN")

    def test_Nr62_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--. --- -.- .- --.. ..- .--- ."), "POKAZUJE")

    def test_Nr63_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. .."), "CI")

    def test_Nr64_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- .-. --- -. -.- . "), "KORONKE")

    def test_Nr65_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- .-- --- .."), "TWOI")

    def test_Nr66_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- . -.. . -. "), "JEDEN")

    def test_Nr67_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- . -.. . -. "), "JEDEN")

    def test_Nr68_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --.."), "Z")

    def test_Nr69_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- .-- --- .. -.-. ...."), "TWOICH")

    def test_Nr70_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- .-.. . --. --- .--"), "KOLEGOW")

    def test_Nr71_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-... -.-- .-.. "), "BYL")

    def test_Nr72_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" -.- .. . -.. -.-- ..."), "KIEDYS")

    def test_Nr73_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--"), "W")

    def test_Nr74_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- .-. -.-- -- .. -. .- .-.. . "), "KRYMINALE")

    def test_Nr75_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("... .. . -.. --.. .. .- .-.."), "SIEDZIAL")

    def test_Nr76_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".. "), "I")

    def test_Nr77_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" --- -. "), "ON")

    def test_Nr78_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-- ..-"), "MU")

    def test_Nr79_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-- --- .-- .."), "MOWI")

    def test_Nr80_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".... -- --"), "HMM")

    def test_Nr81_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- .-- --- .."), "TWOI")

    def test_Nr82_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- .-.. . -.. --.. -.--"), "KOLEDZY")

    def test_Nr83_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-- ... - .- .--- .-"), "WSTAJA")

    def test_Nr84_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .--- .- -.. .-"), "JADA")

    def test_Nr85_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. .. ."), "CIE")

    def test_Nr86_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-- "), "W")

    def test_Nr87_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.. --.. .. ..- .-. . "), "DZIURE")

    def test_Nr88_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" - .-- --- .--- .- "), "TWOJA")

    def test_Nr89_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.- --- -... .. - .-"), "KOBITA")

    def test_Nr90_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .-- ... - .- .--- ."), "WSTAJE")

    def test_Nr91_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .--. ..-. ..-"), "PFU")

    def test_Nr92_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--. .-.. ..- .--- ."), "PLUJE")

    def test_Nr93_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-. .-"), "NA")

    def test_Nr94_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. .. . -... .. . "), "CIEBIE")

    def test_Nr95_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" .."), "I")

    def test_Nr96_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-- ... --.. -.-- ... -.-. -.-- "), "WSZYSCY")

    def test_Nr97_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--- -.. "), "OD")

    def test_Nr98_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" -.-. .. . -... .. ."), "CIEBIE")

    def test_Nr99_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--- -.. -.-. .... --- -.. --.. .-"), "ODCHODZA")

    def test_Nr100_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".- "), "A")

    def test_Nr101_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- -.--"), "TY")

    def test_Nr102_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- .- -.- .. -.-. .... "), "TAKICH")

    def test_Nr103_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".-.. ..- -.. --.. .. "), "LUDZI")

    def test_Nr104_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-. .. ."), "NIE")

    def test_Nr105_dekoduj_morse(self):
        self.assertEqual(
            dekoduj_morse("... --.. .- -. ..- .--- . ... --.. "), "SZANUJESZ"
        )

    def test_Nr106_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- .- -.- .. . "), "TAKIE")

    def test_Nr107_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- . ... -"), "JEST")

    def test_Nr108_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--.. -.-- -.-. .. . "), "ZYCIE")

    def test_Nr109_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("- ---"), "TO")

    def test_Nr110_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--- . ... -"), "JEST")

    def test_Nr111_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--"), "W")

    def test_Nr112_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(".--. .-. --.. . -. --- ... -. .."), "PRZENOSNI")

    def test_Nr113_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-... .- .--- -.- .-"), "BAJKA")

    def test_Nr114_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--.. .- -... .- .-- .-"), "ZABAWA")

    def test_Nr115_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("--. .-. .- "), "GRA")

    def test_Nr116_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-- --- .-- -.-. .. ."), "MOWCIE")

    def test_Nr117_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse(" ... --- -... .. ."), "SOBIE")

    def test_Nr118_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. ---"), "CO")

    def test_Nr119_dekoduj_morse(self):
        self.assertEqual(dekoduj_morse("-.-. .... -.-. . -.-. .. . "), "CHCECIE")
