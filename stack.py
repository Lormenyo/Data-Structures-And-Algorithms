# A stack is an ordered collection of items where the addition of new items and the removal of the existing items take place at the same end(the top).
# the opposite end is the base.
# Last In First out principle, newwer items at the top and older items at the base.
# The order of insertion is the reverse of the of the order of removal.
# example of the stack is the use of navigation in web browsers or apps.

'''
Stack() creates an empty stack
push(item) adds a new item to the top of the stack.
pop() removes the top of the stack
isEmpty() checks if the stack is empty
peek() checks if the stack is empty bu t does not remove it.
size() returns the number of elements in the stack

'''

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



s = Stack()
print(s.isEmpty())
s.push(1)
s.push('Hannah')
print(s.peek())

