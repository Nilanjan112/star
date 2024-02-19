from tkinter import *

# GUI
window = Tk()
window.title("Calculator by Nilanjan..")
window.configure(bg="black")
# Functions
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)

def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        entry.insert(0, f_num / float(second_number))


     
# Calculator Widgets
entry = Entry(window,bg="gray",width=30, bd=9, font=('arial', 13, 'bold'), justify='right')
entry.grid(row=0, column=0, columnspan=4)

button_1 = Button(window, text='1', fg="white", bg="black", width=10, height=2, command=lambda: button_click(1))
button_2 = Button(window, text='2', fg="white", bg="black", width=10, height=2, command=lambda: button_click(2))
button_3 = Button(window, text='3', fg="white", bg="black", width=10, height=2, command=lambda: button_click(3))
button_4 = Button(window, text='4', fg="white", bg="black", width=10, height=2, command=lambda: button_click(4))
button_5 = Button(window, text='5', fg="white", bg="black", width=10, height=2, command=lambda: button_click(5))
button_6 = Button(window, text='6', fg="white", bg="black", width=10, height=2, command=lambda: button_click(6))
button_7 = Button(window, text='7', fg="white", bg="black", width=10, height=2, command=lambda: button_click(7))
button_8 = Button(window, text='8', fg="white", bg="black", width=10, height=2, command=lambda: button_click(8))
button_9 = Button(window, text='9', fg="white", bg="black", width=10, height=2, command=lambda: button_click(9))
button_0 = Button(window, text='0', fg="white", bg="black", width=10, height=2, command=lambda: button_click(0))
button_clear = Button(window, text='C', fg="white", bg="blue", width=10, height=2, command=button_clear)
button_add = Button(window, text='+', fg="white", bg="red", width=10, height=2, command=button_add)
button_sub = Button(window, text='-', fg="white", bg="red", width=10, height=2, command=button_sub)
button_mul = Button(window, text='*', fg="white", bg="red", width=10, height=2, command=button_mul)
button_div = Button(window, text='/', fg="white", bg="red", width=10, height=2, command=button_div)
button_equal = Button(window, text='=', fg="white", bg="green", width=10, height=2, command=button_equal)

# Grid placement for the buttons
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)


button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_div.grid(row=4, column=3)
button_equal.grid(row=4, column=2)


window.mainloop()

 