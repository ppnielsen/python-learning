# '''
# Saving an image from the web
# '''

# import random
# import urllib.request

# def dlImg(url):
#     name = random.randrange(1, 1000)
#     fullname = f'{str(name)}.jpg'
#     urllib.request.urlretrieve(url, fullname)

# dlImg('http://a.espncdn.com/combiner/i?img=/photo/2016/0322/r66173_1296x518_5-2.jpg')

# '''
# Writing to a new file
# '''

# fw = open('sample.txt', 'w') #preparing to write text to file
# fw.write('Writing some stuff here bro!\n')
# fw.write('Did you see this coming!?')
# fw.close() # close, otherwise it hangs in memory


# '''
# Reading file
# '''
# fr = open('sample.txt', 'r')
# text = fr.read()
# print(text)

# '''
# Downloading csv and reading it
# '''

# from urllib import request
# csvLink = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

# def dlTrans(url):
#     response = request.urlopen(url)
#     csv = response.read()
#     csvStr = csv.decode('utf-8') #convert to a string to avoid any issues down the road
#     lines = csvStr.split('\\n')
#     dest = r'goog.csv' #r = raw - dont have to escape all characters
#     fx = open(dest, 'w')
#     for line in lines:
#         fx.write(f'{line}\n')
#     fx.close()

# dlTrans(csvLink)


# '''
# Word Counter
# '''
# # https://omaha.craigslist.org/search/sss?query=jordan&sort=rel

# import requests
# from bs4 import BeautifulSoup
# import operator

# def getWords(url):
#     wordList = [] # blank list
#     sourceCode = requests.get(url).text # retrieving source code from webpage
#     soup = BeautifulSoup(sourceCode, 'html.parser') # making source code usable!
#     for post_text in soup.find_all('a', {'class': 'result-title'}): # fin all links with a class of result-title
#         title = post_text.string
#         words = title.lower().split() # lowers all words in the title and splits them out by word!
#         for word in words:
#             wordList.append(word)
#     cleanList(wordList)


# def cleanList(wordListing):
#     cleanWordList = []
#     for word in wordListing:
#         removeThese = '!@#$%^&*()_+=-{}|\][;:,<.>/?'
#         for i in range(0, len(removeThese)):
#             word = word.replace(removeThese[i],"")
#         if len(word) > 0:
#             print(word)
#             cleanWordList.append(word)
#     createDict(cleanWordList)


# def createDict(wordListing):
#     wordCount = {}
#     for word in wordListing:
#         if word in wordCount:
#             wordCount[word] += 1
#         else:
#             wordCount[word] = 1
#     for key, value in sorted(wordCount.items(), key=operator.itemgetter(1)):
#         print(key, value)

# getWords('https://omaha.craigslist.org/search/sss?query=jordan&sort=rel')

# '''
# Unpacking objects
# '''
# name, age, sex = ['Philip', 31, 'male']

# print(name)
# print(age)
# print(sex)

# def dropFirstLast(grades):
#     first, *middle, last = grades
#     avg = sum(middle) / len(middle)
#     print(avg)

# dropFirstLast([1,2,3,4,5,6,7,8,9])


# '''
# Zip - Creates a tuple of elements. (first, last)
# '''

# first = ['phil', 'joe', 'tom']
# last = ['hart', 'buck', 'cruise']

# names = zip(first, last)

# for a, b in names:
#     print(a, b)

# '''
# Lambda - functions without names... small time function, one time use

# *
# '''


# answer = lambda x: x*7 # passing in x as a variable
# print(answer(7))



# '''
# Min, Max, Sort Dictionaries
# '''

# stocks = {
#     'UNP': 113.25,
#     'ZOOG': 650.13,
#     'AMZN': 450.12,
#     'AAPL': 118.51
# }

# # Sorted by the first item that is zipped
# minimum = min(zip(stocks.values(), stocks.keys()))
# asc = max(zip(stocks.keys(), stocks.values()))

# print(minimum)
# print(asc)

# '''
# Pillow - Image editor
# '''

# from PIL import Image

# img = Image.open('kb.jpg') # now converted to a Pillow object
# print(img.size)
# print(img.format)

# Saving a portion of a picture
# area = (100,100,300,375)
# croppedImg = img.crop(area)

# croppedImg.show()

# img.show() # opens in default image handler.

# Copying an image on top of another
# cart = Image.open('kb-cartoon.jpg')
# life = Image.open('kb.jpg')

# area = (100,100) # last two parameters not needed!
# cart.paste(life, area)

# cart.show()


import requests
import random
import urllib.request

def dl_img(url):
    urllib.request.urlretrieve(url, 'kobe.jpg')

dl_img('https://pixel.nymag.com/imgs/daily/intelligencer/2016/04/13/13-kobe-bryant-2016.w710.h473.2x.jpg')




