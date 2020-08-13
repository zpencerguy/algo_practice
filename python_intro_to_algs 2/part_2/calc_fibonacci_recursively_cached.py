from typing import NamedTuple

from fibonacci_test_cases import FIBONACCI_TEST_CASES

__author__ = 'kclark'

# light weight way to store 'state' or cache data (3.7 has data class)
class FibonacciResult(NamedTuple):
    number: int
    operations: int = 0


fibonacci_sequence_cache = {}


def run_fibonacci_recursively_cached():
    for test_case in FIBONACCI_TEST_CASES:
        sequence = test_case.get('sequence')
        expected_number = test_case.get('expected_number')
        fib_result = calculate_fibonacci(sequence)

        assert fib_result.number == expected_number
        print(f'Sequence {sequence} => {expected_number} : {fib_result.operations} operations')


def calculate_fibonacci(nth_term: int, fib_operations: int = 0) -> FibonacciResult:
    fib_operations += 1

    if nth_term in fibonacci_sequence_cache:
        fib_number = fibonacci_sequence_cache[nth_term]
        return FibonacciResult(fib_number, fib_operations)

    if nth_term <= 1:
        return FibonacciResult(nth_term, fib_operations)

    first_fib_result = calculate_fibonacci(nth_term-1, fib_operations)
    second_fib_result = calculate_fibonacci(nth_term-2, fib_operations)

    fib_number = first_fib_result.number + second_fib_result.number
    fib_operations = first_fib_result.operations + second_fib_result.operations
    fibonacci_sequence_cache[nth_term] = fib_number

    return FibonacciResult(fib_number, fib_operations)


if __name__ == '__main__':
    run_fibonacci_recursively_cached()
