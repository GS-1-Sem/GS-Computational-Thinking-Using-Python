# ================================================================
# Aplicação: Sistema de Monitoramento de Ecopontos
# Nome: Pedro Henrique Sartorelli Ferreira RM:563281,
#       Arthur Ferreira Alves dos Santos RM:564958,
#       GUSTAVO MOURA BARBOSA RM:566190
# ================================================================

Ecopontos = []
print("Seja bem-vindos à o sistema de ecopontos")
while True:
    if len(Ecopontos) <= 0:
        print("A gente não possui nenhum ecoponto cadastrado no nosso sistema")
        print("Opção"+"-"*10+"Descrição")
        print("1"+"-"*10+"Cadastrar um novo ecoponto")
        print("0" + "-" * 10 + "Sair do sistema")
        opcoes = int(input("Digite à opção que você deseja: "))
        if opcoes == 1:
            print("Cadastrar novo ecoponto")
            ecoponto = input("Digite o nome do escoponto: ")
            Ecopontos.append(ecoponto)
        if opcoes == 0:
            break
    if len(Ecopontos) > 0:
        print("Esses sãos os escopontos que foram cadastrados")
        print(Ecopontos)
        print("Opção" + "-" * 10 + "Descrição")
        print("1" + "-" * 10 + "Cadastrar um novo ecoponto")
        print("2" + "-" * 10 + "Excluir ecoponto")
        print("0" + "-" * 10 + "Sair do sistema")
        opcoes = int(input("Digite à opção que você deseja: "))
        if opcoes == 1:
            print("Cadastrar novo ecoponto")
            ecoponto = input("Digite o nome do escoponto: ")
            Ecopontos.append(ecoponto)
            print(Ecopontos)
        if opcoes == 2:
            print("Excluir ecoponto")
            print(Ecopontos)
            ecoponto = input("Qual o nome do ecoponto que você deseja excluir ecoponto : ")
            if ecoponto in Ecopontos:
                Ecopontos.remove(ecoponto)
                print(f"{ecoponto} removido!")
            else:
                print(f"{ecoponto} não existe!")
            print(Ecopontos)
        if opcoes == 0:
            break
print("Você saiu de nosso sistema")
print("Esses são os escopontos que foram cadastrados")
print(Ecopontos)