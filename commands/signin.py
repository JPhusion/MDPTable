from gui.widgets.weather import *
from gui.widgets.covid import *
from gui.widgets.clock import *
from gui.widgets.calendar import *

def signin():
    return [widget_clock(3, 2, (3,0)), widget_covid(3, 2, (3,2)), widget_weather(3, 2, (0, 0)), widget_cal(3, 3, (0, 2))]
