# Samuel Henrique Dias Mioni - Nº24 - 2ºB

import random, time

def criar_personagem(nome, classe):
    if classe == "1":
        personagem = {
            "nome": nome,
            "classe": "Guerreiro",
            "vida": 100,
            "forca": 20,
            "defesa": 10
        }
    elif classe == "2":
        personagem = {
            "nome": nome,
            "classe": "Mago",
            "vida": 80,
            "forca": 25,
            "defesa": 5
        }
    elif classe == "3":
        personagem = {
            "nome": nome,
            "classe": "Arqueiro",
            "vida": 90,
            "forca": 15,
            "defesa": 8
        }
    else:
        raise ValueError("Classe inválida. Escolha 1, 2 ou 3.")
    return personagem

def atacar(personagem, monstro):
    dano = personagem["forca"] - monstro["defesa"]
    if dano < 0:
        dano = 0
    monstro["vida"] -= dano
    if monstro["vida"] < 0:
        monstro["vida"] = 0
    print(f"{personagem['nome']} atacou {monstro['nome']} causando {dano} de dano!")
    return monstro

def exibir_status(personagem):
    print(f"Status de {personagem['nome']}:")
    print(f"Classe: {personagem['classe']}")
    print(f"Vida: {personagem['vida']}")
    print(f"Força: {personagem['forca']}")
    print(f"Defesa: {personagem['defesa']}")

#inicio do jogo
print("Seja bem vindo!! Vamos criar seu personagem!")
time.sleep(0.5)
print("==========================")

nome = input("Digite o nome do seu personagem: ")
classe = input("Digite a classe do seu personagem: \n(1 - Guerreiro, 2 - Mago, 3 - Arqueiro): ")
personagem = criar_personagem(nome, classe)
time.sleep(0.5)
print("==========================")
print(f"Personagem criado: {personagem['nome']} - Classe: {personagem['classe']}")
time.sleep(0.5)
print("==========================")

# monstros
goblin = {
    "nome": "Goblin",
    "vida": 50,
    "forca": 10,
    "defesa": 5
}

aranha_gigante = {
    "nome": "Aranha Gigante",
    "vida": 70,
    "forca": 15,
    "defesa": 8
}

slime = {
    "nome": "Slime",
    "vida": 30,
    "forca": 5,
    "defesa": 2
}

# Menu de ações
opcao = input("escolha uma ação: \n(1 - Lutar, 2 - Exibir status do personagem, 3 - Sair): ")
time.sleep(0.5)
print("==========================")

while opcao != "3":
    if opcao == "1":

        monstro = random.choice([goblin, aranha_gigante, slime])
        atacar(personagem, monstro)
        time.sleep(0.5)
        print("==========================")

    elif opcao == "2":
        exibir_status(personagem)
    else:
        print("Opção inválida. Tente novamente.")
    
    opcao = input("Escolha uma ação: \n(1 - Lutar, 2 - Exibir status do personagem, 3 - Sair): ")
    time.sleep(0.5)
    print("==========================")

