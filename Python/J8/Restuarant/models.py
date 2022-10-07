import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bill = 0
        self.cart = {}
        self.history = {}

    def pay_bill(self):
        self.history[datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")] = [self.cart, self.bill]
        self.bill = 0
        self.cart = {}

    def show_history(self):
        return self.history

    def __str__(self):
        return self.username


class Restaurant:

    def __init__(self, name):
        self.name = name
        self.menu = None
        self.set_menu()

    def set_menu(self):
        self.menu = Menu()

    def show_menu(self):
        return self.menu.list_of_foods

    def __str__(self):
        return self.name


class Menu:

    def __init__(self):
        self.list_of_foods = {}

    def add_food(self, name, price, stock):
        food = Food(name, price, stock)
        self.list_of_foods[name] = food

    def edit_food(self, food_name, param_name, param_value):
        '''
        edit_food(pizza, "price", 15000)
        :param food_name:
        :param param_name:
        :param param_value:
        :return:
        '''
        food = self.list_of_foods.get(food_name, None)
        if food:
            setattr(food, param_name, param_value)

        else:
            raise Exception("Food not found")

    def choose_food(self, food_name, count):
        food: Food = self.list_of_foods.get(food_name)
        if food:
            if food.stock >= count:
                food.stock -= count
                bill = food.price * count
                return bill
            else:
                raise Exception("Not enough stock")
        else:
            raise Exception("Food not found")


class Food:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.name
