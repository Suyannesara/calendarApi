from Google import convert_to_RFC_datetime
from tasksServer import tasksServer

# CREATE TASKS LISTS
# tasklistRestaurants = tasksServer.tasklists().insert(
#     body={'title': 'Restaurants to try'}
# ).execute()

# for i in range(100):
#     tasksServer.tasklists().delete(body={'title': 'Tasklst #{0}'.format(i+1)}).execute()

# LIST METHOD
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

# print(tasksList)

# DELETE METHOD
# for item in tasksList:
#     try:
#         if isinstance(int(item.get('title').replace('Restaurants to try', '')), int):
#             if int(item.get('title').replace('Restaurants to try', '')) < 50:
#                 tasksServer.tasklists().delete(tasklist=item.get('id')).execute()
#     except:
#         pass

response = tasksServer.tasklists().list(maxResults=100).execute()
# print(response.get('items'))


# UPDATE METHOD 
items = response.get('items')

toUpdate = list(filter(lambda tasklist: tasklist['title'] == 'Restaurants to try', items))

for item in toUpdate:
    item['title'] = 'Restaurantes man'
    tasksServer.tasklists().update(tasksList=item['id'], body=item).execute()

