from tkinter import *
r=Tk()
r.geometry("500x500")
def bike1(root):
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")

    def totalbill():
        label_0 = Label(root, text="Instant go", width=20, font=("bold", 30))
        label_0.place(x=0, y=53)

        label_1 = Label(root, text="bike model :   yamaha rtx", width=20, font=("bold", 15))
        label_1.place(x=80, y=130)

        label_2 = Label(root, text="    millage    : 25 km/l", width=20, font=("bold", 15))
        label_2.place(x=68, y=180)

        label_3 = Label(root, text="cost/Hr :  250₹ ", width=20, font=("bold", 15))
        label_3.place(x=68, y=220)

        total = int(entry_2.get()) * 250
        label = Label(root, text="total bill " + str(total), width=20, font=("bold", 15))
        label.place(x=68, y=300)

    label_0 = Label(root, text="Instant go", width=20, font=("Helvetica", 30))
    label_0.place(x=0, y=53)

    label_1 = Label(root, text="bike model :   yamaha rtx", width=20, font=("bold", 15))
    label_1.place(x=80, y=130)

    label_2 = Label(root, text="    millage    : 25 km/l", width=20, font=("bold", 15))
    label_2.place(x=68, y=180)

    label_3 = Label(root, text="cost/Hr :  250₹ ", width=20, font=("bold", 15))
    label_3.place(x=68, y=220)

    label_4 = Label(root, text="no.of hours required ", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=280)

    Button(root, text='BOOK NOW ', width=20, bg='brown', fg='white', command=totalbill).place(x=180, y=330)
    # it is use for display the registration form on the window

    root.mainloop()
    print("registration form  sucessfully created...")
def bike2(root):
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")

    def totalbill():
        label_0 = Label(root, text="Instant go", width=20, font=("bold", 30))
        label_0.place(x=0, y=53)

        label_1 = Label(root, text="bike model :   FZ", width=20, font=("bold", 15))
        label_1.place(x=80, y=130)

        label_2 = Label(root, text="    millage    : 20 km/l", width=20, font=("bold", 15))
        label_2.place(x=68, y=180)

        label_3 = Label(root, text="cost/Hr :  340₹ ", width=20, font=("bold", 15))
        label_3.place(x=68, y=220)

        total = int(entry_2.get()) * 340
        label = Label(root, text="total bill " + str(total), width=20, font=("bold", 15))
        label.place(x=68, y=300)

    label_0 = Label(root, text="Instant go", width=20, font=("Monotype Corsiva", 30))
    label_0.place(x=0, y=53)

    label_1 = Label(root, text="bike model :   FZ SPORTS", width=20, font=("bold", 15))
    label_1.place(x=80, y=130)

    label_2 = Label(root, text="    millage    : 20 km/l", width=20, font=("bold", 15))
    label_2.place(x=68, y=180)

    label_3 = Label(root, text="cost/Hr :  340₹ ", width=20, font=("bold", 15))
    label_3.place(x=68, y=220)

    label_4 = Label(root, text="no.of hours required ", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=280)

    Button(root, text='BOOK NOW ', width=20, bg='brown', fg='white', command=totalbill).place(x=180, y=330)
    # it is use for display the registration form on the window

    root.mainloop()
    print("registration form  sucessfully created...")
def bike3(root):
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")

    def totalbill():
        label_0 = Label(root, text="Instant go", width=20, font=("bold", 30))
        label_0.place(x=0, y=53)

        label_1 = Label(root, text="bike model :   bmw x3", width=20, font=("bold", 15))
        label_1.place(x=80, y=130)

        label_2 = Label(root, text="    millage    : 29 km/l", width=20, font=("bold", 15))
        label_2.place(x=68, y=180)

        label_3 = Label(root, text="cost/Hr :  380₹ ", width=20, font=("bold", 15))
        label_3.place(x=68, y=220)

        total = int(entry_2.get()) * 380
        label = Label(root, text="total bill " + str(total), width=20, font=("bold", 15))
        label.place(x=68, y=300)

    label_0 = Label(root, text="Instant go", width=20, font=("bold", 30))
    label_0.place(x=0, y=53)

    label_1 = Label(root, text="bike model :   bmw x3", width=20, font=("bold", 15))
    label_1.place(x=80, y=130)

    label_2 = Label(root, text="    millage    : 29 km/l", width=20, font=("bold", 15))
    label_2.place(x=68, y=180)

    label_3 = Label(root, text="cost/Hr :  380₹ ", width=20, font=("bold", 15))
    label_3.place(x=68, y=220)

    label_4 = Label(root, text="no.of hours required ", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)

    entry_2 = Entry(root)
    entry_2.place(x=240, y=280)

    Button(root, text='BOOK NOW ', width=20, bg='brown', fg='white', command=totalbill).place(x=180, y=330)
    # it is use for display the registration form on the window

    root.mainloop()
    print("registration form  sucessfully created...")


label_0=Label(r,text="Instant go",font=("Arieal",20)).place(x=55,y=5)
gg=PhotoImage(file="ijk (3).png")
ss=gg.subsample(10,10)
label=Label(r,image=ss,text="Fz bike",compound="left")
label.bind('<Button-1>',bike1)
label.place(x=10,y=55)

gg1=PhotoImage(file="ijk (1).png")
ss1=gg1.subsample(10,10)
label=Label(r,image=ss1,text="R15",font=("Times",10),compound="left")
label.bind('<Button-1>',bike2)
label.place(x=10,y=195)

gg2=PhotoImage(file="ijk (2).png")
ss2=gg2.subsample(10,10)
label=Label(r,image=ss2,text="R15",font=("Times",10),compound="left")
label.bind('<Button-1>',bike3)
label.place(x=10,y=335)

gg2=PhotoImage(file="ijk (2).png")
ss2=gg2.subsample(10,10)
label=Label(r,image=ss2,text="R15",font=("Times",10),compound="left")
label.bind('<Button-1>',bike3)
label.place(x=10,y=335)
r.mainloop()
