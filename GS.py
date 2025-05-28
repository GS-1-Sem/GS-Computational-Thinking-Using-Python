# ================================================================
# Aplicação: Sistema de Monitoramento de Ecopontos
# Nome: Pedro Henrique Sartorelli Ferreira RM:563281,
#       Arthur Ferreira Alves dos Santos RM:564958,
#       GUSTAVO MOURA BARBOSA RM:566190
# ================================================================

# Lista vazia para armazenar os ecopontos cadastrados
Ecopontos = []

# Mensagem de boas-vindas ao sistema
print("Seja bem-vindos à o sistema de ecopontos")

# Laço principal do sistema — roda até que o usuário escolha sair
while True:
    # Verifica se ainda não há ecopontos cadastrados
    if len(Ecopontos) <= 0:
        print("A gente não possui nenhum ecoponto cadastrado no nosso sistema")
        
        # Menu de opções para quando não há nenhum ecoponto
        print("Opção" + "-" * 10 + "Descrição")
        print("1" + "-" * 10 + "Cadastrar um novo ecoponto")
        print("0" + "-" * 10 + "Sair do sistema")

        # Recebe a opção digitada pelo usuário
        opcoes = int(input("Digite à opção que você deseja: "))

        # Se o usuário escolher a opção 1, permite cadastrar um novo ecoponto
        if opcoes == 1:
            print("Cadastrar novo ecoponto")
            ecoponto = input("Digite o nome do ecoponto: ")
            Ecopontos.append(ecoponto)  # Adiciona o ecoponto à lista

        # Se o usuário escolher sair
        if opcoes == 0:
            break  # Encerra o loop e o sistema

    # Se já existem ecopontos cadastrados
    if len(Ecopontos) > 0:
        print("Esses são os ecopontos que foram cadastrados")
        print(Ecopontos)  # Mostra todos os ecopontos

        # Menu de opções quando há ecopontos cadastrados
        print("Opção" + "-" * 10 + "Descrição")
        print("1" + "-" * 10 + "Cadastrar um novo ecoponto")
        print("2" + "-" * 10 + "Excluir ecoponto")
        print("0" + "-" * 10 + "Sair do sistema")

        # Recebe a opção digitada pelo usuário
        opcoes = int(input("Digite à opção que você deseja: "))

        # Opção 1: Cadastrar novo ecoponto
        if opcoes == 1:
            print("Cadastrar novo ecoponto")
            ecoponto = input("Digite o nome do ecoponto: ")
            Ecopontos.append(ecoponto)  # Adiciona o novo ecoponto
            print(Ecopontos)  # Mostra a lista atualizada

        # Opção 2: Excluir um ecoponto
        if opcoes == 2:
            print("Excluir ecoponto")
            print(Ecopontos)  # Mostra ecopontos atuais
            ecoponto = input("Qual o nome do ecoponto que você deseja excluir: ")

            # Verifica se o ecoponto está na lista
            if ecoponto in Ecopontos:
                Ecopontos.remove(ecoponto)  # Remove da lista
                print(f"{ecoponto} removido!")  # Confirmação
            else:
                print(f"{ecoponto} não existe!")  # Mensagem de erro

            print(Ecopontos)  # Lista atualizada após exclusão

        # Opção 0: Sair do sistema
        if opcoes == 0:
            break  # Encerra o loop e o sistema

# Mensagem final após o encerramento
print("Você saiu de nosso sistema")
print("Esses são os ecopontos que foram cadastrados")
print(Ecopontos)