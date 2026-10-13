def partition(a, l, r, indents=1):
    prefix = "  " * indents
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    i = l - 1
    j = r + 1
    assignments += 2

    print(f"{prefix}Вибираємо опорний елемент (pivot): {pivot}")

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
            sub = a[l:r + 1] if l < r else [a[l]]
            print(f"{prefix}Поточні індекси: i = {i}, j = {j}. Масив: {sub}")
            print(f"{prefix}Індекси перетнулися. Поділ завершено. Повертаємо j={j}.")
            return j, comparisons, assignments

        a[i], a[j] = a[j], a[i]
        assignments += 3
        sub = a[l:r + 1]
        print(f"{prefix}Поточні індекси: i = {i}, j = {j}. Обмінюємо a[{i}] ({a[i]}) i a[{j}] ({a[j]}). Масив: {sub}")


def quicksort(a, l, r, indents=0):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    print(f"Quicksort виклик: масив = {a}, l = {l}, r = {r}")

    if l < r:
        q, c1, a1 = partition(a, l, r, indents + 1)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q, indents + 1)
        c3, a3, r3 = quicksort(a, q + 1, r, indents + 1)

        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
        print(f"Після Quicksort для l={l}, r={r}: масив = {a}")
    else:
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


if __name__ == "__main__":
    my_list = [7, 89, 4, 68, 70, 49, 10, 62, 51]
    print("--- Quicksort за схемою Хоара з трасуванням ---")
    print("Оригінальний список:", my_list)
    sorted_list = my_list.copy()
    comps, assigs, rec_calls = quicksort(sorted_list, 0, len(sorted_list) - 1)
    print("\nФінальний відсортований список:", sorted_list)
    print(f"Загальна кількість порівнянь: {comps}")
    print(f"Загальна кількість присвоювань: {assigs}")
    print(f"Загальна кількість рекурсивних викликів: {rec_calls}")
