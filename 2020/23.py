from collections import deque

class node:
    def __init__(self, element, next_node, prev_node):
        self.element = element
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return self.element

    def __str__(self):
        return str(self.element)

class linkedlist:
    def __init__(self):
        self.first = None
        self.lookup = {}
    
    def append(self, x):
        if self.first == None:
            self.first = node(x, self.first, self.first)
            self.first.prev_node = self.first
            self.first.next_node = self.first
            self.lookup[x] = self.first
        else:
            n = node(x,self.first, self.first.prev_node)
            self.first.prev_node.next_node = n
            self.first.prev_node = n
            self.lookup[x] = n

    def remove(self, node):
        if node == self.first:
            x = self.first.element
            self.first = node.next_node
            self.lookup[x] = None
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        node.next_node = None
        node.prev_node = None
        return node
    
    def insert(self, node, pos):
        self.lookup[node.element] = node
        node.next_node = pos.next_node
        pos.next_node.prev_node = node
        node.prev_node = pos
        pos.next_node = node

    def find(self, x):
        assert self.lookup[x] != None
        return self.lookup[x]
       
    def __iter__(self):
        node = self.first
        yield node
        node = node.next_node
        while node is not self.first:
            yield node
            node = node.next_node
            if node == self.first:
                break

    def __str__(self):
        node = self.first
        temp = [str(node)]
        node = node.next_node
        while node != self.first:
            temp.append(str(node))
            node = node.next_node
        return '->'.join(temp)


line = 974618352
moves = 10000000
numofcups = 1000001
cups = [int(c) for c in str(line)]
ll = linkedlist()
for c in cups:
    ll.append(c)
for i in range(10,numofcups):
    ll.append(i)

curr = ll.first
while moves:
    a, b, c = ll.remove(curr.next_node), ll.remove(curr.next_node), ll.remove(curr.next_node)
    a.next_node = b
    b.next_node = c
    c.prev_node = b
    b.prev_node = a

    temp_elem = [a.element, b.element, c.element]
    diff = numofcups - 1 if curr.element - 1 == 0 else curr.element - 1
    while diff in temp_elem:
        diff -= 1
        if diff == 0:
            diff = numofcups - 1

    pos = ll.find(diff)
    ll.insert(a,pos)
    ll.insert(b,a)
    ll.insert(c,b)
    curr = curr.next_node
    moves -= 1
pos = ll.find(1)
print(pos.next_node.element * pos.next_node.next_node.element)
