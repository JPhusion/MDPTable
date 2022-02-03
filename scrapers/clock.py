import datetime


def date(worded=False):
    return (
        datetime.date.today().strftime("%B %d, %Y")
        if worded
        else datetime.date.today().strftime("%d/%m/%Y")
    )


def time(twentyFourHour=False):
    return (
        datetime.datetime.now().strftime("%H:%M:%S")
        if twentyFourHour
        else datetime.datetime.now().strftime("%I:%M:%S")
    )
