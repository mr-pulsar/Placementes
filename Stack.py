class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class Stack:
    def __init__(self) -> None:
        self.head = None
        self.temp = None
    def create(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.temp=node
        else:
            node.next=self.head
            self.head=node
    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next
sanjay=Stack()
l=list(map(int,input().split()))
for i in l:
    sanjay.create(i)
sanjay.print()