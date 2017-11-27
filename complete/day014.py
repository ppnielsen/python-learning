'''
Cup of Code day 14 of Python
'''

# allow two inputs, month and day, and program will output the season

def season_finder():
    '''
    Given month and day, function will output the season
    '''
    month = input('What month? ')
    day = int(input('What day? '))

    winter = ('January', 'February', 'March')
    spring = ('April', 'May', 'June')
    summer = ('July', 'August', 'September')
    fall = ('October', 'November', 'December')

    if month in winter:
        season = 'Winter'
    elif month in spring:
        season = 'Spring'
    elif month in summer:
        season = 'Summer'
    elif month in fall:
        season = 'Autumn'
    else:
        print('Type your month properly!')

    if season:
        if month == 'March' and day > 20:
            season = 'Spring'
        elif month == 'June' and day > 20:
            season = 'Summer'
        elif month == 'September' and day > 20:
            season = 'Fall'
        elif month == 'December' and day > 20:
            season = 'Winter'

    if season:
        print('Season is', season)

# season_finder()

# give me date of birth and I'll give you your sign
def your_sign():
    '''
    Given your birthday, you'll be told your horoscope sign!
    '''
    mth = input('What is your birth month? ')
    day = int(input('What is your numerical day of birth? '))

    if mth == 'December':
        sign = 'Sagittarius' if day < 22 else 'Capricorn'
    elif mth == 'January':
        sign = 'Capricorn' if day < 20 else 'Aquarius'
    elif mth == 'February':
        sign = 'Aquarius' if day < 19 else 'Pisces'
    elif mth == 'March':
        sign = 'Pisces' if day < 21 else 'Aries'
    elif mth == 'April':
        sign = 'Aries' if day < 20 else 'Taurus'
    elif mth == 'May':
        sign = 'Taurus' if day < 21 else 'Gemini'
    elif mth == 'June':
        sign = 'Gemini' if day < 21 else 'Cancer'
    elif mth == 'July':
        sign = 'Cancer' if day < 23 else 'Capricorn'
    elif mth == 'August':
        sign = 'Sagittarius' if day < 23 else 'Leo'
    elif mth == 'September':
        sign = 'Leo' if day < 23 else 'Virgo'
    elif mth == 'October':
        sign = 'Virgo' if day < 23 else 'Scorpio'
    elif mth == 'November':
        sign = 'Scorpio' if day < 22 else 'Sagittarrius'

    print('Your star sign is', sign)

# your_sign()

# program to find the median of 3 numbers

def median_finder():
    '''
    Finds median of three numbers
    '''

    first = int(input('First number: '))
    second = int(input('Second number: '))
    third = int(input('third number: '))

    if first > second:
        if first < third:
            median = first
        elif second > third:
            median = second
        else:
            median = third
    else:
        if first > third:
            median = first
        elif second < third:
            median = second
        else:
            median = third
    
    print('Median is', median)

# median_finder()
