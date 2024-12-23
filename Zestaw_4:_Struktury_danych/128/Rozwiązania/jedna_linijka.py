def distance(T):
    return sum(bit * (2**i) for i, bit in enumerate(reversed(max(T)))) - sum( bit * (2**i) for i, bit in enumerate(reversed(min(T))))
