# casabot
Bot to send invitation requests to housing advertisers. You only have to edit your contact parameters in the same file and run it with: 
#./python3 checkEmail.py. 

#Prerequirties: 
you receive the filtered housing advertisment to your email.

#Mechanism of this bot:
It checks your email inbox, find new housing advertisments, adds the id of the ad to a text file (.wgids), then sends requests to all newly added ad's ids, it will randomly choose a cover letter from "anschreiben" or "anschreiben2" files. Check out my cover letters!.

This bot runs on Python3, following dependencies required:
#1_ Pyautogui -Library to interact with the graphical user interface. This is the core of simplicity in this bot.
#2_ Pyperclip -Also part of the simplicity core, needed for copying to clipboard.
#3_ I don't remember what else, just trust the program and install the other required libraries.
