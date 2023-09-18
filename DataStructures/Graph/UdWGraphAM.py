<<<<<<< HEAD
# Undirected Weighted Graph using Adjacency Matrix (we use 2D List)

class UGraph:
    def __init__(self, vertices):
        # self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.matrix = []
        for i in range(vertices):
            row=[]
            for j in range(vertices):
                row.append(0)
            self.matrix.append(row)

    def addEdge(self, a, b, w):
        i = ord(a) - ord('A')
        j = ord(b) - ord('A')
        self.matrix[i][j] = w
        self.matrix[j][i] = w

    def display(self):
        # print("\n".join([str(row) for row in self.matrix]))
        for row in self.matrix:
            print()
            print(row)


g = UGraph(4)

g.addEdge('A','B',4)
g.addEdge('A','C',5)
g.addEdge('B','C',3)
g.addEdge('B','D',4)
g.addEdge('C','D',2)

=======
# Undirected Weighted Graph using Adjacency Matrix (we use 2D List)

class UGraph:
    def __init__(self, vertices):
        # self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.matrix = []
        for i in range(vertices):
            row=[]
            for j in range(vertices):
                row.append(0)
            self.matrix.append(row)

    def addEdge(self, a, b, w):
        i = ord(a) - ord('A')
        j = ord(b) - ord('A')
        self.matrix[i][j] = w
        self.matrix[j][i] = w

    def display(self):
        # print("\n".join([str(row) for row in self.matrix]))
        for row in self.matrix:
            print()
            print(row)


g = UGraph(4)

g.addEdge('A','B',4)
g.addEdge('A','C',5)
g.addEdge('B','C',3)
g.addEdge('B','D',4)
g.addEdge('C','D',2)

>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
g.display()