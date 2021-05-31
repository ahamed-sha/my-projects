from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# Labels
init_label = Label(text="is equal to")
init_label.grid(row=1, column=0)

# Entries
entry = Entry(width=15)
entry.grid(row=0, column=1)

# Labels
label = Label(text="miles")
label.grid(row=0, column=2)


# Labels
label1 = Label(text="kilometer")
label1.grid(row=1, column=2)


# Buttons
def action():
    # Miles to km
    miles_value = float(entry.get())
    miles = round(miles_value * 1.609, 1)
    label2 = Label(text=miles)
    label2.grid(row=1, column=1)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)


window.mainloop()
