import os


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def get_militar_time(timelist:list[str]) -> str:
    return timelist[0]+":"+timelist[1] +":"+timelist[2]

def get_meridiam(s:str) -> str:
    return s[-2:] 

def get_time(s:str):
	return s[:len(s)-2].split(":")

def timeConversion(s):
    
	meridiam = get_meridiam(s).upper()
      
	timelist = get_time(s)

	if meridiam == "PM" and int(timelist[0]) < 12:
		timelist[0] = str(12 + int(timelist[0]) )      
    
	if meridiam == "AM" and int(timelist[0]) == 12:
		timelist[0] = '00'
      
    
	return get_militar_time(timelist)

if __name__ == '__main__':
	# Get the directory of the current script
	script_dir = os.path.dirname(os.path.abspath(__file__))

	# Define the output file path in the same directory as the script
	output_path = os.path.join(script_dir, 'output.txt')
    
	fptr = open(output_path, 'w')

	s = input()

	result = timeConversion(s)

	fptr.write(result + '\n')

	fptr.close()