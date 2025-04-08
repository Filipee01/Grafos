from lerArquivo import load_from

def main():

    # Pergunta ao usuário o número de vértices e carrega o grafo correspondente
    n = input("Informe a quantidade de vértices (4/10/50/177): ")
    grafo = load_from("input/pcv" + n + ".txt")

    # Mostra a estrutura do grafo
    grafo.exibir_grafo()

    # Executa a busca em profundidade
    print("Resultado da busca em profundidade:")
    grafo.busca_em_profundidade()

    # Solicita o vértice inicial para a busca em largura
    origem = int(input("Informe o vértice de origem: "))
    d, p = grafo.busca_em_largura(origem)

    # Exibe as distâncias do vértice inicial para os demais
    print("Distâncias do vértice de origem para os outros vértices:")
    print(d)

    # Solicita o vértice final e exibe o caminho
    destino = int(input("Informe o vértice de destino: "))
    print("Vértice anterior no caminho origem -> destino:")
    print(p)
    print("Caminho completo da origem até o destino:")
    grafo.caminho(p, destino)



# Chama a função principal
main()