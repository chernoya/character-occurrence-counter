
#character occurrence counter (supports unicode, i think)

def getString():
    global string
    string = input("Enter a string to evaluate: ")

def getChar():
    global char
    char = input("Enter the character to count the occurrence of: ")

def occurrence_counter(string, char):
    count = 0
    arr = list(string)
    for letter in arr:
        if char == letter:
            count = count + 1
    return count

getString()
getChar()
print(occurrence_counter(string, char))