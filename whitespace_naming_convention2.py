# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class Pizza:
    def __init__(self, mybread_type, CHEESE_TYPE, meatType, pizza_toppings, size):
        self.bread_type = mybread_type
        self.cheese_type = CHEESE_TYPE
        self.meatType = meatType
        self.toppings = pizza_toppings
        self.size = size

    @classmethod
    def Create_ChicagoPizza(cls, class_type, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meatType = 'Italian sausage'
        toppings = ['green bell pepper', 'mushroom',
                    'chunky tomato sauce', 'onion']
        return class_type(bread, cheese, meatType, toppings, size)

    @classmethod
    def createCalifornia_pizza(cls, class_type, meat_Type, size):
        bread = 'thin crust'
        CHEESE = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return class_type(bread, CHEESE, meat_Type, toppings, size)

    def printInfo(self):
        print('bread type is: ', self.bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))


myPizza = Pizza.createCalifornia_pizza('chicken', 'large')
myPizza.printInfo()
