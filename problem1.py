#problem: Write a function that reverses a string
'''
Input: "Hello"
Output: "olleH"
'''

#Understand:
#summary: we need to take in a string than reverse its order
#Input is a string, output is a string
#edge cases: if the string is empty
#questions: do spaces count in reversing?

#Clues:
#takes in string so will have to use string methods like len and a for loop as we are traversing through word

#Assemble & solve:

#step 1: define function & input
def string_reverse(word):
    #create return string
    reverse = ""
    #create for loop
    for letter in word:
        #add each letter to beginning of word
        reverse = letter + reverse
    return reverse

#test
print(f'Test 1 - Word: Hello, Reverse: ' + string_reverse("Hello"))