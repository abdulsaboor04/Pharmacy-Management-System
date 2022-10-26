import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3


def Database():
    global conn, cursor
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (productID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, productNAME TEXT, Quantity TEXT, Price TEXT)")
    conn.commit()

class features:

    def AddPoduct(self):
        Database()
        try:
            cursor.execute("INSERT INTO `product` (productID, productNAME, Quantity, Price) VALUES(?, ?, ?,?)",(ID.get(), pName.get(),quantity.get(),price.get()))
        except sqlite3.IntegrityError:
            tk.messagebox.showerror("Error","Please fill the required fields.")
        conn.commit()
        cursor.close()
        conn.close()

    def delProduct(self):
        Database()
        query = "DELETE FROM `product` WHERE `productID` = ?"
        try:
            cursor.execute(query, (delID.get()))
        except sqlite3.ProgrammingError:
            tk.messagebox.showerror("Error", "Please fill the required field")
        conn.commit()
        cursor.close()
        conn.close()

    def modifyProduct(self):
        Database()
        if modID.get()=="":
            tk.messagebox.showerror("Error","Enter Product ID")
        elif (modQuantity.get()=="") or (modPrice.get()==""):
            tk.messagebox.showerror("Error","Please fill the required fields")
        else:
            cursor.execute("UPDATE product SET Quantity =:x , Price=:y WHERE productID=:z",{'x':modQuantity.get(),
                                                                                           'y':modPrice.get(),
                                                                                           'z':modID.get()})
        conn.commit()
        cursor.close()
        conn.close()

    def logout(self):
        main.destroy()
        gui.loginGUI()

    def viewInv(self):
        Database()
        cursor.execute("SELECT * FROM `product`")
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def back(self):
        main.destroy()
        gui.MainGUI()

FEATURES=features()

class Admins:

    def createAdmin(self):
        UserName = Username.get()
        password = Password.get()
        name = Name.get()
        email = Email.get()

        infile = open("UserID.txt", 'r+')
        content = infile.read()
        listofidpw = content.split()
        if UserName in listofidpw:
            tk.messagebox.showerror("Error", "User Already Exist")
        elif (UserName == "") or (password == "") or (name == "") or (email == ""):
            tk.messagebox.showerror("Error", "Please fill all the fields")


        else:
            infile = open('UserID.txt', 'r+')
            content = infile.read()
            infile.write(" {0} {1}".format(UserName, password))
            tk.messagebox.showinfo("Success", "Customer Registered Successfully")
            infile.close()

    def loginAdmin(self):

        uname = Entry1.get()
        pwd = Entry2.get()

        global User, pwindex
        for i in range(3000):
            infile = open("UserID.txt", 'r+')
            content = infile.read()
            listofidpw = content.split()

            if uname not in listofidpw:
                tk.messagebox.showinfo("Error", "This username does not exist.")
                break
            else:
                pwindex = listofidpw.index(uname) + 1

            if listofidpw[pwindex] == pwd:
                User = uname
                tk.messagebox.showinfo("Login", "Logged In Successfully")
                main.destroy()
                gui.MainGUI()

                break
            else:
                tk.messagebox.showinfo("Error", "Access denied, Invalid Password/Username")
                break

ADMIN = Admins()


