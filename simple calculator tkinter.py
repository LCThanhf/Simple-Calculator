import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Simple Calculator")
app.geometry("250x350")
app.config(bg="#000000")

font1 = ('Arial', 20, 'bold')

i = 0
equation = ""

def show(value):
    global i, equation
    if value == "%":
        value = "/100"
    equation += value
    result_entry.insert(i, value)
    i += len(value)

def clear():
    global equation, i
    result_entry.delete(0, END)
    equation = ""
    i = 0

def calculate():
    global equation
    try:
        result = eval(equation)
        clear()
        result_entry.insert(0, result)
    except:
        messagebox.showerror(title="Error", message="Please enter a valid number")

result_entry = customtkinter.CTkEntry(app, font=font1, width=250, fg_color="#FFFFFF", bg_color="#000000", border_color="#000000")
result_entry.place(x=0, y=10)

button_data = [
    ("C", clear, 10, 60, 50, 2, "#b5520b", "#b5520b"),
    ("%", lambda: show("%"), 70, 60, 50, 2, "#b5520b", "#b5520b"),
    ("/", lambda: show("/"), 130, 60, 50, 2, "#b5520b", "#b5520b"),
    ("*", lambda: show("*"), 190, 60, 50, 2, "#b5520b", "#b5520b"),
    ("7", lambda: show("7"), 10, 120, 50, 2, "#2a2a27", "#2a2a27"),
    ("8", lambda: show("8"), 70, 120, 50, 2, "#2a2a27", "#2a2a27"),
    ("9", lambda: show("9"), 130, 120, 50, 2, "#2a2a27", "#2a2a27"),
    ("+", lambda: show("+"), 190, 120, 50, 2, "#b5520b", "#b5520b"),
    ("4", lambda: show("4"), 10, 180, 50, 2, "#2a2a27", "#2a2a27"),
    ("5", lambda: show("5"), 70, 180, 50, 2, "#2a2a27", "#2a2a27"),
    ("6", lambda: show("6"), 130, 180, 50, 2, "#2a2a27", "#2a2a27"),
    ("-", lambda: show("-"), 190, 180, 50, 2, "#b5520b", "#b5520b"),
    ("0", lambda: show("0"), 10, 240, 50, 2, "#2a2a27", "#2a2a27"),
    ("1", lambda: show("1"), 70, 240, 50, 2, "#2a2a27", "#2a2a27"),
    ("2", lambda: show("2"), 130, 240, 50, 2, "#2a2a27", "#2a2a27"),
    ("3", lambda: show("3"), 190, 240, 50, 2, "#2a2a27", "#2a2a27"),
    (".", lambda: show("."), 10, 300, 50, 2, "#2a2a27", "#2a2a27"),
    ("=", calculate, 70, 300, 170, 2, "#b5520b", "#b5520b"),
]

for text, command, x, y, width, height, fg_color, hover_color in button_data:
    btn = customtkinter.CTkButton(app, command=command, text=text, font=font1, width=width, height=height, fg_color=fg_color, hover_color=hover_color)
    btn.place(x=x, y=y)

# Thiết lập văn bản mặc định
result_entry.insert(0, " ")

app.mainloop()
