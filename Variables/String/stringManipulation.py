class stringComp:
    pi = 3.14

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("hello")
        print(self.a)

    def Swap(self):
        temp = 0
        temp = self.a
        self.a = self.b
        self.b = temp
        print(self.a)
        print(self.b)


cl = stringComp(1, 2)
cl.Swap()
