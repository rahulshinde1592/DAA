import time

# Counting Sort according to the current digit
def counting_sort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10

    # Store count of occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count so that it contains positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]


# Radix Sort
def radix_sort(arr):

    max_num = max(arr)

    exp = 1
    passes = 0

    while max_num // exp > 0:

        counting_sort(arr, exp)

        passes += 1

        print(f"\nAfter Pass {passes} (Digit = {exp})")
        print(arr)

        exp *= 10

    return passes


# Main Program
n = int(input("Enter the number of elements: "))

arr = []

print(f"Enter {n} integers:")

for i in range(n):
    arr.append(int(input()))

start = time.perf_counter()



passes = radix_sort(arr)
passes = radix_sort(arr)
passes = radix_sort(arr)



end = time.perf_counter()
end = time.perf_counter()
end = time.perf_counter()



print("\nSorted Array:")
print("\nSorted Array:")
print("\nSorted Array:")
print(arr)
print(arr)
print(arr)



print("\nTotal Passes :", passes)
print("\nTotal Passes :", passes)
print("\nTotal Passes :", passes)



print("Execution Time : {:.8f} seconds".format(end - start))
print("Execution Time : {:.8f} seconds".format(end - start))
print("Execution Time : {:.8f} seconds".format(end - start))



print("\n========== Complexity Analysis ==========")
print("\n========== Complexity Analysis ==========")
print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Space Complexity             : O(n + k)")
print("Space Complexity             : O(n + k)")
print("Space Complexity             : O(n + k)")



print("\n========== Properties ==========")
print("\n========== Properties ==========")
print("\n========== Properties ==========")
print("Stable   : Yes")
print("Stable   : Yes")
print("Stable   : Yes")
print("In-Place : No")
print("In-Place : No")
print("In-Place : No")



print("\n========== Comparison with Quick Sort ==========")
print("\n========== Comparison with Quick Sort ==========")
print("\n========== Comparison with Quick Sort ==========")
print("Radix Sort is generally faster for sorting large")
print("Radix Sort is generally faster for sorting large")
print("Radix Sort is generally faster for sorting large")
print("integers with a fixed number of digits because")
print("integers with a fixed number of digits because")
print("integers with a fixed number of digits because")
print("it does not rely on comparisons.")
print("it does not rely on comparisons.")
print("it does not rely on comparisons.")
print("Quick Sort has average complexity O(n log n)")
print("Quick Sort has average complexity O(n log n)")
print("Quick Sort has average complexity O(n log n)")
print("while Radix Sort runs in O(d × (n + k)).")
print("while Radix Sort runs in O(d × (n + k)).")
print("while Radix Sort runs in O(d × (n + k)).")
end = time.perf_counter()
end = time.perf_counter()
end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nTotal Passes :", passes)

print("Execution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Space Complexity             : O(n + k)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : No")

print("\n========== Comparison with Quick Sort ==========")
print("Radix Sort is generally faster for sorting large")
print("integers with a fixed number of digits because")
print("it does not rely on comparisons.")
print("Quick Sort has average complexity O(n log n)")
print("while Radix Sort runs in O(d × (n + k)).")
end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nTotal Passes :", passes)

print("Execution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Space Complexity             : O(n + k)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : No")

print("\n========== Comparison with Quick Sort ==========")
print("Radix Sort is generally faster for sorting large")
print("integers with a fixed number of digits because")
print("it does not rely on comparisons.")
print("Quick Sort has average complexity O(n log n)")
print("while Radix Sort runs in O(d × (n + k)).")
end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nTotal Passes :", passes)

print("Execution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Space Complexity             : O(n + k)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : No")

print("\n========== Comparison with Quick Sort ==========")
print("Radix Sort is generally faster for sorting large")
print("integers with a fixed number of digits because")
print("it does not rely on comparisons.")
print("Quick Sort has average complexity O(n log n)")
print("while Radix Sort runs in O(d × (n + k)).")
end = time.perf_counter()

print("\nSorted Array:")
print(arr)

print("\nTotal Passes :", passes)

print("Execution Time : {:.8f} seconds".format(end - start))

print("\n========== Complexity Analysis ==========")
print("Best Case Time Complexity    : O(d × (n + k))")
print("Average Case Time Complexity : O(d × (n + k))")
print("Worst Case Time Complexity   : O(d × (n + k))")
print("Space Complexity             : O(n + k)")

print("\n========== Properties ==========")
print("Stable   : Yes")
print("In-Place : No")

print("\n========== Comparison with Quick Sort ==========")
print("Radix Sort is generally faster for sorting large")
print("integers with a fixed number of digits because")
print("it does not rely on comparisons.")
print("Quick Sort has average complexity O(n log n)")
print("while Radix Sort runs in O(d × (n + k)).")

