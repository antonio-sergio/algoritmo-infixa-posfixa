vetor1 = [22, 5, 18, 7, 1, 10, 2, 7, 3, 6, 4, 20]
vetor2 = [15, 5, 7, 8, 10, 2, 9, 1, 4, 4, 2, 7, 13, 2, 3]

def getIndice(vetor):
    somaAnterior = somaPosterior = 0   #zerando as variaveis
    for i, valor in enumerate(vetor):  #for pegando indice e valor
        somaAnterior = sum(vetor[0:i])  #fatiamento pegando as partes solicitadas
        somaPosterior = sum(vetor[i + 1:])
        if somaAnterior == somaPosterior:  #comparando os valores obtidos através do fatiamento
            return i


print(f"Vetor 1: {getIndice(vetor1)}")
print(f"Vetor 2: {getIndice(vetor2)}")
