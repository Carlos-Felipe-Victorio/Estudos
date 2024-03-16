"""
Exercício Análise de Desempenho do Aluno

Objetivo: Desenvolver um programa que avalie o desempenho de um aluno ao
longo dos bimestres. Para isso, o programa deve solicitar as quatro
notas bimestrais do aluno e, com base nelas, realizar as seguintes ações:

    1. Calcular e exibir a média das notas.
    2. Determinar e mostrar a maior e a menor nota entre as inseridas.
    3. Com base na média, informar ao usuário se o aluno está aprovado,
    em recuperação ou reprovado. Considere os seguintes critérios:
        - Aprovado: média >= 7
        - Em recuperação: 5 <= média < 7
        - Reprovado: média < 5

    4. Calcular e mostrar a quantidade de notas que estão acima da média calculada.
"""


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 +nota4) / 2
print(f"A média entre as notas é: {media}")

maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)

print(f"A maior nota é {maior_nota}")
print(f"A menor nota é {menor_nota}")

if media >= 7 :
    print("Aluno Aprovado")

elif media >= 5 :
    print("Aluno em Recuperação")

else:
    print("Aluno Reprovado")


notas_acima = 0

for i in [nota1, nota2, nota3, nota4]:
    if i > 7 :
        notas_acima += 1
        print(f"Nota: {i}")
print(f"A quantidade de notas acima da média são {notas_acima}")

