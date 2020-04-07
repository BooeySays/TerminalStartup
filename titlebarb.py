#!/usr/bin/env python3

import shutil
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--title", dest="titlestring", help="Set title", default=" ", action="store")
parser.add_argument("-d", "--desc", dest="descstring", help="Set description", action="store")
args = parser.parse_args()


COLS, LINES = shutil.get_terminal_size()

TITLE = None
BARCOLOR = "\033[48;5;196m"

def drawbar():
	TITLEA = args.titlestring
	print(BARCOLOR + " \033[38;5;15m" + TITLEA + " " * (COLS - int(len(TITLEA) + 1)) + "\033[m\r")

drawbar("testing")
print(args.titlestring)
