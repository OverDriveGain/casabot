from evdev import InputDevice, ecodes
#dev = InputDevice('/dev/input/event3')
import pyautogui
import time
import tkinter as Tk
import pyperclip
import webbrowser


WG_BEWERBUNG_FILE='anschreiben'
INFO_ARRAY=[['name','Manar'],['family', 'Zaboub'],['email','manar.zaboub@gmail.com'],['phone','017620003272']]

def writeBewerbung():
	toCopy=""
	with open(WG_BEWERBUNG_FILE,'r') as infile:
		for line in infile:
			#for letter in line:
			#pyautogui.typewrite(line)
			toCopy=''.join([toCopy,line])
			print(line)
		pyperclip.copy(toCopy)
	pyautogui.hotkey("ctrl","v")	

def writeInfo(x):
	for info in INFO_ARRAY:
		if info[0]==x:
			for letter in info[1]:
				pyautogui.press(letter)

	
def doThis(URL):
	internetspeed=20.0	#speed between displaying the email
	webbrowser.get('firefox').open_new_tab(URL)
	time.sleep(internetspeed)	
	out=True
#	for light in dev.leds(verbose=True):
#		if light[0]=='LED_NUML':
#			out=True
	if out:
		pyautogui.press('tab')
		writeBewerbung()
		pyautogui.press('tab')
		pyautogui.press('down')
		pyautogui.press('tab')
		writeInfo('name')
		pyautogui.press('tab')
		writeInfo('family')
		pyautogui.press('tab')
		writeInfo('email')
		pyautogui.press('tab')
		writeInfo('phone')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('tab')
		pyautogui.press('space')
		pyautogui.press('enter')
		time.sleep(2)
	return out