import time

# Accept number of elements
n = int(input("Enter the number of elements: "))

arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

comparisons = 0
movements = 0

start_time = time.perf_counter()

gap = n // 2

while gap > 0:

    for i in range(gap, n):

        temp = arr[i]
        j = i

        while j >= gap:

            comparisons += 1

            if arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                movements += 1
                j -= gap
            else:
                break

        arr[j] = temp

    print(f"\nArray after Gap = {gap}")
    print(arr)

    gap //= 2

end_time = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nComparisons :", comparisons)
print("Movements   :", movements)
print("Execution Time : {:.8f} seconds".format(end_time - start_time))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(n log n)")
print("Average Case Time Complexity : O(n^1.5)")
print("Worst Case Time Complexity   : O(n²)")
print("Space Complexity             : O(1)")

print("\n========== Properties ==========")
print("Stable   : No")
print("In-Place : Yes")

print("\n========== Comparison with Insertion Sort ==========")
print("Shell Sort is generally faster because it moves elements")
print("over larger gaps before performing the final insertion sort.")
print("Insertion Sort compares only adjacent elements.")


