# singly linked list is a collection of nodes
#  head and tail of a linkedlist
#  going through the nodes is called traversing the linkedlist(link hopping or pointer hopping)
# Linked list does not have a predetermined fixed size
#  It uses space proportionally to the number of elements 


#  nodes are pointers in python 
#  the data and address of the next location of the data element is stored.

# Inserting elements in a linked list involves reassigning the pointers from the existing nodes to newly inserted node.

class Node:

    def __init__(self, ele):
        self.ele = ele
        self.next_ele = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        first_ele = self.head
        while first_ele is not None:
            print(first_ele.ele)
            first_ele = first_ele.next_ele

    # insert node at the beginning 
    def insertBegin(self, new_ele):
        new_node = Node(new_ele)

        new_node.next_ele = self.head  # change the new_node's next element to the existing head

        self.head = new_node

    # insert node at the end
    def insertEnd(self, new_ele):
        new_node = Node(new_ele)

        if self.head is None:
            self.head = new_node
            return

        last_ele = self.head
        while (last_ele.next_ele):
            last_ele = last_ele.next_ele
        
        # assign last element to te new node
        last_ele.next_ele = new_node

    
    def InsertBetween(self, new_ele, existing_node):

        if existing_node is None:
            print("Node is absent")
            return 
        
        new_node = Node(new_ele)
        # the next node of the existing node is referenced by the new node
        new_node.next_ele = existing_node.next_ele

        existing_node.next_ele = new_node
    

a = Node(1)
b = Node(2)
c = Node(3)

llist = Linkedlist()
llist.head = a

# Link first node to the seond node 
llist.head.next_ele = b

# link the second node to the third node
b.next_ele = c

# insert node at the beginning
llist.insertBegin(7)

# insert node at the end
llist.insertEnd(8)

# insert node after the second node
llist.InsertBetween(9, llist.head.next_ele)

# traverse through the linked list
llist.traverse()







