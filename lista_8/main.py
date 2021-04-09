import numpy as np


class Grafo:
    def __init__(self, x, y, n, m, content):
        self.x = x
        self.y = y
        self.n = n
        self.m = m
        self.content = content


if __name__ == '__main__':
    paths = []

    for i in range(1, 27):
        paths.append("grafos/" + str(i) + ".txt")

    grafos = []
    for path in paths:
        fileContent = open(path, 'r').readlines()
        xy = fileContent[0]
        nm = fileContent[1]
        dContent = fileContent[2:]
        (x, y) = xy.split(' ', 1)
        y = y.rstrip("\n")
        (n, m) = nm.split(' ', 1)
        m = m.rstrip("\n")
        content = []
        for string in dContent:
            content.append(string.replace("\n", ''))
        grafos.append(Grafo(int(x), int(y), int(n), int(m), content))

    for grafo in grafos:
        if grafo.x == 1:
            if grafo.y == 1:
                matris = np.zeros((grafo.n, grafo.n))
                for i in grafo.content:
                    (a, b) = i.split(' ')
                    matris[int(a) - 1][int(b) - 1] = 1
                # escrever no documento
            elif grafo.y == 2:
                matris = np.zeros((grafo.n, grafo.m))
                for index, par in enumerate(grafo.content):
                    (a, b) = par.split(' ')
                    matris[int(a) - 1][index] = 1
                    matris[int(b) - 1][index] = 1
                # escrever no documento
            elif grafo.y == 3:
                matris = np.zeros((grafo.n, grafo.m))
                matris[0][0] = 1
                for par in grafo.content:
                    (a, b) = par.split(' ')
                    if matris[int(a) - 1][0] != int(a):
                        matris[int(a) - 1][0] = int(a)
                        matris[int(a) - 1][1] = int(b)
                    else:
                        for index in range(0, grafo.m):
                            if matris[int(a) - 1][index] == 0:
                                matris[int(a) - 1][index] = int(b)
                                break
                    if matris[int(b) - 1][0] != int(b):
                        matris[int(b) - 1][0] = int(b)
                        matris[int(b) - 1][1] = int(a)
                    else:
                        for index in range(0, grafo.m):
                            if matris[int(b) - 1][index] == 0:
                                matris[int(b) - 1][index] = int(a)
                                break
                # escrever no documento

        elif grafo.x == 2:
            if grafo.y == 1:
                matris = np.zeros((grafo.n, grafo.n))
                for i in range(0, grafo.n):
                    for j in range(0, grafo.n):
                        matris[i][j] = grafo.content[i][j]
                # escrever no documento
            elif grafo.y == 2:
                print(y)
            elif grafo.y == 3:
                print(y)
        elif grafo.x == 3:
            if grafo.y == 1:
                print(y)
            elif grafo.y == 2:
                print(y)
            elif grafo.y == 3:
                print(y)

    print(grafos[0].content)
