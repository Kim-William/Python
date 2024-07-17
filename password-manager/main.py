from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    text_pass.delete(0, END)
    password_list = []

    for char in range(nr_letters):
        password_list.append(choice(letters))

    for char in range(nr_symbols):
        password_list += choice(symbols)

    for char in range(nr_numbers):
        password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
    pyperclip.copy(password)
    text_pass.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    
    website = text_website.get()
    id = text_id.get()
    password = text_pass.get()
    new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }
    if len(website) == 0:
        messagebox.showerror(title='Website Error', message='There is no Website.\nPlease Enter the Website.')
        return

    if len(id) == 0:
        messagebox.showerror(title='Email/Username Error', message='There is no Email/Username.\nPlease Enter the Email/Username.')
        return

    if len(password) == 0:
        messagebox.showerror(title='Password Error', message='There is no Password.\nPlease Enter the Password.')
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                        f"\nEmail: {id}"
                        f"\nPassword: {password}"
                        f"\nIs it ok to save?")

    if is_ok:
        with open('passwordfile.txt', 'a') as file:
            file.write(f'{website}|{id}|{password}\r')

        text_website.delete(0, END)
        text_id.delete(0, END)
        text_pass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title = 'Password Manager'
window.config(padx=50, pady=50)

# row 0
canvas = Canvas()
canvas.config(width=200, height=200)
canvas_logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image = canvas_logo)
canvas.grid(column=1, row=0)



# Labels
label_web = Label(text='Website:')
label_web.grid(row=1, column=0)
label_id = Label(text='Email/Username:')
label_id.grid(row=2, column=0)
label_pass = Label(text='Password:')
label_pass.grid(row=3, column=0)


# Entries
text_website = Entry(width=35)
text_website.grid(row=1, column=1, columnspan=2)
text_website.focus()
text_id = Entry(width=35)
text_id.grid(row=2, column=1, columnspan=2)
text_pass = Entry(width=21)
text_pass.grid(row=3, column=1)


# Buttons
button_genpass = Button(text='Generate Password', command=generate_password)
button_genpass.grid(row=3, column=2)
button_add = Button(text='Add', width=36, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()