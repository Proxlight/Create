# CREATE - A tool that is used to create Modern Gui Using Tkinter

import os
from tkinter import Frame
from tkinter.constants import RADIOBUTTON
import pyfiglet 
title=pyfiglet.figlet_format("C R E A T E")


    



app_name=input("Enter your app name : ")
if app_name == "":
    print("Please enter a valid name !")


f =open(app_name+".py","a+")

f.write('''import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("'''+app_name+'''")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea''')

f.flush()

########################################### Functions ###########################################


def text():
    print("\nADD TEXT :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    Label= input("   Add text here :")
    fg_color= input("   Add foreground colour : ")  
    font=input("   Enter font name : ")
    align=input("   Align text to ( left / right / center ): ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    pady=input("   Add y spacing : ")
    f.write('''
# Label
'''+widget_name+''' = ttk.Label('''+layout+''', text="'''+Label+'''",font="'''+font+'''" ,justify="'''+align+'''",foreground="'''+fg_color+'''")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', pady='''+pady+''', columnspan=2)''')
    print("\nText added successfully !\n")
    f.flush()

def button():
    print("\nSelect Button Style :-")
    print("\n 1. Normal Button")
    print(" 2. Accent Button")
    print(" 3. Toggle button")
    button_type = input("\n   Enter Button Style [1-3] :")
    widget_name=input("   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    text=input("\n   Add text : ")
    row=input("   Add row number :")
    column=input("   Add column number :")
    padx=input("   Add x spacing :")
    pady=input("   Add y spacing :")
    if button_type=="1":
        f.write('''
'''+widget_name+''' = ttk.Button('''+layout+''', text="'''+text+'''")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew")''')
        f.flush()
        print("\nButton added successfully !\n")
    if button_type=="2":
        f.write('''
'''+widget_name+''' = ttk.Button('''+layout+''', text="'''+text+'''",style="AccentButton")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew")''')
        f.flush()
        print("\nButton added successfully !\n")
    if button_type=="3":
        f.write('''
'''+widget_name+''' = ttk.Button('''+layout+''', text="'''+text+'''",style="ToggleButton")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew")''')
        f.flush()
        print("\nButton added successfully !\n")
    
    
def wedget_frame():
    print("\nADD Widget Frame :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    padding=input("   Add spacing (x,y,z,value) : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")
    index=input("   Add index number : ")
    weight=input("   Add border weight :")
    f.write('''
'''+widget_name+''' = ttk.Frame('''+layout+''', padding='''+ padding+''')
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew", rowspan=3)
'''+widget_name+'''.columnconfigure(index='''+index+''', weight='''+weight+''')''')
    print("\nWidget Frame added successfully !\n")
    f.flush()

def entry_box():
    print("\nADD Entry Frame :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    l_text=input("   Add text : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")

    f.write(  '''  
# Entry
'''+widget_name+''' = ttk.Entry('''+layout+''')
'''+widget_name+'''.insert(0, "'''+ l_text +'''")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="ew")''')
    f.flush()
    print("\nEntry added successfully !\n")

def radio_button():
    print("\nADD Radio Button :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    text_radio=input("   Add text here : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")

    f.write(
'''
'''+widget_name+''' = ttk.Radiobutton('''+layout+''', text="'''+text_radio+'''")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew")''')
    f.flush()
    print("\nRadio Button added successfully !\n")
    

def Spinbox():
    print("\nADD Spinbox :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")

    f.write(
'''
'''+widget_name+''' = ttk.Spinbox('''+layout+''', from_=0, to=100, increment=0.1)
'''+widget_name+'''.insert(0, "'''+ text+'''")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="ew")''')

    f.flush()
    print("\nSpinbox added successfully !\n")

def Combobox():
    print("\nADD Combobox :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")

    f.write(
'''
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]

'''+widget_name+''' = ttk.Combobox('''+layout+''',values=combo_list)
'''+widget_name+'''.combobox.current(0)
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="ew")''')
    f.flush()
    print("\nCombobox added successfully !\n")

    
def Switch():
    print("\nADD Switch :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    add_text=input("   Add text here : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")


    f.write(
'''
# Switch
'''+widget_name+''' = ttk.Checkbutton('''+layout+''', text="'''+add_text+'''", style="Switch")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew") ''')
    f.flush()
    print("\nCombobox added successfully !\n")

def frame():
    print("\nADD Frame :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    add_text=input("   Add text here : ")
    padding=input("   Add Spacing : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")


    f.write('''
# Create a Frame 
'''+widget_name+''' = ttk.LabelFrame('''+layout+''', text="'''+add_text+'''", padding='''+padding+''')
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="nsew") ''')
    f.flush()
    print("\nFrame added successfully !\n")

def Slider():
    print("\nADD Slider :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")


    f.write(
'''
g = tk.DoubleVar(value=75.0)
'''+widget_name+''' = ttk.Scale('''+layout+''', from_=100, to=0, variable=g, command=lambda event: g.set('''+widget_name+'''.get()))
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="ew") 
''')
    f.flush()
    print("\nSlider added successfully !\n")

def Progressbar():
    print("\nProgressbar :-")
    widget_name=input("\n   Enter widget name : ")
    layout= input("   Add widget to(root / custom_widget) :")
    value=input("\n   Enter value here : ")
    row=input("   Add row number : ")
    column=input("   Add column number : ")
    padx=input("   Add x spacing (value1,value2) : ")
    pady=input("   Add y spacing (value1,value2) : ")


    f.write(
'''
g = tk.DoubleVar(value=75.0)
'''+widget_name+''' = ttk.Progressbar('''+layout+''', value='''+value+''', variable=g, mode="determinate")
'''+widget_name+'''.grid(row='''+row+''', column='''+column+''', padx='''+padx+''', pady='''+pady+''', sticky="ew")
''')
    f.flush()
    print("\nProgressbar added successfully !\n")


def run():
    f=open(app_name+".py")
    output = []

    for line in f:

        if not "root.mainloop()" in line:

            output.append(line)

    f.close()

    f = open("Run_Demo.py", 'w')

    f.writelines(output)
    f.write('''\nroot.mainloop()''')
    f.flush()
    os.popen("python Run_Demo.py")
    print("Running "+app_name+".py")

def export():
    commands=input("Enter Commands here (--onedir / --console) : ")
    os.popen('''pyinstaller --noconfirm '''+commands+''' --icon "icon.ico" "'''+app_name+'''.py"''')




def image():
    print("\nADD Image (Not supported yet!) ")
    









################################# MAIN APP ####################################################################

app_size = input("Enter size of "+ app_name +" (w x h) : ")

f.write('''
root.geometry("'''+ app_size + '''")''')

f.flush()


app_R= input("Do you want to make "+ app_name +" responsive (y/n) : ")

if app_R=="y":
    f.write('''
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))''')
    f.flush()

if app_R=="n":
    f.write('''
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)'''  )
    f.flush()

app_theme=input("Select theme for "+ app_name +" (dark/light) :")
if app_theme== "dark" :
    f.write('''# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "proxttk-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)''')
else:
    f.write('''# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "proxttk.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk")

d = tk.IntVar(value=2)''')

f.flush()


    
print(
    115*"-"

)
print(title)
     
def print_menu():       ## Your menu design here
    print ("\n",50 * "-" , "Add Widgets" , 50 * "-","\n")
    print ("\n1. Text\n")
    print ("2. Widget Frame\n")
    print ("3. Button\n")
    print ("4. Image\n")
    print ("5. Entry Box\n")
    print ("6. Spinbox\n")
    print ("7. Combobox\n")
    print ("8. Switch\n")
    print ("9. Frame\n")
    print ("10. Slider\n")
    print ("11. Progressbar\n")
    print ("12. Radio Button\n")
    print ("13. Run Final "+app_name+"\n")
    print ("14. Export\n")
    print ("15. Exit\n")
    print ("\n",115 * "-")
 
loop=True 
 
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-15]: ")
    
    if choice=="1":     
        text()
    elif choice=="2":
        wedget_frame()
        
    elif choice=="3":
        button()
        
    elif choice=="4":
        image()

    elif choice=="5":
        entry_box()
        ## You can add your code or functions here
    elif choice=="6":
        Spinbox()
        ## You can add your code or functions here   
    elif choice=="7":
        Combobox()
        ## You can add your code or functions here   
    elif choice=="8":
        Switch()
        ## You can add your code or functions here   
    elif choice=="9":
        frame()
        ## You can add your code or functions here   
    elif choice=="10":
        Slider()
        ## You can add your code or functions here   

    elif choice=="11":
        Progressbar()
        ## You can add your code or functions here   
    elif choice=="12":
        radio_button()
        ## You can add your code or functions here   
    elif choice=="13":
        run()
        ## You can add your code or functions here   
    elif choice=="14":
        export()
        ## You can add your code or functions here   
    elif choice=="15":

        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")
