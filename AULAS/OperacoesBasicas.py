"""
Exercício Operações Matemáticas Básicas

Objetivo: Desenvolver um programa que solicite ao usuário a entrada
de dois números e, com base nesses números, realize as seguintes operações:

    1. Calcular e mostrar a soma dos dois números.

    2. Calcular e mostrar a subtração do primeiro número pelo segundo.

    3. Calcular e mostrar a multiplicação dos dois números.

    4. Calcular e mostrar a divisão do primeiro número pelo
    segundo (se o segundo número não for zero).

    5. Verificar e informar se algum dos números (ou ambos) é zero.

    6. Calcular e mostrar a média dos dois números.

    7. Comparar os dois números e informar qual é maior ou se são iguais.

"""


num1 = int(input("Digite o primeiro número: \n"))

num2 = int(input("Digite o segundo número: \n"))

soma = num1 + num2
print(f"A soma dos dois números é: {soma}\n")

subtracao = num1 - num2
print(f"A subtração dos dois números é: {subtracao}\n")

multiplicacao = num1 * num2
print(f"A multiplicação dos dois números é: {multiplicacao}\n")

if num2 != 0 :
    divisao = num1 / num2
    print(f"A divisao dos dois números é: {divisao}\n")

    if num1 == 0 :
        print("O primeiro número é Zero\n")
    elif num1 == num2 :
            print("Os números são iguais\n")
    elif num1 > num2 :
            print(f"{num1} é maior que {num2}\n")
    else:
            print(f"{num2} é maior que {num1}\n")

    media = (num1 + num2) / 2
    print(f"A média dos números é {media}\n")

else:
    print("Divisão por zero inválida !\n")
    if num1 == 0 :
        print("O primeiro número é Zero\n")
    elif num2 == 0 :
        print("O segundo número é Zero\n")

