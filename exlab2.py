print("Lab 2: Singly Linked List & Stack")
print("---------------------------------")


# -------------------------------------------------------
# CLASS: Node (for Linked List)
# -------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data        # Node data
        self.next = None        # Pointer to next node


# -------------------------------------------------------
# CLASS: Singly Linked List
# -------------------------------------------------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None        # Initialize empty linked list

    # Insert at front
    def insert_front(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    # Insert at end
    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    # Delete from front
    def delete_front(self):
        if self.head:
            self.head = self.head.next

    # Traverse and print all nodes
    def traverse(self):
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next


# -------------------------------------------------------
# MAIN PROGRAM FOR LINKED LIST
# -------------------------------------------------------
ll = SinglyLinkedList()

# Take input for linked list
n = int(input("Enter size of linked list: "))
vals = []
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    vals.append(val)

# Insert elements
for x in vals:
    ll.insert_end(x)

# Delete front node
ll.delete_front()

# Display list
print("After deletion at front:", end=" ")
ll.traverse()



# -------------------------------------------------------
# CLASS: Stack (using list)
# -------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []         # Initialize empty stack

    # Push element
    def push(self, x):
        self.items.append(x)

    # Pop element
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    def is_empty(self):
        return not self.items
s = Stack()
m = int(input("\nEnter size of stack: "))
for i in range(m):
    val = int(input(f"Enter element {i+1}: "))
    s.push(val)
s.pop()
print("Top element after pop:", s.peek())
