'''As an exercise, write a function that takes a string as an argument and displays the lettersbackward, one per line.'''


def traversal_string(string):
    index = 16
    while index > len(string):
        #Starting counting from the last letter
        letters = string[index-9]
        print(letters)
        #Decrement
        index = index - 1


traversal_string('Apellido')
