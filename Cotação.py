from tkinter import *
import requests
import json

window=Tk()

window.title("Cotações")

response = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
response = response.json()
dolar = response["USDBRL"]["bid"]
euro=response["EURBRL"]["bid"]
bitcoin = response["BTCBRL"]["bid"]

def show():
    button.pack_forget()
    dol=Label(window,text=f"Dólar: {dolar}")
    dol.pack()
    eur=Label(window,text=f"Euro: {euro}")
    eur.pack()
    btc=Label(window,text=f"Bitcoin: {bitcoin}")
    btc.pack()

welcome=Label(window,text="Cotações em relação ao Real Brasileiro")
welcome.pack()
button=Button(window,text="Ver",command=lambda:show())
button.pack()

window.mainloop()
