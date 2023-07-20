# Task Composed type

from enum import Enum
import array as arr
import numpy as np


"""
    Task Slices
        A slice is a way to extract a portion of a sequence, such as a list or a string, using the square bracket notation with start and end indices
"""
def show_slices():
    # Init 
    fruits = ["apple", "banana", "orange", "mango"]
    #Output console
    print(f"fruits : {fruits}")
    
    # Access 
    print(f"fruits[0] : {fruits[0]}" ) # apple
    print(f"fruits[1] : {fruits[1]}")  # banana
    
    # Modifying an element
    print(f"Before fruits[1] : {fruits[1]}")  # pineapple
    fruits[1]= "pineapple"
    print(f"After fruits[1] : {fruits[1]}")  # pineapple
    
    # Appending element to list
    print(f"Before fruits : {fruits}")
    fruits.append("strawerry")
    print(f"After fruits : {fruits}")
    
    # Removimg element to list
    print(f"Before fruits : {fruits}")
    fruits.remove("strawerry")
    print(f"After fruits : {fruits}")
    
    # Checking if an element is in the list
    check = "apple" in fruits
    print(f"Is the apple in the list ? : {check}")
    check = "Apple" in fruits
    print(f"Is the Apple in the list ? : {check}")
    
    # Getting the length of the list
    print(f"The length of fruis is : {len(fruits)}")
    
    # Iterating over the list
    print("elements in the list")
    for f in fruits:
        print(f"fruit: {f}")
        
    # Using indices
    # List all elements
    print(f"fruits[:]: {fruits[:]}")
    print(f"fruits[:len(fruits)]: {fruits[:len(fruits)]}")
    print(f"fruits[0:3]: {fruits[0:3]}")
    print(f"fruits[1:2]: {fruits[1:2]}")
    print(f"fruits[3:]: {fruits[1:]}")
    #Skipping elements in a list
    print(f"fruits[0:4:2]: {fruits[0:4:2]}")
    
    # Slice using negative indices
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(f"letters: {letters}")
    print(f"letters[-4:-1]: {letters[-4:-1]}")
    
    print(f"fruits[len(fruits):0:-1]: {fruits[len(fruits):0:-1]}")
    # Reversing a list
    print(f"fruits[::-1]: {fruits[::-1]}")

def chanllenge1():
    """
        w = None  # <- Change this
        x = None  # <- Change this
        y = None  # <- Change this
        z = None  # <- Change this
        
        Expected output is [8,6,4]
    
    """
    w = -2  # <- Change this
    x = 2  # <- Change this
    y = 8  # <- Change this
    z = 1  # <- Change this
    #      0  1  2  3  4  5  6  7  8  9
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    first_slice = lst[::z]
    second_slice = first_slice[:y]
    third_slice = second_slice[x:]
    last_slice = third_slice[::w]
    print(last_slice)
    #print(last_slice)    

# Task Enum
class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3
        
def show_enum():
    print(f"from Enum Color.RED = {Color.RED}")
    print(f"from Enum Color.BLUE.value ={ Color.RED.value}")

# Task Structure of record    
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
def show_record():
    # init
    person = Person("John",23)
    print(f"Person age:{person.age}")

""""
    array is a collection of elements of the same type. In Python, you can use the array module to create arrays with various data types.
"""
    
def show_array():
    # init
    numbers = arr.array('i', [1, 2, 3, 4, 5])
    print(f"Array numbers: {numbers}")
    
    # Accessing elements
    print(f"numbers[0]: {numbers[0]}")    # 1
    
    # Modifying an elemen
    print(f"Before numbers[1] : {numbers[1]}") 
    numbers[1]= 999
    print(f"After numbers[1] : {numbers[1]}")   
    print(f"Array : {numbers}")  
    
    # Appending elements
    print(f"Before array : {numbers}")  
    numbers.append(6)
    print(f"After array : {numbers}")  

    # Removing an element by index
    print(f"Before array : {numbers}")  
    del numbers[3]
    print(f"After array : {numbers}")  

    # Getting the length of the array
    length = len(numbers)
    print(f"length = {length}")    

    # Iterating over elements
    print(f"Array : {numbers}")  
    print("Elements:")
    for num in numbers:
        print(num)

    # Converting array to a list
    numbers_list = numbers.tolist()
    print(numbers_list)    # [1, 2, 10, 5, 6] 

"""
    Multi-dimensional arrays are arrays with more than one dimension. They can be used to represent matrices or tensors and are supported by libraries like NumPy.

"""

def show_multi_dimensions():
    
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    # Accessing multi-dimensional array elements
    print(matrix[0, 1])    # 2
    print(matrix[1, 2])    # 6   

"""
    Tuples are ordered collections of elements that are immutable, meaning they cannot be modified once created. They are typically used to group related data together.
"""    
def show_tuples():
    person = ("John Doe", 25, "john@example.com")

    # Accessing tuple elements
    print(person[0])    # John Doe
    print(person[2])    # john@example.com
    
