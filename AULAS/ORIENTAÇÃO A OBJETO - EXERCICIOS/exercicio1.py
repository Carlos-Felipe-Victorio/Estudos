"""
Exercício - Informações de Frutas em uma Mercearia

Em uma mercearia, várias frutas são vendidas, e você deseja criar um
sistema simples para gerenciar as informações sobre essas frutas.

Objetivos:

    1. Definir uma classe chamada Fruta.
    2. Instanciar um ou mais objetos desta classe.
    3. Acessar e exibir os atributos dos objetos instanciados.

Instruções:

    1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).

    2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:

        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]

"""



class Fruta:
    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):
        self.nome = nome
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque


maca = Fruta("Maça", 15.00, 50)
banana = Fruta("Banana", 12.00, 100)

print(f"Nome da Fruta: {maca.nome}\n Preço por Kg: {maca.preco_por_kg}\n Quantidade em Estoque: {maca.quantidade_em_estoque}\n")

print(f"Nome da Fruta: {banana.nome}\n Preço por Kg: {banana.preco_por_kg}\n Quantidade em Estoque: {banana.quantidade_em_estoque}\n")

