from gui.widgets.weather import *
from gui.widgets.covid import *
from gui.widgets.clock import *

def get_squares(width, height, position):
    for i in range(width):
        for j in range(height):
            yield (i + position[0], j + position[1])

def widget(command, widgets):
    cmd_args = command.split(' ')
    occupied = []
    for widget in widgets:
        occupied += list(widget.squares_occupied())
    if cmd_args[1] == 'add':
        squares = list(get_squares(int(cmd_args[3]), int(cmd_args[4]), (int(cmd_args[5]), int(cmd_args[6]))))
        if not set(occupied).isdisjoint(squares):
            return widgets
        if len(cmd_args) != 7:
            return widgets
        if cmd_args[2].lower() == 'covid':
            widgets.append(widget_covid(int(cmd_args[3]), int(cmd_args[4]), (int(cmd_args[5]), int(cmd_args[6]))))
        elif cmd_args[2].lower() == 'clock':
            widgets.append(widget_clock(int(cmd_args[3]), int(cmd_args[4]), (int(cmd_args[5]), int(cmd_args[6]))))
    if cmd_args[1] == 'rm':
        if len(cmd_args) != 4:
            return widgets
        pos = (int(cmd_args[2]), int(cmd_args[3]))
        for widget in widgets:
            if pos in widget.squares_occupied():
                widgets.remove(widget)
    return widgets