"""
    Vectors are one-dimensional arrays commonly used in linear algebra and numerical computations. NumPy is a popular library for working with arrays and provides convenient vector operations.
"""

def show_vector():

    vector = np.array([1, 2, 3])

    # Vector operations
    result = vector * 2
    print(result)    # [2, 4, 6]

    dot_product = np.dot(vector, result)
    print(dot_product)    # 28

"""
    Dictionaries or maps are collections of key-value pairs. They allow you to associate values (the "values") with unique identifiers (the "keys") for efficient retrieval.

"""    
def show_dictionary():
    # Init
    dic1 = dict()
    dic2 = {}
    print(dic1,dic2)
    
    # Create a dictionary
    person = {
        "name": "John Doe",
        "age": 25,
        "email": "john@example.com"
    }

    # Accessing values
    print(person["name"])    # "John Doe"
    print(person.get("age"))    # 25
    
    print(person.get("age2","nothing"))   
    

    # Modifying values
    person["email"] = "john.doe@example.com"
    print(person)    # {'name': 'John Doe', 'age': 25, 'email': 'john.doe@example.com'}

    # Adding new key-value pairs
    person["city"] = "New York"
    print(person)    # {'name': 'John Doe', 'age': 25, 'email': 'john.doe@example.com', 'city': 'New York'}

    # Removing a key-value pair
    del person["age"]
    print(person)    # {'name': 'John Doe', 'email': 'john.doe@example.com', 'city': 'New York'}

    # Checking if a key exists
    print("name" in person)    # True
    print("age" in person)     # False

    # Getting the number of key-value pairs
    length = len(person)
    print(length)    # 3

    # Iterating over keys or values
    # form 1
    print("*** Form 1")
    for key in person:
        print(key, person[key])

    print("*** Form 2")
    for key, value in person.items():
        print(key, value)


    
    # Get Key
    keys = list(person.keys())
    values = list(person.values())
    items = list(person.items())
    
    print(f"keys[0]= {keys[0]}")
    print(f"All keys = {keys}")
    
    print(f"values[0]= {values[0]}")
    print(f"All values = {values}")
    
    print(f"All items = {items}")
    
    # Clearing the dictionary
    person.clear()
    print(person)    # {}

    
def show_sets():
    # Create a set
    fruits = {"apple", "banana", "orange"}

    # Adding elements
    fruits.add("mango")
    print(fruits)    # {'apple', 'banana', 'orange', 'mango'}

    # Removing elements
    fruits.remove("banana")
    print(fruits)    # {'apple', 'orange', 'mango'}

    # Checking membership
    print("banana" in fruits)    # False
    print("apple" in fruits)     # True

    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Union
    union_set = set1.union(set2)
    print(union_set)    # {1, 2, 3, 4, 5, 6, 7, 8}

    # Intersection
    intersection_set = set1.intersection(set2)
    print(intersection_set)    # {4, 5}

    # Difference
    difference_set = set1.difference(set2)
    print(difference_set)    # {1, 2, 3}

    # Subset
    subset = set1.issubset(set2)
    print(subset)    # False

    # Superset
    superset = set1.issuperset(set2)
    print(superset)    # False

    # Clearing the set
    fruits.clear()
    print(fruits)    # set()

"""
    list is a built-in data type in Python that represents an ordered collection of elements. It is a mutable data type
"""


def show_list():

    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Accessing elements
    print(my_list[0])    # 1
    print(my_list[2])    # 3

    # Modifying elements
    my_list[1] = 10
    print(my_list)    # [1, 10, 3, 4, 5]

    # Appending elements
    my_list.append(6)
    print(my_list)    # [1, 10, 3, 4, 5, 6]

    # Removing elements
    my_list.remove(3)
    print(my_list)    # [1, 10, 4, 5, 6]

    # Checking if an element is in the list
    print(10 in my_list)    # True
    print(7 in my_list)     # False

    # Getting the length of the list
    length = len(my_list)
    print(length)    # 5

    # Iterating over elements
    for element in my_list:
        print(element)

    # Slicing a list
    slice_list = my_list[1:4]
    print(slice_list)    # [10, 4, 5]

    # Reversing a list
    reversed_list = my_list[::-1]
    print(reversed_list)    # [6, 5, 4, 10, 1]

    # Sorting a list
    sorted_list = sorted(my_list)
    print(sorted_list)    # [1, 4, 5, 6, 10]


if __name__ == "__main__":
    #show_slices()
    #chanllenge1()
    #show_enum()
    #show_record()
    # show_array()
    # show_multi_dimensions()
    # show_tuples()
    # show_vector()
    # show_dictionary()
    # show_sets()
    
    int_value = input("Enter an integer: ")
    name = input("What is your name? ")
    if not int_value.isdigit() :
        print(f"Hello, {name.capitalize() }")
    else:
        print(f"Hello, {name.upper()}")
        