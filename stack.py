class Stack:
    def __init__(self):
        self.s=[]
        self.count=0

    def push(self, value):
        self.s.append(value)
        self.count+=1

    def pop(self):
        if self.count>0:
            count=-1
            return self.s.pop()

#.................................................;;

obj=Stack()

obj.push(10)
obj.push(20)
obj.push(30)
print("stack: ", obj.s)
print("popped item: ", obj.pop())
