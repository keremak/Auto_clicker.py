import pyautogui
import random
import win32api,win32con
from time import sleep
import tkinter as tk
from tkinter.ttk import Combobox
import customtkinter as ctk

main = tk.Tk()
main.geometry("500x300+720+400")
main.resizable(False,False)
main.title("AutoClicker by benkerem")
buttonpressed = False
cps = 0
cpsCount = 0
changespeed = 1
clickCount = 0
i = 0
topMost = False
infinitechecker = False
cpsController = False
ischecked = tk.IntVar()
infinitecheck = tk.IntVar()
infinitecheck.set(0)
ischecked.set(0)
color = "#"
nums = "1234567890"
abc = "ecabf"
digits = nums + abc

colors = [
    "white",
    "gray",
    "red",
    "blue",
    "light blue",
    "green",
    "light green",
    "Rainbow"
]

languages = [
    "Türkçe",
    "English"
]

cpsget = tk.Entry(main, bg="white")
clickCountGet = tk.Entry(main, bg="white")
changespeedget = tk.Entry(main, bg="white", width=8)

clickCountGet.pack(pady=[2], ipadx=[1],ipady=[1])
cpsget.pack(ipadx=[1],ipady=[1], pady=[2])
changespeedget.place(y=[71], x=[445])

def topmostcmd():
    global topMost
    if ischecked.get() == 0:
        topMost = False
        main.wm_attributes("-topmost", topMost)
        alwaysOnDisplay.config(bg="light grey")
    elif ischecked.get() == 1:
        topMost = True
        main.wm_attributes("-topmost", topMost)
        alwaysOnDisplay.config(bg="light green")

def infiniteclicker():
    global infinitechecker
    if infinitecheck.get() == 0:
        infinitechecker = False
        infiniteClicks.config(bg="light grey")
        clickCountLabel.config(state="normal", disabledforeground="white")
        clickCountGet.config(state="normal", disabledbackground="white", disabledforeground="white")
    elif infinitecheck.get() == 1:
        infinitechecker = True
        infiniteClicks.config(bg="light green")
        clickCountLabel.config(state="disabled", disabledforeground="grey")
        clickCountGet.config(state="disabled", disabledbackground="light grey", disabledforeground="grey")
        
def click():
    global clickCount, cps, buttonpressed, infinitechecker
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.00001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
    if infinitechecker == False:
        clickCount -= 1
        Remaining["text"] = f"Remaining {clickCount} clicks."
        if buttonpressed:
            if clickCount > 0:
                main.after(int(1000 / float(cps)), click)
            else:
                Remaining["text"] = f"Finished!"
                Start.config(state="normal", bg="light green")
    elif infinitechecker:
        if buttonpressed:
            main.after(int(1000 / float(cps)), click)
            Remaining["text"] = f"Remaining 'INFINITY'"




def başlat():
    global cps, clickCount, buttonpressed

    Start.config(state="disabled",bg="light grey")
    if infinitechecker == False:
        cps = cpsget.get()
        clickCount = int(clickCountGet.get())
        if clickCount.is_integer():
            click()
    elif infinitechecker:
        cps = cpsget.get()
        print(type(cps), type(cpsget))
        click()

def isPressed():
    global cps, clickCount, buttonpressed
    buttonpressed = True
    Remaining.config(text="Starting in 3 seconds!")
    main.after(3000, başlat)

def bitir():
    global buttonpressed, clickCount, infinitechecker
    print(f"Pressed :")
    Start.config(state="normal", bg="light green")
    if infinitechecker == False:
        Remaining["text"] = f"Stopped in {clickCount} click left."
        buttonpressed = False
    elif infinitechecker:
        Remaining["text"] = f"'INFINITY' click stopped"
        buttonpressed = False

