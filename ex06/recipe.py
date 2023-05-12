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

    ingredients = recipe["ingredients"]
    meal = recipe["meal"]
    prep_time = recipe["prep_time"]

    print(f"Recipe for {name}:")
    print(f"  Ingredients list: {recipe}")
    print(f"  To be eaten for {meal}.")
    print(f"  Takes {prep_time} minutes of cooking.")
