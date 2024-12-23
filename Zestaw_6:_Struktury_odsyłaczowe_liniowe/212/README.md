<picture>
  <source srcset="../../srt/zbior_zadan/212.png" media="(prefers-color-scheme: light)">
  <source srcset="../../srt/zbior_zadan/black_212.png" media="(prefers-color-scheme: dark)">
  <img src="../../srt/zbior_zadan/black_212.png" alt="zadanie 212">
</picture>

```python
# wszystkie zadania poprzednie edytujace/usuwające nie potrzebuja juz zwracac noda tylko mogą edytować in place
# argumenty liczy sie od p.next
# tyle ze zmian jak bedzie jakies wieksza zmiana dodam ponizej zadanie 

# 209
def repair(p):
    """bede tworzyl 2 lancuchy ktore potem zlacze"""
    odd_head = odd_tail = Node(0)
    even_head = even_tail = Node(0)

    current = p.next
    while current:
        if current.val % 2 == 1:  # nieparzysta dołączam do odd_tail
            odd_tail.next = current
            odd_tail = odd_tail.next
        else:  # parzysta dołączam do even_tail
            even_tail.next = current
            even_tail = even_tail.next
        current = current.next

    # Doczepiam listę parzystą na koniec listy nieparzystej
    odd_tail.next = even_head.next
    even_tail.next = None
    p.next = odd_head.next # ustawiamy wartownika by wskazywal na wynik

```
