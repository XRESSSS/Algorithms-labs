def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            return j, comparisons, assignments

        a[i], a[j] = a[j], a[i]
        assignments += 3


def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)

        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


if __name__ == "__main__":
    my_list = [7, 89, 4, 68, 70, 49, 10, 62, 51]
    original_list = my_list.copy()
    print("Оригінальний список:", original_list)
    comps, assigs, rec_calls = quicksort(my_list, 0, len(my_list) - 1)
    print("Відсортований список:", my_list)
    print(f"Загальна кількість порівнянь: {comps}")
    print(f"Загальна кількість присвоювань: {assigs}")
    print(f"Загальна кількість рекурсивних викликів: {rec_calls}")
