
"""
    Types of operators
"""
#Task Aritmetic Operators
def show_aritmetic_operators():
    
    # Addition
    result = 5 + 3
    print(result)  # Output: 8

    # Subtraction
    result = 10 - 4
    print(result)  # Output: 6

    # Multiplication
    result = 2 * 6
    print(result)  # Output: 12

    # Division
    result = 15 / 4
    print("Division;",result)  # Output: 3.75
    
    # Floor division or integer division. Quotient when a is divided by b, rounded to the next smallest whole number
    a= 15//4
    print ("Floor division",a) # Output: 3

    # Modulus (Remainder)
    result = 17 % 5
    print(result)  # Output: 2

    # Increment
    num = 5
    num += 1
    print(num)  # Output: 6

    # Decrement
    num = 8
    num -= 1
    print(num)  # Output: 7
    
    # Exponential. Form 1
    base = 3
    exponent = 4
    print("Exponential Value is: ", base ** exponent)
    
    # Exponential. Form 2
    base = 2
    exponent = 4
    print("Exponential Value is: ", pow(base, exponent))
    


#Task Assignment operators
def show_assigment_operators():
    # Assignment operator
    x = 10
    print(x)  # Output: 10

    # Compound assignment operators
    y = 5
    y += 2
    print(y)  # Output: 7

    z = 10
    z *= 3
    print(z)  # Output: 30

    w = 15
    w /= 2
    print(w)  # Output: 7.5

    m = 10
    m %= 3
    print(m)  # Output: 1

#Task: Comparison operators:
def show_comparison_operators():
    # Equality
    result = (5 == 5)
    print(result)  # Output: True

    # Inequality
    result = (7 != 3)
    print(result)  # Output: True

    # Greater than
    result = (10 > 8)
    print(result)  # Output: True

    # Less than
    result = (6 < 4)
    print(result)  # Output: False

    # Greater than or equal to
    result = (5 >= 5)
    print(result)  # Output: True

    # Less than or equal to
    result = (3 <= 2)
    print(result)  # Output: False

# Task:  Logical operators
def show_logical_operators():
    # Logical AND
    result = True and False
    print(result)  # Output: False

    # Logical OR
    result = True or False
    print(result)  # Output: True

    # Logical NOT
    result = not True
    print(result)  # Output: False

#Task: Conditional operators
def show_conditional_operator():
    # Ternary conditional operator
    x = 10
    result = "Even" if x % 2 == 0 else "Odd"
    print(result)  # Output: Even

#Task: Concatenate String
def show_concatenante_string():
    # string definition
    x = "This is a string"
    y = " This is a string2"
    result = x + y
    print(result)  # Output: Even


if __name__ == "__main__":
    show_aritmetic_operators()
    show_assigment_operators()
    show_comparison_operators()
    show_logical_operators()
    show_concatenante_string()
    show_conditional_operator()

