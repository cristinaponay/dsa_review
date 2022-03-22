class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
            # if temp: print("'")

    # define the push function
    def push(self, value):
        new_node = Node(value)  # create new node
        if self.height == 0:
            self.top = new_node # make new node as top
        else:
            new_node.next = self.top # set the current top as next node
            self.top = new_node     # set the new node the new top
        self.height += 1    # increment height
        return new_node

    # define the pop function
    def pop(self):
        if self.height == 0:
            return None # nothing to pop
        temp = self.top
        self.top = temp.next    # set node next to temp as the new top
        temp.next = None    # set the next node of temp to None to remove it from the stack
        self.height -= 1 # decrement the height
        return temp

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(1)
my_stack.print_stack()
my_stack.pop()
print("\n")
my_stack.print_stack()
my_stack.pop()
print("\n")
my_stack.print_stack()