from ..servers.Google import convert_to_RFC_datetime

# RETURN ALL TASKS OF A LIST 

def listTasksFromFlag(server, listId):
    # INITAL RESPONSE 
    response = server.tasks().list(
        tasklist=listId,
        maxResults=100,
        # showDeleted=True,
        showCompleted=True,
        # dueMin=convert_to_RFC_datetime(2023, 3, 10),
    ).execute()

    items = response.get('items')
    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        response = server.tasks().list(
            tasklist=listId,
            maxResults=100,
            showDeleted=True,
            showCompleted=True,
            # dueMax=convert_to_RFC_datetime(2023, 2, 10),
            pageToken=nextPageToken
        ).execute()
        items = response.get('items')
        nextPageToken = response.get('nextPageToken')
    # print(pd.DataFrame(items))
    return items
