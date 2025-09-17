<picture>
  <source srcset="../../srt/zbior_zadan/221.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_221.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_221.png" alt="zadanie 221">
</picture>

```python
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left


def zbuduj_drzewo_morse()->Node:
    morse_code = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
        'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
        'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
        'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----'
    }

    root = Node("")

    for char, code in morse_code.items():
        current = root
        for symbol in code:
            if symbol == ".":
                if not current.left: # tworze droge jak brakuje 
                    current.left = Node("")
                current = current.left
            else:
                if not current.right: # tworze droge jak brakuje 
                    current.right = Node("")
                current = current.right
        current.val = char  # Ustawiamy znak na końcu ścieżki

    return root

def dekoduj_morse(kod)->str:
    drzewo = zbuduj_drzewo_morse()
    wynik = ""
    for znak in kod.split(' '):
        current = drzewo
        for symbol in znak:
            if symbol == '.':
                current = current.left
            else:
                current = current.right

        wynik += current.val
    return wynik
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
