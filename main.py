def add():
  with open("todolist.txt","a") as f:
    task=input("enter your task")
    f.write(task+"\n")
def view():
  with open("todolist.txt","r") as f:
    for line in f:
      print(line)

while True:
  a=input("if you want to add a task press add and to view press view and q for exit>>>>>")
  if a=="add":
    add()
  elif a=="view":
    view()
  elif a=="q":
    break
      
  else:
    print("invalid input")