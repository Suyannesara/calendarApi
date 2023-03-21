from src.servers.Google import convert_to_RFC_datetime
from src.services.listTaskLists import listTasksList, listTasksInList
from src.servers.tasksServer import Task
import pandas as pd

server = Task().init()

# PEGAR TASKS DE UMA LISTA X
# flagsList = listTasksList()

tasksLen = {}
tasks = {}
totalTasks = 0


listTasksInList(server)






# for flag in flagsList:
#     response = server.tasks().list(
#         tasklist=flag['id'],
#         maxResults=100,
#         showDeleted=False,
#         showCompleted=True,
#         # completedMax='2023-02-11T00:00:00.000Z'
#     ).execute()
#     items = response.get('items')

#     totalTasks += len(items)
#     # Group items in a object according to its flag 
#     tasks[flag['title']] = items
#     # Group items LENGTH in a object according to its flag 
#     tasksLen[flag['title']] = len(items)

# print(totalTasks)

# # 1- CALCULAR PORCENTAGEM IMPACTO DA LISTA X NO TOTAL DE ATIVIDADES
# # RETORNAR QUANTAS TAREFAS DE CADA LISTA FORAM FEITAS
# # X% das suas atividades sao advindas da lista Y 
# percentLists = {}
# for key, value in tasksLen.items():
#     percentLists[key] = round((value/totalTasks)*100)
#     print(f"{percentLists[key]}% of your tasks comes from flag: {key}")


# # DE QUAL LISTA VEM AS TASKS QUE EU MAIS CONCLUO
# notConcludedTasks = {}
# for key, value in tasks.items():
#     notConcludedTasks[key] = 0
#     for item in value:
#         print(f"\n {item['title']}")
#         if item['status'] == 'needsAction':
#             notConcludedTasks[key] += 1

# # print(notConcludedTasks)
# # for key, value in tasks.items():
# #     print(f"{value}\n")
