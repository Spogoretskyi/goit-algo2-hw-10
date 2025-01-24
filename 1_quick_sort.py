import random
import time
import matplotlib.pyplot as plt
import numpy as np


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    return time.time() - start_time


if __name__ == "__main__":
    array_sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times = []
    deterministic_times = []

    # Проведення вимірювань
    for size in array_sizes:
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]

        # Вимірюємо середній час виконання рандомізованого QuickSort
        random_time = np.mean(
            [
                measure_execution_time(randomized_quick_sort, test_array)
                for _ in range(5)
            ]
        )
        randomized_times.append(random_time)

        # Вимірюємо середній час виконання детермінованого QuickSort
        determ_time = np.mean(
            [
                measure_execution_time(deterministic_quick_sort, test_array)
                for _ in range(5)
            ]
        )
        deterministic_times.append(determ_time)

    # Вивід результатів у термінал
    for i, size in enumerate(array_sizes):
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {randomized_times[i]:.4f} секунд")
        print(f"   Детермінований QuickSort: {deterministic_times[i]:.4f} секунд")

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(
        array_sizes, randomized_times, marker="o", label="Рандомізований QuickSort"
    )
    plt.plot(
        array_sizes, deterministic_times, marker="s", label="Детермінований QuickSort"
    )
    plt.title("Порівняння часу виконання QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Час виконання (секунди)")
    plt.legend()
    plt.grid(True)
    plt.show()
