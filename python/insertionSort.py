import time

# Accept number of elements
n = int(input("Enter the number of elements: "))

arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

comparisons = 0
shifts = 0

# Start timer
start_time = time.perf_counter()

# Insertion Sort
for i in range(1, n):

    key = arr[i]
    j = i - 1

    while j >= 0:
        comparisons += 1

        if arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        else:
            break

    arr[j + 1] = key

    # Display intermediate passes
    print(f"\nPass {i}: ", end="")
    for x in arr:
        print(x, end=" ")

# Stop timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\n\nSorted Array:")
for x in arr:
    print(x, end=" ")

print("\n")
print("Comparisons :", comparisons)
print("Shifts      :", shifts)
print(f"Execution Time : {execution_time:.8f} seconds")

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(n)")
print("Average Case Time Complexity : O(n²)")
print("Worst Case Time Complexity   : O(n²)")
print("Space Complexity             : O(1)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : Yes")

print("\n========== Performance on Nearly Sorted Data ==========")
print("Insertion Sort performs very efficiently on nearly sorted arrays.")
print("It requires very few comparisons and shifts.")
print("Therefore, it performs much faster than Bubble Sort and Selection Sort on nearly sorted data.")

