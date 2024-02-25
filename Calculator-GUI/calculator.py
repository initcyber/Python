## This uses tkinter to show a graphical interface for a basic calculator

import tkinter as tk

root = tk.Tk()
root.title("Calculator")

#Define all of the calculations and display them on TKINTER
def addition():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def subtraction():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def multiplication():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def division():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 / num2
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def squareroot():
    num1 = int(entry1.get())
    result = num1 ** 0.5
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def power():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 ** num2
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def numberTimesPi():
    num1 = int(entry1.get())
    result = num1 * 3.14
    entry3.delete(0, tk.END)
    entry3.insert(0, result)

def factorial():
    num1 = int(entry1.get())
    result = 1
    for i in range(1, num1 + 1):
        result *= i
    entry3.delete(0, tk.END)
    entry3.insert(0, result)


#Define the GUI
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Result:")
label3.grid(row=2, column=0)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

button1 = tk.Button(root, text="Add", command=addition)
button1.grid(row=3, column=0)

button2 = tk.Button(root, text="Subtract", command=subtraction)
button2.grid(row=3, column=1)

button3 = tk.Button(root, text="Multiply", command=multiplication)
button3.grid(row=4, column=0)

button4 = tk.Button(root, text="Divide", command=division)
button4.grid(row=4, column=1)

button5 = tk.Button(root, text="Square Root of Number 1", command=squareroot)
button5.grid(row=5, column=0)

button6 = tk.Button(root, text="Power of Number 1 and Number 2", command=power)
button6.grid(row=5, column=1)

button7 = tk.Button(root, text="Number 1 times Pi", command=numberTimesPi)
button7.grid(row=6, column=0)

button8 = tk.Button(root, text="Factorial of Number 1", command=factorial)
button8.grid(row=6, column=1)

root.mainloop()
