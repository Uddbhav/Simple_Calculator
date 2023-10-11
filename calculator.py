from tkinter import *
import math
import numpy as np

# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op


tk_calc = Tk()
tk_calc.configure(bg="grey34", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 4, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}


button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=1, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=1, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=1, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'), text='\u232B', 
                    command=button_delete, bg='#db701f').grid(row=1, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='AC', 
                    command=button_clear_all, bg='#db701f').grid(row=1, column=4, sticky="nsew")

button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=2, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=2, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=2, column=2, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='X',
             command=lambda:button_click('*')).grid(row=2, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text="\u00F7",
             command=lambda:button_click('/')).grid(row=2, column=4, sticky="nsew")

button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=3, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=3, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=3, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=3, column=4, sticky="nsew", rowspan=2)
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=3, column=3, sticky="nsew")

button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=4, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=4, column=1, sticky="nsew")
equal = Button(tk_calc, bd=5, fg='#000', bg='green', font=('sans-serif', 20, 'bold'), text='=',
               command=button_equal).grid(row=4, columnspan=2, column=2, sticky="nsew")

tk_calc.mainloop()