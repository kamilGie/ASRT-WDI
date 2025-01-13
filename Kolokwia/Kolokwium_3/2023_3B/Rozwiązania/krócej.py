class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def make_order(p):
    malejacy, nijaki, rosnacy = Node(""), Node(""), Node(None)
    nijaki.next, rosnacy.next = malejacy, nijaki
    while p:
        next_p = p.next
        idx = 0 if all(p.val[i] < p.val[i + 1] for i in range(len(p.val) - 1)) else 2 if all(p.val[i] > p.val[i + 1] for i in range(len(p.val) - 1)) else 1
        p.next = [rosnacy, nijaki, malejacy][idx].next
        [rosnacy, nijaki, malejacy][idx].next = p
        p = next_p
    return rosnacy.next
