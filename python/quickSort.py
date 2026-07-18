import time

# Function to display partition steps
def display(arr):
    print(arr)

# Partition Function
def partition(arr, low, high):

    # Last element as Pivot
    pivot = arr[high]

    i = low - 1

    print("\nPivot =", pivot)

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print("After Partition:", end=" ")
    display(arr)

    return i + 1


# Quick Sort Function
def quick_sort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)

        quick_sort(arr, pi + 1, high)


# Main Program

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")

for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

quick_sort(arr, 0, n - 1)

end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nExecution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(n log n)")
print("Average Case Time Complexity : O(n log n)")
print("Worst Case Time Complexity   : O(n²)")
print("Space Complexity             : O(log n)")

print("\n========== Properties ==========")
print("Stable   : No")
print("In-Place : Yes")

print("\n========== Pivot Selection Strategy ==========")
print("Current Program uses LAST ELEMENT as Pivot")
print("Other Pivot Strategies:")
print("1. First Element")
print("2. Last Element")
print("3. Middle Element")
print("4. Random Pivot")
print("5. Median of Three")


