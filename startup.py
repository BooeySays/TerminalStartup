#!/usr/bin/env python3

import os
import shutil
import argparse

_VERSION_ = "0.4"

#class clr:
black = "16m"
red = "196m"
green = "46m"
yellow = "190m"
blue = "21m"
magenta = "201m"
cyan = "51m"
white = "15m"
BLACK = "16m\033[01m"
RED = "196m\033[01m"
GREEN = "46m\033[01m"
YELLOW = "190m\033[01m"
BLUE = "21m\033[01m"
MAGENTA = "201m\033[01m"
CYAN = "51m\033[01m"
WHITE = "15m\1033[01m"

HOME = os.getenv("HOME")
if os.getenv("WSL_DISTRO_NAME") is not None:
	DISTRONAME = os.getenv("WSL_DISTRO_NAME")
else:
	DISTRONAME = None

COLS, LINES = shutil.get_terminal_size()
parser = argparse.ArgumentParser(description='Simple app that draws a banner at the top of the terminal screen during start up, and displays which distro was just booted')

parser.add_argument('-t', dest="title", action="store", default=None, help="Sets title")
parser.add_argument('-fg', dest="font", action="store", default="7", help="Sets font color")
parser.add_argument('-bg', dest="barcolor", action="store", default="1", help="Sets bar color")
parser.add_argument('-b', '--bold', dest="boldfont", action="store_true", default="False", help="Font Format: Bold")
parser.add_argument('-i', '--italic', dest="italicfont", action="store_true", default="False", help="Font Format: Italics")
parser.add_argument('-u', '--underline', dest="underlinefont", action="store_true", default="False", help="Font Format: Underline")
parser.add_argument('1', nargs='+', help="\033[31mRed\033[m\n\tgde")

args = parser.parse_args()

BGCOLOR = ("\033[4" + str(args.barcolor) + "m")
FGCOLOR = ("\033[3" + str(args.font) + "m")
if args.boldfont is True:
	FGCOLOR = ("\033[01m" + FGCOLOR)

if args.italicfont is True:
	FGCOLOR = ("\033[03m" + FGCOLOR)

if args.underlinefont is True:
	FGCOLOR = ("\033[04m" + FGCOLOR)


if args.title is not None:
	DISTRONAME = args.title


def drawbanner():
	if DISTRONAME is not None:
		print("\033c\033[m" + BGCOLOR + " " * COLS + "\r\033[" + str(int((COLS - len(DISTRONAME))/2)) + "C" + FGCOLOR + DISTRONAME + "\033[m\n")
	else:
		print("\033c\033[m" + BGCOLOR + " " * COLS + "\033[m\n")

drawbanner()