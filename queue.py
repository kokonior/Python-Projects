class queue:
    def __init__(self):
        self.q=[]
        self.count=0

    def enque(self, value):
        self.q.append(value)
        self.count+=1

    def deque(self):
        if self.count>0:
            count=-1
            return self.q.pop(0)

#.................................................;;

obj=queue()

obj.enque(10)
obj.enque(20)
obj.enque(30)
print("Queue: ", obj.q)
print("popped item: " ,obj.deque())
