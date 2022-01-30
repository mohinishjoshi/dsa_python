class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def __str__(self):
        return f"Node - {self.value}"
