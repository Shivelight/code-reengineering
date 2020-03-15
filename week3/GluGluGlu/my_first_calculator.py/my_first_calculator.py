# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}   

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.div
    }   
print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
op_func = ops[sign]
print(f"{num1} {sign} {num2} = {op_func(num1, num2)}")
print("Thanks for using this calculator, goodbye :)")
