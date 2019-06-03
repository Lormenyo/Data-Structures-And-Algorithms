# ################## Deque #######################
# a double ended queue that is an ordered collectin of items similar to the queue
# unrestrictive nature of adding items(at front or rear)


class Deque():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        return self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)   

d = Deque()
print(d.isEmpty())
d.addFront('Hannah')
d.addRear('Lormenyo')
print(d.removeRear())