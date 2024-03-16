"""
Exercício Análise de Números

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de
um número e, com base nesse número, realiza as seguintes operações:

    1. Mostrar o número informado.
    2. Informar se o número é par ou ímpar.
    3. Informar se o número é positivo, negativo ou zero.
    4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

"""


num = int(input("Digite um número: "))

print(num)

if num % 2 != 0 :
    print(f"O número {num} é ímpar")

    if num < 0:
        print(f"{num} é negativo !")

    else:
        print(f"{num} é positivo !")
        import math

        numero = num
        raiz_quadrada = math.sqrt(num)
        print(f"{raiz_quadrada:.2f}")

elif num == 0 :
    print("O número é zero !")

else :
    print(f"O número {num} é par")

    if num < 0:
        print(f"{num} é negativo !")

    else:
        print(f"{num} é positivo !")
        import math

        numero = num
        raiz_quadrada = math.sqrt(num)
        print(f"{raiz_quadrada:.2f}")








