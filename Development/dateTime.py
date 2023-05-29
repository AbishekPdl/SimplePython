import datetime

def date():
    #importing current date from OS
    now=datetime.datetime.now
    return str(now().date())

def time():
    #importing current time from Os
    now = datetime.datetime.now
    return str(now().time())