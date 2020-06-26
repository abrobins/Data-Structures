
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

# return all values in the list a -> b -> c -> d -> None
    def __str__(self):
        output = ''
        current_node = self.head  # create a tracker node variable - important
        while current_node is not None:  # loop until it's none - important
            output += f'{current_node.value}'
            # update tracker node to the next node - important
            current_node = current_node.next_node

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node  # need to better understand these 2 lines
            self.tail = new_node  # need to better understand

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def remove_tail(self):
        pass
        # if not self.head:
        #     return None

        # if self.head is self.tail:
        #     value = self.head.get_value()
        #     self.head = None
        #     self.tail = None
        #     return value

        # current = self.head

        # while current.get_next() is not self.tail:
        #     current = current.get_next()

        # value = self.tail.get_value()
        # self.tail = current
        # return value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        current = self.head.next_node
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next_node
        return max_value


# example
# linked_list = LinkedList()

# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')
# print(f'does our LL contain 2? {linked_list.contains(2)}')

# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.add_to_head(5)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.remove_head()
# print(f'the start of the list is {linked_list.head.value}')
