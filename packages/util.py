from datetime import datetime

def showtoday():
    now = datetime.now()
    prettydate = datetime.strftime(now, '%d-%m-%Y %H:%M:%S')
    return now

if __name__ == '__main__':
    n = showtoday()
    print(n)

    # What does python call this module?
    # every module run directly is called '__main__'
    print(f'This module is currently known as {__name__}')