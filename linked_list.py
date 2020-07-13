class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_value(self):
        # returns the node's data
        return self.data

    def get_next(self):
        # returns the thing pointed at by the node's `next` reference
        return self.next

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next = new_next


node = Node(1)
node.set_next(Node(2))
