# Task Loops

#Task Range
def range_loop():
    # note: start in 0 and end in 9
  print("Simple range loop")  
  for i in range(10):
      print(f"i = {i}")
      
  print("Simple range of string")  
  s = "This is a string"
  i = 0
  for i in range(len(s)):
      print(f"s[{i}] = {s[i]}")
      i+=1
  
  print("range loop with start 5") 
  for i in range(5, 20):
      print(f"i = {i}")
      
  print("range loop with start 0 & step 5") 
  for i in range(0, 20, 5):
      print(f"i = {i}")
  
  print("range loop with start -5, stop -20 & step -3") 
  for i in range(-5, -50, -5):
      print(f"i = {i}")

  print("iteration a list by index") 
  lst = [1,2,3,4,5,True,False]
  for idx in range(len(lst)):
      print(f"lst[{idx}] = {lst[idx]}")


  print("iteration a list by index & element") 
  lst = [11,12,13,14,15,True,False]
  for i, element in enumerate(lst):
      print(f"element {i} = {element}")
      
  
#Task Break & Continue
def break_and_continue_loop():
    
    print("break when the range reaches 15") 
    for i in range(20):
        print(f"i = {i} ")
        if i == 15:
            break
        
    print("continue when the range reaches 15") 
    for i in range(20):
        if i != 15:
            print(f"i = {i} ")
        else:
            continue  
    
    print("loop with else") 
    for i in range(5):
        print(i)
    else:
        print("Loop completed!")

     

#Task Nested loops
def nested_loop():

    print("Neste loop ") 
    for i in range(1,10):
        for j in range(1,11):
            print(f"{i} x {j} = {i*j} ")
        print("***")


if __name__ == "__main__":
    #range_loop()
    #break_and_continue_loop()
    #nested_loop()
    lst = [-2, 0, 4, 5, 1, 2]

    total = 0    
    for i in range(0, len(lst)-1):
        total = lst[i] + lst[i+1]
        print(total)
 
        
