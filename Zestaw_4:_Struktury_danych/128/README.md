<picture>
  <source srcset="../../srt/zbior_zadan/128.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_128.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_128.png" alt="zadanie 128">
</picture>

```python
def bin_to_deci(row):
    result = 0
    power_of_two = 1

    for i in range(len(row) - 1, -1, -1):
        result += row[i] * power_of_two
        power_of_two *= 2  # Następna potęga dwójki

    return result


def distance(T):
    min_idx = max_idx = 0
    for i in range(1, len(T)):
        # leksykograficznie porównuje listy dokladnie tak jak chcemy
        if T[i] > T[max_idx]:
            max_idx = i
        elif T[i] < T[min_idx]:
            min_idx = i

    return bin_to_deci(T[max_idx]) - bin_to_deci(T[min_idx])

```


---
Jeśli repo się podoba, zostaw gwiazdkę 🙏
