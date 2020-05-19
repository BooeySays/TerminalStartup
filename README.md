# TerminalStartup
A small script I made to help me differenciate which Ubuntu distro I just booted up, and/or which window has which distro, etc, etc.

I made the script because I have a few different Ubuntu distros installed on my Windows box, and sometimes I would get confused which distro I am working in, and/or which distro I just booted up.

This script will display a bar at the top of the console and by default, the script will print out the distro's name and version number.


<<<<<<< HEAD
#SYNTAX:
startbar [-b "BGCOLOR"]/[-f "FGCOLOR"]/[-t "TITLE"]
=======
# HOW TO USE:
This script is meant to be used with those Linux installs on Windows. One of the variables the script looks for is
the $WSL_DISTRO_NAME variable, which those Linux installs has, but are missing in regular Linux distros.

The variable contains the Linux distro name and version number, which the script uses when displaying the distro name
in the start up bar. 
>>>>>>> 75839f13f1ea1b9d3d031833232f1574311d05b3
