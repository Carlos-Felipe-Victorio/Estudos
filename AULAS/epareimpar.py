
N = int(input("Quantos números deseja usar ?"))

vet = [0 for x in range(N)]

for i in range (0, N):
    vet[i] = int(input("Digite os números selecionados: "))

numeros_par = 0
numeros_impar = 0

for i in range (0, N):
    if vet[i] % 2 == 0 :

        numeros_par += 1
        print(f" É par :{vet[i]}")


    else:

        numeros_impar += 1
        print(f" É impar :{vet[i]}")


print(f"A quantidade de números par é {numeros_par}")
print(f"A quantidade de números ímpar é {numeros_impar}")