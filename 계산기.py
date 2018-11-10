class Calculater():
    def __init__(self):
        self.result = 0
    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result
    def dec(self, num1, num2):
        self.result = num1 - num2
        return self.result
    def mul(self, num1, num2):
        self.result = num1 * num2
        return self.result
    def div(self, num1, num2):
        self.result = num1 / num2
        return self.result


con = Calculater()
print(con.add(1, 2))
print(con.dec(1, 2))
print(con.mul(1, 2))
print(con.div(1, 2))
