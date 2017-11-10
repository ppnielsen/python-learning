# create a class that has two methods
# getString: grab string from input
# printString: print string in upper case

class Prints():
    def __init__(self):
        self.st = ''
    def getString(self):
        self.st = input('Please input a string...')
    def printString(self):
        print(self.st.upper())

s = Prints()
s.getString()
s.printString()