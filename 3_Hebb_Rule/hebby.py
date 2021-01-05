def entrada():
    e = open('inputs.txt','r')

    inp = []
    for i in e:
        splitter = i.split(',')
        inp.append(splitter)

    size = len(inp)
    return inp, size

def run():
    inp, size = entrada()

    pesos = []

    # usando o tamanho da linha
    for i in range(len(inp[0]) - 1):
        pesos.append(0)

    output = []

    for i in range(size):
        output.append(inp[i][len(inp[i]) - 1])

    for i in range(size):
        entradaAtual = []
        for j in range(len(inp[i]) - 1):
            entradaAtual.append(inp[i][j])
            aux = int(output[i])

            pesos[j] = pesos[j] + (int(entradaAtual[j]) * aux)

        print('\nEntradas: ', entradaAtual, 'Saida: ',str(output[i]),'Pesos: ',pesos)

if __name__ == "__main__":
    run()