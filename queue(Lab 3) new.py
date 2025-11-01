print("Lab 3: Queue and Circular Queue")
print("-------------------------------")
class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return self.rear == self.size - 1
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return
        data = self.queue[self.front]
        print(f"Dequeued: {data}")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1

    def front_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print(f"Front element: {self.queue[self.front]}")
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()
class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.f = -1
        self.r = -1
        self.size = size
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
size = int(input("Enter queue size: "))
A = ArrayQueue(size)
elements = input("Enter elements to enqueue: ").split()
for x in elements:
    A.enqueue(int(x))
num_deq = int(input("Enter how many dequeues: "))
for _ in range(num_deq):
    A.dequeue()
A.display()
A.front_element()
size = int(input("\nEnter circular queue size: "))
C = CircularQueue(size)
elements = input("Enter elements to enqueue in circular queue: ").split()
for x in elements:
    C.enqueue(int(x))
num_deq = int(input("Enter how many dequeues: "))
for _ in range(num_deq):
    C.dequeue()
new_val = int(input("Enter element to enqueue again: "))
C.enqueue(new_val)
C.display()
