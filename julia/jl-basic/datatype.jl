# Data type
# define a constant
const MI_CONSTANTE = 100

# use constant. Note: constants are defined at beginning of the file
println(MI_CONSTANTE)

function get_types()

    # Integer
    my_integer = 10
    println("Integer value:", my_integer)
    println("Integer type:", typeof(my_integer))

    # Float
    my_float = 3.14
    println("Float value:", my_float)
    println("Float type:", typeof(my_float))

    # String
    my_string = "Hello, world!"
    println("String value:", my_string)
    println("String type:", typeof(my_string))

    # Boolean
    my_boolean = true
    println("Boolean value:", my_boolean)
    println("Boolean type:", typeof(my_boolean))

    # Array
    my_array = [1, 2, 3, 4, 5]
    println("Array value:", my_array)
    println("Array type:", typeof(my_array))

    # Tuple
    my_tuple = (6, 7, 8, 9, 10)
    println("Tuple value:", my_tuple)
    println("Tuple type:", typeof(my_tuple))

    # Set
    my_set = Set([1, 2, 3])
    println("Set value:", my_set)
    println("Set type:", typeof(my_set))

    # Dictionary
    my_dict = Dict("name" => "John", "age" => 30, "city" => "New York")
    println("Dictionary value:", my_dict)
    println("Dictionary type:", typeof(my_dict))

    # String
    # Multiline

    multiline_string = """
    This is a
    multiline
    string.
    """
    println(multiline_string)

    # Concatenation:

    str1 = "Hello"
    str2 = "World"
    concatenated_str = string(str1, " ", str2)
    println(concatenated_str)

    # Char: In Julia, individual characters are represented using single quotation marks.
    char = 'A'
    println(char)

    # Declaring Variables. Explicit:
    my_explicit_variable::Int64 = 10
    println(my_explicit_variable)

    # Implicit
    my_implicit_variable = 3.14
    println(my_implicit_variable)

    # Group of Declarations:
    var1, var2, var3 = 1, "two", true
    println(var1, " ", var2, " ", var3)

    # Multiple Declarations Inline:
    x = y = z = 0
    println(x, " ", y, " ", z)

    #Check Type:
    my_variable = 10
    println(typeof(my_variable))

    # Casting Data Types
    #=
        Other programming languages arbitrarily chose some way of rounding here (often truncation but sometimes rounding to nearest). Julia doesn't guess and requires you to be explicit. If you want to round, truncate, take a ceiling
    =#

    my_float1 = 3.14656565
    my_int1 = Int64(round(my_float1))
    println(my_int1)
    println(typeof(my_int1))

    #=
        Mutability / Immutability:
        In Julia, variables are mutable by default. However, you can make a variable immutable by using the const keyword or declaring it with the immutable keyword.
    =#

    #=
        Special types:
        Null value:

        In Julia, the null value is represented by nothing. It is used to indicate the absence of a value.

        Pointers & Address:

        Julia is a high-level language that abstracts away direct memory management and pointer operations. Pointers and memory addresses are not typically used in everyday Julia programming.
    =#

end
  
get_types() # Julia doesnt need a main function