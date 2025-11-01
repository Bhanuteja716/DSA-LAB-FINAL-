print("Lab 6: Min Heap and Heap Sort")
print("------------------------------")
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
def extract_min(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr.pop(0)
    root = arr[0]
    arr[0] = arr.pop()
    heapify(arr, len(arr), 0)
    return root
def insert_key(arr, key):
    arr.append(key)
    i = len(arr) - 1
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] < arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break
def heap_sort(arr):
    build_min_heap(arr)
    sorted_list = []
    temp = arr.copy()
    while temp:
        sorted_list.append(extract_min(temp))
    return sorted_list
n = int(input("Enter number of elements for heap: "))
nums = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    nums.append(element)
build_min_heap(nums)
print("\nMin-Heap:", nums)
min_val = extract_min(nums)
print("Extracted Min:", min_val)
new_val = int(input("Enter number to insert: "))
insert_key(nums, new_val)
print("After Insertion:", nums)
m = int(input("\nEnter number of elements for heap sort: "))
nums2 = []
for i in range(m):
    element = int(input(f"Enter element {i + 1}: "))
    nums2.append(element)
print("Heap Sort Result:", heap_sort(nums2))
