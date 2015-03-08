class Node():

    def __init__(self,rootdata):
        self.LeftP = int(0)
        self.Data = str(rootdata)
        self.RightP = int(0)

class BinaryTree(Node):
    '''inherit the attributes of Node'''
    def setRightChild(self, pointer):
        self.RightP = int(pointer)

    def getRightChild(self):
        return self.RightP

    def setLeftChild(self, pointer):
        self.LeftP = int(pointer)

    def getLeftChild(self):
        return self.LeftP

    def setRootVal(self, data):
        self.Data = data

    def getRootVal(self):
        return self.Data

    def AddItemToBinaryTree(NewFreeItem):
        global Root, NextFreePosition, LastMove, PreviousPosition

        if NextFreePosition == 0:
            print("ERROR No free node available.")
        else:
            ThisTree[NextFreePosition].setRootVal(str(NewTreeItem))
            ThisTree[NextFreePosition].setLeftChild(int(0))
            ThisTree[NextFreePosition].setRightChild(int(0))
            
        
        
        if Root == 0:
            Root = NextFreePosition
            else:
                '''traverse the tree to find the position for the new value'''
                CurrentPosition = Root
                LastMove = 'X'
                while not CurrentPosition == 0:
                    PreviousPosition == CurrentPosition:
                    if NewFreeItem < ThisTree[CurrentPosition].data:
                        '''move left'''
                        LastMove = 'L'
                        CurrentPosition = ThisTree[CurrentPosition].LeftP
                    else:
                        '''move right'''
                        LastMove = 'R'
                        CurrentPosition = ThisTree[CurrentPosition].RightP

        if LastMove = 'R':
            ThisTree[PreviousPosition].RightP = NextFreePosition
        else:
            ThisTree[PreviousPosition].LeftP = NextFreePosition
        NextFreePosition = ThisTree[NextFreePosition].LeftP

    
        
                

#initialise variables
Root = 0 #set Root to be 0 for initial empty binary tree
NextFreePosition = 1 #first free node is initialise to 1
LastMove = 'X'
PreviousPosition = Root

#initialise array of linked list of 20 nodes
ThisTree = [BinaryTree('') for x in range(21)]
#declare array of 20 nodes
#index 0 is ignored, start from index 1
#node 1 has index 1 in ThisTree, node 2 has index 2, and so on

#initialise left pointer of all nodes to point to next node
#except for last node, the left pointer is 0
for i in range(1,20):
    ThisTree[i].LeftP = int(i+1)
ThisTree[20].LeftP = int(0) #assign left pointer of node 20 to 0

#initialise right pointer of all nodes to be 0
for i in range(1,21):
    ThisTree[i].RightP = int(0)



def OutputData():
    print("Value of Root is", Root)
    print("Value of NextFreePosition is", NextFreePosition)
    print("Contents of ThisTree in index order is")
    print("-"*56) #print a line on screen
    print("|{0:^6}|{1:^15}|{2:^15}|{3:^15}|".format("Node","Left","Data","Right"))
    print("-"*56) #print a line on screen
                  

    for i in range(1,21):
          if ThisTree[i].getRootVal() != '':  #check for non-empty data
              print(("|{0:^6}|{1:^15}|{2:^15}|{3:^15}|").\
                    format(i,ThisTree[i].getLeftChild(),ThisTree[i].getRootVal(),ThisTree[i].RightChild())

    print("-"*56) #print a line on screen

def inorder(tree, index): #Task 3.6: display in alphabetical order
    if index != 0:                              #if not child/leaf node
        inorder(tree, tree[index].getLeftChild()) #process left subtree in inorder
        print(tree[index].getRootVal()) # access root node
        inorder(tree, tree[index].getRightChild()) #process right subtree in inorder
    
    
def main(): #Task 3.4
    global ThisTree
    newdata = input("Enter new data items to be added to binary tree. [XXX to end]\n>>>")
    while newdata != "XXX":
        AddItem            
