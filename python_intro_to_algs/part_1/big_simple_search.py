from random import choice
from statistics import mean

# Check if a customer vehicle selection still exists in inventory e.g. before a starting purchase.
# Return the number of search operations through the inventory before a matching stocknumber is found.


def run_big_simple_search():
    inventory = list(range(10000))
    inventory_count = len(inventory)

    simulations = []
    num_simulations = 1000

    for num in range(0, num_simulations):
        random_num = choice(range(0, inventory_count))
        customer_selection = inventory[random_num]

        num_operations = simple_search(inventory, customer_selection)

        simulations.append(num_operations)

    avg_num_operations = mean(simulations)
    max_num_operations = max(simulations)

    print(f'{num_simulations} Simple Search Simulations - {inventory_count} Inventory Count')
    print(f'Number of Operations - Worst-Case Scenario: {max_num_operations}')
    print(f'Number of Operations - Average-Case Scenario: {avg_num_operations}\n')


def simple_search(inventory, customer_selection):
    for index, stocknumber in enumerate(inventory):
        if stocknumber == customer_selection:
            num_operations = index + 1
            return num_operations


if __name__ == '__main__':
    run_big_simple_search()