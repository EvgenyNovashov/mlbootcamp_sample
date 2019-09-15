def quicksort(A):
    print(A)
    if not A:
        return A
    pivot = A.pop()
    lA = list(filter(lambda x: x < pivot, A))
    rA = list(filter(lambda x: x > pivot, A))
    return quicksort(lA) + [pivot] + quicksort(rA)


a = [1, 5, 4, 7, 8, 9, 2, 3]

print(quicksort(a))