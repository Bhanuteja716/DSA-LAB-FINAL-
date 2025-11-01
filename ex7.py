# -------------------------------------
# Lab 7: Hash Table with Linear Probing
# -------------------------------------

print("Lab 7: Hash Table with Linear Probing")
print("-------------------------------------")
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # initialize all slots to None
    def _hash(self, key):
        return key % self.size
    def insert(self, key):
        index = self._hash(key)  # find hash index
        while self.table[index] is not None:  # find next empty slot
            index = (index + 1) % self.size
        self.table[index] = key
    def search(self, key):
        index = self._hash(key)
        start = index  # to detect full loop
        while self.table[index] is not None:
            if self.table[index] == key:
                return True  # key found
            index = (index + 1) % self.size
            if index == start:  # looped through full table
                break
        return False  # key not found
    def delete(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                return  # key deleted
            index = (index + 1) % self.size
    def display(self):
        print("Hash Table:", self.table)
size = int(input("Enter hash table size: "))
h = HashTable(size)
keys = list(map(int, input("Enter keys to insert: ").split()))
for k in keys:
    h.insert(k)
h.display()
key = int(input("Enter key to search: "))
if h.search(key):
    print("Found")
else:
    print("Not Found")
key = int(input("Enter key to delete: "))
h.delete(key)
h.display()
