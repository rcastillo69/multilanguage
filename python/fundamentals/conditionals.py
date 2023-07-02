# Task Conditional

# Task Simple conditional
def simple_conditional():
    greeting = "This is a simple conditional"
    condition = (1>0) and (1>= 0)
    
    if condition:
        print(greeting)

# Task If else block
def simple_if_else_conditional():
    greeting = "Condition equal to True"
    condition = (1>0) and (1>= 10)
    
    if condition:
        print(greeting)
    else:
        print("Condtion equal to False")

# Task If elif block
def simple_if_elif_conditional():
    number = int(input("Enter a number:"))
    
    if number == 0:
        print(f"Number{number} equal to 0")
    elif number >= 0:
        print(f"Number {number} greater than or equals to 0")
    else:
        print(f"Number {number} less than or equal to 0")
        
# Task If and else combinedº
def simple_if_and_else_combined():
    number = int(input("Enter a number:"))
    
    if number == 0:
        print(f"Number {number} equal to 0")
    elif number >= 0:
        if number % 2 == 0:
            print(f"Number {number} is even")
        else:
            print(f"Number {number} is not even")
    else:
        print(f"Number {number} less than or equal to 0")

# Case 1:
def resolve_case1():
    number = float(input("Enter a number: "))
    if number >= 10 and number <=20:
        number2=float(input("Enter another number: "))
        sum_of_numbers = number + number2
        print(f"The sum of these two numbers is: { sum_of_numbers}")
        
        if sum_of_numbers > 100:
            print("That is a large sum!")

if __name__ == "__main__":
    # simple_conditional()
    # simple_if_else_conditional()
    # simple_if_elif_conditional()
    #simple_if_and_else_combined()
    resolve_case1()


# You'll have to use the following strings:
# 1) "Enter a number: "
# 2) "Enter another number: "
# 3) "The sum of these two numbers is:"
# 4) "That is a large sum!"
