'''
Day 16 of Cup of Code's Python tutorial
'''

def workday():
    '''
    Fun way to remind you to take a break!
    '''
    import time
    import webbrowser

    total_breaks = 3
    break_count = 0

    print('This program started on', time.ctime())

    while break_count < total_breaks:
        time.sleep(15) # 15 seconds of program pausing
        webbrowser.open('https://youtube.com/watch?v=z1B2m_MgahE&t=24s')
        break_count += 1

workday()
