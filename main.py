from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)
    entry3.insert(0, password)
    copy(password)



def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",  message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)


def find_password():
    past = entry1.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if past in data:
            email = data[past]["email"]
            password = data[past]["password"]
            messagebox.showinfo(title=past, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Detail for {past} exists.")


window = Tk()
window.title("password")
window.config(padx=20, pady=20)
main_lable = Label(text="PASSWORD GENERATOR", font=("Arial", 25, "bold"))
main_lable.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)

entry1 = Entry(width=35)
entry1.focus()
entry1.grid(row=1, column=1, columnspan=2)
entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)
entry3 = Entry(width=35)
entry3.grid(row=3, column=1, columnspan=2)

button1 = Button(text="Generate Password",  command=generate_password)
button1.grid(row=3, column=2)
button = Button(text="Add", width=30, command=save)
button.grid(row=4, column=1, columnspan=2)
button2 = Button(text="Search", width=13, command=find_password)
button2.grid(row=1, column=2)

window.mainloop()
