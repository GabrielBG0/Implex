import numpy as np


class Grafo:
    def __init__(self, x, y, n, m, content, id):
        self.x = x
        self.y = y
        self.n = n
        self.m = m
        self.content = content
        self.id = id


def escreveDocumento(y, n, m, matris, id):
    path = "resultado/" + id + ".txt"
    headder = str(n) + " " + str(m)
    if y == 3:
        np.savetxt(fname=path, X=matris, header=headder,
                   fmt="%01i", delimiter=" -> ")
    else:
        np.savetxt(fname=path, X=matris, header=headder, fmt="%01i")


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
        id = path.rstrip(".tx")
        id = id[7:]
        grafos.append(Grafo(int(x), int(y), int(n), int(m), content, id))

    print("trasncrevendo documentos...")

    for grafo in grafos:
        if grafo.x == 1:
            if grafo.y == 1:
                matris = np.zeros((grafo.n, grafo.n))
                for i in grafo.content:
                    (a, b) = i.split(' ')
                    matris[int(a) - 1][int(b) - 1] = 1
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
            elif grafo.y == 2:
                matris = np.zeros((grafo.n, grafo.m))
                for index, par in enumerate(grafo.content):
                    (a, b) = par.split(' ')
                    matris[int(a) - 1][index] = 1
                    matris[int(b) - 1][index] = 1
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
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
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
        elif grafo.x == 2:
            if grafo.y == 1:
                matris = np.zeros((grafo.n, grafo.n))
                for i in range(0, grafo.n):
                    for j in range(0, grafo.n):
                        matris[i][j] = int(grafo.content[i][j])
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
            elif grafo.y == 2:
                matris = np.zeros((grafo.n, grafo.m))
                pares = []
                for i in range(0, grafo.n):
                    for j in range(0, grafo.n):
                        if grafo.content[i][j] == "1":
                            par = [i, j] if i < j else [j, i]
                            if par not in pares:
                                pares.append(par)
                for i in range(grafo.m):
                    matris[pares[i][0]][i] = 1
                    matris[pares[i][1]][i] = 1
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
            elif grafo.y == 3:
                matris = np.zeros((grafo.n, grafo.m))
                matris[0][0] = 1
                pares = []
                for i in range(0, grafo.n):
                    for j in range(0, grafo.n):
                        if grafo.content[i][j] == "1":
                            pares.append([i, j])
                for par in pares:
                    if matris[par[0]][0] != par[0] + 1:
                        matris[par[0]][0] = par[0] + 1
                        matris[par[0]][1] = par[1] + 1
                    else:
                        for index in range(1, grafo.m):
                            if matris[par[0]][index] == 0:
                                matris[par[0]][index] = par[1] + 1
                                break
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
        elif grafo.x == 3:
            if grafo.y == 1:
                matris = np.zeros((grafo.n, grafo.n))
                for i in range(grafo.m):
                    par = []
                    for j in range(grafo.n):
                        if grafo.content[j][i] == "2":
                            matris[j][j] = 1
                            break
                        elif grafo.content[j][i] == "1":
                            par.append(j)
                    matris[par[0]][par[1]] = 1
                    matris[par[1]][par[0]] = 1
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
            elif grafo.y == 2:
                matris = np.zeros((grafo.n, grafo.m))
                for i in range(grafo.n):
                    for j in range(grafo.m):
                        matris[i][j] = int(grafo.content[i][j])
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
            elif grafo.y == 3:
                matris = np.zeros((grafo.n, grafo.m))
                matris[0][0] = 1
                pares = []
                for i in range(grafo.m):
                    par = []
                    for j in range(grafo.n):
                        if grafo.content[j][i] == "2":
                            matris[j][j] = 1
                            break
                        elif grafo.content[j][i] == "1":
                            par.append(j)
                    pares.append(par)
                for par in pares:
                    if matris[par[0]][0] != par[0] + 1:
                        matris[par[0]][0] = par[0] + 1
                        matris[par[0]][1] = par[1] + 1
                    else:
                        for index in range(1, grafo.m):
                            if matris[par[0]][index] == 0:
                                matris[par[0]][index] = par[1] + 1
                                break
                escreveDocumento(grafo.y, grafo.n, grafo.m, matris, grafo.id)
    print("programa concluido")
