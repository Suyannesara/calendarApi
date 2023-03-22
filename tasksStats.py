from src.services.listFlags import listFlags
from src.services.listTasksFromFlag import listTasksFromFlag
from src.servers.tasksServer import Task
import pandas as pd

server = Task().init()

# A - CALCULAR PORCENTAGEM DE IMPACTO DA LISTA X NO TOTAL DE ATIVIDADES
# RETORNAR QUANTAS TAREFAS DE CADA LISTA FORAM FEITAS
# X% das suas atividades sao advindas da lista Y 

# ROUTE A
def percentOfTasksFromFlag(server, listTitle):
    tasksLen = {}
    totalTasks = 0

    flagsList = listFlags(server)

    # GET TOTAL TASKS AND TASKS LEN OF A LIST
    for flag in flagsList:
        items = listTasksFromFlag(server, flag['id'])

        totalTasks += len(items)
        # Group items LENGTH in a object according to its flag 
        tasksLen[flag['title']] = len(items)

    for key, value in tasksLen.items():
        if key == listTitle:
            percentFromList = round((value/totalTasks)*100)
            return percentFromList
            # print(f"{percentLists[key]}% of your tasks comes from flag: {key}")

percent  = percentOfTasksFromFlag(server, 'Minhas tarefas')
print(percent)

# ROUTE B
def flagOfMostCompletedTasks():
    # DE QUAL LISTA VEM AS TASKS QUE EU MAIS CONCLUO
    notConcludedTasks = {}
    for key, value in tasks.items():
        notConcludedTasks[key] = 0
        for item in value:
            print(f"\n {item['title']}")
            if item['status'] == 'needsAction':
                notConcludedTasks[key] += 1

    # print(notConcludedTasks)
    # for key, value in tasks.items():
    #     print(f"{value}\n")
