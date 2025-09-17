<picture>
  <source srcset="../../srt/zbior_zadan/223.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_223.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_223.png" alt="zadanie 223">
</picture>

```python
def Zadanie_223(T, target):
    def binary_search(direction):
        """Znajduje indeks pierwszego lub ostatniego wystąpienia elementu."""
        left, right = 0, len(T) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if T[mid] == target:
                result = mid
                if direction == "left":
                    right = mid - 1  # Szukamy dalej na lewo
                else:
                    left = mid + 1  # Szukamy dalej na prawo
            elif T[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first_index = binary_search("left")
    if first_index == -1:  # Element nie występuje
        return 0
    last_index = binary_search("right")

    return last_index - first_index + 1
```


---
### Sprawdź też moje inne projekty z odpowiedziami:
- [Rosnotes-Dyskretna](https://github.com/kamilGie/Rosnotes-Dyskretna)
