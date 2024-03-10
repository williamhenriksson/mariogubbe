import tkinter as tk


field_text = ""


def add_to_field(sth):
    global field_text
    field_text = field_text+str(sth)


window = tk.Tk()
window.title("miniräknare")
window.geometry("300x300")
field = tk.Text(window, height=2, width=21, font=("times new roman", 20))
field.grid(row=1, column=1, columnspan=4)
field.delete("1.0", "end")
field.insert("1.0", field_text)


def kalkylera():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)


def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")


def addition(nummer1, nummer2):
    return nummer1 + nummer2


def subtraktion(nummer1, nummer2):
    return nummer1 - nummer2


def division(nummer1, nummer2):
    return nummer1 / nummer2


def multiplikation(nummer1, nummer2):
    return nummer1 * nummer2


def Button(height, width, text, command):
    tk.Button(command=command, height=height, text=text, width=width)


Button(height=10, width=5, text="+", command=addition(nummer1=input(float()),
nummer2=input(float())))

nummer1 = input(float())
nummer2 = input(float())





window.mainloop()