values = input('I need comma separated values:')
list = values.split(',')
tuple = tuple(list) # can't edit a tuple!
print(list, tuple)