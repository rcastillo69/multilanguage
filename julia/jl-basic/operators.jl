# Operatos

#=
  Task Arithmetic operators
=#
function show_arithmetic_operators()
println("* Aritmentic operators")
# Addition
result = 5 + 3
println(result)  # Output: 8

# Subtraction
result = 10 - 4
println(result)  # Output: 6

# Multiplication
result = 2 * 6
println(result)  # Output: 12

# Division
result = 15 / 4
println(result)  # Output: 3.75

# Modulus (Remainder)
result = 17 % 5
println(result)  # Output: 2

# Increment
num = 5
num += 1
println(num)  # Output: 6

# Decrement
num = 8
num -= 1
println(num)  # Output: 7
    
end

# Task: Assignment operators:
function show_assignmentc_operators()

println("* Assignment operators")
# Assignment operator
x = 10
println(x)  # Output: 10

# Compound assignment operators
y = 5
y += 2
println(y)  # Output: 7

z = 10
z *= 3
println(z)  # Output: 30

w = 15
w /= 2
println(w)  # Output: 7.5

m = 10
m %= 3
println(m)  # Output: 1

end

#Task: Comparison operators
function show_comparison_operator()

println("* Comparison operators")
# Equality
result = (5 == 5)
println(result)  # Output: True

# Inequality
result = (7 != 3)
println(result)  # Output: True

# Greater than
result = (10 > 8)
println(result)  # Output: True

# Less than
result = (6 < 4)
println(result)  # Output: False

# Greater than or equal to
result = (5 >= 5)
println(result)  # Output: True

# Less than or equal to
result = (3 <= 2)
println(result)  # Output: False

end

#Task: Comparison operators
function show_logical_operators()

println("* Logical operators")    
# Logical AND
result = true && false
println(result)  # Output: false

# Logical OR
result = true || false
println(result)  # Output: true

# Logical NOT
result = !true
println(result)  # Output: false

   
end

#Task: Concatenational operator 
function show_concatenation_operator()

println("* Concatenation operator")    
# String concatenation
greeting = "Hello, "
name = "John"
message = greeting * name
println(message)  # Output: Hello, John

end

#Task: Ternary conditional operator
function show_ternary_operator()

    println("* Ternary conditional operator")    
    x = 10
    result = (x % 2 == 0) ? "Even" : "Odd"
    println(result)  # Output: Even
    
 end

show_arithmetic_operators() 
show_assignmentc_operators()
show_comparison_operator()
show_logical_operators()
show_concatenation_operator()
show_ternary_operator()