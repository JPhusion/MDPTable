import time
import threading


def function():
    global i
    i = 10
    def load():
        global i
        i = 6
    load()
    print(i)

    
function()
