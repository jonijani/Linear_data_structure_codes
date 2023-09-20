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



  
    

if __name__=='__main__':
    stack = Stack(10)

    print('is it empty ? :',stack.is_empty())






