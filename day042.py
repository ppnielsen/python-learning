'''
Day 42 Cup of Code

Find Unique Characters in Strings

Given a string, are all characters unique?
Return a True or False

Uses python built in structures
'''

def unique(string):
    string = string.replace(' ', '')

    # set: list of unordered, unique values
    return (len(set(string))) == len(string)

# print(unique('a bb cdef'))


# without built-in functions
def unique2(s):
    s = s.replace(' ', '')
    characters = set()

    for letter in s:
        if letter in characters:
            return False

        else:
            characters.add(letter)
    
    return True

print(unique2('z8 ika b cdef5'))