class GUI:
    def loginGUI(self):

        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        font10 = "-family {Segoe UI} -size 21 -weight bold"
        font11 = "-family {Segoe UI} -size 12 -weight bold"
        font12 = "-family {Segoe UI} -size 11 -weight bold"

        global Entry1,Entry2,Username,Password,Name,Email,main

        main= Tk()
        main.geometry("788x679+409+121")
        main.resizable(0, 0)
        main.title("Login Page")
        main.configure(background="#4b57e2")

        Frame1 = tk.Frame(main)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.237, relwidth=0.997)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#d9d9d9")

        Frame2 = tk.Frame(main)
        Frame2.place(relx=0.0, rely=0.25, relheight=0.342, relwidth=0.997)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")

        Entry1 = tk.Entry(Frame2)
        Entry1.place(relx=0.394, rely=0.319,height=30, relwidth=0.183)
        Entry1.configure(background="white")
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")

        Entry2 = tk.Entry(Frame2)
        Entry2 .place(relx=0.394, rely=0.517,height=30, relwidth=0.183)
        Entry2 .configure(background="white")
        Entry2 .configure(font="TkFixedFont")
        Entry2 .configure(foreground="#000000")
        Entry2.configure(show="*")

        Label1 = tk.Label(Frame2)
        Label1.place(relx=0.267, rely=0.302, height=28, width=94)
        Label1.configure(background="#d9d9d9")
        Label1.configure(font=font12)
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Username''')

        Label2 = tk.Label(Frame2)
        Label2.place(relx=0.267, rely=0.517, height=27, width=94)
        Label2.configure(background="#d9d9d9")
        Label2.configure(font=font12)
        Label2.configure(foreground="#000000")
        Label2.configure(text='''Password''')

        Label3 = tk.Label(Frame2)
        Label3.place(relx=0.293, rely=0.039, height=45, width=283)
        Label3.configure(background="#d9d9d9")
        Label3.configure(font=font10)
        Label3.configure(foreground="#000000")
        Label3.configure(text='''LOGIN''')

        Button1 = tk.Button(Frame2,command=ADMIN.loginAdmin)
        Button1.place(relx=0.433, rely=0.677, height=35, width=87)
        Button1.configure(background="#4b57e2")
        Button1.configure(font=font11)
        Button1.configure(foreground="#ffffff")
        Button1.configure(text='''Login''')

        Frame3 = tk.Frame(main)
        Frame3.place(relx=0.0, rely=0.604, relheight=0.398, relwidth=0.997)
        Frame3.configure(relief='groove')
        Frame3.configure(borderwidth="2")
        Frame3.configure(relief="groove")
        Frame3.configure(background="#d9d9d9")

        Label4 = tk.Label(Frame3)
        Label4.place(relx=0.293, rely=0.041, height=53, width=283)
        Label4.configure(background="#d9d9d9")
        Label4.configure(font=font10)
        Label4.configure(foreground="#000000")
        Label4.configure(text='''SIGN UP''')

        Name = tk.Entry(Frame3)
        Name.place(relx=0.178, rely=0.333,height=30, relwidth=0.196)
        Name.configure(background="white")
        Name.configure(font="TkFixedFont")
        Name.configure(foreground="#000000")

        Username = tk.Entry(Frame3)
        Username.place(relx=0.598, rely=0.333,height=30, relwidth=0.196)
        Username.configure(background="white")
        Username.configure(font="TkFixedFont")
        Username.configure(foreground="#000000")

        Email = tk.Entry(Frame3)
        Email.place(relx=0.178, rely=0.593,height=30, relwidth=0.196)
        Email.configure(background="white")
        Email.configure(font="TkFixedFont")
        Email.configure(foreground="#000000")

        Password = tk.Entry(Frame3)
        Password.place(relx=0.598, rely=0.593,height=30, relwidth=0.196)
        Password.configure(background="white")
        Password.configure(font="TkFixedFont")
        Password.configure(foreground="#000000")

        Button2 = tk.Button(Frame3,command=ADMIN.createAdmin)
        Button2.place(relx=0.40, rely=0.800, height=35, width=107)
        Button2.configure(background="#3744df")
        Button2.configure(font=font11)
        Button2.configure(foreground="#ffffff")
        Button2.configure(text='''Sign up''')

        Label5 = tk.Label(Frame3)
        Label5.place(relx=0.064, rely=0.333, height=31, width=84)
        Label5.configure(background="#d9d9d9")
        Label5.configure(font=font12)
        Label5.configure(foreground="#000000")
        Label5.configure(text='''Name''')

        Label6 = tk.Label(Frame3)
        Label6.place(relx=0.064, rely=0.593, height=31, width=84)
        Label6.configure(background="#d9d9d9")
        Label6.configure(font=font12)
        Label6.configure(foreground="#000000")
        Label6.configure(text='''Email''')

        Label7 = tk.Label(Frame3)
        Label7.place(relx=0.483, rely=0.333, height=31, width=84)
        Label7.configure(background="#d9d9d9")
        Label7.configure(font=font12)
        Label7.configure(foreground="#000000")
        Label7.configure(text='''Username''')

        Label8 = tk.Label(Frame3)
        Label8.place(relx=0.483, rely=0.593, height=31, width=84)
        Label8.configure(background="#d9d9d9")
        Label8.configure(font=font12)
        Label8.configure(foreground="#000000")
        Label8.configure(text='''Password''')

        icon = PhotoImage(file="logo.png")
        logo = Label(Frame1, image=icon)
        logo.pack()
        main.mainloop()

    def MainGUI(self):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        font10 = "-family {Segoe UI} -size 24 -weight bold"
        font12 = "-family {Segoe UI} -size 16 -weight bold"
        font13 = "-family {Segoe UI} -size 12 -weight bold"
        font14 = "-family {Segoe UI} -size 14 -weight bold"
        font15 = "-family {Segoe UI} -size 15 -weight bold"

        global main,ID,pName,quantity,price,delID,modQuantity,modPrice,modID

        main = Tk()
        main.geometry("953x696+335+75")
        main.resizable(0, 0)
        main.title("Main Page")
        main.configure(background="#4a4aff")

        Frame1 = tk.Frame(main)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.273, relwidth=1.004)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#d9d9d9")

        Frame2 = tk.Frame(main)
        Frame2.place(relx=0.0, rely=0.532, relheight=0.385, relwidth=0.325)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")

        ID = tk.Entry(Frame2)
        ID.place(relx=0.419, rely=0.101, height=30, relwidth=0.432)
        ID.configure(background="white")
        ID.configure(font="TkFixedFont")
        ID.configure(foreground="#000000")

        pName = tk.Entry(Frame2)
        pName.place(relx=0.419, rely=0.269, height=30, relwidth=0.432)
        pName.configure(background="white")
        pName.configure(font="TkFixedFont")
        pName.configure(foreground="#000000")

        price = tk.Entry(Frame2)
        price.place(relx=0.419, rely=0.44, height=30, relwidth=0.432)
        price.configure(background="white")
        price.configure(font="TkFixedFont")
        price.configure(foreground="#000000")

        quantity = tk.Spinbox(Frame2, from_=1.0, to=100.0)
        quantity.place(relx=0.419, rely=0.608, relheight=0.101, relwidth=0.177)
        quantity.configure(background="white")
        quantity.configure(font="TkDefaultFont")
        quantity.configure(foreground="black")

        Label1 = tk.Label(Frame2)
        Label1.place(relx=0.097, rely=0.101, height=28, width=94)
        Label1.configure(background="#d9d9d9")
        Label1.configure(font=font13)
        Label1.configure(foreground="#000000")
        Label1.configure(text='''ID''')

        Label2 = tk.Label(Frame2)
        Label2.place(relx=0.097, rely=0.261, height=28, width=94)
        Label2.configure(background="#d9d9d9")
        Label2.configure(font=font13)
        Label2.configure(foreground="#000000")
        Label2.configure(text='''Name''')

        Label3 = tk.Label(Frame2)
        Label3.place(relx=0.097, rely=0.44, height=28, width=94)
        Label3.configure(background="#d9d9d9")
        Label3.configure(font=font13)
        Label3.configure(foreground="#000000")
        Label3.configure(text='''Price''')

        Label4 = tk.Label(Frame2)
        Label4.place(relx=0.097, rely=0.608, height=28, width=94)
        Label4.configure(background="#d9d9d9")
        Label4.configure(font=font13)
        Label4.configure(foreground="#000000")
        Label4.configure(text='''Quantity''')

        Button1 = tk.Button(Frame2,command=FEATURES.AddPoduct)
        Button1.place(relx=0.258, rely=0.81, height=34, width=177)
        Button1.configure(background="#4a4aff")
        Button1.configure(font=font14)
        Button1.configure(foreground="#ffffff")
        Button1.configure(text='''Add''')

        Frame3 = tk.Frame(main)
        Frame3.place(relx=0.336, rely=0.532, relheight=0.384
                     , relwidth=0.325)
        Frame3.configure(relief='groove')
        Frame3.configure(borderwidth="2")
        Frame3.configure(relief="groove")
        Frame3.configure(background="#d9d9d9")

        delID = tk.Entry(Frame3)
        delID.place(relx=0.355, rely=0.371, height=30, relwidth=0.561)
        delID.configure(background="white")
        delID.configure(font="TkFixedFont")
        delID.configure(foreground="#000000")
        delID.configure(state="normal")

        Label5 = tk.Label(Frame3)
        Label5.place(relx=0.032, rely=0.375, height=28, width=94)
        Label5.configure(background="#d9d9d9")
        Label5.configure(font=font13)
        Label5.configure(foreground="#000000")
        Label5.configure(text='''ID''')

        Button2 = tk.Button(Frame3,command=FEATURES.delProduct)
        Button2.place(relx=0.226, rely=0.813, height=34, width=177)
        Button2.configure(background="#4a4aff")
        Button2.configure(font=font15)
        Button2.configure(foreground="#ffffff")
        Button2.configure(text='''Delete''')

        Frame4 = tk.Frame(main)
        Frame4.place(relx=0.672, rely=0.532, relheight=0.385
                     , relwidth=0.325)
        Frame4.configure(relief='groove')
        Frame4.configure(borderwidth="2")
        Frame4.configure(relief="groove")
        Frame4.configure(background="#d9d9d9")

        modID = tk.Entry(Frame4)
        modID.place(relx=0.419, rely=0.168, height=30, relwidth=0.432)
        modID.configure(background="white")
        modID.configure(font="TkFixedFont")
        modID.configure(foreground="#000000")

        modPrice = tk.Entry(Frame4)
        modPrice.place(relx=0.419, rely=0.34, height=30, relwidth=0.432)
        modPrice.configure(background="white")
        modPrice.configure(font="TkFixedFont")
        modPrice.configure(foreground="#000000")

        modQuantity = tk.Spinbox(Frame4, from_=1.0, to=100.0)
        modQuantity.place(relx=0.419, rely=0.507, relheight=0.101, relwidth=0.21)
        modQuantity.configure(background="white")
        modQuantity.configure(font="TkDefaultFont")
        modQuantity.configure(foreground="black")

        Label6 = tk.Label(Frame4)
        Label6.place(relx=0.097, rely=0.168, height=28, width=97)
        Label6.configure(background="#d9d9d9")
        Label6.configure(font=font13)
        Label6.configure(foreground="#000000")
        Label6.configure(text='''ID''')

        Label7 = tk.Label(Frame4)
        Label7.place(relx=0.097, rely=0.34, height=28, width=94)
        Label7.configure(background="#d9d9d9")
        Label7.configure(font=font13)
        Label7.configure(foreground="#000000")
        Label7.configure(text='''Set Price''')

        Label8 = tk.Label(Frame4)
        Label8.place(relx=0.065, rely=0.522, height=28, width=111)
        Label8.configure(background="#d9d9d9")
        Label8.configure(font=font13)
        Label8.configure(foreground="#000000")
        Label8.configure(text='''Set Quantity''')

        Button3 = tk.Button(Frame4,command=FEATURES.modifyProduct)
        Button3.place(relx=0.194, rely=0.81, height=34, width=177)
        Button3.configure(background="#4a4aff")
        Button3.configure(font=font15)
        Button3.configure(foreground="#ffffff")
        Button3.configure(text='''Modify''')

        Label9 = tk.Label(main)
        Label9.place(relx=0.063, rely=0.481, height=34, width=184)
        Label9.configure(background="#4a4aff")
        Label9.configure(disabledforeground="#a3a3a3")
        Label9.configure(font=font12)
        Label9.configure(foreground="#ffffff")
        Label9.configure(text='''Add Product''')

        Label10 = tk.Label(main)
        Label10.place(relx=0.388, rely=0.481, height=34, width=207)
        Label10.configure(background="#4a4aff")
        Label10.configure(font=font12)
        Label10.configure(foreground="#ffffff")
        Label10.configure(text='''Delete Product''')

        Label11 = tk.Label(main)
        Label11.place(relx=0.724, rely=0.481, height=34, width=221)
        Label11.configure(background="#4a4aff")
        Label11.configure(font=font12)
        Label11.configure(foreground="#ffffff")
        Label11.configure(text='''Modify Product''')

        Label12 = tk.Label(main)
        Label12.place(relx=0.031, rely=0.287, height=80, width=913)
        Label12.configure(background="#4a4aff")
        Label12.configure(font=font10)
        Label12.configure(foreground="#ffffff")
        Label12.configure(text='''INVENTORY SYSTEM''')

        Button4 = tk.Button(main,command=lambda:[main.destroy(),gui.invGUI()])
        Button4.place(relx=0.388, rely=0.92, height=44, width=227)
        Button4.configure(background="#4a4aff")
        Button4.configure(borderwidth="10")
        Button4.configure(font=font12)
        Button4.configure(foreground="#ffffff")
        Button4.configure(overrelief="raised")
        Button4.configure(relief="groove")
        Button4.configure(text='''Show Inventory''')

        Button5 = tk.Button(main,command=FEATURES.logout)
        Button5.place(relx=0.01, rely=0.92, height=44, width=117)
        Button5.configure(background="#4a4aff")
        Button5.configure(borderwidth="10")
        Button5.configure(font=font12)
        Button5.configure(foreground="#ffffff")
        Button5.configure(relief="groove")
        Button5.configure(overrelief="raised")
        Button5.configure(text='''Sign Out''')

        TSeparator1 = ttk.Separator(main)
        TSeparator1.place(relx=0.0, rely=0.431, relwidth=0.997)

        icon = PhotoImage(file="logo1.png")
        logo = Label(Frame1, image=icon)
        logo.pack()

        main.mainloop()

    def invGUI(self):

        global tree,main
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        main = Tk()
        main.geometry("580x659+498+118")
        main.resizable(0, 0)
        main.title("Inventory")
        main.configure(background="#5555ff")


        Frame1 = tk.Frame(main)
        Frame1.place(relx=0.0, rely=0.0, relheight=0.25, relwidth=0.998)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief="groove")
        Frame1.configure(background="#d9d9d9")
        Frame1.configure(highlightbackground="#d9d9d9")
        Frame1.configure(highlightcolor="black")

        Label1 = tk.Label(main)
        Label1.place(relx=0.017, rely=0.258, height=51, width=554)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(activeforeground="black")
        Label1.configure(background="#5555ff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font="-family {Segoe UI} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        Label1.configure(foreground="#ffffff")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        Label1.configure(text='''INVENTORY''')

        Button1 = tk.Button(main,command=FEATURES.back)
        Button1.place(relx=0.017, rely=0.941, height=34, width=117)
        Button1.configure(background="#5555ff")
        Button1.configure(borderwidth="7")
        Button1.configure(font="-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
        Button1.configure(foreground="#ffffff")
        Button1.configure(overrelief="raised")
        Button1.configure(relief="groove")
        Button1.configure(text='''Back''')

        tree = ttk.Treeview(main, columns=("ProductID", "Product Name", "Product Qty", "Product Price"),
                            selectmode="extended", height=18)

        tree.heading('ProductID', text="ProductID", anchor=W)
        tree.heading('Product Name', text="Product Name", anchor=W)
        tree.heading('Product Qty', text="Product Qty", anchor=W)
        tree.heading('Product Price', text="Product Price", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=205)
        tree.column('#3', stretch=NO, minwidth=0, width=125)
        tree.column('#4', stretch=NO, minwidth=0, width=125)
        tree.place(x=3, y=220)
        FEATURES.viewInv()

        icon = PhotoImage(file="logo2.png")
        logo = Label(Frame1, image=icon)
        logo.pack()

        main.mainloop()
gui=GUI()
gui.loginGUI()




