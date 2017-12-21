'''
Sets up environment for downloading of invoice backup (given receivables and guids) provided by sql query
'''

import os # used to create directories


def useable_data_folders():
    '''
    Manipulating data (receivable/guid) retrieved from sql to useable form
    Creates distinct folder for downloads to go into
    '''

    import errno # used to determine errors
    import pyodbc # used to query against db

    # dictionary that will house receivables and guids
    listing = {
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

    # adding data to listing dict
    for row in rows:

        # adding rcvbs that are not in listing dict along with the associated guid
        if row[0] not in listing['rcvb_id']:
            listing['rcvb_id'].append(row[0])
            listing['guids'].append([row[1]])

        # adding guids to listing dict if rcvb exists and guid does not
        else:
            i = listing['rcvb_id'].index(row[0])
            if row[1] not in listing['guids'][i]:
                listing['guids'][i].append(row[1])


    # creating disputes folder in main directory if it doesn't exist
    try:
        os.makedirs('./disputes')
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise

    # creating directory if it does not exists
    for rcvb in listing['rcvb_id']:

        try:
            os.makedirs('./disputes/' + str(rcvb))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise

    # outputting data for downloading
    return listing

WORK = useable_data_folders()
print(WORK)
