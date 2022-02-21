import webbrowser
from tkinter import *
import os
import sys


main = Tk()



b3 = Button(main,text="b1")
b4 = Button(main,text="b1")
b5 = Button(main,text="b1")
b6 = Button(main,text="b1")
b7 = Button(main,text="b1")
b8 = Button(main,text="b1")
b9 = Button(main,text="b1")
b10 = Button(main,text="b1")


def setup():
    with open('safe.txt' , 'r') as safe_file:
        adress = safe_file.read()
        currentsave.configure(text=adress[adress.find("https://") + 8:adress.find(".com")])
        if adress.find("www") > 0:
            currentsave.configure(text=adress[adress.find("https://www") + 12:adress.find(".com")])
        

def saveadress():
    adress = e1.get()
    with open('safe.txt','w') as safe_file:
        safe_file.write("")
        safe_file.write(e1.get())
        currentsave.configure(text=adress[adress.find("https://") + 8:adress.find(".com")])
        if adress.find("www") > 0:
            currentsave.configure(text=adress[adress.find("https://www") + 12:adress.find(".com")])
            

def define_browser():
    with open('safe.txt','r') as safe_file:
        adress = safe_file.read()
    
    webbrowser.open(adress)
    
b1 = Button(main,text="open",command=define_browser)
b2 = Button(main,text="safe",command=saveadress)
e1 = Entry(main)
currentsave = Label(main,text="")
    
setup()




currentsave.pack()
b2.pack()
b1.pack()
e1.pack()


main.mainloop()
