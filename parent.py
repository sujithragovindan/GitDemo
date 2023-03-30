class Cal:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("constructor")

    def get(self):
        print("hi")

    def summation(self):
        return self.a + self.b + Cal.num


obj = Cal(2, 3)
obj.get()
print(obj.num)
print(obj.summation())

obj1 = Cal(4, 5)
obj1.get()
print(obj1.num)
print(obj.summation())
