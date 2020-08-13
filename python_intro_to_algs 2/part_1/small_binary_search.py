from random import choice
from statistics import mean

# Check if a customer vehicle selection still exists in inventory e.g. before a starting purchase.
# Return the number of search operations through the inventory before a matching stocknumber is found.


def run_small_binary_search():
    inventory = [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 20008, 20009]
    inventory_count = len(inventory)

    simulations = []
    num_simulations = 1000

    for num in range(0, num_simulations):
        random_num = choice(range(0, inventory_count))
        customer_selection = inventory[random_num]

        num_operations = binary_search(inventory, customer_selection)

        simulations.append(num_operations)

    avg_num_operations = mean(simulations)
    max_num_operations = max(simulations)

    print(f'{num_simulations} Binary Search Simulations - {inventory_count} Inventory Count')
    print(f'Number of Operations - Worst-Case Scenario: {max_num_operations}')
    print(f'Number of Operations - Average-Case Scenario: {avg_num_operations}\n')


def binary_search(inventory, customer_selection):
    # track search count iterations
    num_operations = 0

    # low and high keep track of which part the inventory list we'll search in
    low = 0
    high = len(inventory) - 1

    # run while we haven't narrowed it down to one stocknumber
    while low <= high:
        num_operations += 1

        # check the middle element
        mid = int((low + high) / 2)
        stocknumber = inventory[mid]

        # found the matching stocknumber
        if stocknumber == customer_selection:
            return num_operations

        # stocknumber guess is either too high or too low - cut list in half accordingly
        if stocknumber > customer_selection:
            high = mid - 1
        else:
            low = mid + 1

    # stocknumber does not exist in inventory
    return None


if __name__ == '__main__':
    run_small_binary_search()