

vet = [0 for x in range(2)]

while True :
    for i in range (0, 2):
        vet[i] = int(input("Digite um número positivo: "))

    if vet[0] <= 0 or vet[1] <= 0 :
        print("Digite os números novamente !!!")

    else :
        resultado = vet[0] / vet[1]
        print(resultado)

        break


