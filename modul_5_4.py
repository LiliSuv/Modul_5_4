class House:
    __instance = None

    def __new__(cls, *args, **kwargs, ):
        cls.args = args
        cls.houses_history = houses_history
        for i in range (len (args)):
            houses_history.append (args[i])
        return object.__new__ (cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            print (new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):

        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")

        return self.number_of_floors == other

    def __lt__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors < other

    def __le__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")

        return self.number_of_floors <= other

    def __gt__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors > other

    def __ge__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors >= other

    def __ne__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors != other

    def __add__(self, valuo):

        self.number_of_floors = self.number_of_floors + valuo
        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __radd__(self, valuo):
        self.number_of_floors = valuo + self.number_of_floors
        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __iadd__(self, valuo):

        self.number_of_floors += valuo
        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print (f'{self.name} снесён, но он останется в истории')


houses_history = []
h1 = House ('ЖК Горский', 18)
print (House.houses_history)
h2 = House ('Домик в деревне', 2)
print (House.houses_history)
h3 = House ('ЖК Золотой Родник', 9)
print (House.houses_history)
