import tkinter


er_today = 549
def convert_currency():
    amount = float(dollar_input.get())
    print(type(amount))
    result = er_today * amount
    print(result)
    colones_lbl.config(text=str(result))
    #return result



window = tkinter.Tk()
window.title("Tipo de cambio")
window.minsize(width=400,height=400)

er = tkinter.Label(text='Tipo de Cambio:', font=("calibri", 18, "bold"))
er.grid(column=0,row=0)

er_amount= tkinter.Label(text=str(er_today), font=("calibri", 18))
er_amount.grid(column=1,row=0)

dollar_lbl = tkinter.Label(text='Dolares:', font=("calibri", 16, "bold"))
dollar_lbl.grid(column=0, row=1)

dollar_input = tkinter.Entry(width=10)
dollar_input.insert(index='0', string="0")
dollar_input.grid(column=1, row=1)

convert = tkinter.Button( text='Convertir', command=convert_currency)
convert.grid(column=3, row=1)

colones_lbl = tkinter.Label(text='Colones:', font=("calibri", 16, "bold"))
colones_lbl.grid(column=0, row=2)

colones_lbl = tkinter.Label(text= '0', font=("calibri", 16, "bold"))
colones_lbl.grid(column=1, row=2)

window.mainloop()
