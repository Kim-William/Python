from tkinter import *

window = Tk()

window.title("My Firsdt GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=200)

input = Entry(width=30)
input.grid(row=0, column=1)
input.config(text='0')
# input.pack()

label_miles = Label(text='Miles')
label_miles.grid(row=0, column=2)

label_equal = Label(text='is equal to')
label_equal.grid(row=1, column=0)

label_value = Label(text='value')
label_value.grid(row=1, column=1)
label_value.config(text = '0')

label_km = Label(text='Km')
label_km.grid(row=1, column=2)

def button_calculate_clicked():
    miles = float(input.get())
    km = round(miles * 1.609)
    label_value.config(text= f'{km}')

button_calculate = Button(text='Calculate', command= button_calculate_clicked)
button_calculate.grid(row=2, column=1)

# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# # my_label.pack()
# my_label.grid(row=0, column=0)
# my_label.config(padx=50, pady=50)

# my_label['text'] = 'New Text'
# # my_label.config(text='New Text')

# def button_clicked():
#     my_label['text'] = input.get()

# button = Button(text='Click Me', command=button_clicked)
# button.grid(row=1, column=1)
# # button.pack()

# button2 = Button(text='Click Me', command=button_clicked)
# button2.grid(row=0, column=2)
# # button.pack()




window.mainloop()

