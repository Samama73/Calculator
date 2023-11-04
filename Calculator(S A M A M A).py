import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = str(eval(expression))
        result_label.config(text="Result: " + result)
    except Exception as e:
        result_label.config(text="Error")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])


window = tk.Tk()
window.title("Simple Calculator")


entry = tk.Entry(window)
entry.pack()


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

button_frame = tk.Frame(window)
button_frame.pack()

for button in buttons:
    tk.Button(button_frame, text=button, width=5, height=2, command=lambda b=button: entry.insert('end', b) if b != '=' else calculate()).grid(row=buttons.index(button)//4, column=buttons.index(button)%4)


tk.Button(button_frame, text='Del', width=5, height=2, command=backspace).grid(row=4, column=3)


result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()-0