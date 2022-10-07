from models import Restaurant, User


class Application:
    list_of_users = {}
    list_of_restaurants = {}

    def __init__(self):
        self.user = None
        self.restaurant = None

    def login(self, username, password):
        user: User = Application.list_of_users.get(username, None)
        if user:
            if user.password == password:
                self.user = user
                return
            else:
                raise Exception("Wrong password")

        raise Exception("User Not found")

    def register(self, username, password):
        user: User = Application.list_of_users.get(username, None)
        if not user:
            Application.list_of_users[username] = User(username, password)
            return self.login(username, password)
        else:
            raise Exception("User already exists")

    @staticmethod
    def add_restaurant(name) -> Restaurant:
        restaurant = Application.list_of_restaurants.get(name)
        if not restaurant:
            Application.list_of_restaurants[name] = Restaurant(name)
            return Application.list_of_restaurants[name]

        raise Exception("Restaurant already exists")

    @staticmethod
    def show_restaurants():
        return Application.list_of_restaurants.keys()

    def choose_restaurant(self, restaurant_name):
        restaurant: Restaurant = Application.list_of_restaurants.get(restaurant_name, None)
        if restaurant:
            self.restaurant = restaurant
            return

        raise Exception("Restaurant not found")

    def show_menu(self):
        return self.restaurant.show_menu()

    def choose_food(self, food_name, count):
        bill = self.restaurant.menu.choose_food(food_name, count)
        self.user.bill += bill
        if food_name in self.user.cart:
            self.user.cart[food_name] += count
        else:
            self.user.cart[food_name] = count

    def pay_bill(self):
        self.user.pay_bill()

    def logout(self):
        self.user = None
        self.restaurant = None


if __name__ == "__main__":
    app = Application()
    app.register("behrad", "1234567")

    print(app.user)

    res = app.add_restaurant("res1")
    res.menu.add_food("food1", 10000, 10)
    res.menu.add_food("food2", 20000, 1)
    res.menu.add_food("food3", 30000, 10)

    res = app.add_restaurant("res2")
    res.menu.add_food("food4", 40000, 5)
    res.menu.add_food("food5", 20000, 1)
    res.menu.add_food("food6", 30000, 10)

    print(app.show_restaurants())

    app.choose_restaurant("res1")
    print(app.show_menu())

    print(app.restaurant)

    while True:
        try:
            food_name = input()
            count = int(input())
            if food_name == "Done":
                break
            app.choose_food(food_name, count)
        except Exception as e:
            print(e)

    print(app.user.bill)
    print(app.user.cart)

    app.pay_bill()

    print(app.user.history)
    print(app.user.bill)
    print(app.user.cart)
