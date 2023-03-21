from ..servers.Google import convert_to_RFC_datetime
import pandas as pd


# RETURNS A LIST OF TASKLISTS 
def listTasksList(server):
    response = server.tasklists().list().execute()

    tasksList = response.get('items')
    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        response = server.tasklists().list(
            maxResults=30,
            pageToken=nextPageToken
        )
        tasksList.extend(response.get('items'))
        nextPageToken = response.get('nextPageToken')

    return tasksList

def listTasksInList(server):
    # PEGAR TASKS DE UMA LISTA X
    flagsList = listTasksList(server)

    # INITAL RESPONSE 
    
    response = server.tasks().list(
        tasklist=flagsList[0]['id'],
        maxResults=100,
        # showDeleted=True,
        showCompleted=True,
        # completedMax=convert_to_RFC_datetime(2023, 2, 10),
    ).execute()

    items = response.get('items')
    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        for flag in flagsList:
            response = server.tasks().list(
                tasklist=flag['id'],
                maxResults=100,
                showDeleted=True,
                showCompleted=True,
                # dueMax=convert_to_RFC_datetime(2022, 2, 10),
                pageToken=nextPageToken
            ).execute()
            items = response.get('items')
            nextPageToken = response.get('nextPageToken')
    print(pd.DataFrame(items))


    # tasksNextPageToken = response.get('nextPageToken')

    # while nextPageToken:
    #     print("tem taskss")
    #     nextPageToken = response.get('nextPageToken')

    # return tasksList



    # tasksLen = {}
    # tasks = {}
    # totalTasks = 0

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


# listTasksInList()
