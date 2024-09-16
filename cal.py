# tkinter is used to create gui via python

import tkinter as tk 

def add_to_cal(symbol):
    pass                        #pass statement does nothing (does not execute anything)

def evaluate_to_cal():
    pass

def clear_field():
    pass

root = tk.Tk()  #. It helps to display the root window and manages all the other components of the tkinter application.

text_result = tk.Text(root,height=2,width=16,font=("Ariel",24))     # text_result is the variable tkinter uses to store text widget

text_result.grid(columnspan=5)  #we'll have a grid structure with 5 columns in total
 
root.geometry("300x300")
root.mainloop()
