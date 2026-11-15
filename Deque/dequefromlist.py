class DequeFromList:

    def __init__(self, k):
        self.k = k
        self.arr = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0
        

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.k) % self.k

        self.arr[self.front] = value
        self.count += 1
        return True
    

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k

        self.arr[self.rear] = value
        self.count += 1
        return True
        

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.arr[self.front] = None
        self.front = (self.front + 1 ) % self.k
        self.count -= 1
        return True
        

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.arr[self.rear] = None
        self.rear = ((self.rear - 1) + self.k) % self.k
        self.count -= 1
        return True
        

    def getFront(self):
        if self.count == 0:
            return -1
        return self.arr[self.front]
        

    def getRear(self):
        if self.count == 0:
            return -1
        return self.arr[self.rear]
        

    def isEmpty(self):
        if self.count == 0:
            return True
        return False
        

    def isFull(self):
        if self.count == self.k:
            return True
        return False
        


deque = DequeFromList(10)
deque.insertFront(10)
deque.insertLast(11)
deque.insertLast(12)
deque.insertFront(13)
print(deque.arr)
print(deque.getFront())
print(deque.getRear())