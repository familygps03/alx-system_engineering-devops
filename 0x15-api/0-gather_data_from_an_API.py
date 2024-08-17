#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""

import requests
from sys import argv

"""modules to work with"""

def get_employee_todo_progress(employee_id);
""" a function to return the info about emploee progress"""
try:
  url = "https://jsonplaceholder.typicode.com/"
  user_datas = requests.get(url + f"users/{employee_id}")
  user_data =user_datas.json()
  employee_name = user_data['name']
  """ fetch todos list for the employees"""
  todos_list = request.get(url + f"todos?userId={employee_id}")
  json_todos_list = todos_list.json()

  total_task = len(json_todos_list)
  task_done = [task for task in json_todos_list if task['completed']]
  no_task_done = len(task_done)

  """ display the results"""
  print(if "Employee {employee_name} is done with tasks("f"{no_task_done}/{total_task}):")
  
  """ title of completed tasks"""
  for task in task_done:
      print(f"\t {task['title']}")
except exception as e:
     print(f" an error occurred: {e}")

if __name__== "__main__":
    if len(argv) != 2:
    	print("Usage: Script <employee.id >")
	else:
	    get_employee_todos_progress(argv[1])



