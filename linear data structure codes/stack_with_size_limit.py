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
    
    def get_top_element_value(self):
        if self.is_empty():
            return 'stack is empty'
        return self.list[len(self.list)-1]
    
        # delete all elements in list
    def delete_all_elements_in_stack(self):
        if self.is_empty():
            return 'its already empty'
        self.list.clear()
        return 'all elements are deleted'
    
        # print_all elements
    def print_all(self):
        if self.is_empty():
            print('nothing to print')
            return 'stack is empty nothing to print'
        for i in range(len(self.list),0,-1):
            print(i)

  
    

if __name__=='__main__':
    stack = Stack(10)

    print('is it empty ? :',stack.is_empty())

     #stack.add_element_stack(v1)
    # print('is it empty ? :',stack.is_empty())

    # print('is stack full ? :',stack.is_stack_full())

    #v1 = Stack(1)

    stack.add_element_stack(1)
    stack.add_element_stack(2)
    stack.add_element_stack(3)
    stack.add_element_stack(4)
    stack.add_element_stack(5)
    stack.add_element_stack(6)
    # stack.pop_top_element_in_stack()


   

    # print('top element value is : ',stack.get_top_element_value())
    
    #stack.delete_all_elements_in_stack()
    stack.print_all()
    stack.delete_all_elements_in_stack()
    stack.print_all()






