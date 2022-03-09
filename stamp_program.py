'''
start
get the numbers of sheets
sheets / 5
round answer to next number
output the result to the user
end
'''

import math
#input: sheet

def calculate(sheet):
    #step 1
    answer = sheet/3
    #step 2
    rounded = math.ceil(answer)
    print("Sheet is: ", sheet)
    print("The answer is: ", answer)
    print("Rounded is: ", rounded)
    print("====================================")
    #output: number of stamps needed
    return rounded

output = calculate(16)

print("The number of stamps needed is: ", output)