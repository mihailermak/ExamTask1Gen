import random
import networkx as nx
import matplotlib.pyplot as plt

def generation(size):
    array = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            array[i][j] = random.randint(0, 1)
            array[j][i] = array[i][j]
    return array

def checkmatrix(array):
    for row in array:
        count = sum(row)
        if not (count >= 2 and count <= 4):
            return False
    return True
def savegraph(resultmatrix):
    G = nx.Graph()

    for i in range(1, len(resultmatrix)):
        G.add_node(i)

    for i in range(len(resultmatrix)):
        for j in range(i + 1, len(resultmatrix)):
            if resultmatrix[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=12)
    plt.savefig('graph.png')

size = 8
resultmatrix = generation(size)
while not checkmatrix(resultmatrix):
    resultmatrix = generation(size)

print(resultmatrix)
print(savegraph(resultmatrix))