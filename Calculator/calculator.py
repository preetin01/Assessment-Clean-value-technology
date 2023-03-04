# Author: Preeti Nishad
# College: Raj Kumar Goel Institute of Technology, Ghaziabad
# College Id: 2000330100163@rkgit.edu.in

def cal_func(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return "{:.2f}".format(num1 / num2)
    else:
        print('Invalid Operator')    
    
while True:
    n1 = input("Enter the first parameter: ")
    if n1 == "exit":
        break
    op = input("Enter the operator to perform (+, -, /, *): ")
    n2 = input("Enter the second parameter: ")
    n1 = int(n1)
    n2 = int(n2)
    result = cal_func(n1, op, n2)
    print('Result: ',result)
