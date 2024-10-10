class Stack: 
    def __init__(self,n):
        self.stack= []
        self.n = n #maximum number of elements in the stack

    #methods/functions -1.Default functions, 2. Custom functions (depends on you what to do with the stack)
#1 Basic - default functions 
        
    def push(self,k): #adding item k into list 
        if len(self.stack) <self.n:
            self.stack.append(k)
        else:
            print("stack is full")
    
    def pop(self): #removes top item from the stack
        #if the stack is empty then we cannot pop anything from the stack 
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            self.stack.pop(-1) #deletes the last item from the stack and returns it 

    def top(self):#identify what is at the top of the stack 
        if len(self.stack) == 0:
            print("stack is empty")
        else:
           return self.stack[-1]
#custom methods - creating methods according to our choices or needs 
    def display(self):
        print(self.stack)

    def size(self):
        print(f"the length of the stack is {len(self.stack)}")


        

#example 
stack = Stack(5)
stack.push(3)
stack.push(4)
stack.push(7)
stack.push(9)
stack.push(2)
stack.display()
stack.size()

stack.pop()

stack.display()







