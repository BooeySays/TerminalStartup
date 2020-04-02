#!/usr/bin/env python3

import os
import shutil
import argparse

class clr:
	black = "15m"
	red = "196m"
	green = "46m"
	yellow = "190m"
	blue = "21m"
	magenta = "201m"
	cyan = "51m"
	white = "16m"
	BLACK = "15;01m"
	RED = "196;01m"
	GREEN = "46;01m"
	YELLOW = "190;01m"
	BLUE = "21;01m"
	MAGENTA = "201;01m"
	CYAN = "51;01m"
	WHITE = "16;01m"

HOME = os.getenv("HOME")
BGCOLOR = ("\033[48;5;" + red)
FGCOLOR = ("\033[38;5;" + WHITE)

COLS, LINES = shutil.get_terminal_size()

def drawbanner():
	print("\033c" + BGCOLOR + " " * COLS +