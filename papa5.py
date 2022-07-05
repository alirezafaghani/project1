import pyttsx3
from tkinter import *



def sendCommand():
    awnserEntry.delete(0, END)
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)
    
    
    userCommand = askQuestionEntry.get()
    
    if "hi" in userCommand.lower():
        awnserEntry.insert(END," Hello There")
        engine.say("Hello There")
    if "how are you" in userCommand.lower():
        awnserEntry.insert(END," I'm Good Thanks")
        engine.say("I'm Good Thanks")
    if "alireza" in userCommand.lower(): 
        awnserEntry.insert(END," he is a good programmer")
        engine.say("he is a good programmer")
    if "cat" in userCommand.lower(): 
        awnserEntry.insert(END,"gorgeous pet")
        engine.say("gorgeous pet")  
    if "what is you name" in userCommand.lower():
        awnserEntry.insert(END," my name is papa5")
        engine.say("my name is papa5")
    if "poya" in userCommand.lower():
        awnserEntry.insert(END," he is loved pandas")
        engine.say("he is a panda")
    if "ali daei" in userCommand.lower():
        awnserEntry.insert(END," Ali Daei is an Iranian football manager and former player")
        engine.say("Ali Daei is an Iranian football manager and former player")
    if "bitcoin" in userCommand.lower():
        awnserEntry.insert(END," Bitcoin is a decentralized digital currency ")
        engine.say("Bitcoin is a decentralized digital currency")
    if "mehdi" in userCommand.lower():
        awnserEntry.insert(END," he is a good speaker")
        engine.say("he is a good speaker")
    

        
    engine.runAndWait()
        
    
def volumeUp():
    pass
def volumeDown():
    pass


root = Tk(className="papa5")
root.geometry("400x150")
root.config(bg='#121212')
root.resizable(0,0)

askQuestionEntry = Entry(root, bg='#121212', fg='white', width=30)
askQuestionButton = Button(root, bg='#121212', fg='white', command=sendCommand, text='Ask Question', width=15)
awnserEntry = Entry(root, bg='#121212', fg='white', width=30)
volumeUpButton = Button(root, bg='#121212', fg='white', command=volumeUp, text='Turn Volume Up', width=15)
volumeDownButton = Button(root, bg='#121212', fg='white', command=volumeDown, text='Turn Volume Down', width=15)

askQuestionEntry.grid(row=0, column=0, padx=20, pady=(20,0))
askQuestionButton.grid(row=0, column=1, padx=20, pady=(20,0))
awnserEntry.grid(row=1, column=0, padx=20, pady=(20,0))
volumeUpButton.grid(row=1, column=1, padx=20, pady=(10,0))
volumeDownButton.grid(row=2, column=1, padx=20, pady=(10,0))

root.mainloop()