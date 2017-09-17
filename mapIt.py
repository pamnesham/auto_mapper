#! python3
#mapIt.py - automatically search Google Maps by copying an address

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #get address from cmd
    address = ''.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

#todo: get address from clipboard
