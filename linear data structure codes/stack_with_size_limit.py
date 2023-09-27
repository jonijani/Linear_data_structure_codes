class Stack:
    def __init__(self,max_size):
        self.list = []
        self.max_size = max_size
    
    # is stack empty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # id stack full
    def is_stack_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    # add element to stack
    def add_element_stack(self,value):
        if self.is_stack_full():
            return 'stack is full new element cant be added'
        elif len(self.list) == self.max_size:
                return 'new element cant be added as max limit exceeded'
        return self.list.append(value)


        # pop top element of stack
    def pop_top_element_in_stack(self):
        if self.is_empty():
            return 'stack is empty'
        return self.list.pop()
  
    

if __name__=='__main__':
    stack = Stack(10)

    print('is it empty ? :',stack.is_empty())






