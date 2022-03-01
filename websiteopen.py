import webbrowser
from tkinter import *
import os
import sys


main = Tk()



def setup():
    
    with open('graveyard.txt' , 'r') as graveyard:
        adress = graveyard.read()
    with open('graveyard.txt','w') as graveyard:
        graveyard.write(adress)
        b3.configure(text=adress[adress.find("https://") + 8:adress.find(".com")])
        if adress.find("www.") > 0:
            b3.configure(text=adress[adress.find("https://www.") + 12:adress.find(".com")])
        currentsave.pack()
        b2.pack()
        b1.pack()
        e1.pack()
        inf.pack()
        e2.pack()
        space.pack()
        inf2.pack()
        b3.pack()  

        if adress.find("www") > 0:
            currentsave.configure(text="current website : " + adress[adress.find("https://www") + 12:adress.find(".com")])
            currentsave.pack()
            b2.pack()
            b1.pack()
            e1.pack()
            inf.pack()
            e2.pack()
            space.pack()
            inf2.pack()
            b3.pack()  


    with open('safe.txt' , 'r') as safe_file:
        adress = safe_file.read()
        fname_start = adress.find("nS")
        fname_end = adress.find("nE")
        if fname_end - fname_start >= 2:
            currentsave.configure(text="current website : " + adress[adress.find("https://") + 8:adress.find(".com")])
            if adress.find("www") > 0:
                currentsave.configure(text="current website : " + adress[adress.find("https://www") + 12:adress.find(".com")])
        else:
            print(fname_end - fname_start)
            currentsave.configure(text="current website : " + adress[fname_start + 2:fname_end])
        

def saveadress():
    with open('safe.txt' , 'r') as safe_file:
        adress = safe_file.read()
        fname_start = adress.find("nS")
        fname_end = adress.find("nE")
        
    with open('graveyard.txt','w') as graveyard:
        graveyard.write(adress)
        b3.configure(text=adress[adress.find("https://") + 8:adress.find(".com")])
        currentsave.pack()
        b2.pack()
        b1.pack()
        e1.pack()
        inf.pack()
        e2.pack()
        space.pack()
        inf2.pack()
        b3.pack()
        if adress.find("www") > 0:
            currentsave.configure(text="current website : " + adress[adress.find("https://www") + 12:adress.find(".com")])
            currentsave.pack()
            b2.pack()
            b1.pack()
            e1.pack()
            inf.pack()
            e2.pack()
            space.pack()
            inf2.pack()
            b3.pack()  

    adress = e1.get()
        
    with open('safe.txt','w') as safe_file:
        safe_file.write("")
        safe_file.write(e1.get() + "nS" + e2.get() + "nE")
        if e2.get() == "":
            currentsave.configure(text="current website : " + adress[adress.find("https://") + 8:adress.find(".com")])
            if adress.find("www") > 0:
                currentsave.configure(text="current website : " + adress[adress.find("https://www") + 12:adress.find(".com")])
        else:
            currentsave.configure(text ="current website : " +  str(e2.get()))
            

def define_browser():
    with open('safe.txt','r') as safe_file:
        adress = safe_file.read()
    
    webbrowser.open(adress[0:adress.find("nS")])
def opengraveyard():
    with open('graveyard.txt','r') as safe_file:
        adress = safe_file.read()
    
    webbrowser.open(adress[0:adress.find("nS")])
    
b1 = Button(main,text="open",command=define_browser)
b3 = Button(main,text="close",command = opengraveyard)
b2 = Button(main,text="safe",command=saveadress)
e1 = Entry(main,bd=1)
e2 = Entry(main,bd=2)
currentsave = Label(main,text="")

inf = Label(main,text="def")
inf2 = Label(main,text="graveyard")

space = Label(main,text="")
    
setup()




currentsave.pack()
b2.pack()
b1.pack()
e1.pack()
inf.pack()
e2.pack()



main.mainloop()