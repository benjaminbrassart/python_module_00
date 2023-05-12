cookbook = {
    "Sandwhich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}

def print_recipe_names():
    for k in cookbook.keys():
        print(k)

def print_recipe_details():
    print("Please enter a recipe name to get its details:")
    name = input(">> ")

    recipe = cookbook.get(name)

    if recipe is None:
        print("invalid recipe")
        return

    ingredients = recipe["ingredients"]
    meal = recipe["meal"]
    prep_time = recipe["prep_time"]

    print(f"Recipe for {name}:")
    print(f"  Ingredients list: {ingredients}")
    print(f"  To be eaten for {meal}.")
    print(f"  Takes {prep_time} minutes of cooking.")

def delete_recipe():
    print("Please enter a recipe name to delete:")
    name = input(">> ")

    deleted = cookbook.pop(name, None)

    if deleted is None:
        print("invalid recipe")
        return

    print(f"{name} deleted")

def add_recipe():
    print("Enter a name:")
    name = input(">> ")

    if name in cookbook:
        print("{name} already exists")
        return

    print("Enter ingredients:")
    ingredients = []

    while True:
        iname = input(">> ")

        if len(iname) == 0:
            break
        
        ingredients += iname

    print("Enter a meal type:")
    meal = input(">> ")

    while True:

        print("Enter a preparation time:")
        ipt = input(">> ")

        try:
            prep_time = int(ipt)

            if prep_time >= 0:
                break
        except:
            pass

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }

def quit_cookbook():
    print("Cookbook closed. Goodbye!")
    exit(0)

options = {
    "1": ("Add a recipe", add_recipe),
    "2": ("Delete a recipe", delete_recipe),
    "3": ("Print a recipe", print_recipe_details),
    "4": ("Print the cookbook", print_recipe_names),
    "5": ("Quit", quit_cookbook),
}

def usage():
    print("List of available option:")

    for k, (desc, _) in options.items():
        print(f"{k}: {desc}")

print("Welcome to the Python Cookbook !")
usage()

while True:
    print()
    print ("Please select an option:")
    choice = input(">> ")
    
    print()

    opt = options.get(choice, None)

    if opt is None:
        print("Sorry, this option does not exist.")
        usage()
        continue

    _, func = opt

    func()
