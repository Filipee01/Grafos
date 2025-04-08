from grafos import Grafo

def load_from(fileName):
    """ Ler o arquivo com a matriz de adjacentes """

    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Grafo(n)
    
    l = 0

    for line in f:

        line.strip()
        numeros = line.split("\t")
        c = 0

        for i in numeros:

            if(c == n):
                break

            g.matriz_adjacentes[l][c] = int(i)

            if int(i) != 0:
                g.vetor_adjacentes[l].append(c)
            
            c += 1
        l += 1
    
    return g # Retorna o grafo