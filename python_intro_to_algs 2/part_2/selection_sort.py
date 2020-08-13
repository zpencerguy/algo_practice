from random import shuffle
from typing import List

__author__ = 'kclark'


def run_selection_sort_simulation():
    ordered_values = list(range(10000))  # 10,000 numbers
    input_values = ordered_values.copy()
    shuffle(input_values)

    sorted_values = _compute_selection_sort(input_values)

    assert sorted_values == ordered_values

    print(f'Selection Sort simulation on a list of {len(ordered_values)} numbers')


def _compute_selection_sort(input_values: List[int]):
    sorted_values = []

    for idx in range(len(input_values)):
        # find the smallest element in the list, then remove it from the list and add it onto the sorted list
        # starting a function name with _ means it should only be used in this module
        smallest_idx = _find_smallest_idx(input_values)
        sorted_values.append(input_values.pop(smallest_idx))

    return sorted_values


def _find_smallest_idx(input_values: List[int]) -> int:
    smallest_idx = 0  # store the index of the smallest value
    smallest = input_values[0]  # store the smallest value

    for idx in range(1, len(input_values)):
        if input_values[idx] < smallest:
            smallest = input_values[idx]
            smallest_idx = idx

    return smallest_idx


if __name__ == '__main__':
    run_selection_sort_simulation()
