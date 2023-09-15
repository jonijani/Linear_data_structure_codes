class Stack:
    def __init__(self):
        self.list = []

    # is Empty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
        
        # append method
    def add_element(self,value):
        self.list.append(value)
        return 'value added to stack list'
    
        # pop method
    def pop_last_element(self):
        if self.is_empty():
            print('stack list is empty')
        return self.list.pop()
    
        # get top element    
    def get_peek_element(self):
        if self.is_empty():
            print('stack list is empty')
        return self.list[len(self.list)-1]

    # delete all elemeents in list
    def delete_all_elements(self):
        self.list = None
        return 'all elements are  deleted in list'


    # print_all
    def print_all(self):
        if self.is_empty():
            raise Exception ('stack list is  empty')

        for i in range(len(self.list),0,-1):
            print(i)




if __name__=='__main__':
    stack = Stack()
    
    stack.add_element(1)
    stack.add_element(2)
    stack.add_element(3)
    stack.add_element(4)
    stack.add_element(5)
    stack.add_element(6)



    #stack.is_empty()
    #print(stack.list)
    #print('is empty ?: ',stack.is_empty())
    stack.print_all()
    #print('pop last element:', stack.pop_last_element())

    #print('top element of the list is :', stack.get_peek_element())

    print(stack.delete_all_elements())

    stack.print_all()















