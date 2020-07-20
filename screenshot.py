import tkinter as tk
import pyautogui

win=tk.TK()
win.title("Take Screenshot")

def takescreenshot():
    screenshot=pyautogui.screenshot()
    screenshot.save(r'C:\Users\hp\Pictures\screenshot.png')
    
button=tk.Button(win,text="Capture Screenshot",command=takescreenshot)
button.pack()

win.mainloop()
    
