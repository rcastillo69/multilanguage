# Conditions

# Operator Equallity
def use_equality():
     a = 10
     b = 10
     if a == b:
         print(f"the values a = {a} and b = {b} are equal.")

# Operator Not Equallity
def use_not_equality():
     a = 10
     b = 11
     if a != b:
         print(f"the values a = {a} and b = {b} are notequal.")

# Operator >
def use_greater_than():
     a = 10
     b = 11
     if b > a:
         print(f"the values b = {b} is greater than a = {a}.")

# Operator <
def use_less_than():
     a = 10
     b = 11
     if a < b:
         print(f"the values a = {a} is less than b = {b}.")    

# Operator >=
def use_greater_than_or_equal_to():
     a = 10
     b = 11
     c = 11
     if b >= a:
         print(f"the values b = {b} is greater than or equal to a = {a}.")
                    
     if b >= c:
         print(f"the values b = {b} is greater than or equal to c = {c}.")           

# Operator <=
def use_less_than_or_equal_to():
     a = 10
     b = 11
     c = 11
     if a <= b:
         print(f"the values a = {a} is less than or equal to b = {b}.")
                    
     if b <= c:
         print(f"the values b = {b} is greater than or equal to c = {c}.") 
         
# Operator AND (and)
def use_and():
     a = 10
     b = 11
     if a == 10 and b == 11:
         print(f"the values a = {a} and b = {b} are equals.")

# Operator AND (and)
def use_or():
     a = 10
     if a == 10 or a == 11:
         print(f"the value a = {a} is equal to 10 or 11")

# Case 1
def resolve_case1():
    w = "ello"  # <- Change this
    x = "hello"  # <- Change this
    y = "hello"  # <- Change this
    z = "d"  # <- Change this

    # Don't change any of these `condition_` variables.
    condition_1 = w != "a"
    condition_2 = w < x
    condition_3 = x == y
    condition_4 = y == "hello"
    condition_5 = z > "c"

    # All of these should print `True`.
    print(condition_1)
    print(condition_2)
    print(condition_3)
    print(condition_4)
    print(condition_5)

# Predence
def precedence():
    # precedencia: 1 not 2 and 3 or
    condition = not True and not False or True
    '''
         not True and not False or True
         False    and True      or True
         False or True
         True
    '''
    print(f"not True and not False or True = {condition} ")
    

# Case 2
def resolve_case2():
    """
    Assume that three variables x, y, and z are always equal to either True or False, respectively. This means that there are eight unique combinations of values for x, y, and z.
    How many of these eight combinations make the following expression evaluate to True?

    x and y or z
    """

    '''
    X Y Z
    -----
    T T T = T
    F T T = 2
    T F T = 3
    F F T = 4
    T T F = 5
    F T F 
    F F F
    T F F 

    '''
    a = 0

# Case 3
def resolve_case3():
    '''
    Set the valus of x, y and z such that all of the condition_ variables evaluate to TRUE
    
    Only use boolean values
    '''
    w = True  # <- Change this
    x = True  # <- Change this
    y = False  # <- Change this
    z = True  # <- Change this

    # Don't change any of these `condition_` variables.
    condition_1 = w and x and not y or not z
    # Simplify implies not (w and not w) = not w or not w 
    condition_2 = not (w and not w)
    # Simplify implies not w or not (y or y) = not w or not y
    condition_3 = not (w and y or y)
    
    condition_4 = x and (y or z and w)

    # All of these should print `True`.
    print(condition_1)
    print(condition_2)
    print(condition_3)
    print(condition_4)



if __name__ == "__main__":
    use_equality()
    use_not_equality()
    use_greater_than()
    use_less_than()
    use_greater_than_or_equal_to()
    use_less_than_or_equal_to()
    use_and()
    use_or()
    resolve_case1()
    precedence()
    resolve_case2()
    resolve_case3()


