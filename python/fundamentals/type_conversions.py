# Task: Type convertions

# Task convert striing to int
def convert_string_to_int():
    value = "4"
    value_int = int(value)
    
    # 
    print("initial value string:", value)
    print("type of initial value string:", type(value))
    print("converted value:", value_int)
    print("type of converted values:", type(value_int))

# Task convert string to float
def convert_string_to_float():
    value = 10.2
    value_float = float(value)
    
    # 
    print("initial value string:", value)
    print("type of initial value string:", type(value))
    print("converted value:", value_float)
    print("type of converted values:", type(value_float))

# Task convert float to int 
def convert_float_to_int():
    value = 11.2
    value_float = int(value)
    
    # 
    print("initial value int:", value)
    print("type of initial value int:", type(value))
    print("converted value:", value_float)
    print("type of converted values:", type(value_float))
    
    
if __name__ == "__main__":
    convert_string_to_int()
    convert_string_to_float()
    convert_float_to_int()