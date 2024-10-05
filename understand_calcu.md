Basic Operations: The basic_operations function handles arithmetic operations like addition, subtraction, multiplication, and division. It uses the operator module to perform these operations.
Advanced Operations: The advanced_operations function handles advanced math functions such as square root, trigonometric functions, and factorial.

Explaining all the functions and key terms used...
. import math
This statement imports Python's built-in math module, which provides access to advanced mathematical functions like square root (sqrt), trigonometric functions (sin, cos, tan), factorials (factorial), and more.
2. import operator
The operator module provides a set of efficient functions corresponding to standard operators (like addition, subtraction, multiplication, etc.). Instead of using a + b, we can use operator.add(a, b). This is particularly useful for mapping operations to strings or for functional programming.
3. basic_operations(op, a, b=None)
This function handles basic arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation.
4.advanced_operations(op, a)
This function handles more advanced mathematical operations like square root, trigonometric functions (sine, cosine, tangent), and factorials.
5. calculator()
This is the main function that ties everything together and provides a user interface for the calculator.

Basic operations
Parameters:
  op: A string representing the operation to be performed (e.g., '+', '-', '*', '/', '**').
  a: The first operand (a number).
  b: The second operand (another number), which is optional when the operation doesn't require two operands (but in this case, all basic operations need two).

Working:
A dictionary operations is created, mapping strings representing operations (+, -, *, /, **) to functions in the operator module that perform these operations.
The program checks if op is a supported operation. If it is, it applies the corresponding operation to a and b using operations[op](a, b).
Exception Handling: A try-except block is used to catch division by zero errors, returning "Cannot divide by zero" if the user tries to divide a number by zero.

 Advanced operations
 Parameters:
   op: A string representing the advanced operation to be performed (e.g., 'sqrt', 'sin', 'cos', 'tan', 'factorial').
   a: The operand (a number), which will be used as input to the selected operation.

Working:
This function checks if op matches any of the supported advanced operations. If it does, it applies the appropriate function from the math module to a.
For trigonometric operations (sin, cos, tan), the input a is first converted to radians using math.radians(a) because Python's trigonometric functions expect input in radians, not degrees.
Exception Handling: This function catches errors like ValueError (for cases where operations are mathematically undefined, e.g., square root of a negative number) and OverflowError (when the result is too large, especially for factorial).

Main working function(calculator working)
The function prints a welcome message and lists the available operations.
It enters an infinite loop (while True) that continuously asks the user to input a desired operation (like '+', '-', 'sqrt', etc.).
Based on the user's input:
If the operation is a basic operation (e.g., +, -, *, /, **), it asks for two numbers and calls basic_operations() to compute the result.
If the operation is an advanced one (e.g., sqrt, sin, factorial), it asks for one number and calls advanced_operations() to compute the result.
If the user types 'exit', the loop breaks, and the program ends.
The result of each operation is printed out to the user.


Key Python Concepts Used in the Program:
1. Dictionary:
A dictionary is used to map operator strings ('+', '-', '*', '/', '**') to corresponding functions in the operator module.
2. Function:
Functions like basic_operations() and advanced_operations() are blocks of reusable code. They allow the calculator program to be modular and maintainable.
3. Control Flow:
if-elif statements are used to determine which operation the user wants and to handle invalid inputs.
while True is an infinite loop that keeps asking the user for input until they type 'exit'.
4. Exception Handling:
Python's try-except block is used to handle potential errors like dividing by zero or taking the square root of a negative number. This makes the program more robust by ensuring it doesn't crash due to invalid inputs.
5. math.radians():
Trigonometric functions like sin, cos, and tan in Python's math module expect the input to be in radians, not degrees. The math.radians(a) function converts the degree input into radians.
