# tkinter is used to create gui via python

import tkinter as tk 

calculation = ""
def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)                      #pass statement does nothing (does not execute anything)

def evaluate_to_cal():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")
        
        

def clear_field():
    global calculation
    calculation =""
    text_result.insert(1.0,"end")
      

root = tk.Tk()  #. It helps to display the root window and manages all the other components of the tkinter application.

text_result = tk.Text(root,height=2,width=16,font=("Ariel",24))     # text_result is the variable tkinter uses to store text widget

text_result.grid(columnspan=5)  #we'll have a grid structure with 5 columns in total
 
root.geometry("300x300")


#creating all the number button using tk.button function , all the functions are listed below with their functionality

btn_1 = tk.Button(root, text="1" , command=lambda: add_to_cal(1),width=5,font= ("Ariel", 14))
btn_1.grid(row=4,column=1)

btn_2 = tk.Button(root, text="2" , command=lambda: add_to_cal(2),width=5,font= ("Ariel", 14))
btn_2.grid(row=4,column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_cal(3),width=5,font= ("Ariel", 14 ,)
                  )
btn_3.grid(row=4,column=3)

btn_4 = tk.Button(root, text="4" , command=lambda: add_to_cal(4),width=5,font= ("Ariel", 14))
btn_4.grid(row=3,column=1)

btn_5 = tk.Button(root, text="5" , command=lambda: add_to_cal(5),width=5,font= ("Ariel", 14))
btn_5.grid(row=3,column=2)

btn_6 = tk.Button(root, text="6" , command=lambda: add_to_cal(6),width=5,font= ("Ariel", 14))
btn_6.grid(row=3,column=3)

btn_7 = tk.Button(root, text="7" , command=lambda: add_to_cal(7),width=5,font= ("Ariel", 14))
btn_7.grid(row=2,column=1)

btn_8 = tk.Button(root, text="8" , command=lambda: add_to_cal(8),width=5,font= ("Ariel", 14))
btn_8.grid(row=2,column=2)

btn_9 = tk.Button(root, text="9" , command=lambda: add_to_cal(9),width=5,font= ("Ariel", 14))
btn_9.grid(row=2,column=3)

btn_0 = tk.Button(root, text="0" , command=lambda: add_to_cal(0),width=5,font= ("Ariel", 14))
btn_0.grid(row=5,column=2)

# now creating all the calculation functions buttons

btn_plus = tk.Button(root, text="+" , command=lambda: add_to_cal("+"),width=5,font= ("Ariel", 14))
btn_plus.grid(row=2,column=4)

btn_minus = tk.Button(root, text="-" , command=lambda: add_to_cal("-"),width=5,font= ("Ariel", 14))
btn_minus.grid(row=3,column=4)

btn_multi = tk.Button(root, text="*" , command=lambda: add_to_cal("*"),width=5,font= ("Ariel", 14))
btn_multi.grid(row=4,column=4)

btn_div = tk.Button(root, text="/" , command=lambda: add_to_cal("/"),width=5,font= ("Ariel", 14))
btn_div.grid(row=5,column=4)

# adding parenthesis for basic calculations

btn_open = tk.Button(root, text="(" , command=lambda: add_to_cal("("),width=5,font= ("Ariel", 14))
btn_open.grid(row=5,column=1)

btn_close = tk.Button(root, text=")" , command=lambda: add_to_cal(")"),width=5,font= ("Ariel", 14))
btn_close.grid(row=5,column=3)

# adding equals and clear for basic calculations (Adding them separetly because they call different functions)

btn_equals = tk.Button(root, text="=" , command= evaluate_to_cal,width=11,font= ("Ariel", 14))
btn_equals.grid(row=6,column=3, columnspan=2)

btn_clear = tk.Button(root, text="AC" , command=clear_field,width=11,font= ("Ariel", 14))
btn_clear.grid(row=6,column=1,columnspan=2)


# tk.Button: Creates a button widget.
# root: Refers to the parent window or frame in which the button is placed.
# text=1: The text displayed on the button is "1".
# command=lambda: add_to_cal(1): When the button is clicked, it will call the add_to_cal(1) function, where 1 is passed as an argument.
# width=5: The width of the button is set to 5 units.


root.mainloop()
