import DownloadExchangeRate

import tkinter as tk

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Currences")
        self.choose=tk.IntVar()
        self.choose.set(1)
        self.kurs=0
        self.name_kurs = "USD"
        self.radio_button_USD = tk.Radiobutton(self.window, text="USD", variable=self.choose, value=1,command=self.sel)
        self.radio_button_USD.pack(anchor=tk.CENTER)

        self.radio_button_euro = tk.Radiobutton(self.window, text="EUR", variable=self.choose, value=2, command=self.sel)
        self.radio_button_euro.pack(anchor=tk.CENTER)

        self.radio_button_pound = tk.Radiobutton(self.window, text="GBP", variable=self.choose, value=3, command=self.sel)
        self.radio_button_pound.pack(anchor=tk.CENTER)

        self.radio_button_frank = tk.Radiobutton(self.window, text="CHF", variable=self.choose, value=4, command=self.sel)
        self.radio_button_frank.pack(anchor=tk.CENTER)

        self.label_currency=tk.Label(self.window,text="Currence")
        self.label_currency.pack(anchor=tk.CENTER)

        self.value_field=tk.Entry(self.window,width=24)
        self.value_field.pack(anchor=tk.CENTER)

        self.button_oblicz=tk.Button(self.window,text="Przelicz",command=lambda:self.convertToPLN())
        self.button_oblicz.pack(anchor=tk.CENTER)


        self.actal_curs_str = tk.StringVar(value="Aktualny kurs")
        self.actual_curs=tk.Label(self.window,textvariable=self.actal_curs_str)
        self.actual_curs.pack(anchor=tk.CENTER)

        self.convert_to_PLN_text = tk.StringVar(value="")
        self.convert_to_PLN = tk.Label(self.window, textvariable=self.convert_to_PLN_text)
        self.convert_to_PLN.pack(anchor=tk.CENTER)

        self.window.mainloop()
    def sel(self):
        if self.choose.get()==1:
            self.kurs=DownloadExchangeRate.dollar()
            self.name_kurs="USD"
        elif self.choose.get()==2:
            self.kurs=DownloadExchangeRate.euro()
            self.name_kurs = "EUR"
        elif self.choose.get()==3:
            self.kurs=DownloadExchangeRate.pound()
            self.name_kurs = "GBP"
        elif self.choose.get()==4:
            self.kurs=DownloadExchangeRate.franc()
            self.name_kurs = "CHF"
        self.actal_curs_str.set("Aktualny kurs "+self.name_kurs+" :"+str(self.kurs))

    def convertToPLN(self):
        self.convert_to_PLN_text.set("Po przeliczneiu z "+self.name_kurs+" na PLN wynosi: "+str(self.kurs*float(self.value_field.get())))


