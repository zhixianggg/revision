##super-class: Stack
class Stack_front(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        text=""
        for i in range((len(self.items)-1), -1, -1):
            text = text + "  " + self.items[i]
        return text

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def infix2postfix(infix_exp): #parameter infix_exp is separated by space
    prec = {} #set precedence weight for operators
    prec["*"] = 3 
    prec["/"] = 3 
    prec["+"] = 2 
    prec["-"] = 2 
    prec["("] = 1 #lowest precedence
    opStack = Stack_front() #call an instance of stack
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
print(infix2postfix("3 + 7"))
print(infix2postfix("5 * ( 6 + 2 ) - 12 / 4"))

def postfixEval(postfix_exp):
    opStack = Stack_front() #call an instance of stack
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
