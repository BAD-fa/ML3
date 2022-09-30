
# small = 10
# medium = 15
# big = 20
#
# try:
#     budget = int(input())
#
#     if budget < 0:
#         raise Exception
#
#     if budget < 10:
#         print("ghahve nadarim")
#     elif 10 <= budget < 15:
#         print("ghahve small")
#         print(f"baghi pool {budget - 10}")
#     elif 15 <= budget < 20:
#         print("ghahve medium")
#         print(f"baghi pool {budget - 15}")
#     elif 20 <= budget:
#         print("ghahve big")
#         print(f"baghi pool {budget - 20}")
#
# except:
#     print("boro biroon")
#
#

class Coffee:
    cup = 10

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @staticmethod
    def check_budget(budget):
        try:
            budget = int(budget)
            if budget < 0:
                return False
            return int(budget)
        except:
            return False

    def sell(self, budget):
        if _budget := self.check_budget(budget):
            if _budget >= self.price:
                Coffee.cup -= 1
                return f"{self.size} coffee \n baghie pool {_budget - self.price}"

        return "boro biroon"

    def change_price(self, new_price):
        self.price = new_price


if __name__ == "__main__":
    small = Coffee("small", 10)
    # print(small.cup, small.price)
    medium = Coffee("medium", 15)
    # print(medium.cup, medium.price)
    big = Coffee("big", 20)
    # print(big.cup, big.price)

    budget = input()

    print(small.sell(budget))
    print(small.cup)
    print(medium.cup)
    print(big.cup)
    print(medium.sell(budget))
    print(small.cup)
    print(medium.cup)
    print(big.cup)
    print(big.sell(budget))
    print(small.cup)
    print(medium.cup)
    print(big.cup)

    small.change_price(30)
    print(small.price)
    print(medium.price)
    print(big.price)
