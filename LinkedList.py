##super-class Node

class Node(object):

    def __init__(self,data=None, ptr=None):
        '''node with data and ptr'''
        self.data = data
        self.ptr = None

#Method 1: __str__(self)
    def __str__(self):
        '''str representation of data part of Node'''
        return str(self.data)

##sub-class LinkedList
class LinkedList(object):

    def __init__(self):
        node = Node(None, None)
        self.first = node
        self.length = 0

##Method 1: __str__(self)
    def __str__(self):
        text=''
        self.temp = self.first
        count=self.length
        while count != 0:
            text = text + "|" + self.temp.data + "|->"
            self.temp = self.temp.ptr
            count -= 1
        return text

##Method 2: isEmpty(self)
    def isEmpty(self):
        '''returns true if linked list is empty'''
        return self.length == 0

##Method 3: insertfront(self,data)
    def insertfront(self, data):
        node = Node(data)
        if self.isEmpty(): #empty linked list
            self.first = node
            self.length += 1
        else:
            self.temp = self.first
            self.first = node
            self.first.ptr = self.temp
            self.length += 1

##Method 4: insertlast(self,data)
    def insertlast(self,data):
        node = Node(data) #create instance of a node.
        if self.isEmpty():
            self.first = node #let first node be the node you inserted.
            self.length += 1 #increment length of linked list.
        else:
            self.temp = self.first 
            while self.temp.ptr != None:
                self.temp = self.temp.ptr #these 3 lines are to find the last node(before it is null)
            self.temp.ptr = node
            self.length += 1

##Method 5: removelast(self)
    def removelast(self):
        if self.isEmpty():  #empty linked list
            print("\nError: Nothing to remove!")
        else:
            self.prev = self.first
            self.curr = self.first
            while self.curr.ptr != None:
                self.prev = self.curr
                self.curr = self.curr.ptr
            self.prev.ptr = None
            self.length -= 1

    
            
