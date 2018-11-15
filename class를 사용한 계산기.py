class Calculater():
    def __init__(self):
        self.result = 0
    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result
    def sub(self, num1, num2):
        self.result = num1 - num2
        return self.result
    def mul(self, num1, num2):
        self.result = num1 * num2
        return self.result
    def div(self, num1, num2):
        self.result = num1 / num2
        return self.result

number1 = input("첫번째 수를 입력하세요 : ")
number2 = input("두번쨰 수를 입력하세요 : ")

con = Calculater()
print(con.add(int(number1), int(number2)))
print(con.sub(int(number1), int(number2)))
print(con.mul(int(number1), int(number2)))
print(con.div(int(number1),int(number2)))
