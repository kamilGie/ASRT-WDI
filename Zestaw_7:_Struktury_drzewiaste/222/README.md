<picture>
  <source srcset="../../srt/zbior_zadan/222.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_222.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_222.png" alt="zadanie 222">
</picture>

```python
class Node:
    def __init__(self, freq, char=None, left=None, right=None) -> None:
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right


def calculate_frequencies(input_text):
    """Tworzy listę wystąpień każdej litery w formie (znak, częstotliwość)."""
    frequencies = []
    for char in input_text:
        for i in range(len(frequencies)):
            if frequencies[i][0] == char:  # Sprawdzam, czy znak już istnieje
                frequencies[i] = (frequencies[i][0], frequencies[i][1] + 1)  # Zwiększam częstotliwość
                break
        else:  # nie wystapil brake znak nie został znaleziony
            frequencies.append((char, 1))  # Dodaję nowy znak z częstotliwością 1
    return frequencies


def build_huffman_tree(frequencies):
    """Tworzy drzewo Huffmana na podstawie listy częstotliwości liter."""
    # Tworzenie posortowanej listy węzłów z częstotliwościami i znakami
    nodes = [Node(freq, char) for char, freq in frequencies]
    nodes.sort(key=lambda node: node.freq)

    while len(nodes) > 1:
        left, right = nodes.pop(0), nodes.pop(0) # najmniejsze czestotliwosci
        merged = Node(left.freq + right.freq, f"{left.char}{right.char}", left, right) # rodzic najmniejszych

        i = 0
        while i < len(nodes) and nodes[i].freq < merged.freq:
            i += 1
        nodes.insert(i, merged) # Nowy węzeł w odpowiednie miejsce w posortowanej liście

    return nodes[0]  # Zwracam korzeń drzewa


def find_huffman_code(huffman_tree, char):
    """Znajduje kod Huffmana dla podanego znaku, poruszając się po drzewie."""
    char_code = ""
    while huffman_tree.char != char:  # Szukam liścia reprezentującego znak
        if char in huffman_tree.left.char:  # Znak znajduje się w lewym poddrzewie
            huffman_tree = huffman_tree.left
            char_code += "1"
        else:  # Znak znajduje się w prawym poddrzewie
            huffman_tree = huffman_tree.right
            char_code += "0"
    return char_code


def Zadanie_222(input_text):
    huffman_tree = build_huffman_tree(calculate_frequencies(input_text))

    binary_output = ""
    for char in input_text:
        binary_output += find_huffman_code(huffman_tree, char)

    return binary_output
```

# Opis Rozwiązania 

zadanie na podstawie https://home.agh.edu.pl/~turcza/ts/1_Huffman.pdf



---
Jeśli kod był pomocny, zostaw gwiazdkę ✨
