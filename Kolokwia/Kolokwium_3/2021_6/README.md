<picture>
  <source srcset="../../../srt/zbior_zadan/2021_6.png" media="(prefers-color-scheme: light)">
  <source srcset="../../../srt/zbior_zadan/black_2021_6.png" media="(prefers-color-scheme: dark)">
  <img src="../../../srt/zbior_zadan/black_2021_6.png" alt="zadanie 2021_6">
</picture>


```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def is_repairable(head, step):
    current_val = head.val
    while head.next:
        current_val *= step
        if current_val == head.next.val:  # Jeśli osiągnąłem wartość następnego elementu, przechodzę do niego
            head = head.next
        elif abs(step) > 1 and abs(current_val) > abs(head.next.val):  # Sprawdzam, czy przekroczyłem ciąg rosnący
            return False
        elif abs(step) < 1 and abs(current_val) < abs(head.next.val):  # Sprawdzam, czy przekroczyłem ciąg malejący
            return False
    return True


def repair(p):
    original_step = abs(p.next.val / p.val)  # Iloraz dwóch pierwszych elementów
    divisor = 1  # Liczba kroków potrzebnych do przejścia od pierwszego do drugiego elementu
    step = original_step

    # Docelowy krok iloczynu będzie ilorazem dwóch pierwszych elementów,
    # spierwiastkowanym do odpowiedniej potęgi w zależności od liczby kroków, pomiędzy 1 a 2 elementem.
    while not is_repairable(p, step) and not is_repairable(p, -step):  # Dopóki krok nie naprawia ciągu
        divisor += 1
        step = original_step ** (1 / divisor)  # Krok to pierwiastek stopnia równego liczbie kroków

    step = -step if is_repairable(p, -step) else step  # Jeśli poprawny krok jest ujemny, zmieniam na wartość ujemną

    inserted_count = 0
    while p.next:
        if p.val * step != p.next.val:  # Jeśli nie dotarłem do wartości następnego elementu w ciągu
            p.next = Node(p.val * step, p.next)  # Dodaję brakujący element do listy
            inserted_count += 1
        p = p.next
    return inserted_count
```

Precyzyjne rozwiązanie eliminujące problemy związane z zaokrąglaniem liczb zmiennoprzecinkowych w \Rozwiązania\precyzyjne.py
