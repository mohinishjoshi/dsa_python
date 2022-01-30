from linked_list.Node import Node


class LinkedList:
    # def __init__(self):
    #     print("__init")
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def __init__(self, lst):
        self.head = None
        self.tail = None
        self.length = 0
        for val in lst:
            self.append(val)

        print(f'Initialize Linked List with elements:', lst)
        print(self)

    def __str__(self):
        curr = self.head
        value = ""
        while curr is not None:
            value += str(curr.value) + " -> "
            curr = curr.next
        return value.strip(" -> ")

    def push(self, value):
        print('Pushing to Linked List', value)
        print(self)

        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        if self.tail is None:
            self.tail = self.head
        print(self)
        print('Pushed to Linked List\n\n')

    def append(self, value):
        print('Append to Linked List', value)
        print(self)
        node = Node(value)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        print(self)
        print('Appended to Linked List \n\n')

    def insert(self, value, location=0):
        print('Insert into Linked List', value, location)
        print(self)
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return

        assert self.length >= location >= -1, "Location should be between -1(end) and length of List"

        if location == 0:
            self.push(value)
        elif location == -1 or location == self.length - 1:
            node.next = None
            self.tail.next = node
            self.tail = node
            self.length += 1
        else:
            curr = self.head
            for i in range(0, location):
                curr = curr.next
            node.next = curr.next
            curr.next = node
            self.length += 1
            if curr == self.tail:
                self.tail = curr

        print(self)
        print('Inserted into Linked List \n\n')

    def indexOf(self, value):
        print('Index of', value)
        print(self)
        assert self.head is not None, "List is empty"
        curr = self.head
        index = 0
        while curr is not None:
            if curr.value == value:
                break
            index += 1
            curr = curr.next
        if curr is not None and curr.value == value:
            return index
        else:
            return -1

    def pop(self):
        assert self.length > 0 and self.tail is not None, "The linked List is empty"
        print('Popping from the Linked List')
        print(self)
        curr = self.head
        while curr.next is not self.tail:
            curr = curr.next

        to_delete = self.tail
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        val = to_delete.value
        del to_delete
        print(self)
        return val

    def delete(self, location):
        assert self.length > location >= -1, "location should be between -1 and length of list"
        deletedNode = None
        print('Delete from Linked List', location)
        print(self)
#       Delete 1st(Head) Node. Location = 0
        if location == 0:
            deletedNode = self.head
            self.head = self.head.next
            self.length -= 1
            val = deletedNode.value
            del deletedNode
# Delete Last Node. Location = -1
        elif location == -1 or location == self.length - 1:
            val = self.pop()
# Delete node at location
        else:
            index = 1
            curr = self.head.next
            while index < location-1:
                curr = curr.next
                index += 1
            deletedNode = curr.next
            curr.next = deletedNode.next
            self.length -= 1
            val = deletedNode.value
            del deletedNode

        print(self)
        print('Deleted', val, "\n\n")
        return val

    def clear(self):
        print('Delete/Clear Linked List')
        self.head = None
        self.tail = None
        self.length = 0
        print('Delete/Clear Linked List completed', self)




# lst = LinkedList([1, 2, 3, 4])
# lst.push(5)
# lst.pop()
# lst.append(5)
# lst.insert(50, -1)
# lst.insert(60, 0)
# lst.insert(70, 3)
# lst.insert(80, 7)
# print("80", lst.indexOf(80))
# print("60", lst.indexOf(60))
# print("1", lst.indexOf(1))
# print(lst.delete(-1))
# print(lst.delete(0))
# print(lst.delete(3))
# lst.clear()
# print(lst)

