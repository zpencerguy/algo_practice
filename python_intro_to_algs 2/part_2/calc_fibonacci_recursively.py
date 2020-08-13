from fibonacci_test_cases import FIBONACCI_TEST_CASES

from typing import Tuple

__author__ = 'kclark'


def run_fibonacci_recursively():
    for test_case in FIBONACCI_TEST_CASES:
        sequence = test_case.get('sequence')
        expected_number = test_case.get('expected_number')<
        fib_number, fib_operations = calculate_fibonacci(sequence)

        assert fib_number == expected_number
        print(f'Sequence {sequence} => {expected_number} : {fib_operations} operations')


def calculate_fibonacci(nth_term: int, fib_operations: int = 0) -> Tuple[int, int]:
    fib_operations += 1

    if nth_term <= 1:
        return nth_term, fib_operations

    first_fib_number, first_fib_operations = calculate_fibonacci(nth_term-1, fib_operations)
    second_fib_number, second_fib_operations = calculate_fibonacci(nth_term-2, fib_operations)

    fib_number = first_fib_number + second_fib_number
    fib_operations = first_fib_operations + second_fib_operations

    return fib_number, fib_operations


if __name__ == '__main__':
    run_fibonacci_recursively()
