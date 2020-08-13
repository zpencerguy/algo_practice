from random import shuffle
from typing import List

__author__ = 'kclark'


def run_quick_sort_simulation():
    ordered_values = list(range(100000))  # 100,000 numbers
    input_values = ordered_values.copy()
    shuffle(input_values)

    sorted_values = _compute_quick_sort(input_values)

    assert sorted_values == ordered_values

    print(f'Quick Sort simulation on a list of {len(ordered_values)} numbers')
    return ordered_values


def _compute_quick_sort(input_values: List[int]):
    if len(input_values) < 2:
        # base case for lists with 0 or 1 elements are already "sorted"
        return input_values
    else:
        # recursive case to further divide-and-conquer problem
        pivot = input_values[0]

        # sub-arrays of all the elements less or greater than the pivot value
        # note: this could be optimized with a single loop over input_values and appending into the sub lists
        less_sub_list = [i for i in input_values[1:] if i <= pivot]
        greater_sub_list = [i for i in input_values[1:] if i > pivot]

        return _compute_quick_sort(less_sub_list) + [pivot] + _compute_quick_sort(greater_sub_list)


if __name__ == '__main__':
    run_quick_sort_simulation()
