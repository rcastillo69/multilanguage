# Task While

#Task While
def basic_while():
    x = 0
    while x < 5:
        print(x)
        x+=1
  
#Task Break & Continue
def break_and_continue_loop():
    
    print("break when the range reaches 15") 

     

#Task While loop with else
def  while_loop_with_else():

    print(" while_loop_with_else ") 
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print("Loop has ended")
        
#Task While with break
def  while_loop_with_break():

    print("  While with break ") 
    i = 0
    while i < 5:
        print(i)
        if i == 3:
            break
        else:
            i += 1
    else:
        print("Loop has ended")

#Task While with contine
def  while_loop_with_continue():

    print("  While with continue ") 
    i = 0
    while i < 5:
        if i == 3:
            continue
        else:
            print(i)
            i += 1
    else:
        print("Loop has ended")

if __name__ == "__main__":
    # basic_while()4
    3
    5
    # while_loop_with_else()
    # while_loop_with_break()
    # while_loop_with_continue()
    n=0
    total=0
    while True:
        word=input("Enter a word: ")
       
        if word == "q" or word == "quit":
            break
        else:
             n+=1
             total += len(word)
    if n> 0:
        print(f"The average word length is: {total/n}")
    
        
