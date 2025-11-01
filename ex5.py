# ----------------------------------------
# Lab 5: Binary Search Tree Operations
# ----------------------------------------
print("Lab 5: Binary Search Tree Operations")
print("------------------------------------")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def insert(self, root, val):
        if root is None:
            return Node(val)
        if val < root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data:
            root.right = self.insert(root.right, val)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    def search(self, root, val):
        if root is None or root.data == val:
            return root
        if val < root.data:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
    def delete(self, root, val):
        if root is None:
            return root
        if val < root.data:
            root.left = self.delete(root.left, val)
        elif val > root.data:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root
bst = BST()
root = None
n = int(input("Enter number of elements to insert: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    root = bst.insert(root, val)
print("\nInorder traversal after insertion:", end=" ")
bst.inorder(root)
val = int(input("\n\nEnter value to search: "))
found_node = bst.search(root, val)
if found_node:
    print(f"Element {val} found in BST at index {i}")
else:
    print(f"Element {val} not found in BST")
val = int(input("\nEnter value to delete: "))
root = bst.delete(root, val)
print("\nInorder traversal after deletion:", end=" ")
bst.inorder(root)
print()
