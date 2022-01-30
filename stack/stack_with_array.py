class StackWithArray:
    def __init__(self):
        self.top = -1
        self.length = 0
        self.stack = []

    def __str__(self):
        if self.top == -1:
            return "Stack Empty"
        else:
            curr = self.top
            values = []
            while curr >= 0:
                values.append(self.stack[curr])
                curr -= 1
            return "\n^\n".join([str(value) for value in values])

    def push(self, value):
        self.stack.append(value)
        self.top += 1
        print("___________________________________")
        print("After Pushing: ", value)
        print("Stack:\n")
        print(self)
        print("___________________________________\n\n")

    def pop(self):
        if self.top == -1:
            return
        else:
            value = self.peek()
            del self.stack[self.top]
            self.top -= 1

        print("___________________________________")
        print("After Popping: ", value)
        print("Stack:\n")
        print(self)
        print("___________________________________\n\n")

    def peek(self):
        if self.top == -1:
            return
        else:
            return self.stack[self.top]



# stack = StackWithArray()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("Peeking Top:", stack.peek())
# stack.pop()
# print("Peeking Top:", stack.peek())
# stack.pop()
# print("Peeking Top:", stack.peek())
