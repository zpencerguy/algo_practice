from part_2.fibonacci_test_cases import FIBONACCI_TEST_CASES

__author__ = 'kclark'


fibonacci_sequence_cache = {}


def run_fibonacci_recursively_condensed():
    for test_case in FIBONACCI_TEST_CASES:
        sequence = test_case.get('sequence')
        expected_number = test_case.get('expected_number')
        fib_number = calculate_fibonacci(sequence)

        assert fib_number == expected_number
        print(f'Sequence {sequence} => {expected_number}')


def calculate_fibonacci(nth_term: int,) -> int:
    if nth_term in fibonacci_sequence_cache:
        fib_number = fibonacci_sequence_cache[nth_term]
        return fib_number

    if nth_term <= 1:
        return nth_term

    fib_number = calculate_fibonacci(nth_term-1) + calculate_fibonacci(nth_term-2)
    fibonacci_sequence_cache[nth_term] = fib_number

    return fib_number


if __name__ == '__main__':
    run_fibonacci_recursively_condensed()
