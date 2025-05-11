# Exercício - Lista de tarefas com desfazer e refazer
 # Música para codar =)
 # Everybody wants to rule the world - Tears for fears
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']
import os
import json

worklist = []
worklist_removed = []
removed = None

def print_list(list):
    print('Tarefas:')
    print()
    for value in list:
        print(value)
    return

def undo(list, removed_list):
    if not list:
        print('Não existem tarefas para desfazer')
        return
    removed = list.pop()
    removed_list.append(removed)
    print_list(list)

def redo(list, removed_list):
    if not removed_list:
            print('Não existem tarefas para refazer')
            return
    removed = removed_list.pop()
    list.append(removed)
    print_list(list)

def listi(list):
    if not list:
        print('Não existem tarefas')
        return
    print_list(list)

def add(list,input):
    list.append(input)
    print_list(list)

    return

def create_json(list):
    with open('aula192.json', 'w+', encoding='UTF8') as arquivo:
        json.dump(
            list, 
            arquivo,
            indent=2
    )

def read_json():
    try:
        with open('aula192.json', 'r', encoding='UTF8') as arquivo:
            list = json.load(arquivo)
            return list
    except FileNotFoundError:
        print('Arquivo nao existe')
        return []

worklist = read_json()

while True:
    inp = input('Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ')
    print()
    # if inp == 'listar':
    #     listi(worklist)
    # elif inp == 'desfazer':
    #     undo(worklist, worklist_removed)
    # elif inp == 'refazer':
    #     redo(worklist, worklist_removed)
    # elif inp == 'clear':
    #     os.system('cls')
    # else:
    #     add(worklist, inp)

    # outra forma de fazer:

    comandos = {
        'listar': lambda: listi(worklist),
        'desfazer': lambda: undo(worklist, worklist_removed),
        'refazer': lambda: redo(worklist, worklist_removed),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: add(worklist, inp),
    }
    
    comando = comandos.get(inp) if comandos.get(inp) is not None else comandos['adicionar']
    comando()
    create_json(worklist)



