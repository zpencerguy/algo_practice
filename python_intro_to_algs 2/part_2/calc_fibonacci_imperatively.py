from part_2.fibonacci_test_cases import FIBONACCI_TEST_CASES

from typing import Tuple

__author__ = 'kclark'


def run_fibonacci_imperatively():
    for test_case in FIBONACCI_TEST_CASES:
        sequence = test_case.get('sequence')
        expected_number = test_case.get('expected_number')
        fib_number, fib_operations = calculate_fibonacci(sequence)

        assert fib_number == expected_number
        print(f'Sequence {sequence} => {expected_number} : {fib_operations} operations')


#  type hinting ->
def calculate_fibonacci(nth_term: int) -> Tuple[int, int]:
    fib_operations = 0
    fib_number = 0
    fib_next = 1

    if nth_term <= 1:
        fib_operations = 1
        fib_number = nth_term
        return fib_number, fib_operations

    while fib_operations < nth_term:
        fib_shift = fib_number + fib_next
        fib_number = fib_next
        fib_next = fib_shift
        fib_operations += 1

    return fib_number, fib_operations


if __name__ == '__main__':
    run_fibonacci_imperatively()
