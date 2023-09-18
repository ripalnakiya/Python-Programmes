# Undirected Weighted Graph using Adjacency List (we use dictionary)

class UGraph:
    def __init__(self, vertices):
        # self.d = {i: [] for i in range(vertices)}
        self.d = {}
        for i in range(vertices):
            self.d[i] = []


    def addEdge(self, a, b, w):
        i = ord(a) - ord('A')
        j = ord(b) - ord('A')

        self.d[i].append([j,w]); 
        self.d[j].append([i,w]);            


    def display(self):
        for key, value in self.d.items():
            print(key, " : ", value)


    def isDconnected(self,start,end):
        start = ord(start) - ord('A')
        end = ord(end) - ord('A')

        for j in self.d[start]:
            if j[0] == end:
                return j[1]
        return False



g = UGraph(4)

g.addEdge('A','B',4)
g.addEdge('A','C',5)
g.addEdge('B','C',3)
g.addEdge('B','D',4)
g.addEdge('C','D',2)

# g.display()

start = input("Enter first Node: ")
end = input("Enter second Node: ")
print(g.isDconnected(start,end))

