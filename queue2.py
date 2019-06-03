# Given a stack class implement a queue class using two stacks.
#a stack reverses the order[LIFO] but a queue doesn't[FIFO] 
# therefore, we pop elements from the instack and push to the outstack to form a queue

class Queue2Stacks:

    def __init__(self):

        #uses lists instead of owm stack  class

        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)
        print(self.instack)

    def dequeue(self):
        for ele in range(len(self.instack)):
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Queue2Stacks()
for i in  range(5):
    q.enqueue(i)


for i in  range(5):
    print(q.dequeue())