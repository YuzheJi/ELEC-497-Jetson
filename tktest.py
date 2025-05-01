import tkinter as tk

def button_handle():
    label.config(text="hello world")

root = tk.Tk()
root.geometry("1200x700+100+50")
root.title("Tk Test")

label = tk.Label(root, text="hello world")
label.pack(padx=10)
button = tk.Button(root,text="this is a button", command=button_handle)
button.pack(pady=10)

root.mainloop()