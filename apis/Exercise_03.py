'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Mikiko200",
    "last_name": "Freund200",
    "email": "mikiko200@gmail.com",
}

response = requests.post(base_url, json=body)

response1 = requests.get(base_url)
print(response1.content)
