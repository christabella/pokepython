import sys
    
if sys.version_info[0] > 2:
    print("This game runs on Python 2 because curriculum")

from pokepython.gamelib.gui import play


def main():
    play()
