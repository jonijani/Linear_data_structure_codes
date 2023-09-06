class Stack:
    def __init__(self):
        self.list = []

    # is Empty
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False




if __name__=='__main__':
    stack = Stack()

    print(stack.is_empty())



