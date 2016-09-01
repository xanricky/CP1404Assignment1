def subject():
 """ This is pseudocode for two functions
    def Loading_items():
        display welcome to shopping List
        get_user_input = "please enter S to see shopping list"
            if (get_user_input != s or S)
            prompt
            else get_user_input = items()
            def items():
            display (Fish fingers,12.95,2,r/Metal detector,42.5,3,r/Coffee beans,40.0,1,r)
            return Loading_items
        def completing_items()
            user_input = "please enter C for see completed items
            elif user_input != C or c
            prompt
            user_input = Complete_items()
        return completing_items
        def Complete_items()
             display (complete items)"""
#Thu Ya Aung,2nd September 2016, This is a shopping list Program.User can see required and completed items.Moreover, user can add new items and mark as complete.
#Items will be sorted in piriority.The price of each items and total will be showed in each case.
#Github-link: https://github.com/xanricky/CP1404Assignment1.git

from operator import itemgetter
def welcome_msg ():
    get_name = str(input("Please enter name:"))
    print("welcome to shoppinglist {}".format(get_name))


def print_menu():
    menu_str = """
    Shopping List 1.0 - by Thu Ya Aung
    Menu:
    R - List required items
    C - List completed items
    A - Add new item
    M - Mark an item as completed
    Q - Quit """
    print (menu_str)

def get_input(valid_input):
    user_input = input(">>>").lower()
    if user_input not in valid_input:
        user_input = input(">>>").lower()
    return user_input

def req_items():
    list_items.sort(key=itemgetter(2,0))
    count = 0
    total_price = 0
    for q in list_items:
        if(q[3]== "r"):
            total_price += float(q[1])
            print("{}. {} ${} ({})".format(count, q[0], float(q[1]), q[2]))
            count +=1
    if count == 0:
        print("No required items")
    else:
        print("Total price ${}".format(total_price))


def comp_items():
    list_items.sort(key=itemgetter(2,0))
    count = 0
    total_price = 0
    for j in list_items:
        if(j[3] == "c"):
            total_price += float(j[1])
            print("{}. {} ${} ({})".format(count, j[0], float(j[1]), j[2]))
            count += 1

    if count == 0:
        print("No items completed")
    else:
        print("Total price ${}".format(total_price))

def add_items():
    i = []
    while True:
        item_name = str(input("please enter name of item:"))
        if  item_name =="":
            print("Cannot be blank")
            continue
        elif item_name ==" ":
            print("cannot Space")
            continue
        if item_name !=" ":
            i.append(item_name)
            break
    while True:
        try:
            item_price = int(input("please enter price:"))
        except ValueError:
            print("enter a number:")
            continue
        if item_price < 50:
            print ("Price must be at least $50")
            continue
        else:
            i.append(item_price)
            break
    while True:
        priority = input("Please enter priority")
        try:
           int(priority)
        except ValueError:
            print("Invalid")
            continue
        if priority not in ('1', '2', '3'):
            print("Priority must be 1, 2 or 3 ")
        else:
            i.append(priority)
            i.append("r")
            break
    print("{}, ${} (priority {}) added to shopping list.".format(i[0], float(i[1]), i[2]))

    list_items.append(i)

def mark_comp():
    req_items()

    t = []
    for item in list_items:
       if(item[3] == "r"):
            t.append(item)
    user_input = int(input("Enter the number of the item to mark as complete: "))
    count = 0
    for item in t:
        if(count == user_input):
            print("{} marked as complete".format(item[0]))
            item[3] = "c"
        count += 1
        for item in t:
         if(item[3] == "c"):
            for each in list_items:
                if(each[0] == item[0]):
                    each[3] = "c"
                    break


def load_items():
    file_pointer = open("items.csv", "r")
    for each in file_pointer:
        list_items.append(each.replace("\n", "").split(","))

    file_pointer.close()

list_items = []
load_items()

while True:
    print("Please enter Y to see pseudocode, N to quit")
    user_input = get_input(["y","n"])
    if user_input == "y":
        print(subject.__doc__)
        welcome_msg()
    else:
        welcome_msg()
    break

while True:
    print_menu()
    user_choice = get_input(["r", "c", "a", "m", "q"])
    if user_choice == "q":
        print("Items have been saved to items.csv.Have a nice day ")
        break
    elif user_choice == "r":
        req_items()
    elif user_choice == "c":
        comp_items()
    elif user_choice == "a":
        add_items()
    elif user_choice == "m":
        mark_comp()
