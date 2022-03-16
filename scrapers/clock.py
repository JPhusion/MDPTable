import datetime


def date(worded=False):
    return (
        datetime.date.today().strftime("%B %d, %Y")
        if worded
        else datetime.date.today().strftime("%d · %m · %Y")
    )


def hour(twentyFourHour=False):
    return (
        datetime.datetime.now().strftime("%H")
        if twentyFourHour
        else datetime.datetime.now().strftime("%I")
    )
    
    
def minutes():
    return datetime.datetime.now().strftime("%M")


def seconds():
    return datetime.datetime.now().strftime("%S")
