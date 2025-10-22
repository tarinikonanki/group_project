#problem: Given an integer n, return a string array answer where:
'''
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

'''

#Understand
#summary: based on the integer, check if it follows certain standards, and if it meets those standards, set the answer array to that value
#input: integer (basically the number/length of array)
#output: string array
#edge cases: if input is not int
#questions: does it traverse n amount of times?

#clues:
#using array so will have use for loop / traversal, checking various conditions so will use if statements

#assemble & solve

#step 1: define function
def answer_array(n):
    #create array of strings
    return_array = []
    #create for loop to run n times
    for i in range(n):
        #check various conditions
        if i % 3 and i % 5:
            answer[i] = "FizzBuzz"
        elif i % 3:
            answer[i] = "Fizz"
        elif i % 5:
            answer[i] = "Buzz"
               