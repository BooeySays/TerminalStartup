

DX2RC = os.getenv("DX2RC")
startbar_rc_file = (DX2RC + "/startbar.rc")
startbar_rc = "export PROMPT_COMMAND=\"tput sc; tput cup 0, 0; startbar1; tput rc\""

f = open(startbar_rc_file, 'w')
f.write(startbar_rc)
f.close()


