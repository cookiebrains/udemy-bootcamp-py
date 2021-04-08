from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = round(int(input.get()) * 1.609344)
    result["text"] = new_text


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=15, pady=15)

# Label
miles = Label(text="Miles", font=("Ariel", 12))
miles.grid(column=2, row=0)
miles.config(padx=15, pady=15)

km = Label(text="Km", font=("Ariel", 12))
km.grid(column=2, row=1)
km.config(padx=15, pady=15)

my_label = Label(text="is equal to", font=("Ariel", 12))
my_label.grid(column=0, row=1)

result = Label(text=" ", font=("Ariel", 12))
result.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


new_button = Button(text="click me, too", command=button_clicked)



# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
