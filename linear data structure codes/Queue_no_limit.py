class Queue:
    def __init__(self):
        self.elements = []

      # is empty
    def is_empty(self):
        if self.elements == []:
            return True
        else:
            return False


  # add elements at end of the queue
    def enqueue(self, value):
        self.elements.append(value)
        return "value added in queue list"
    
      # pop dequeue element
    def dequeue(self):
        if self.is_empty():
            return "queue is empty can not pop first element"
            self.elements.pop(0)
            return "first element is removed "
      #get top value
    def peek(self):
      if self.is_empty():
        return "queue is empty can show top element"
      return self.elements[0]
    
      # delete all elements in queue
    def delete_all(self):
      if self.is_empty():
        return "queue is empty can not delete all elements "
      self.elements.clear()
      return 'all deleted '
    
      # print all elements
    def print_all(self):
      if self.is_empty():
        return "Queue is empty nothing to print"
      for i in self.elements:
        print(i)











