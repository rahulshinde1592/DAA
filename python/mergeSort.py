import time

merge_count = 0

def merge(arr, left, mid, right):
    global merge_count

    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    merge_count += 1

    print(f"Merge {merge_count}: {arr}")


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# Main Program
n = int(input("Enter the number of elements: "))

arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()

merge_sort(arr, 0, n - 1)

end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nTotal Merge Operations :", merge_count)
print("Execution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(n log n)")
print("Average Case Time Complexity : O(n log n)")
print("Worst Case Time Complexity   : O(n log n)")
print("Space Complexity             : O(n)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : No")
