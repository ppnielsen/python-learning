'''
Manipulating data retrieved from pyodbc to useable form
'''

import pyodbc # used to query against db
import os # used to create directories
import errno # used to determine errors

# dictionary that will house receivables and guids
work = {
    'rcvb_id': [],
    'guids': []
}

# connecting to db
cnxn = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}', server='PPJN', database='RRTEST')
cursor = cnxn.cursor()

# executing sql
cursor.execute("select distinct * from invoices")

# retrieving rows
rows = cursor.fetchall()

# adding data to work dict
for row in rows:
    
    # adding rcvbs that are not in work dict along with the associated guid
    if row[0] not in work['rcvb_id']:
        work['rcvb_id'].append(row[0])
        work['guids'].append([row[1]])

    # adding guids to work dict if rcvb exists and guid does not
    else:
        i = work['rcvb_id'].index(row[0])
        if row[1] not in work['guids'][i]:
            work['guids'][i].append(row[1])
                
# print work dict
print(work)

try:
    os.makedirs('./disputes')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# creating directory if it does not exists
for rcvb in work['rcvb_id']:

    try:
        os.makedirs('./disputes/' + str(rcvb))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
