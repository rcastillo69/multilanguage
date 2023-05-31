from datetime import date
from datetime import time
from datetime import datetime

"""
    Task Datatype manager
"""
#Task Entry point
def get_types():
    print("*** Types ***")
    
    # Integer
    my_integer = 10
    print("Integer value:", my_integer)
    print("Integer type:", type(my_integer))

    # Float
    my_float = 3.14
    print("Float value:", my_float)
    print("Float type:", type(my_float))

    # String
    my_string = "Hello, world!"
    print("String value:", my_string)
    print("String type:", type(my_string))

    # Boolean
    my_boolean = True
    print("Boolean value:", my_boolean)
    print("Boolean type:", type(my_boolean))

    # List Mutable
    my_list = [1, 2, 3, 4, 5]
    print("List value:", my_list)
    print("List type:", type(my_list))

    # Tuple Inmutalble
    my_tuple = (6, 7, 8, 9, 10)
    print("Tuple value:", my_tuple)
    print("Tuple type:", type(my_tuple))

    # Set
    my_set = {1, 2, 3}
    print("Set value:", my_set)
    print("Set type:", type(my_set))

    # Dictionary
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    print("Dictionary value:", my_dict)
    print("Dictionary type:", type(my_dict))
    
    # Constant
    # Python doesn't support constant
    MY_CONSTANT = "my_constant" # By convention
    print("My constant ", MY_CONSTANT)
    
    my_date = date(2023, 5, 30)
    print(my_date)
    print("date type:", type(my_date))
    
    my_time = time(9, 30, 45)
    print(my_time)
    print("time type:", type(my_time))
    
    my_dt = datetime(2023, 5, 30, 9, 30, 45)
    print(my_dt)
    print("date time type:", type(my_dt))
    
    # String multiline
    ml = """ This is a
    multiline 
    string
    """
    print(ml)
    
    #Concatenation
    str1 = "Hello"
    str2 = "World"
    concatenated_str = str1 + " " + str2
    print(concatenated_str)
    
    #Char: In Python, there is no distinct "char" data type like in some other programming languages. 
    char = 'A'
    print(char)

    # Declaring Variables 
    # Explicit:
    my_explicit_variable: int = 10
    print(my_explicit_variable)
    
    # Implicit:
    my_implicit_variable = 3.14
    print(my_implicit_variable)
    
    # Group of Declarations:
    var1, var2, var3 = 1, "two", True
    print(var1, var2, var3)
    
    # Multiple Declarations Inline
    x = y = z = 0
    print(x, y, z)
    
    # Check Type:
    my_variable = 10
    print(type(my_variable))
    
    # Casting data type
    
    my_int = 10
    my_float = float(my_int)
    print(my_float)
    
"""
Special types:
    Null value:

    In Python, the null value is represented by None. It is often used to indicate the absence of a value or as a default placeholder.

    Pointers & Address:

    Python does not expose pointers and memory addresses to the same extent as some low-level programming languages
 
 """   
    
if __name__ == "__main__":
    get_types()