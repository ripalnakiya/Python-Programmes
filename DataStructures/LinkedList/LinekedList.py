class Node:
    def _init_(self):
        self.data=None
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None

    def insertLast(self,value):
        node=Node()
        node.data=value
        if(self.head==None):
            self.head=node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node

    def insertFirst(self,value):
        node=Node()
        node.data=value
        
        if (self.head == None):
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    def size(self):
        count=0
        temp=self.head
        while(temp!=None):
            count+=1
            temp=temp.next
        print(count)

    def getFirst(self):
        print(self.head.data)

    def getLast(self):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        print(temp.data)

    def removeFirst(self):
        print(self.head.data)
        self.head=self.head.next

    def removeLast(self):
        if(self.head.next==None ): # or size()==1
            self.head=None
        else:
            temp=self.head
            prev=None
            while(temp.next!=None):
                prev=temp
                temp=temp.next
            print(temp.data)
            prev.next = None