""" This is the basic (+) advance calculator, I assure you that it can help you in every aspect of Mathematical calculation in day two day life...
 I know this is not a best calculator in this whole world ...if you like any change please let me know that ..."""

import math
import operator

def basic_operations(op, a, b=None):  #Supported operations: +, -, *, /, ** (power)
   
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow
    }
    
    if op not in operations:
        return "Unsupported operation"
    
    if b is None:
        return "Two operands required for this operation."
    
    try:
        return operations[op](a, b)
    except ZeroDivisionError:
        return "Cannot divide by zero"

def advanced_operations(op, a):  # Supported operations: sqrt, sin, cos, tan, factorial....
    
    
    try:
        if op == 'sqrt':
            return math.sqrt(a)
        elif op == 'sin':
            return math.sin(math.radians(a))
        elif op == 'cos':
            return math.cos(math.radians(a))
        elif op == 'tan':
            return math.tan(math.radians(a))
        elif op == 'factorial':
            return math.factorial(a)
        else:
            return "Unsupported operation"
    except ValueError:
        return "Math domain error"
    except OverflowError:
        return "Result too large"
    
def calculator():
    print("Python Calculator")
    print("Available operations: +, -, *, /, **, sqrt, sin, cos, tan, factorial")
    
    while True:
        choice = input("Enter operation (or 'exit' to quit): ")
        
        if choice == 'exit':
            print("Exiting calculator...")
            break
        
        if choice in ['+', '-', '*', '/', '**']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = basic_operations(choice, a, b)
        
        elif choice in ['sqrt', 'sin', 'cos', 'tan', 'factorial']:
            a = float(input("Enter number: "))
            result = advanced_operations(choice, a)
        
        else:
            print("Invalid operation.")
            continue
        
        print(f"Result: {result}\n")
    

calculator()
