from part_1.custom_queue import run_custom_queue_example
from part_1.small_simple_search import run_small_simple_search
from part_1.small_binary_search import run_small_binary_search
from part_1.big_simple_search import run_big_simple_search
from part_1.big_binary_search import run_big_binary_search

# Intro to Algs - Part I Algs
part_1_run_config = {
  'custom_queue': True,
  'small_simple_search': False,
  'small_binary_search': False,
  'big_simple_search': False,
  'big_binary_search': False
}

if part_1_run_config.get('custom_queue'):
  run_custom_queue_example()

if part_1_run_config.get('small_simple_search'):
  run_small_simple_search()

if part_1_run_config.get('small_binary_search'):
  run_small_binary_search()

if part_1_run_config.get('big_simple_search'):
  run_big_simple_search()

if part_1_run_config.get('big_binary_search'):
  run_big_binary_search()