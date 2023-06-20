class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def print_ll(self):
        if self.is_empty():
            print("list is Empty")
            return
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
        
if __name__ == "__main__":
    ll = SinglyLL()
        