def ColorChange(event=None):
    global i, color, abc, nums, digits
    if ColorChose.get() == colors[7]:
        color = "#"
        for i in range(0,6):
            color += digits[random.randint(0, len(digits) - 1)]


        cpsLabel.config(bg=color)
        clickCountLabel.config(bg=color)
        cpsLabel.config(bg=color)
        clickCountLabel.config(bg=color)
        Remaining.config(bg=color)
        calculatedCps.config(bg=color)

        main.config(bg=color)
        color = "#"
        changespeed = changespeedget.get()
        try:
            if len(changespeed) <= 2:
                main.after(int(1000 / float(changespeed)),ColorChange)
            else:
                Remaining.config(text="Max char limit <2>")
        except ValueError:
            Remaining.config(text="Must be include a number!")


    elif ColorChose.get() != colors[7]:
        color = ColorChose.get()

        cpsLabel.config(bg=color)
        clickCountLabel.config(bg=color)
        cpsLabel.config(bg=color)
        clickCountLabel.config(bg=color)
        Remaining.config(bg=color)
        calculatedCps.config(bg=color)

        main.config(bg=color)
        print(f"Color : {color}")

def languageChosed(event=None):
    if languageChose.get() == "Türkçe":
        clickCountLabel.config(text=" Tıklama s :")
        cpsLabel.config(text="Sbt :")
        Start.config(text="Başlat")
        Stop.config(text="Durdur")
        alwaysOnDisplay.config(text="Her zaman ekranda")
        infiniteClicks.config(text="Sınırsız tıklama")
        Cpstest.config(text="Sbt testine başlamak için tıkla")
    else:
        clickCountLabel.config(text="Click count :")
        cpsLabel.config(text="Cps :")
        Start.config(text="Start")
        Stop.config(text="Stop")
        alwaysOnDisplay.config(text="Always on display")
        infiniteClicks.config(text="Infinity clicks")
        Cpstest.config(text="Click to start cps test")
    print(languageChose.get())

def cpsCountCommand():
    global cpsCount, cpsController
    cpsCount += 1
    Remaining.config(text=f"{cpsCount}")
    if cpsController == False:
        main.after(1000, cpsCalculator)
        cpsController = True


def cpsCalculator():
    global cpsCount, cpsController
    calculatedCps.config(text=f"{cpsCount / 1}")
    cpsCount = 0
    cpsController = False

cpsLabel = tk.Label(main, text="Cps :", font=("bold",10))
clickCountLabel = tk.Label(main, text="Click count :", font=("bold",10))
cpsLabel.place(x=150,y=25)
clickCountLabel.place(x=108, y=0)

alwaysOnDisplay = tk.Checkbutton(main,command=topmostcmd, text="Always on display", variable=ischecked, borderwidth=1, relief="solid", font=("bold",10), bg="light grey")
infiniteClicks = tk.Checkbutton(main ,command=infiniteclicker, text="Infinity clicks", variable=infinitecheck, borderwidth=1, relief="solid", font=("bold", 10), bg="light grey")
ColorChose = Combobox(main, values=colors, state="readonly", font="bold 10", height=5, width=10)
languageChose = Combobox(main,values=languages, state="readonly", font="bold 10", height=5, width=10)

ColorChose.place(x=350,y=70)
languageChose.place(x=5, y=5)
languageChose.bind("<<ComboboxSelected>>", languageChosed)
ColorChose.bind("<<ComboboxSelected>>", ColorChange)
infiniteClicks.place(x=350,y=40)
alwaysOnDisplay.place(x=350,y=10)

Start = tk.Button(main, fg="black",bg="light green", text="Start", font=("Latha", 10), command=isPressed)
Stop = tk.Button(main, fg="black",bg="orange", text="Stop", font=("Latha", 10), command=bitir)
Cpstest = tk.Button(main, fg="black", bg="light gray", text="Click to start cps test", font=("bold", 10), relief="flat", command=cpsCountCommand)
Remaining = tk.Label(main, font=("bold", 8), text="")
calculatedCps = tk.Label(main, font=("bold", 10), text="...")

Remaining.pack(side="bottom")
Start.place(x=200, y=50)
Stop.place(x=250, y=50)
Cpstest.place(x =0,y =130, relheight=1/2, relwidth=1)
calculatedCps.place(x=237, y=100)

main.mainloop()
