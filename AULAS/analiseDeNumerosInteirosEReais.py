"""
Exercício Análise de Números Inteiros e Reais

Objetivo: Desenvolver um programa que obtenha do usuário dois
números inteiros e um número real, e em seguida realize e apresente
uma série de cálculos e análises relacionadas a esses números.

Instruções:

    1. Solicite ao usuário dois números inteiros.
    2. Solicite ao usuário um número real.
    3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo.
    4. Calcule e exiba a soma do triplo do primeiro número com o terceiro número.
    5. Calcule e exiba o terceiro número elevado ao cubo.
    6. Determine e informe se o primeiro número é par ou ímpar.
    7. Determine e informe se o terceiro número é positivo, negativo ou zero.
    8. Calcule e mostre a média aritmética entre os três números.
"""


num1 = int(input("1- Digite um número inteiro: \n"))
num2 = int(input("2- Digite outro número inteiro: \n"))
num_real = float(input("3- Digite um número real: \n"))

produto = (num1 * 2) * (num2 / 2)
print(f"3- O produto do dobro do primeiro número com metade do segundo é: {produto}\n")

soma = (num1 * 3) + num_real
print(f"4- A soma do triplo do primeiro número com o terceiro número é: {soma}\n")

cubo = num_real ** 3
print(f"5- O terceiro número elevado ao cubo é: {cubo}\n")

if num1 % 2 == 0 :
    print(f"6- O número {num1} é par !\n")
else:
    print(f"6- O número {num1} é ímpar !\n")

if num_real > 0 :
    print(f"7- {num_real} é positivo !\n")
elif num_real == 0 :
    print("7- O número escolhido é zero\n")
else:
    print(f"7- {num_real} é negativo !\n")

media = (num1 + num2 + num_real) / 3

print(f"8- A média entre os três números é: {media:.2f}\n")

