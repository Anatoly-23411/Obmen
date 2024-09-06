# from cProfile import label
# from pickletools import name2i

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

# # from idna import check_label


def update_c_label(event):
    code = t_combobox.get()
    name = cur[code]
    c_label.config(text=name)
# from bottle import response, delete
# from PyInstaller.loader.pyiboot01_bootstrap import entry
def exchange():
    # code = entry.get()
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", f"Введите код валюты!")

cur = {
    "RUB": 'Российский рубль',
    "EUR": 'Евро',
    "GBP": 'Бритоанский фунт стерлингов',
    "JPY": 'Японская йена',
    "CNY": 'Китайский юань',
    "KZT": 'Казахский тенге',
    "UZS": 'Узбекский сум',
    "CHF": 'Швейцарский франк',
    "AED": 'Дирхам ОАЭ',
    "CAD": 'Канадский доллар',
    "USD": 'Доллар США'
}

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)

# cur = ["RUB", "EUR", "GBP", "JPY", "CNY", "KZT", "UZS", "CHF", "AED", "CAD"]
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_c_label)


c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()










