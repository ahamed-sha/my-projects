import requests
from datetime import datetime, timedelta

TOKEN = "11011"
USERNAME = "jeff"
GRAPH_ID = "new_graph"


current_date = datetime.now() - timedelta(1)
current_date = datetime.strftime(current_date, '%Y%m%d')

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

entry_config = {
    "date": current_date,
    "quantity": "7"
}

update_config = {
    "quantity": "10"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
entry_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"

# -------------------------------------------------------------------------------------------------------#

# Create a new user

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# -------------------------------------------------------------------------------------------------------#

# Create a graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# -------------------------------------------------------------------------------------------------------#

# Create an entry

# response = requests.post(url=entry_endpoint, json=entry_config, headers=headers)
# print(response.text)

# -------------------------------------------------------------------------------------------------------#

# Update an entry

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# -------------------------------------------------------------------------------------------------------#

# Delete an entry

# response = requests.delete(url=update_endpoint,headers=headers)
# print(response.text)
