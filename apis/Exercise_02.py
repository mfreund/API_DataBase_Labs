'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")
data = response.json()

email_list = []

for user in data['data']:
    list.append(user['email'])

print(email_list)


# OR
# emails = [x['email'] for x in data['data']]
#
# print(emails)
