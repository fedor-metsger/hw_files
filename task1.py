from classes import CookBook

RECIPES_FILE = "recipes.txt"

cb = CookBook("cook_book")

with open(RECIPES_FILE, encoding="utf-8") as f:
    cb.load_from_file(f)
#print(cb)

cb_dict = cb.convert_to_dict()
print(cb_dict)