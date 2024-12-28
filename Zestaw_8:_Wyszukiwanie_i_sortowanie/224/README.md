<picture>
  <source srcset="../../srt/zbior_zadan/224.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_224.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_224.png" alt="zadanie 224">
</picture>

```python
def Zadanie_224(T, target):
    left, right = 0, len(T) - 1

    while left <= right:
        # Obliczam dwie granice podziału
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3

        if T[one_third] == target:  # Znak w pierwszym punkcie podziału
            return one_third
        if T[two_third] == target:  # Znak w drugim punkcie podziału
            return two_third

        if target < T[one_third]:  # Element w pierwszej 1/3
            right = one_third - 1
        elif target > T[two_third]:  # Element w ostatniej 1/3
            left = two_third + 1
        else:  # Element w środkowej 1/3
            left = one_third + 1
            right = two_third - 1

    return -1  # Element nie został znaleziony
```