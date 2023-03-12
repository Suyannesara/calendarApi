from src.servers.Google import convert_to_RFC_datetime
from src.services.listTaskLists import listTasksList
from src.servers.tasksServer import Task
import pandas as pd

server = Task().init()

# PEGAR TASKS DE UMA LISTA X
flagsList = listTasksList(server)

tasksLen = {}
tasks = {}
totalTasks = 0

for flag in flagsList:
    response = server.tasks().list(
        tasklist=flag['id'],
        maxResults=20,
        showDeleted=False,
        dueMax='2023-02-11T00:00:00.000Z'
    ).execute()
    items = response.get('items')

    totalTasks += len(items)
    # Group items in a object according to its flag 
    tasks[flag['title']] = items
    # Group items LENGTH in a object according to its flag 
    tasksLen[flag['title']] = len(items)

print(totalTasks)

# RETORNAR QUANTAS TAREFAS DE CADA LISTA FORAM FEITAS

# CALCULAR PORCENTAGEM IMPACTO DA LISTA X NO TOTAL DE ATIVIDADES
# X% das suas atividades sao advindas da lista Y 
percentLists = {}
for key, value in tasksLen.items():
    percentLists[key] = round((value/totalTasks)*100)

    # print(f"{percentLists[key]}% of your tasks comes from flag: {key}")


# DE QUAL LISTA VEM AS TASKS QUE EU MAIS CONCLUO
notConcludedTasks = {}
for key, value in tasks.items():
    notConcludedTasks[key] = 0
    for item in value:
        print(f"\n {item['title']}   |  {item['status']}")
        if item['status'] == 'needsAction':
            notConcludedTasks[key] += 1

print(notConcludedTasks)
# print(tasks)
