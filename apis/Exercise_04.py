'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 151,
    "first_name": "mikikooo",
    "last_name": "freundddd",
    "email": "mikikooo@gmail.com"
}

response = requests.put(url, json=body)

response1 = requests.get(url)
print(response1.content)