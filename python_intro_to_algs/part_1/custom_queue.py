class Queue:

    def __init__(self):
        self.customers = []

    def add(self, customer):
        print(f'Adding {customer} to the queue')
        self.customers.append(customer)

    def priority_add(self, customer):
        print(f'Adding {customer} to the front of the queue as a top priority')
        self.customers.insert(0, customer)

    def next(self):
        if self.customers:
            customer = f'Completed call with {self.customers.pop(0)}'
        else:
            customer = 'Nobody waiting in the queue'

        return f'{customer}'

    def size(self):
        queue_size = len(self.customers)

        response = f'Queue has {queue_size} customer(s) in it'

        if queue_size:
            for customer in self.customers:
                response += f'\n{customer}'

        return response


def run_custom_queue_example():
    queue = Queue()  # initialize Queue class instance
    queue.add('Maxwell Edison')  # add customer to queue
    queue.add('Loretta Martin')  # add customer to queue
    queue.add('Lovely Rita')  # add customer to queue
    queue.add('Mr. Mustard')  # add customer to queue

    # queue is adding up need to start serving customers while still taking in new customers
    print(queue.size())
    print(queue.next())
    print(queue.next())

    # important customer needs to be prioritized
    queue.priority_add('Her Majesty')

    # continue serving customers
    print(queue.next())
    print(queue.next())
    print(queue.next())
    print(queue.next())
    print(queue.size())

    # one more customer
    queue.add('Bungalow Bill')

    print(queue.size())
    print(queue.next())
    print(queue.size())


if __name__ == '__main__':
    run_custom_queue_example()