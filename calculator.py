from tkinter import *

# basic window of app for settings
brick = Tk()

# size of window

brick.geometry("298x210")
brick.title("Calculator")
# config for making changes as background

brick.config(background="Skyblue")

expression = ""

output = StringVar()

# small rectangle window for values => integers => input from user
user_field_input = Entry(textvariable=output)
user_field_input.grid(columnspan=4, ipadx=87, ipady=12)


# function for showing number in small window after clicking button
def button_number(number):
    global expression
    expression += str(number)
    output.set(expression)


# function for equal button
def equal_button():
    try:
        global expression
        total = str(eval(expression))
        output.set(total)
        expression = total
    except:
        output.set('There is error')
        expression = ""


def clear():
    global expression
    expression = ""
    output.set("")


# buttons from 1 to 0
button_1 = Button(text="1", height=2, width=9, command=lambda: button_number(1))
button_1.config(background='Yellow')
button_1.grid(row=3, column=0)

button_2 = Button(text="2", height=2, width=9, command=lambda: button_number(2))
button_2.config(background='Pink')
button_2.grid(row=3, column=1)

button_3 = Button(text="3", height=2, width=9, command=lambda: button_number(3))
button_3.config(background='Yellow')
button_3.grid(row=3, column=2)

button_4 = Button(text="4", height=2, width=9, command=lambda: button_number(4))
button_4.config(background='Pink')
button_4.grid(row=3, column=3)

button_5 = Button(text="5", height=2, width=9, command=lambda: button_number(5))
button_5.config(background='Pink')
button_5.grid(row=4, column=0)

button_6 = Button(text="6", height=2, width=9, command=lambda: button_number(6))
button_6.config(background='Yellow')
button_6.grid(row=4, column=1)

button_7 = Button(text="7", height=2, width=9, command=lambda: button_number(7))
button_7.config(background='Pink')
button_7.grid(row=4, column=2)

button_8 = Button(text="8", height=2, width=9, command=lambda: button_number(8))
button_8.config(background='Yellow')
button_8.grid(row=4, column=3)

button_9 = Button(text="9", height=2, width=9, command=lambda: button_number(9))
button_9.config(background='Yellow')
button_9.grid(row=5, column=0)

button_0 = Button(text="0", height=2, width=9, command=lambda: button_number(0))
button_0.config(background='Pink')
button_0.grid(row=5, column=1)

# symbols +, -
button_plus = Button(text="+", height=2, width=9, command=lambda: button_number('+'))
button_plus.config(background='Yellow')
button_plus.grid(row=5, column=2)

button_minus = Button(text="-", height=2, width=9, command=lambda: button_number('-'))
button_minus.config(background='Pink')
button_minus.grid(row=5, column=3)

button_multiply = Button(text="*", height=2, width=9, command=lambda: button_number('*'))
button_multiply.config(background='Pink')
button_multiply.grid(row=7, column=0)

button_divide = Button(text="/", height=2, width=9, command=lambda: button_number('/'))
button_divide.config(background='Yellow')
button_divide.grid(row=7, column=1)

button_equal = Button(text="=", height=2, width=9, command=equal_button)
button_equal.config(background='Pink')
button_equal.grid(row=7, column=2)

button_clear = Button(text="C", height=2, width=9, command=clear)
button_clear.config(background='Yellow')
button_clear.grid(row=7, column=3)

brick.mainloop()
