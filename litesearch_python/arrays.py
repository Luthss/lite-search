# Todo learn array
run = True
house = ['Big' , 'Small', 'Tall']

house.append('Grand')

main_prompt = """
    Choose to add or delete a house type:
    Commands include:
        1. add :- to add a house type
        2. exit :- exit the program
        3. pop :- Delete the last item
        4. view :- view the list
        5. delete :- Delete an item you specify
        6. count :- count the items inside the array
    """

wrong_input = """
    Wrong Input !
    Try Again

    """

while(run):
    user_input = input(main_prompt)
    if user_input == "add":
        house.append(input("item to add = "))
    elif user_input == "pop":
        house.pop()
    elif user_input == "exit":
        run = False
    elif user_input == "view":
        print(house)
    elif user_input == "delete":
        print(house)
        house.remove(input("item to delete = "))
    elif user_input == "count":
        mycount = len(house)
        print(f'num of items = {mycount}')
    else:
        print(wrong_input)
