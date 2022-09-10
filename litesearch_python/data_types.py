run = True
colors = []



colors.append('Red')
colors.append('Blue')
colors.append('Yellow')

while(run):
    user_input = input() 
    if user_input == "delete":
        colors.pop()
    if user_input == "add":
        add_item = input()
        colors.append(add_item)
    if user_input == "exit":
        run = False
    print(colors)