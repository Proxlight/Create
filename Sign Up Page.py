import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign Up Page")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("1000x600")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style
style = ttk.Style(root)
widgets_frame = ttk.Frame(root, padding=(40,0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
# Import the tcl file
root.tk.call("source", "proxttk-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)
# Label
text1 = ttk.Label(widgets_frame, text="SIGN UP",font="colortube 20",foreground="white")
text1.grid(row=0, column=0, pady=50, columnspan=2)




d = tk.IntVar(value=2)

# Entry
box = ttk.Entry(widgets_frame)
box.insert(0, "")
box.grid(row=2, column=0, padx=200, pady=0, sticky="ew")





# Entry
box2 = ttk.Entry(widgets_frame)
box2.insert(0, "Enter e-mail here...")
box2.grid(row=8, column=0, padx=200, pady=50, sticky="ew")

# Entry
box = ttk.Entry(widgets_frame)
box.insert(0, "Enter name here...")
box.grid(row=2, column=0, padx=200, pady=0, sticky="ew")
a=box.get()
b=box2.get()


 





accentbutton = ttk.Button(widgets_frame, text="SIGN UP", style="AccentButton")
accentbutton.grid(row=10, column=0, padx=300, pady=10, sticky="nsew")
root.mainloop()