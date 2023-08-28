import tkinter
##Alternate import to remove all module mentions
#from tkinter import *
#create  a window. To keep open see last line of code
window = tkinter.Tk()



#modifying window properties
window.title('Program')
window.minsize(width=500, height=300)


#label
#create label first
my_label=tkinter.Label(text="Label", font=("arial", 24, "bold"))
#to show label in window. pack label on screen

#my_label.pack() -  Replaced by Place that gives more precision
#my_label.place(x=0,y=0) - replaced by grid as is less specific in scaled solutions

my_label.grid(column=0,row=0)

#Button


def button_click():
    my_label["text"]=input.get()


button = tkinter.Button()
button.config(text='Click me', command=button_click)


#button.pack()
button.grid(column=0, row=1)

#Entry

def read_input():
    print(input.get())


input = tkinter.Entry(width=10)
#input.pack()

input.grid(column=0,row=2)




# Creates a loop to avoid closing window automatically
window.mainloop()
