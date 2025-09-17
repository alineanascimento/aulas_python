"""Gerenciador de Tarefas Simples
Este script permite adicionar, ver, atualizar, completar e deletar tarefas."""


def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completa": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada.")
    return


def ver_tarefas(tarefas):
    print("\nLista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        for indice, tarefa in enumerate(tarefas):
            status = "Completa" if tarefa["completa"] else "Incompleta"
            print(f"{indice + 1}. {tarefa['tarefa']} - {status}")
    return

def atualizar_nome_tarefa(tarefas, indice, novo_nome_tarefa):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice + 1} atualizada para '{novo_nome_tarefa}'.")
    else:
        print("Índice inválido.")
    return
def completar_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["completa"] = True
        print(f"Tarefa {indice + 1} marcada como completa.")
    else:
        print("Índice inválido.")
    return
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completa"]:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa['tarefa']}' deletada.")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice, novo_nome_tarefa)
        
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice = int(input("Digite o número da tarefa que deseja marcar como completa: ")) - 1
        completar_tarefa(tarefas, indice)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break
    
print("programa encerrado.")
"""RESOLVER PROBLEMA NO CODIGO ###### NAO ESTA EXIBINDO A OPCAO 2####
"""