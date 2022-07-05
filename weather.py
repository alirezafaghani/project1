from imp import source_from_cache
from bs4 import BeautifulSoup
import requests
from tkinter import *






root = Tk(className="weather")
root.geometry('700x170')
root.config(bg='#00FFFF')
root.resizable(0,0)


cityNameLabel = Label(root, bg='#FFDAB9', text='please enter your city')
cityNameEntry = Entry(root)

degreeLabel = Label(root, bg='#FFDAB9', text='please choose')

choosed = StringVar()
choosed.set('choose')
degreeMenu = OptionMenu(root,choosed, "Celsius", "Farenheit")


def save():
    global city
    global value
    city = cityNameEntry.get()
    value = choosed.get()
    procces()

def procces():
    address = '''
https://www.google.com/search?q={}+weather+{}&rlz=1C1ASUC_enIR597IR597&sxsrf=ALiCzsYDO7vGH_8RoRKyyz2wCunQBG8PTA%3A1656795459736&ei=Q7HAYsjALNmE9u8Pvpmw0A4&oq=+{}+weather&gs_lcp=Cgdnd3Mtd2l6EAEYCDIMCCMQJxCdAhBGEIACMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEB4QBzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAUoECEEYAEoECEYYAVCIWFiIWGD-e2gHcAF4AIAB9AOIAfQDkgEDNS0xmAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz
'''.format(city, value, city)
    source = requests.get(address)
    soup = BeautifulSoup(source.content, 'html.parser')
    global CityName, date, degree
    CityName = soup.find('span', class_="BNeawe tAd8D AP7Wnd")
    date = soup.find('div', class_="BNeawe tAd8D AP7Wnd")
    degree = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
    status()

def myDelete():
    try:
        WeatherStatus.destroy()
        labelError.destroy()
    except Exception:
        WeatherStatus.destroy()
    ConfirmButton['state'] = NORMAL
    DeleteButton['state'] = DISABLED


def status():
    global WeatherStatus , labelError
    try:
        WeatherStatus = Label(root, text= "the weather in {} on {} is {}".format(CityName.text, date.text, degree.text) )
        WeatherStatus.grid(row=2,column=1, padx=20, pady=(10,0))
    except Exception:
        labelError = Label(root, text="city not found")
        labelError.grid(row=2,column=1, padx=20, pady=(10,0))
    ConfirmButton['state'] = DISABLED
    DeleteButton['state'] = NORMAL

ConfirmButton = Button(root, bg='#FFDAB9', text='confirm', command=save)



DeleteButton = Button(root,bg='#FFDAB9', fg='red', text='Delete', command=myDelete )



cityNameLabel.grid(row=0, column=2, padx=20, pady=(20,0))
cityNameEntry.grid(row=1, column=2, padx=20, pady=(10,0))
degreeLabel.grid(row=0, column=1, padx=40, pady=(20,0))
degreeMenu.grid(row=1, column=1, padx=20, pady=(10,0))
DeleteButton.grid(row=0, column=0, padx=60, pady=(10,0))
ConfirmButton.grid(row=1, column=0, padx=20, pady=(10,0))


root.mainloop()