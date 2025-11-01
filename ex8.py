# Lab 8: B-Tree Implementation (Order m = 3)
# Objective: Implement B-trees for indexing (CO2)
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Order (m=3 => t=2)
    def split_child(self, parent, i, child):
        t = self.t
        new_child = BTreeNode(child.leaf)
        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, child.keys[t - 1])
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        if not child.leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]
    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i, node.children[i])
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(False)
            new_root.children.insert(0, root)
            self.split_child(new_root, 0, root)
            i = 0
            if k > new_root.keys[0]:
                i += 1
            self.insert_non_full(new_root.children[i], k)
            self.root = new_root
        else:
            self.insert_non_full(root, k)
    def search(self, node, k):
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == k:
            return True
        if node.leaf:
            return False
        return self.search(node.children[i], k)
t = 2  # Order m = 3 => t = 2
btree = BTree(t)
n = int(input("Enter number of elements to insert: "))
print("Enter elements:")
for _ in range(n):
    val = int(input())
    btree.insert(val)
print("\nB-Tree Root Keys:", btree.root.keys)
for i, child in enumerate(btree.root.children):
    print(f"Child {i+1} keys:", child.keys)
key = int(input("\nEnter key to search: "))
if btree.search(btree.root, key):
    print(f"Key {key} found in B-Tree.")
else:
    print(f"Key {key} not found in B-Tree.")
