



# use *args 
def add (*args):
    result = 0
    for n in args:
        result+= n
    return result

print(add(1,2,3,4,5))
print(add(2,3,4))


divide = 'divide'
minus = 'minus'
add = 'add'
multiply = 'multiply'

# use **kwargs 
def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs[add])

    n+=kwargs[add]
    n*= kwargs[multiply]

    print(f'result {n}')


calculate(2, add=3, multiply = 5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')
        print(type(self.seats))
        if self.seats == None:
            self.seats = 4

# my_car = Car(make='Nissan', model='GT-R')

my_car = Car(make='Nissan')

print(my_car.model)
print(my_car.seats)




from tkinter import *

window = Tk()

window.title("My Firsdt GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label['text'] = 'New Text'
# my_label.config(text='New Text')

def button_clicked():
    my_label['text'] = input.get()
    print(text.get("1.0", END))

button = Button(text='Click Me', command=button_clicked)
button.pack()


input = Entry(width=30)
input.pack()


text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
text.pack()

text.pack()

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()
scale.pack()

def check_changed():
    if checked_state.get() == 1:
        checkbutton['text'] = 'Is On!'
    else:
        checkbutton['text'] = 'Is Off!'

checked_state = IntVar()
checked_state.set(1)
checkbutton = Checkbutton(text='Is On!', variable=checked_state, command=check_changed)
checkbutton.pack()

def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_state.set(1)
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

