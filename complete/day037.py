'''
Day 37

given a string of words, reverse all the words

start = 'this is the best'
finsih = 'best the is this
'''

def reverse(s):
    # A:
    # s = s.split() # splits it into pieces
    # s.reverse() # reverses objects
    # return s

    # B:
    # return "-".join(reversed(s.split())) # join is a separator!

    # C:
    # return "-".join(s.split()[::-1]) # :: start at beg, go to end, reverse that order

    # D:
    length = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces: # used to find space or last letter of word
                i += 1

            words.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(s))

print(reverse('this is the best'))
