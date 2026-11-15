
class QueueFromList:


    def __init__(self,k):
        self.k = k
        self.arr = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0


    def enqueue(self,val):
        if self.is_full():
            raise ValueError("Queue is Full")
        if self.is_empty():
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.k
        self.arr[self.rear] = val
        self.count += 1



    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.k
        self.count -= 1
            


    def visit(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def is_full(self):
        if self.count == self.k:
            return True
        return False

    def is_empty(self):
        if self.count == 0:
            return True
        return False




if __name__ == "__main__":
    # Example
    q = QueueFromList(10)
    print(q.is_empty())
    q.enqueue(12)
    q.enqueue(15)
    q.enqueue(13)
    q.enqueue(21)
    q.enqueue(12)
    q.enqueue(11)
    q.enqueue(18)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(1)
    print(q.is_full())
    for i in range(10):
        print(q.visit())
        q.dequeue()
