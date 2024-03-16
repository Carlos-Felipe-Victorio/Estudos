"""
Exercício Cálculo do Salário com Horas Extras e Imposto de Renda

Objetivo: Desenvolver um programa que ajude o usuário a entender a
composição do seu salário mensal. O programa deve considerar o valor
recebido por hora, as horas trabalhadas no mês, o cálculo de horas
extras e o desconto do imposto de renda.

Instruções:

    1. Solicite ao usuário o valor que ele ganha por hora.
    2. Pergunte quantas horas foram trabalhadas no mês.
    3. Calcule o salário bruto multiplicando o valor por hora
    pelas horas trabalhadas.

    4. Se o usuário tiver trabalhado mais de 160 horas no mês,
    calcule o valor das horas extras. Cada hora extra deve ser
    compensada com um adicional de 50% sobre o valor da hora comum.

    5. Calcule o imposto de renda sobre o salário (considerando as horas extras).
    O imposto de renda tem uma taxa fixa de 11% sobre o salário.

    6. Mostre ao usuário uma descrição detalhada contendo:
        - Salário Bruto.
        - Valor das Horas Extras (se aplicável).
        - Valor do Imposto de Renda.
        - Salário Líquido (Salário Bruto + Horas Extras - Imposto de Renda).
"""


salario_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas_mes = float(input("Digite quantas horas você trabalhou no mês: "))

salario_bruto = horas_trabalhadas_mes * salario_hora

print(f"- Salário bruto : {salario_bruto}\n")

if horas_trabalhadas_mes > 160 :

    horas_extras_trab = float(horas_trabalhadas_mes - 160)

    valor_hora_extra = float(salario_hora * 1.5)

    pagamento_horas_extras = float(horas_extras_trab * valor_hora_extra)

    imposto_de_renda = float((salario_bruto + pagamento_horas_extras) * 11 / 100)

    salario_liquido = float(salario_bruto + pagamento_horas_extras - imposto_de_renda)

    print(f"O pagamento das horas extras é: {pagamento_horas_extras}")
    print(f"Valor do Imposto de Renda: {imposto_de_renda}")
    print(f"Salário líquido: {salario_liquido}")


else:

    valor_hora_extra = "Você não teve horas extras no mês !"
    imposto_de_renda = float(salario_bruto * 11 / 100)
    salario_liquido = float(salario_bruto - imposto_de_renda)

    print(f"- Salário bruto : {salario_bruto}\n")
    print(f"Valor hora extra : {valor_hora_extra}")
    print(f"Valor do Imposto de Renda: {imposto_de_renda}")
    print(f"Salário líquido: {salario_liquido}")
    



