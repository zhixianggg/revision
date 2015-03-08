##Stack implemented with linked list
## master-class: Node
class Node(object):
    def __init__(self, initdata): #constructor
        self.data = initdata
        self.ptr = None

## get & set methods

    def getData(self):
        return self.data

    def getNext(self):
        return self.ptr

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newptr):
        self.ptr = newptr

##sub-class: Stack_front

class Stack_front_linkedlist(object): #implement stack using linked list
    '''implement stack using linked list
    push and pop from front of linked list'''
    def __init__(self):
        self.head = Node(None)

	##Stack_front return
	
    def __str__(self):
        '''print contents of stack'''
        text=""
        if self.isEmpty():
            return "Empty Stack!"
        temp=self.head.getNext()
        while temp!=None:
            text = text + "|{0:^30}|\n".format(temp.getData())
            temp = temp.getNext()
        text = text + "-"*32
        return text
	
	## method 1: isEmpty
    def isEmpty(self):
        return self.head.getNext()==None

	## method 2: push
    def push(self,data):
        newnode=Node(data)
        if self.isEmpty():
            self.head.setNext(newnode)
        else:
            newnode.setNext(self.head.getNext())
            self.head.setNext(newnode)

	## method 3: pop
    def pop(self):
        if self.isEmpty():
            print("Empty stack!")
        else:
            data=self.head.getNext()
            self.head.setNext((self.head.getNext))
            return data

	## method 4: peek
    def peek(self): #look at top of 
        if self.isEmpty():
            print("Empty stack!")
        else:
            return self.head.getNext().getData()
        
    
def infix2postfix(infix_exp): #parameter infix_exp is separated by space
    prec = {} #set precedence weight for operators
    prec["*"] = 3 
    prec["/"] = 3 
    prec["+"] = 2 
    prec["-"] = 2 
    prec["("] = 1 #lowest precedence
    opStack = Stack_front_linkedlist() #call an instance of stack
    postfixlist=[] #store final postfix result
    tokenlist = infix_exp.split() #get infix expression into a list

    #step 1
    opStack.push("(")
    tokenlist.append(")")
    

    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":     #step 2a
            postfixlist.append(token)
        elif token == "(": #step 2b
            opStack.push(token)
        elif token in "*/+-": #step 2c
            while (prec[opStack.peek()] >= prec[token]) and (not opStack.isEmpty()):
                postfixlist.append(opStack.pop())
            opStack.push(token)
        elif token == ")": #step 2d
            topToken = opStack.pop()
            while topToken != "(":
                postfixlist.append(topToken)
                topToken = opStack.pop()
                
    return " ".join(postfixlist)

print(infix2postfix("A + B"))


def postfixEval(postfix_exp):
    opStack = Stack_front_linkedlist() #call an instance of stack
    tokenlist = postfix_exp.split()
    #step 1 is unnecessary using Python
    for token in tokenlist: #step 2
        if token in "0123456789": #step 2a
            opStack.push(int(token))
        else: #step 2b, an operator
            operand_x = opStack.pop()
            operand_y = opStack.pop()
            #do the operation
            if token == "*":
                result = operand_y * operand_x
            elif token == "/":
                result = operand_y / operand_x
            elif token == "+":
                result = operand_y + operand_x
            else:
                result = operand_y - operand_x
            opStack.push(result)
    return opStack.pop()

print(postfixEval("5 6 2 + * 12 4 / -"))
