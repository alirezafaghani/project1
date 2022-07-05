from imp import source_from_cache
from bs4 import BeautifulSoup
import requests
from tkinter import *
import pyttsx3



root = Tk(className="cryptocurrency prices")
root.geometry('500x170')
root.config(bg='#E6E6FA')
root.resizable(0,0)



cryptoNameLabel = Label(root, bg='#FFDAB9', text='please enter a crypto')
cryptoNameEntry = Entry(root)

def save():
    global crypto
    crypto = cryptoNameEntry.get()
    procces()


def procces():
    address = '''
https://www.google.com/search?q={}+price+usd&rlz=1C1ASUC_enIR597IR597&sxsrf=ALiCzsYROMCWht_X84aquGtM_0znbJA-AQ%3A1656812517631&ei=5fPAYsOIJqy39u8PtqmJgAM&oq={}+price&gs_lcp=Cgdnd3Mtd2l6EAEYATIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzINCC4QxwEQ0QMQsAMQQzIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYAUoECEEYAEoECEYYAVAAWABgwxFoAnABeACAAQCIAQCSAQCYAQDIARHAAQHaAQYIARABGAk&sclient=gws-wiz'''.format(crypto,crypto) 
    source = requests.get(address)
    soup = BeautifulSoup(source.content, 'html.parser')
    global cryptoName, price
    cryptoName = soup.find('span', class_="r0bn4c rQMQod")
    price = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
    status()


def myDelete():
    try:
        crypoStatus.destroy()
        labelError.destroy()
    except Exception:
        crypoStatus.destroy()
    ConfirmButton['state'] = NORMAL
    DeleteButton['state'] = DISABLED  


def status():
    global crypoStatus, labelError
    try:
        crypoStatus = Label(root, text= "{} {}".format(cryptoName.text, price.text) )
        crypoStatus.grid(row=2,column=1, padx=20, pady=(10,0))
    except Exception:
        labelError = Label(root, text="crypto not found")
        labelError.grid(row=2,column=1, padx=20, pady=(10,0))
    ConfirmButton['state'] = DISABLED
    DeleteButton['state'] = NORMAL


ConfirmButton = Button(root, bg='#E0FFFF', text='confirm', command=save)



DeleteButton = Button(root,bg='#E0FFFF', fg='red', text='Delete', command=myDelete)


cryptoNameLabel.grid(row=0, column=0, padx=20, pady=(20,0))
cryptoNameEntry.grid(row=1, column=0, padx=20, pady=(10,0))
DeleteButton.grid(row=0, column=1, padx=60, pady=(10,0))
ConfirmButton.grid(row=1, column=1, padx=20, pady=(10,0))


root.mainloop()