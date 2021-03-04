import random

class Reverse_Node:
    def __init__(self, prev_Node, data):
        self.data = data
        self.prev_Node = prev_Node


class Reverse_Linked_List:
    def __init__(self, data):
        self.head = Reverse_Node(None, data)

    def add_Node(self, data):
        self.head = Reverse_Node(self.head, data)

    # def remove_node(self, Node, data):
    # if Node.data == data

    def find_data(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.prev_Node
            del temp
        elif self.head.prev_Node is not None:
            iterate_reverse_ll(self.head, self.head.prev_Node, data)


def iterate_reverse_ll(prev_node, next_node, data):
    if next_node is None:
        return
    elif next_node.data == data:
        prev_node.prev_Node = next_node.prev_Node
        del next_node
    else:
        iterate_reverse_ll(next_node, next_node.prev_Node, data)

def print_all_reverse_nodes(rev_node):
    if rev_node is None:
        return
    else:
        print("({})<--------".format(rev_node.data))
        print_all_reverse_nodes(rev_node.prev_Node)

'''

ll = Reverse_Linked_List(0)
for x in range(1,40):
    ll.add_Node(x)

print_all_reverse_nodes(ll.head)
print()
print()
ll.find_data(29)
print_all_reverse_nodes(ll.head)
print()
print()
ll.find_data(40)

for x in range(15,40):
    ll.find_data(x)

print_all_reverse_nodes(ll.head)
'''