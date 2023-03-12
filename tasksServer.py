from Google import Create_Service


CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'tasks'

# TASKS
TASKS_API_VERSION = 'v1'
TASKS_SCOPE = ['https://www.googleapis.com/auth/tasks']

class Task:
    @staticmethod
    def init():
        return Create_Service(CLIENT_SECRET_FILE, API_NAME, TASKS_API_VERSION, TASKS_SCOPE)
