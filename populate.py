from Google import convert_to_RFC_datetime
from tasksServer import tasksServer


# LIST OF TASKLISTS 
response = tasksServer.tasklists().list().execute()

tasksList = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = tasksServer.tasklists().list(
        maxResults=30,
        pageToken=nextPageToken
    )
    tasksList.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

destTaskListId = 'aUN6RUtzU0J4dzVDV3N4UQ'
originList = 'MTM3NDQxMTY2NDU4NzMzODA5MjI6MDow'

# TASKS 
# response = tasksServer.tasks().list(
#     taskList='Minhas tarefas',
#     maxResults=20
# )

# print(response)

# tasks = response.get('items')

# codeTasks = [x for x in tasks if 'CODE' in x['title']]
# print(codeTasks)

# tasksServer.tasks().move(

# ).execute


# GET TASKS WITH 'CODE' IN NAME
response = tasksServer.tasks().list(
    tasklist=originList,
    maxResults=50,
    showDeleted=False,
    # dueMin='2023-03-11T00:00:00.000Z'
).execute()

# print(response)

tasks = response.get('items')

codeTasks = [x for x in tasks if 'CODE' in x['title']]
print(codeTasks[0])

# for i in codeTasks:
#     print(i)



