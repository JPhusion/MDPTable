from gui.widgets.weather import *
from gui.widgets.covid import *
from gui.widgets.clock import *

def widget(command, widgets):
    return [widget_clock(3, 2, (0,0)), widget_covid(3, 2, (3,0))]
