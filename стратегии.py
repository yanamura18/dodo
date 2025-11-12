def first_fit(items, bin_capacity):
    """Стратегия First Fit"""
    bins = []
    for item in items:
        placed = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return bins

def first_fit_decreasing(items, bin_capacity):
    """Стратегия First Fit Decreasing"""
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, bin_capacity)

def best_fit(items, bin_capacity):
    """Стратегия Best Fit"""
    bins = []
    for item in items:
        best_bin = None
        min_space_left = bin_capacity + 1

        for bin in bins:
            space_left = bin_capacity - (sum(bin) + item)
            if 0 <= space_left < min_space_left:
                min_space_left = space_left
                best_bin = bin

        if best_bin is not None:
            best_bin.append(item)
        else:
            bins.append([item])
    return bins

def print_bins(bins, algorithm_name):
    """Вспомогательная функция для красивого вывода результатов"""
    print(f"{algorithm_name}:")
    for i, bin_content in enumerate(bins, 1):
        print(f"  Контейнер {i}: {bin_content} (Сумма: {sum(bin_content)})")
    print(f"  Всего контейнеров: {len(bins)}")
    print()

if __name__ == "__main__":
    main()
