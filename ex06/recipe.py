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
    print(f"  Ingredients list: {recipe}")
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

            if prep_time > 0:
                break
        except:
            pass

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }
