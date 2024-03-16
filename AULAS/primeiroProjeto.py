"""
Exercício: Simulação de Caixa Eletrônico

Objetivo: Desenvolver um programa em Python que simula as 
operações básicas de um caixa eletrônico. O usuário deve ser capaz de 
verificar o saldo, depositar dinheiro, sacar dinheiro e sair do programa.

Requisitos:

    Verificar Saldo:
    
        - Ao escolher essa opção, o programa deve exibir o saldo atual da conta.

    Depositar Dinheiro:
    
        - O usuário deve ser capaz de inserir uma quantia para depositar na conta.
        - A quantia deve ser positiva.
        - Após um depósito bem-sucedido, o saldo da conta deve ser atualizado e uma 
        mensagem de confirmação deve ser exibida.

    Sacar Dinheiro:
    
        - O usuário deve ser capaz de inserir uma quantia para sacar da conta.
        - A quantia deve ser positiva e não deve exceder o saldo atual.
        - Após um saque bem-sucedido, o saldo da conta deve ser 
        atualizado e uma mensagem de confirmação deve ser exibida.

    Sair:
    
        - O usuário deve ser capaz de sair do programa escolhendo essa opção.

    Validação de Entrada:
    
        - O programa deve lidar com entradas inválidas de forma adequada, exibindo mensagens de erro quando aplicável.

    Interface de Usuário:
    
        - O programa deve exibir um menu de opções para o usuário e permitir 
        a seleção de ações a serem realizadas.
        - As opções do menu devem ser apresentadas em um loop, permitindo 
        múltiplas operações até que o usuário escolha sair.
        
            Caixa Eletrônico
            1 - Verificar Saldo
            2 - Depositar Dinheiro
            3 - Sacar Dinheiro
            4 - Sair
            Escolha uma opção (1-4):

    Saldo Inicial:
    
        - A conta deve começar com um saldo inicial de R$ 1000.00.

Instruções:

    - Comece inicializando o saldo e entrando em um loop que apresente o menu de opções.
    - Implemente cada operação como descrito nos requisitos.
    - Certifique-se de testar todas as opções e cenários possíveis para garantir que 
    o programa funcione corretamente.


Dica: Você pode usar condicionais if, elif, e else juntamente com um loop while 
para gerenciar as seleções do usuário e manter o programa em execução 
até que a opção de sair seja escolhida.

"""


#Saldo inicial solicitado no enunciado.
saldo = 1000

#Primeiro menu a aparecer na interface do programa.
print("\n **** Caixa eletrônico **** \n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair \n")

#Variável índice do menu.
escolha_menu = int(input("Escolha uma opção (1-4): "))

#Estrutura while para fazer o menu ficar indo e voltando.
while escolha_menu != 4 :

    # Se o usuário digitar 1 ele verifica seu saldo e escolhe mais alguma opção no menu (ou sai do programa).
    if escolha_menu == 1 :
        print(f"\nSeu saldo é {saldo:.2f} \n")

        print("\n **** Caixa eletrônico **** \n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair ")
        escolha_menu = int(input("Deseja realizar mais alguma operação ?: \n"))

    # Se o usuário digitar 2 ele acrescenta valores a variavel saldo e salva na memória.
    elif escolha_menu == 2 :

        deposito = float(input("\nQuanto você deseja depositar: \n"))
        saldo = saldo + deposito
        print(f"\nDepósito bem sucedido, o seu saldo atual é {saldo:.2f}. \n")

        print("\n **** Caixa eletrônico **** \n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair ")
        escolha_menu = int(input("Deseja realizar mais alguma operação ?: \n"))

    # Se o usuário digitar 3 ele subtrai valores da variavel saldo e salva na memória.
    elif escolha_menu == 3 :
        saque = float(input("\nQuanto você deseja sacar: \n"))

        """ Dentro de menu 3(saque) pus uma condicional para aparecer uma mensagem caso
         o usuário tente sacar um valor maior do que ele tem disponível na conta """
        if saque > saldo :
            print("\nVocê não tem este valor disponível !\n")

        # Se o usuário tentar sacar valor 0, será considerado nulo
        elif saque == 0 :
            print("\n Valor nulo ! \n")

        # Se o saque for menor que o saldo disponível em conta, a operação será bem sucedida !
        else :
            saldo = saldo - saque
            print(f"\nSaque bem sucedido, o seu saldo atual é {saldo:.2f}. \n")

        print("\n **** Caixa eletrônico ****\n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair ")
        escolha_menu = int(input("Deseja realizar mais alguma operação ?: \n"))

    # Esta condicional é para caso no menu de opções o usuário digite um valor inválido.
    elif escolha_menu >= 5 :
        print("\nNúmero do menu inválido !\n")

        print("\n **** Caixa eletrônico ****\n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair ")
        escolha_menu = int(input("Digite um número válido: \n"))

        # Esta condicional é para caso no menu de opções o usuário digite um valor inválido.
    elif escolha_menu == 0 :
        print("\nNúmero do menu inválido !\n")

        print(
            "\n **** Caixa eletrônico ****\n1- Verificar Saldo \n2- Depoistar dinheiro \n3- Sacar Dinheiro \n4- Sair ")
        escolha_menu = int(input("Digite um número válido: \n"))

# Após digitar 4(sair) o programa se encerra.
print("\nObrigado pela preferência, o Banco Python agradece !\n")