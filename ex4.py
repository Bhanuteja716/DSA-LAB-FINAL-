print("Lab 4: Insertion Sort and Merge Sort")
print("------------------------------------")
import time
import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
n = int(input("Enter size of list: "))
nums = []
for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    nums.append(val)
print("\nOriginal List:", nums)
for func in [insertion_sort, merge_sort]:
    arr = nums.copy()  # Copy list to avoid modifying original
    start = time.time()  # Start timer
    sorted_arr = func(arr)  # Perform sorting
    elapsed = round(time.time() - start, 6)  # Time taken
    print(f"\n{func.__name__.replace('_', ' ').title()} Result: {sorted_arr}")
    print("Time Taken:", elapsed, "seconds")
rand_list = random.sample(range(1, 1000), 50)
print("\nRandom 50 Elements Generated:")
print(rand_list)
for func in [insertion_sort, merge_sort]:
    arr = rand_list.copy()
    start = time.time()
    sorted_arr = func(arr)
    elapsed = round(time.time() - start, 6)
    print(f"\n{func.__name__.replace('_', ' ').title()} Sorted Result: {sorted_arr}")
    print("Time Taken:", elapsed, "seconds")
