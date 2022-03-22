class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        printl = ""
        while temp is not None:
            # print(temp.value)
            printl += str(temp.value)
            temp = temp.next
            printl = printl + " -> " if temp else printl
        print(printl)
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        # if list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # point new node's next pointer to the current head
            self.head = new_node # new node is now the head
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head    # set temp to head
        self.head = self.head.next  # set the next node to head as the new head
        temp.next = None # removes the old head from the list
        self.length -= 1
        # checks if length is now 0 after decrementing
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            # print(temp.value)
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        # if inserting at index 0, we can use the prepend()
        if index == 0:
            return self.prepend(value)
        # if inserting at the end, we can use the append()
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)    # get the node on the index before we want to insert the new node
        # first let new node point next to node of temp
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1    
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        prev = self.get(index-1) # get the index of the node before the node we are removing
        temp = prev.next    # the node we are removing
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # exchange the places of head and tail to reverse the list
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next   # this was the head
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
print("")
print(my_linked_list.get(2).value)
my_linked_list.insert(2, 2)
print(my_linked_list.get(2).value)
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
print("")
my_linked_list.print_list()
print("")
print(my_linked_list.remove(4).value)
print(my_linked_list.remove(2).value)
print("")
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
