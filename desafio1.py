"""Sobre o desafio

Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato 
como favorito. O resultado da aplicação deve ser apresentado no terminal, 
assim como foi visto no módulo “Introdução ao Python”."""


"""### Regras da aplicação

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com 
o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato"""
# -*- coding: utf-8 -*-

import os
import sys
import io

# Configuração de encoding para Windows
os.system('chcp 65001')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def adicionar_contato(contatos):
    print("Vamos adicionar os dados do contato.")
    nome = input("Nome: ")
    telefone = input("Telefone: ")  
    email = input("Email: ")
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)  
    print("Contato adicionado com sucesso!")
    return contatos

def ver_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de contatos:")
    for i, contato in enumerate(contatos, 1):
        favorito_status = "✓" if contato['favorito'] else "✗"
        print(f"{i}. Nome: {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   Email: {contato['email']}")
        print(f"   Favorito: {favorito_status}")
        print("-" * 30)

def editar_contato(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    
    ver_contatos(contatos)
    nome_busca = input("Qual contato deseja editar? Digite o nome: ")
    
    contato_encontrado = None
    for contato in contatos:
        if contato["nome"].lower() == nome_busca.lower():
            contato_encontrado = contato
            break
    
    if not contato_encontrado:
        print("Contato não encontrado.")
        return
    
    print("O que deseja editar?")
    print("1 - Nome")
    print("2 - Telefone") 
    print("3 - Email")
    
    opcao_editar = input("Escolha uma opção (1, 2 ou 3): ")
    
    if opcao_editar not in ["1", "2", "3"]:
        print("Opção inválida.")
        return
    
    novo_dado = input("Digite o novo dado: ")

    if opcao_editar == "1":
        contato_encontrado["nome"] = novo_dado
    elif opcao_editar == "2":
        contato_encontrado["telefone"] = novo_dado
    elif opcao_editar == "3":
        contato_encontrado["email"] = novo_dado
        
    print("Contato editado com sucesso!")

def marcar_favorito(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
        
    ver_contatos(contatos)
    nome = input("Nome do contato que deseja marcar/desmarcar como favorito: ")
    
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contato["favorito"] = not contato["favorito"]
            if contato["favorito"]:
                print(f"Contato {nome} marcado como favorito.")
            else:
                print(f"Contato {nome} desmarcado como favorito.")
            return
    
    print("Contato não encontrado.")

def ver_favoritos(contatos):
    contatos_favoritos = [contato for contato in contatos if contato["favorito"]]
    
    if not contatos_favoritos:
        print("Nenhum contato favorito.")
        return
        
    print("\nLista de contatos favoritos:")
    for i, contato in enumerate(contatos_favoritos, 1):
        print(f"{i}. Nome: {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
        print(f"   Email: {contato['email']}")
        print("-" * 30)

def apagar_contato(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
        
    ver_contatos(contatos)
    nome = input("Nome do contato que deseja apagar: ")
    
    for i, contato in enumerate(contatos):
        if contato["nome"].lower() == nome.lower():
            contatos.pop(i)
            print(f"Contato {nome} apagado com sucesso.")
            return
    
    print("Contato não encontrado.")

# Programa principal
contatos = []

while True:
    print("\n" + "="*40)
    print("           AGENDA DE CONTATOS")
    print("="*40)
    print("1. Adicionar contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    print("="*40)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        adicionar_contato(contatos)
    elif opcao == "2":
        ver_contatos(contatos)
    elif opcao == "3":
        editar_contato(contatos)
    elif opcao == "4":
        marcar_favorito(contatos)
    elif opcao == "5":
        ver_favoritos(contatos)
    elif opcao == "6":
        apagar_contato(contatos)
    elif opcao == "7":
        print("Saindo da agenda. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")
    
    input("\nPressione Enter para continuar...")
