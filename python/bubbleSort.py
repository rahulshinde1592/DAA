# Bubble Sort Algorithm
# Program to sort n integers in ascending order
# Counts comparisons and swaps
# Displays performance analysis

# Accept number of elements
n = int(input("Enter the number of elements: "))

# Accept array elements
arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

comparisons = 0
swaps = 0

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        comparisons += 1

        if arr[j] > arr[j + 1]:
            # Swap elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            swaps += 1
            swapped = True

    # Stop if already sorted
    if not swapped:
        break

# Display sorted array
print("\nSorted Array:")
for num in arr:
    print(num, end=" ")

# Display comparisons and swaps
print("\n")
print("Number of Comparisons :", comparisons)
print("Number of Swaps       :", swaps)

# Performance Analysis
print("\n========== Performance Analysis ==========")
print("Best Case Time Complexity    : O(n)")
print("Average Case Time Complexity : O(n²)")
print("Worst Case Time Complexity   : O(n²)")
print("Space Complexity             : O(1)")

# Properties
print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : Yes")
