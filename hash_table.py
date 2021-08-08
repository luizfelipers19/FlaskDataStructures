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
        self.hash_table = [None] * table_size

    def custom_hash(self,key): #function to create a hashed_key from the key value of our given node
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value): #creating a new Node at the custom hashed_key position we'll generate
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            #if the index specified by our hashed_key is not None
            #that's the case when there's already one node at this location,
            # so we make this node point to our new one, in a LinkedList format
            node = self.hash_table[hashed_key] #setting our head node to be the current hashtable item
            while node.next_node: #while there is a next node to our current node, we will traverse them, until we reach the end of them
                node = node.next_node  ## traversing to the last node
            node.next_node = Node(Data(key,value), None) #creating a new Node, without a nextNode assigned

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            if key == node.data.key:
                return node.data.value
        return None

