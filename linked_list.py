class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_linked_list(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        # if self.last_node is None:
        #     node = self.head
        #     while node.next_node:
        #         print("iter", node.data)
        #         node = node.next_node
        #
        #     node.next_node = Node(data, None)
        #     self.last_node = node.next_node
        #
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node

ll = LinkedList()
ll.insert_beginning("data4")
ll.insert_beginning("data3")
ll.insert_beginning("data2")
ll.insert_beginning("data1")
ll.insert_beginning("dataNovo")
ll.insert_at_end("dataend")
ll.print_linked_list()


"""
ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1

ll.print_linked_list()"""

