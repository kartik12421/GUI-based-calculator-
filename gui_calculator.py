import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Generate buttons
for row in buttons:
    r = tk.Frame(btn_frame)
    r.pack(expand=True, fill="both")
    for char in row:
        b = tk.Button(r, text=char, font="Arial 18", relief=tk.GROOVE, bd=5)
        b.pack(side=tk.LEFT, expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
