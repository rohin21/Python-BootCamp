'''
Stack implementation in Python.
    Operations:
        push(item)
        pop()
        peek()
'''
class Stack:

    def __init__(self):
        self.stack = []

    # Returns the Size of the stack
    def size(self):
        if self.check_empty():
            return "The stack is empty"
        else:
            return "The size of the stack is : {}".format(len(self.stack))

    # Checks if the stack is empty
    def check_empty(self):
        return len(self.stack) == 0

    # Push an item to the top of the stack
    def push(self, item):
        self.stack.append(item)
        print("Pushed item : {} ".format(item))

    # Pop an item from the top of the stack.
    def pop(self):
        if self.check_empty():
            return "Stack is empty"
        return self.stack.pop()

    # Print the element at the top of the stack without removing it.
    def peek(self):
        if self.check_empty():
            print("The stack is empty")
        else:
            print("The element at the top is : {}".format(self.stack[-1]))
