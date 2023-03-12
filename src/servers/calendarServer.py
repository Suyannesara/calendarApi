from .Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'calendar'

# CALENDAR 
CALENDAR_API_VERSION = 'v3'
CALENDAR_SCOPE = ['https://www.googleapis.com/auth/calendar']

calendarServer = Create_Service(CLIENT_SECRET_FILE, API_NAME, CALENDAR_API_VERSION, CALENDAR_SCOPE)
