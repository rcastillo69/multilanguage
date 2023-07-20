import array
import numpy as np

from enum import Enum


#Task: Enum operations
class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

def show_enum():
    print("Enum operations")
    
    # Create
    print(Color.RED)  # Output: Color.RED

    # Modify (Enums are immutable, so modification is not allowed)

    # Delete (Enums are immutable, so deletion is not allowed)

    # Search
    print(Color.RED in Color)  # Output: True


#Task: Structure o records

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def show_record():
    print("Record operations")
    # Create
    person = Person("John", 30)
    print(person.name, person.age)  # Output: John 30

    # Modify
    person.age = 31
    print(person.age)  # Output: 31

    # Delete
    del person.age

    # Search
    print(hasattr(person, "name"))  # Output: True    

#Task: Slice
def show_slice():
    print("Slice operations")
    my_list = [1, 2, 3, 4, 5]

    # Create
    sliced_list = my_list[1:4]
    print(sliced_list)  # Output: [2, 3, 4]

    # Modify
    my_list[1:4] = [6, 7, 8]
    print(my_list)  # Output: [1, 6, 7, 8, 5]

    # Delete
    del my_list[1:4]
    print(my_list)  # Output: [1, 5]

    # Search
    print(6 in my_list)  # Output: True


#Task: Array
def show_array():

    print("Array operations")
    # Create
    my_array = array.array('i', [1, 2, 3, 4, 5])
    print(my_array)  # Output: array('i', [1, 2, 3, 4, 5])

    # Modify
    my_array[2] = 6
    print(my_array)  # Output: array('i', [1, 2, 6, 4, 5])

    # Delete
    del my_array[2]
    print(my_array)  # Output: array('i', [1, 2, 4, 5])

    # Search
    print(4 in my_array)  # Output: True

# Task: Multidimensional arrays
def show_multidimensional_array():
    print("Multidimensional arrays")

    # Create
    my_matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(my_matrix)  # Output: [[1 2 3]
                      #          [4 5 6]]

    # Modify
    my_matrix[1, 1] = 7
    print(my_matrix)  # Output: [[1 2 3]
                      #          [4 7 6]]

    # Delete
    my_matrix = np.delete(my_matrix, 1, axis=1)
    print(my_matrix)  # Output: [[1 3]
                      #          [4 6]]

    # Search
    print(4 in my_matrix)  # Output: True

# Task: Vectors
def show_vector():
    print("Vector")

    # Create
    my_vector = np.array([1, 2, 3])
    print(my_vector)  # Output: [1 2 3]

    # Modify
    my_vector[1] = 4
    print(my_vector)  # Output: [1 4 3]

    # Delete
    my_vector = np.delete(my_vector, 1)
    print(my_vector)  # Output: [1 3]

    # Search
    print(3 in my_vector)  # Output: True

# Task: Tuple 
def show_tuple():
    print("Tuples")
    # Create
    my_tuple = (1, 2, 3)
    print(my_tuple)  # Output: (1, 2, 3)

    # Modify (Tuples are immutable, so modification is not allowed)

    # Delete (Tuples are immutable, so deletion is not allowed)

    # Search
    print(2 in my_tuple)  # Output: True

# Task: Dictionaries 
def show_dic():
    print("Dictionaries")
    # Create
    my_dict = {"name": "John", "age": 30}
    print(my_dict)  # Output: {'name': 'John', 'age': 30}

    # Modify
    my_dict["age"] = 31
    print(my_dict)  # Output: {'name': 'John', 'age': 31}

    # Delete
    del my_dict["age"]
    print(my_dict)  # Output: {'name': 'John'}

    # Search
    print("name" in my_dict)  # Output: True

# Task: List 
def show_list():
    print("List")
    # Create
    my_list = [1, 2, 3, 4, 5]
    print(my_list)  # Output: [1, 2, 3, 4, 5]

    # Modify
    my_list[2] = 6
    print(my_list)  # Output: [1, 2, 6, 4, 5]

    # Delete
    del my_list[2]
    print(my_list)  # Output: [1, 2, 4, 5]

    # Search
    print(4 in my_list)  # Output: True

# Task: Sets 
def show_set():
    print("Sets")
    # Create
    my_set = {1, 2, 3, 4, 5}
    print(f"my_set = {my_set}")  # Output: {1, 2, 3, 4, 5}
    
    # Add element
    my_set.add(7)

    # Modify (Sets are mutable, but individual elements cannot be modified)

    # Delete
    my_set.remove(3)
    print("my_set = {my_set}")  # Output: {1, 2, 4, 5, 7}

    # Search
    print(4 in my_set)  # Output: True
    
    # Length
    print(len(my_set))   
    
    # Union
    set2 = {11,13}
    z = my_set.union(set2)
    print(f"set2 = {z}")
    print(f"my_set.union(set2) = {z}")
    
    # Union shortcut
    set4 = {17,21}
    print(f"set4 = {set4}")
    z2 = z  | set4
    print(f" z  | set4 = {z2}")
    
    # Intersection
    i1 = z2.intersection(my_set)
    print(i1)
    
    # Intersection shorcut
    i2 = z2 & z
    print(i2)
    
    # Difference
    d1 = z.difference(z2)
    print(d1)
    
    # Difference
    d2 = z2 -z
    print(d2)
    
    # Simetric Difergence
    c1 = {1,2,3}
    c2 = {1,2,4}
    print(c2.symmetric_difference(c1))
    
    

    
    # clear
    my_set.clear
    print(my_set)  


        
if __name__ == "__main__":
    show_enum()
    show_record()
    show_slice()
    show_array()
    show_multidimensional_array()
    show_vector()
    show_tuple()
    show_dic()
    show_list()
    show_set()
    
    # You'll have to use the following strings:
    num = input("Enter the numerator: ")
    den = input("Enter the denominator: ")
    try:
        
        print(f"The result of this division is {float(num)/float(den)}.")
    except ZeroDivisionError as zd:
        print("You cannot divide by 0.")
        print("This division cannot be performed.")
    except ValueError as ve:
        if not num.isnumeric():
           print("The numerator is not a number.")
        if not den.isnumeric():
            print("The denominator is not a number.")
        print("This division cannot be performed.")
    finally:
        print("Goodbye!")
    # 3) "The numerator is not a number."
    # 4) "The denominator is not a number."
    # 5) "You cannot divide by 0."
    # 6) "This division cannot be performed."
    # 7) "The result of this division is _."
    # 8) "Goodbye!"
        
    


