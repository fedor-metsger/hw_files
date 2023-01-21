class Ingredient:
    def __init__(self, name, quantity, measure):
        self.name = name
        self.quantity = quantity
        self.measure = measure
    
    def __str__(self):
        return "{'ingredient_name': '" + self.name + \
            "', 'quantity': '" + str(self.quantity) + \
            "', 'measure': '" + self.measure + "'}"

    def convert_to_dict(self):
        return {"ingredient_name": self.name, 
               "quantity": self.quantity,
               "measure": self.measure}


class Dish:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ing):
        self.ingredients += [ing]

    def __str__(self):
        ing_str = []
        for i in self.ingredients:
            ing_str += [str(i)]
        return "  '" + self.name + "': [\n    " + \
            ",\n    ".join(ing_str) + \
            "\n    ]"

    def convert_to_list(self):
        lst = []
        for i in self.ingredients:
            lst += [i.convert_to_dict()]
        return lst
        

class CookBook:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes += [dish]

    def __str__(self):
        dish_str = []
        for d in self.dishes:
            dish_str += [str(d)]
        return self.name + " = {\n" + \
            ",\n".join(dish_str) + \
            "\n  }"

    def convert_to_dict(self):
        res = {}
        for d in self.dishes:
            res[d.name] = d.convert_to_list()
        return res

    def load_dish_from_file(self, f):
        while True:
            l = f.readline()
            if not l: return None
            if l.strip() != "": break

        d = Dish(l.strip())
        cnt = int(f.readline())
        for i in range(cnt):
            n, q, m = f.readline().strip().split(" | ")
            d.add_ingredient(Ingredient(n, int(q), m))
        return d
        
    def load_from_file(self, f):
        while True:
            d = self.load_dish_from_file(f)
            if not d: return
            self.dishes += [d]

    def get_dish(self, dish_name):
        for d in self.dishes:
            if d.name == dish_name: return d
        return None
        

class ShopList:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ing, persons):
        if ing.name in self.ingredients:
            self.ingredients[ing.name]["quantity"] += \
                ing.quantity * persons
        else:
            self.ingredients[ing.name] = {
                "quantity": ing.quantity * persons,
                "measure": ing.measure}

    def add_dish(self, dish, persons):
        for i in dish.ingredients:
            self.add_ingredient(i, persons)
            
    def add_dishes(self, cb, dish_list, persons):
        for d in dish_list:
            self.add_dish(cb.get_dish(d), persons)

    def __str__(self):
        ing_str = []
        for i in self.ingredients:
            ing_str += [f"'{i}': " + "{'measure': '" + \
                self.ingredients[i]["measure"] +
                "', 'quantity': '" +
                str(self.ingredients[i]["quantity"]) + "'}"]
        return "{\n  " + ",\n  ".join(ing_str) + "\n}"

    def convert_to_dict(self):
        res = {}
        for i in self.ingredients:
            res[i] = {
                "measure": self.ingredients[i]["measure"],
                "quantity": self.ingredients[i]["quantity"]}
        return res