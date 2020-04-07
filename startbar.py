#!/usr/bin/env python3

"""
	Python script for use with Window's Linux installs that displays
	a bar at the top of the terminal, displaying the distro's name.
"""


import shutil
import os
import argparse
COLS, LINES = shutil.get_terminal_size()
TITLE = os.getenv("WSL_DISTRO_NAME")


parser = argparse.ArgumentParser(description='Short sample app')


parser.add_argument('-t', dest="title", action="store", default=TITLE, help="Sets title")
parser.add_argument('-f', dest="font", action="store", default="\033[01;38;5;15m", help="Sets font color")
parser.add_argument('-b', dest="barcolor", action="store", default="\033[48;5;196m", help="Sets bar color")

args = parser.parse_args()


print("\033c" + args.barcolor + " " * COLS + "\r\033[" + str(int((COLS - len(args.title))/2)) + "C" + args.font  + args.title + "\033[m\n")
