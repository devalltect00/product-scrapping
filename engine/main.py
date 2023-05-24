import json

INGREDIENTS = "ingredients/ingredients.json"

if __name__ == '__main__':
    with open(INGREDIENTS) as i:
        ingredients = json.load(i)
    # print("Hi this is from python")