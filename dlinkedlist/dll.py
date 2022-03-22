class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            printl = printl + " <-> " if temp else printl
        print(printl)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        return new_node

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
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
        before = self.get(index-1)    # get the node on the index before we want to insert the new node
        after = before.next
        # redirect the next and prev pointers to insert new node
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1    
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

my_dlinked_list = DoublyLinkedList(1)
my_dlinked_list.append(2)
my_dlinked_list.append(5)
print(my_dlinked_list.get(0).value)
my_dlinked_list.append(4)
my_dlinked_list.prepend(15)
my_dlinked_list.print_list()
print(my_dlinked_list.get(0).value)
print(my_dlinked_list.get(3).value)
print(my_dlinked_list.get(4).value)
my_dlinked_list.pop()
my_dlinked_list.print_list()
print(my_dlinked_list.get(3).value)
my_dlinked_list.pop_first()
my_dlinked_list.set_value(2, 3)
my_dlinked_list.print_list()
print(my_dlinked_list.get(2).value)
my_dlinked_list.insert(1, 5)
my_dlinked_list.insert(3, 4)
my_dlinked_list.print_list()
my_dlinked_list.remove(1)
my_dlinked_list.print_list()
my_dlinked_list.remove(2)
my_dlinked_list.print_list()