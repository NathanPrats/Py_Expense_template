from PyInquirer import prompt
from user import user_list,user_involved
import json

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": user_list
    },
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved: ",
        "choices": user_involved
    },

]

def new_expense(*args):
    #Add an expense from 3 arguments : Amount, Label, Spender
    infos = prompt(expense_questions)
    involved_users = []
    with open('expense_report.csv', 'a') as file:
     involved = '[' + infos['spender']
     for user in infos['involved']:
         if user != infos['spender']:
          involved += '/' + user
         involved_users.append(user)
     involved += ']'
     involved_users.append(infos['spender'])
     line = infos['amount'] + ',' + infos['label'] + ',' + infos['spender'] + ',' + involved + '\n'
     file.write(line)
    print('Expense Added!')
    #Update users info with expense
    file = open('users.json', 'r')
    data = json.load(file)
    spender = data[infos['spender']]
    total = int(infos['amount'])
    share = int(infos['amount']) / len(involved_users)
    spender['spent'] += total
    spender['owe'] += share - total
    for user in involved_users:
      if user != infos['spender']:
        data[user]['owe'] += share
    with open("users.json", "w") as write_file:
     json.dump(data, write_file)
    return True


