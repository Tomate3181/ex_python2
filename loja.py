# Contexto: Lojas de pequeno e médio porte muitas vezes iniciam seus sistemas de
# controle de estoque usando planilhas ou sistemas simples baseados em scripts. Um
# sistema básico que permita cadastrar produtos, atualizar o estoque e realizar buscas por
# nome pode ser o primeiro passo para digitalizar e organizar esse processo.
# Desafio: Você foi convidado por um comerciante local para desenvolver um sistema
# simples de cadastro de produtos utilizando Python. O sistema deve permitir adicionar
# produtos a uma lista, buscar produtos pelo nome, atualizar a quantidade em estoque e
# exibir a lista completa de produtos. A proposta é que todas as operações sejam
# realizadas usando funções e estruturas básicas, como listas e dicionários.
# As ações necessárias serão: Adicionar produto, buscar produto, listar produto e atualizar
# estoque.

def adicionar_produto(produtos, nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None

def atualizar_estoque(produtos, nome, quantidade):
    produto = buscar_produto(produtos, nome)
    if produto:
        produto["quantidade"] += quantidade
        print(f"Estoque atualizado para o produto '{nome}'. Nova quantidade: {produto['quantidade']}")
    else:
        print(f"Produto '{nome}' não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("Lista de produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

print("Bem-vindo ao sistema de cadastro de produtos!")
produtos = []

import time
time.sleep(0.5)

while True:
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Atualizar estoque")
    print("4 - Listar produtos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        adicionar_produto(produtos, nome, preco, quantidade)
    elif opcao == "2":
        nome = input("Digite o nome do produto a ser buscado: ")
        produto = buscar_produto(produtos, nome)
        if produto:
            print(f"Produto encontrado: {produto}")
        else:
            print(f"Produto '{nome}' não encontrado.")
    elif opcao == "3":
        nome = input("Digite o nome do produto para atualizar o estoque: ")
        quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))
        atualizar_estoque(produtos, nome, quantidade)
    elif opcao == "4":
        listar_produtos(produtos)
    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")