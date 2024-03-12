class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self) -> None:
        self.head=None
        self.temp=None
    def create(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.temp=node
        else:
            self.temp.next=node
            self.temp=node
    def print(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next

sanjay=Linked_List()
l=list(map(int,input().split()))
for i in l:
    sanjay.create(i)
sanjay.print()