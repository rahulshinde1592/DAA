import time

# Accept number of elements
n = int(input("Enter the number of elements: "))

# Accept array elements
arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

comparisons = 0
swaps = 0

# Start timer
start_time = time.perf_counter()

# Selection Sort
for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):

        comparisons += 1

        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

# Stop timer
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display sorted array
print("\nSorted Array:")
for num in arr:
    print(num, end=" ")

print("\n")

print("Number of Comparisons :", comparisons)
print("Number of Swaps       :", swaps)
print(f"Execution Time        : {execution_time:.8f} seconds")

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(n²)")
print("Average Case Time Complexity : O(n²)")
print("Worst Case Time Complexity   : O(n²)")
print("Space Complexity             : O(1)")

print("\n========== Properties ==========")
print("Stable   : No")
print("In-Place : Yes")

print("\n========== Why Selection Sort Performs Fewer Swaps ==========")
print("Selection Sort performs at most one swap in each pass.")
print("Bubble Sort swaps adjacent elements many times.")
print("Therefore, Selection Sort performs fewer swaps than Bubble Sort.")

