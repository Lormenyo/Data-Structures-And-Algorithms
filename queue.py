################ Queue  #######################
# Queue is an ordered collection of items where the addition of new items happens at the one end, called the rear and the removal of the existing items occurs at the other end, commonly called the front.
# As an element enters the queue it starts at the rear and makes it way toward the front, waiting until that time when it is the next element to be removed.
# First In First out
# example is waiting in line for a movie ticket 
# Enqueue - adding a new item at the end of the queue
# Dequeue - removing the front item from the queue



class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

# adds a new item to the rear of the queue
    def enqueue(self, item):
        self.items.insert(0,item)

# removes the front item from the queue and returns the item
    def dequeue(self):
        return self.items.pop()
    

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue('Hannah')
q.enqueue('Lormenyo')
print(q.dequeue())