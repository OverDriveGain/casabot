# casabot
Bot to send invitation requests to housing advertisers. You only have to edit your contact parameters in the same file and run it with
<br/> 
./python3 checkEmail.py. 
<br/>

<h1>Prerequirties and dependencies:</h1>
1_ you receive the filtered housing advertisment to your email.<br/>
2_ Pyautogui -Library to interact with the graphical user interface. This is the core of simplicity in this bot.<br/>
3_ Pyperclip -Also part of the simplicity core, needed for copying to clipboard.<br/>
4_ I don't remember what other libraries are there, just trust the program and install using pip3.<br/>

<h1>Mechanism of this bot:</h1>
It checks your email inbox, find new housing advertisments, adds the id of the ad to a text file (.wgids), then sends requests to all newly added ad's ids, it will randomly choose a cover letter from "anschreiben" or "anschreiben2" files. Check out my cover letters!.
