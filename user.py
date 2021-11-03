from PyInquirer import prompt
import json

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"User - Name: ",
    }
]

user_list = []
user_involved = []

def load_users():
    file = open('users.json', 'r')
    data = json.load(file)
    for user in data:
     user_list.append(user)
     user_involved.append({'name' : user})

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.json', 'r') as file:
        data = json.load(file)
        data[infos['name']] = { 'spent': 0, 'owe': 0 }
        with open("users.json", "w") as write_file:
            json.dump(data, write_file)
    print('User Added!')
    return True