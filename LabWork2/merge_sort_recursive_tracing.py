def merge(left, right, indents=1):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0

    print("  " * indents + f"Зливаємо {left} та {right}")
    while i < len(left) and j < len(right):
        comparisons += 1
        cond = left[i] <= right[j]
        elem = left[i] if cond else right[j]
        print("  " * indents + f"  Порівняння: {left[i]} <= {right[j]} -> {cond}. Додаємо {elem}")
        if cond:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1

    while i < len(left):
        print("  " * indents + f"  Додаємо залишок з лівого масиву: {left[i]}")
        merged_arr.append(left[i])
        i += 1
        assignments += 1

    while j < len(right):
        print("  " * indents + f"  Додаємо залишок з правого масиву: {right[j]}")
        merged_arr.append(right[j])
        j += 1
        assignments += 1

    return merged_arr, comparisons, assignments


def merge_sort_recursive(arr, indents=1):
    comparisons = 0
    assignments = 0
    recursive_calls = 0

    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls

    mid = len(arr) // 2
    assignments += 1
    recursive_calls += 2

    # Рекурсивно ділимо масив на дві половини з відступами
    print("  " * indents + "Розділяємо масив:", arr[:mid])
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid], indents + 1)

    print("  " * indents + "Розділяємо масив:", arr[mid:])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:], indents + 1)

    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2

    # Зливаємо відсортовані половини
    merged_arr, c_merge, a_merge = merge(left_half, right_half, indents)
    print("  " * (indents - 1) + "Злиття завершено. Результат:", merged_arr)

    comparisons += c_merge
    assignments += a_merge

    return merged_arr, comparisons, assignments, recursive_calls


if __name__ == "__main__":
    my_list = [7, 89, 4, 68, 70, 49, 10, 62, 51]
    print("--- РЕКУРСИВНА ВЕРСІЯ ---")
    print("Розділяємо масив:", my_list)
    sorted_list, comps, assigs, rec_calls = merge_sort_recursive(my_list, indents=1)
    print("Фінальний відсортований список:", sorted_list)
    print(f"Загальна кількість порівнянь: {comps}")
    print(f"Загальна кількість присвоювань: {assigs}")
    print(f"Загальна кількість рекурсивних викликів: {rec_calls}")
