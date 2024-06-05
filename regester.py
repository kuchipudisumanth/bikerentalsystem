from tkinter import *
import tkinter.messagebox
import tkinter.font
import tkinter
from tkinter import *

def regester2():
    root = Tk()
    root.geometry('1000x800')
    root.title("Registration Form")
    def validate():
        name = entry_1.get()
        email = entry_2.get()
        if (name == "" or email == ""):
            tkinter.messagebox.showinfo('Invalid Message Alert', "Fields cannot be left empty!")

        else:
            tkinter.messagebox.showinfo('Success Message', "Successfully registered!")

    label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)

    label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)

    label_2 = Label(root, text="Email", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)

    label_1 = Label(root, text="aadhar", width=20, font=("bold", 10))
    label_1.place(x=80, y=470)

    entry_1 = Entry(root)
    entry_1.place(x=240, y=470)

    label_2 = Label(root, text="Driving licence", width=20, font=("bold", 10))
    label_2.place(x=68, y=330)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=330)

    label_1 = Label(root, text="phone number", width=20, font=("bold", 10))
    label_1.place(x=80, y=380)

    entry_1 = Entry(root)
    entry_1.place(x=240, y=380)

    label_2 = Label(root, text="address", width=20, font=("bold", 10))
    label_2.place(x=68, y=420)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=420)

    label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    var = IntVar()
    Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
    Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
    label_4 = Label(root, text="Country", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];
    c = StringVar()
    droplist = OptionMenu(root, c, *list1)
    droplist.config(width=15)
    c.set('Select your country')
    droplist.place(x=240, y=280)

    label_4 = Label(root, text="agree terms and conditions", width=20, font=("bold", 10))
    label_4.place(x=85, y=520)
    var1 = IntVar()
    Checkbutton(root, text="yes", variable=var1).place(x=235, y=520)

    Button(root, text='Submit', width=20, bg='green', fg='white', command=validate).place(x=230, y=580)

    root.mainloop()
regester2()
