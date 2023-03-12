from src.servers.Google import convert_to_RFC_datetime
from src.services.listTaskLists import listTasksList
from src.servers.tasksServer import Task
import pandas as pd


server = Task().init()

# PEGAR TASKS DE UMA LISTA X
flagsList = listTasksList(server)
# print(flagsList)

tasksDf = pd.DataFrame()
tasks = []

for flag in flagsList:
    tasksDf[flag['title']] = ''

    response = server.tasks().list(
        tasklist=flag['id'],
        maxResults=1,
        showDeleted=False,
        # dueMin='2023-03-11T00:00:00.000Z'
    ).execute()
    items = response.get('items')
    # tasks.append({flag['title']: items['id']})
    
    # if items:
    #     tasksDf[flag['title']] = len(items)

# code = len(tasksDf['CODE'])
print(items)
# tasks = response.get('items')


# RETORNAR QUANTAS TAREFAS DE CADA LISTA FORAM FEITAS



# CALCULAR PORCENTAGEM IMPACTO DA LISTA X NO TOTAL DE ATIVIDADES


