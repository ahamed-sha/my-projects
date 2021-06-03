from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*']

    password_letters = [choice(letters) for char in range(randint(7, 9))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 3))]
    password_numbers = [choice(numbers) for num in range(randint(2, 3))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Error", message="Don't leave the fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # reading the old data
                data = json.load(file)
                print(data)  # debug

        except FileNotFoundError:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(new_data, file, indent=4)
        except:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():

    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="First create a new field")
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Error", message="First create a new field")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"{website} doesn't exist")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# label 1
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
# label 2
username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)
# label 3
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entry 1
website_entry = Entry()
website_entry.grid(row=1, column=1)
website_entry.focus()
# entry 2
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "someone@email.com")
# entry 3
password_entry = Entry()
password_entry.grid(row=3, column=1)

# button 1
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# button 2
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# button 3
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)


canvas.mainloop()
