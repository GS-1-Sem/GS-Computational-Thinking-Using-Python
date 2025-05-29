# ================================================================
# Aplicação: Simulação de um back-end de "Ecopontos"
# Para saber o que são ecopontos (Se você não souber) e mais do projeto acesse: link github
#
# Nome: Pedro Henrique Sartorelli Ferreira RM:563281,
#       Arthur Ferreira Alves dos Santos RM:564958,
#       GUSTAVO MOURA BARBOSA RM:566190
# ================================================================

# Lista vazia para armazenar os ecopontos cadastrados
ecopontos = []

print("Bem-vindo! Aqui você pode adicionar ou excluir os ecopontos")

# Menu de opções
print("\nOpções:")
print("1 - Adicionar")
print("2 - Excluir")
print("3 - Listar itens")
print("0 - Sair")

while True:

    # Espaço para melhorar visualização
    print()

    opcao = input("Escolha uma opção: ")

    print('-' * 10)

    # Adiciona um ecoponto na lista.
    if opcao == "1":
        item = input("Digite o item para adicionar: ")

        ecopontos.append(item)

        print()

        print(f"Item '{item}' adicionado.")

        print('-' * 10)

    # Exclui um ecoponto na lista.
    elif opcao == "2":

        if len(ecopontos) == 0:
            print("A lista está vazia, não há itens para excluir.")

            print('-' * 10)
        else:

            # Lista os ecopontos mostrando o índice de cada um na lista.
            print("Itens na lista:")
            for i in range(len(ecopontos)):
                print(f"{i} - {ecopontos[i]}")

            print('-' * 10)

            indice = int(input("Digite o índice do item para excluir: "))

            if 0 <= indice < len(ecopontos):
                removido = ecopontos.pop(indice)
                print(f"Item '{removido}' removido.")
            else:
                print("Índice inválido.")


    elif opcao == "3":
        if len(ecopontos) == 0:
            print("A lista está vazia.")
        else:
            print("Itens na lista:")
            for i in ecopontos:
                print()
                print(i)

        print('-' * 10)

    elif opcao == "0":
        print("Saindo... Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
        print()
