


adicao = 1
subtracao = 2
multiplicacao = 3
divisao = 4
sair = 5

selecao = int(input("\nBEM VINDO A CALCULADORA BÁSICA PYTHON ! \nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))

while selecao != sair :


        if selecao == adicao:

            num1 = float(input("Digite a primeira parcela: "))
            num2 = float(input("Digite a segunda parcela: "))
            result = num1 + num2
            print(f"A soma das parcelas é: {result}")

            selecao = int(input("\nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))

        elif selecao == subtracao:
            num1 = float(input("Digite o minuendo: "))
            num2 = float(input("Digite o subtraendo: "))
            result = num1 - num2
            print(f"O resto da subtração é: {result}")

            selecao = int(input("\nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))


        elif selecao == multiplicacao:
            num1 = float(input("Digite o multiplicando: "))
            num2 = float(input("Digite o multiplicador: "))
            result = num1 * num2
            print(f"O produto da multiplicação é: {result}")

            selecao = int(input("\nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))

        elif selecao == divisao:
            num1 = float(input("Digite o dividendo: "))
            num2 = float(input("Digite o divisor: "))

            if num2 != 0 :

                    result = num1 / num2
                    print(f"O quociente da divisão é: {result}")

                    selecao = int(input("\nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))
            else:
                    print("\nDivisão por zero inválida\n")


        else:
            print("\n Número inválido !")

            selecao = int(input(
                "\nQUAL OPERAÇÃO VOCÊ DESEJA ?\n 1- SOMA \n 2- SUBTRAÇÃO \n 3- MULTIPLICAÇÃO \n 4- DIVISÃO \n 5- SAIR "))




print("Você clicou em sair, muito obrigado por usar nosso aplicativo")







