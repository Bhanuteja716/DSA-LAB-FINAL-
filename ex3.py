print("Lab 3: Queue and Circular Queue")
print("-------------------------------")
class ArrayQueue:
    def __init__(self, size):
        self.q = []  # Initialize empty list for queue
        self.size = size  # Maximum size of queue
    def enqueue(self, x):
        if len(self.q) < self.size:
            self.q.append(x)
        else:
            print("Queue Full")
    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        else:
            return None
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return None
    def display(self):
        print("Queue:", self.q)
size = int(input("Enter queue size: "))
nq = ArrayQueue(size)
elements = input("Enter elements to enqueue: ").split()
for x in elements:
    nq.enqueue(int(x))
num_deq = int(input("Enter how many dequeues: "))
for _ in range(num_deq):
    nq.dequeue()
nq.display()
print("Front element:", nq.front())
class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size  # Fixed-size list
        self.f = -1  # Front pointer
        self.r = -1  # Rear pointer
        self.size = size  # Maximum size
    def enqueue(self, x):
        if (self.r + 1) % self.size == self.f:
            print("Queue Full")
            return
        if self.f == -1:
            self.f = 0
        self.r = (self.r + 1) % self.size
        self.q[self.r] = x
    def dequeue(self):
        if self.f == -1:
            print("Queue Empty")
            return
        val = self.q[self.f]
        if self.f == self.r:
            self.f = self.r = -1
        else:
            self.f = (self.f + 1) % self.size
        return val
    def display(self):
        print("Circular Queue:", self.q)
size = int(input("\nEnter circular queue size: "))
cq = CircularQueue(size)
elements = input("Enter elements to enqueue in circular queue: ").split()
for x in elements:
    cq.enqueue(int(x))
num_deq = int(input("Enter how many dequeues: "))
for _ in range(num_deq):
    cq.dequeue()
new_val = int(input("Enter element to enqueue again: "))
cq.enqueue(new_val)
cq.display()
