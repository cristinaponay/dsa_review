class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class Queue:
    # define the constructor
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        printq = ""
        while temp is not None:
            printq += str(temp.value)
            temp = temp.prev
            printq = printq + " <- " if temp else printq
            
        print(printq)

    # adding item to the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.prev = new_node
            self.last = new_node
        self.length += 1
    
    # remove the first in line from the queue
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first # the node we will remove from the queue
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.prev # the node behind the first will now become first
            temp.prev = None # now removing temp from queue

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(5)
my_queue.print_queue()
print("")
my_queue.dequeue()
my_queue.print_queue()
print("")
my_queue.dequeue()
my_queue.print_queue()