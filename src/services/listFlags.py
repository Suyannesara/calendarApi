# RETURNS A LIST OF TASKLISTS USER HAS

def listFlags(server):
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
