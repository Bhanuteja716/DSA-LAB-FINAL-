print("Lab 1: Array Operations (Without Inbuilt Methods)")
print("-----------------------------------------------")
print("K R N Bhanu Teja : CSE24210 : CSE-C")

# Function to traverse and display array
def traverse(arr):
    print("\nCurrent array elements:")
    for elem in arr:
        print(elem, end=' ')
    print("\n")

# Function to insert element at a given position
def insert_pos(arr, pos, element):
    n = len(arr)
    new_arr = [0] * (n + 1)
    for i in range(pos):
        new_arr[i] = arr[i]
    new_arr[pos] = element
    for i in range(pos, n):
        new_arr[i + 1] = arr[i]
    return new_arr

# Function to delete element from a given position
def delete_pos(arr, pos):
    n = len(arr)
    if pos < 0 or pos >= n:
        print("Invalid position!")
        return arr
    new_arr = [0] * (n - 1)
    for i in range(pos):
        new_arr[i] = arr[i]
    for i in range(pos + 1, n):
        new_arr[i - 1] = arr[i]
    return new_arr

# Function for linear search
def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

# Function to update element at given index
def update_at_index(arr, pos, element):
    if pos < 0 or pos >= len(arr):
        print("Invalid index!")
        return arr
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        if i == pos:
            new_arr[i] = element
        else:
            new_arr[i] = arr[i]
    return new_arr

# --- Main Program ---
n = int(input("Enter size of the array: "))
arr = [0] * n

print("\nEnter array elements:")
for i in range(n):
    val = int(input(f"Element {i+1}: "))
    arr[i] = val

# Display array
traverse(arr)

# Insert element
pos = int(input("Enter position to insert element: "))
element = int(input("Enter element to insert: "))
arr = insert_pos(arr, pos, element)
traverse(arr)

# Delete element
pos = int(input("Enter position to delete element: "))
arr = delete_pos(arr, pos)
traverse(arr)

# Search element
element = int(input("Enter element to search: "))
index = linear_search(arr, element)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found!")

# Update element
pos = int(input("Enter index to update: "))
element = int(input("Enter new element: "))
arr = update_at_index(arr, pos, element)
traverse(arr)
