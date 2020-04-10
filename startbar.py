#!/usr/bin/env python3

"""
	Python script for use with Window's Linux installs that displays
	a bar at the top of the terminal, displaying the distro's name.
"""


import shutil
import os
import argparse
import sys

_VERSION_ = "0.6"
COLS, LINES = shutil.get_terminal_size()
TITLE = os.getenv("WSL_DISTRO_NAME")

def colormap():
	print("\033c\n  [#]\t[Color]")
	print("")
	print("  [0]\t\033[47;30mBlack\033[m")
	print("  [1]\t\033[31mRed\033[m")
	print("  [2]\t\033[32mGreen\033[m")
	print("  [3]\t\033[33mYellow\033[m")
	print("  [4]\t\033[34mBlue\033[m")
	print("  [5]\t\033[35mMagenta\033[m")
	print("  [6]\t\033[36mCyan\033[m")
	print("  [7]\t\033[37mWhite\033[m")
	print("\n")
	print("  Example: White font on Green bar")
	print("\tstartbar -f '7' -b '2'")


parser = argparse.ArgumentParser(description='Short sample app')


parser.add_argument('-t', dest="title", action="store", default=TITLE, help="Sets title")
parser.add_argument('-f', dest="font", action="store", default="7", help="Sets font color - Default: White")
parser.add_argument('-b', dest="barcolor", action="store", default="1", help="Sets bar color - Default: Red")
parser.add_argument('-cm', dest="colormap", action="store_true", default="False", help="Show color map")

args = parser.parse_args()

fontcolor = str(args.font)
barcolor = str(args.barcolor)

"""
	The following checks to see if the color option given has more than
	one digit, or if it has more.

	If the argument is a single digit number, then it will just plug that
	number in between "\033[3" and "m", thus, using a basic color.

	If it is 2 or more digits, the script will add "8;5;" to the argument
	before plugging it between "\033[3" / "\033[4" and "m", thus, using a
	color from the 256 wheel.
"""
if len(fontcolor) > 1:
	fontcolor = ("8;5;" + str(args.font))

if len(barcolor) > 1:
	barcolor = ("8;5;" + str(args.barcolor))


print("\033c\033[4" + str(barcolor) + "m" + " " * COLS + "\r\033[" + str(int((COLS - len(args.title))/2)) + "C\033[01;3" + str(fontcolor) + "m" + args.title + "\033[m\n")

if args.colormap == True:
	colormap()
