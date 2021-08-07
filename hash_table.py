class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data,
        self.next_node = next_node

class Data:
    def __init__(self,key, value):
        self.key = key,
        self.value = value

class Hashtable:
    def __init__(self, table_size):
        self.table_size = table_size