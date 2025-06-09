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

