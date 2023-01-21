from classes import CookBook, ShopList

RECIPES_FILE = "recipes.txt"
cook_book = CookBook("cook_book")


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = ShopList()
    shop_list.add_dishes(cook_book, dishes, person_count)
#    print(shop_list)
    return shop_list.convert_to_dict()


with open(RECIPES_FILE, encoding="utf-8") as f:
    cook_book.load_from_file(f)
#print(cb)

sl_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(sl_dict)