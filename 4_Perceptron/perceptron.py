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

    weights = [0,0,0]
    alpha = 1
    threshold = 0
    epochs = 0

    continuar = True

    while(continuar):
        epochs = epochs+1

        for i in range(size):
            sum = int(weights[2])

            for j in range(len(inp[i]) - 1):
                sum = sum + int(inp[i][j]) * int(weights[j])

            if sum > threshold:
                y = 1
            elif ((sum >= (-threshold)) and (sum <= threshold)):
                y = 0
            elif sum < (-threshold):
                y = -1

            if int(output[i]) == y:
                continuar = False
            else:
                wSize = len(weights)
                for j in range(wSize):
                    if j == 2:
                        weights[j] = int(weights[j]) + (alpha * int(output[i]))
                    else:
                        weights[j] = int(weights[j]) + (alpha * int(output[i]) * int(inp[i][j]))

            print('\nEntradas: '+ str(inp[i]))
            print('Saida: ' + str(output[i]))
            print('Pesos: ' + str(weights))

        epochs = epochs+1
        print('Epocas = ' + str(epochs))


if __name__ == "__main__":
    run()