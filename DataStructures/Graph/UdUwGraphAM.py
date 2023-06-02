# Undirected Unweighted graph using Adjacency Matrix (we use 2D List)

class UGraph:
    def __init__(self, vertices):
        # self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.matrix = []
        for i in range(vertices):
            row=[]
            for j in range(vertices):
                row.append(0)
            self.matrix.append(row)

    def addEdge(self, a, b):
        i = ord(a) - ord('A')
        j = ord(b) - ord('A')
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def display(self):
        # print("\n".join([str(row) for row in self.matrix]))
        for row in self.matrix:
            print(row)


g = UGraph(5)

g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('B','C')
g.addEdge('B','D')
g.addEdge('C','D')
g.addEdge('C','E')
g.addEdge('D','E')

g.display()