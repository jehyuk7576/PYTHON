"""
num1, num2 = input(": ").split()
print(num1)
print(num2)

print("------")
"""

import sum
import mul
import dec
import div

number1 = input("num1 : ")
number2 = input("num2 : ")

sum.sum(int(number1), int(number2))
dec.dec(int(number1), int(number2))
mul.mul(int(number1), int(number2))
div.div(int(number1), int(number2))