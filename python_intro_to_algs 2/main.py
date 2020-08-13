from part_1.custom_queue import run_custom_queue_example
from part_1.small_simple_search import run_small_simple_search
from part_1.small_binary_search import run_small_binary_search
from part_1.big_simple_search import run_big_simple_search
from part_1.big_binary_search import run_big_binary_search
from part_2.calc_fibonacci_imperatively import run_fibonacci_imperatively
from part_2.calc_fibonacci_recursively import run_fibonacci_recursively
from part_2.calc_fibonacci_recursively_cached import run_fibonacci_recursively_cached
from part_2.calc_fibonacci_recursively_condensed import run_fibonacci_recursively_condensed
from part_2.quick_sort import run_quick_sort_simulation
from part_2.selection_sort import run_selection_sort_simulation

# Intro to Algs - Part I
part_1_run_config = {
    'custom_queue': True,
    'small_simple_search': True,
    'small_binary_search': True,
    'big_simple_search': True,
    'big_binary_search': True
}

if part_1_run_config.get('custom_queue'):
    print('\nRun Custom Queue Example')
    run_custom_queue_example()

if part_1_run_config.get('small_simple_search'):
    print('\nRun Small Simple Search')
    run_small_simple_search()

if part_1_run_config.get('small_binary_search'):
    print('\nRun Small Binary Search')
    run_small_binary_search()

if part_1_run_config.get('big_simple_search'):
    print('\nRun Big Simple Search')
    run_big_simple_search()

if part_1_run_config.get('big_binary_search'):
    print('\nRun Big Binary Search')
    run_big_binary_search()


# Intro to Algs - Part II
part_2_run_config = {
    'fibonacci_imperatively': True,
    'fibonacci_recursively': True,
    'fibonacci_recursively_cached': True,
    'fibonacci_recursively_condensed': True,
    'selection_sort': True,
    'quick_sort': True
}

if part_2_run_config.get('fibonacci_imperatively'):
    print('\nRun Fibonacci Imperatively')
    run_fibonacci_imperatively()

if part_2_run_config.get('fibonacci_recursively'):
    print('\nRun Fibonacci Recursively')
    run_fibonacci_recursively()

if part_2_run_config.get('fibonacci_recursively_cached'):
    print('\nRun Fibonacci Recursively Cached')
    run_fibonacci_recursively_cached()

if part_2_run_config.get('fibonacci_recursively_condensed'):
    print('\nRun Fibonacci Recurisvely Condensed')
    run_fibonacci_recursively_condensed()

if part_2_run_config.get('selection_sort'):
    print('\nRun Selection Sort')
    run_selection_sort_simulation()

if part_2_run_config.get('quick_sort'):
    print('\nRun Quick Sort')
    run_quick_sort_simulation()
