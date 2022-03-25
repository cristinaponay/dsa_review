class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            # if new node is less than value then go left
            if new_node.value < temp.value: 
                # if left node is free, then place the new node there
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # if new node is greater than value then go right
            else:
                # if the right node is free, then place the new node there
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        # will keep running while temp is not none
        while temp is not None:
            # is value less than value of temp, then go left
            if value < temp.value:
                temp = temp.left
            # is value greater than value of temp, then go left
            elif value > temp.value:
                temp =  temp.right
            else:
                # value is found!
                return True
        return False 

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("root", my_tree.root.value)
print("left", my_tree.root.left.value)
print("right", my_tree.root.right.value)
print(my_tree.contains(27))
print(my_tree.contains(17))
print("min", my_tree.min_value_node(my_tree.root).value)
print("min", my_tree.min_value_node(my_tree.root.right).value)