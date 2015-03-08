#stack implemented with list
class Stack_front(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        text=""
        for i in range((len(self.items)-1), -1, -1):
            text = text + "" + str(self.items[i])
        return text

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def dec_to_bin(decNumber):
    remainderstack = Stack_front()
    while decNumber != 0:
        remainderstack.push(decNumber%2)
        decNumber = decNumber//2
    print(remainderstack)

dec_to_bin(3)
dec_to_bin(6)
dec_to_bin(9)
dec_to_bin(12)
dec_to_bin(77)
dec_to_bin(129)



def dec_converter(decNumber,baseNumber):
    num = decNumber
    remainderstack = Stack_front()
    if baseNumber == 8:
        while decNumber != 0:
            remainderstack.push(decNumber%8)
            decNumber = decNumber // 8
        print('Octal for' ,num ,   'is', remainderstack)
        
    if baseNumber == 16:
        hexadeclist=[]
        hexadeclist=['A','B','C','D','E','F']
        while decNumber != 0:
            if (decNumber%16) >= 10:
                i = (decNumber %16) - 10
                remainderstack.push(hexadeclist[i])
            else:
                remainderstack.push(decNumber%16)
            decNumber = decNumber // 16
        print('Hex for' ,num ,   'is', remainderstack)

dec_converter(3,8)
dec_converter(3, 16)

dec_converter(7, 8)
dec_converter(7, 16)

dec_converter(8, 8)
dec_converter(8, 16)

dec_converter(15, 8)
dec_converter(15, 16)

dec_converter(55, 8)
dec_converter(55, 16)

dec_converter(129, 8)
dec_converter(129, 16)

def bin_to_dec(binNumber):
    stack = Stack_front()
    binNumber = str(binNumber)
    power = 0
    
    for i in range(len(binNumber)-1, -1,-1):
        num = ((2**power) * (int(binNumber[i])))
        stack.push(num)
        power += 1

    decNumber = 0
    while not stack.isEmpty():
        decNumber = decNumber + stack.pop()

    print(decNumber)

def anybase2decimal(number,base):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    stack = Stack_front()
    power = 0
    number = str(number)
    for i in range((len(number)-1), -1,-1):
        num = (base**power)*digits[(number[i])]
        stack.push(num)
        power += 1

    decNumber = 0
    while not stack.isEmpty():
        decNumber = decNumber + stack.pop()
    print('Dec for' , number ,   'is', decNumber)

BINARY = [1011,10001011,1100000010110101, 100010010010011010101011,11111010010110101010101110101100]

for number in BINARY:
    bin_to_dec(number)

Oct = [10,77,546, 3562]
Hex = ['1F', 'CAD', 'EBCA']

for number in Oct:
    anybase2decimal(number,8)

for number in Hex:
    anybase2decimal(number, 16)
    




