from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import mysql.connector

#copyright Rohan Prakash created on 27-10-2020


mydb = mysql.connector.connect(
    host="localhost",
    user="your username",
    password="your password",

)

mycursor = mydb.cursor()

try :
    mycursor.execute("CREATE DATABASE xperia")
except:
    pass

try:
    mycursor.execute("CREATE TABLE usersystem (name VARCHAR(255), password VARCHAR(255))")
except:
    pass


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.config(bg="#7f9194")
    register_screen.geometry("700x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter your details below", font=('bold', 15)).pack()

    frame = Frame(register_screen, bg='#c6eb34', width=1900, height=500)
    frame.pack()

    lframe1 = LabelFrame(frame, width=250, height=150, font=('arial', 20, 'bold'), relief='ridge', bg='#c6eb34',
                         bd=27)
    lframe1.grid(row=1, column=0)

    lframe2 = LabelFrame(frame, width=130, height=100, font=('arial', 20, 'bold'), relief='ridge', bg='#c6eb34',
                         bd=27)
    lframe2.grid(row=2, column=0)

    my_img2 = Image.open("user_logo.png")
    my_img2 = my_img2.resize((30, 30), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(my_img2)
    my_label1 = Label(lframe1, image=my_img2)
    my_label1.image = my_img2
    my_label1.grid(row=1, column=0, padx=20, pady=10)

    username_entry = Entry(lframe1, textvariable=username, font=('bold'), width=40)
    username_entry.grid(row=1, column=1, padx=20, pady=10)

    my_img3 = Image.open("password_logo.png")
    my_img3 = my_img3.resize((20, 20), Image.ANTIALIAS)
    my_img3 = ImageTk.PhotoImage(my_img3)
    my_label2 = Label(lframe1, image=my_img3)
    my_label2.image = my_img3
    my_label2.grid(row=2, column=0, padx=20, pady=20)

    password_entry = Entry(lframe1, textvariable=password, font=('bold'), show='*', width=40)
    password_entry.grid(row=2, column=1, padx=20, pady=20)

    Button(lframe2, text="Register", width=10,font='bold', height=1, bg="#49eb34", command=register_the_user).grid(row=10,
                                                                                                       column=10)
    Button(lframe2, text="Reset", width=10, height=1, font='bold', bg="#49eb34", command=reset).grid(row=10, column=11)


# registering user _______________________
def register_the_user():
    username_input = username.get()
    password_input = password.get()

    if (username_input == '' or password_input == ''):
        register_screen.destroy()
        messagebox.showerror("showerror", "Given fields can't be empty")
        register()


    else:
        messagebox.showinfo("register","Register Success")

        try:

            sql = "INSERT INTO usersystem (name, password) VALUES (%s, %s)"
            val = (username_input, password_input)
            mycursor.execute(sql, val)
            print("Value inserted")

            mydb.commit()
        except:

            sql = "INSERT INTO usersystem (name, password) VALUES (%s, %s)"
            val = (username.get(), password.get())
            mycursor.execute(sql, val)

            mydb.commit()
            print("VAlue inserted")
        register_screen.destroy()
        login()




# destroying the register screen
###### registration complete----------------------------------------------------

# login of user----------------------------------------------------------------
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Register")
    login_screen.config(bg="#7f9194")
    login_screen.geometry("700x500")

    global user_verification
    global password_verification
    global username_entry_login
    global password_entry_login
    user_verification = StringVar()
    password_verification = StringVar()

    Label(login_screen, text="Enter your details below", font=('bold', 15)).pack()

    frame = Frame(login_screen, bg='#c6eb34', width=1900, height=500)
    frame.pack()

    lframe1 = LabelFrame(frame, width=250, height=150, font=('arial', 20, 'bold'), relief='ridge', bg='#c6eb34',
                         bd=40)
    lframe1.grid(row=1, column=0)

    lframe2 = LabelFrame(frame, width=130, height=100, font=('arial', 20, 'bold'), relief='ridge', bg='#c6eb34',
                         bd=40)
    lframe2.grid(row=2, column=0)

    my_img2 = Image.open("user_logo.png")
    my_img2 = my_img2.resize((30, 30), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(my_img2)
    my_label1 = Label(lframe1, image=my_img2)
    my_label1.image = my_img2
    my_label1.grid(row=1, column=0, padx=20, pady=10)

    username_entry_login = Entry(lframe1, textvariable=user_verification, font=('bold'), width=40)
    username_entry_login.grid(row=1, column=1, padx=20, pady=10)

    my_img3 = Image.open("password_logo.png")
    my_img3 = my_img3.resize((20, 20), Image.ANTIALIAS)
    my_img3 = ImageTk.PhotoImage(my_img3)
    my_label2 = Label(lframe1, image=my_img3)
    my_label2.image = my_img3
    my_label2.grid(row=2, column=0, padx=20, pady=20)

    password_entry_login = Entry(lframe1, textvariable=password_verification, font=('bold'), show='*', width=40)
    password_entry_login.grid(row=2, column=1, padx=20, pady=20)

    Button(lframe2, text="Login",font='bold', width=10, height=1, bg="#49eb34", command=verify_the_user).grid(row=10, column=10)
    Button(lframe2, text="Reset", width=10, font='bold',height=1, bg="#49eb34", command=reset2).grid(row=10, column=11)


# --------------------------------------------------------------------------------

def reset2():
    password_verification.set('')
    user_verification.set('')

def verify_the_user():
    username_1 = user_verification.get()
    password_1 = password_verification.get()

    cmd = "SELECT * FROM usersystem WHERE name='" + username_1 + "' AND password='" + password_1 + "'"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    print(result)
    if (result == []):
        password_wrong()
    else:
        messagebox.showinfo("success", "login success")
        login_sucess()

    return


def password_wrong():
    login_screen.destroy()
    messagebox.showerror("error", "wrong password/username")
    login()


def login_sucess():

    main_home_page()


def reset():
    username.set('')
    password.set('')


# -----------------------------------------------------------------------------------------------------------------------
# Main Homepage
# -----------------------------------------------------------------------------------------------------------------------

def main_home_page():
    global root

    root = Toplevel(main_screen)
    root.geometry('1100x700')
    root.config(bg='#add957')

    frame = Frame(root, bg='#b1ba9e')
    frame.grid(row=0, column=0)
    fram = Frame(root, bg='#add957')
    fram.grid(row=0, column=1)

    # -----------------
    lframe1 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe1.grid(row=0, column=0)
    lframe2 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe2.grid(row=1, column=0)

    lframe3 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe3.grid(row=2, column=0)

    lframe4 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe4.grid(row=3, column=0)
    lframe5 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe5.grid(row=4, column=0)

    lframe6 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe6.grid(row=5, column=0)

    lframe7 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe7.grid(row=6, column=0)

    lframe8 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe8.grid(row=7, column=0)

    lframe9 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe9.grid(row=8, column=0)

    lframe10 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe10.grid(row=0, column=1)
    lframe11 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe11.grid(row=1, column=1)

    lframe12 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe12.grid(row=2, column=1)

    lframe13 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe13.grid(row=3, column=1)

    lframe14 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe14.grid(row=4, column=1)

    lframe15 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe15.grid(row=5, column=1)

    lframe16 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe16.grid(row=6, column=1)

    lframe17 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe17.grid(row=7, column=1)

    lframe18 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe18.grid(row=8, column=1)

    lframe181 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=100)
    lframe181.grid(row=0, column=2)

    lframe19 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe19.grid(row=1, column=2)

    lframe20 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe20.grid(row=2, column=2)

    lframe21 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe21.grid(row=3, column=2)

    lframe22 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe22.grid(row=4, column=2)

    lframe23 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe23.grid(row=5, column=2)

    lframe24 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe24.grid(row=6, column=2)

    lframe25 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe25.grid(row=7, column=2)

    lframe26 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe26.grid(row=8, column=2)

    # Category food grains

    lframe27 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe27.grid(row=0, column=3)

    lframe28 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe28.grid(row=1, column=3)

    lframe29 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe29.grid(row=2, column=3)

    lframe30 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe30.grid(row=3, column=3)

    lframe31 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe31.grid(row=4, column=3)

    lframe32 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe32.grid(row=5, column=3)

    lframe33 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe33.grid(row=6, column=3)

    lframe34 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe34.grid(row=7, column=3)

    lframe35 = LabelFrame(frame, bg='#b1ba9e', bd=3, relief='ridge', height=100, width=1000)
    lframe35.grid(row=8, column=3)

    lframe36 = LabelFrame(fram, bg='#add957', bd=3, relief='ridge', height=100, width=1000, pady=145)
    lframe36.grid(row=0, column=1)
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14
    global var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26
    global var27,var28,var29,var30,var31,var32,var33,var33,var34,var35


    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = StringVar()
    var11 = StringVar()
    var12 = StringVar()
    var13 = StringVar()
    var14 = StringVar()
    var15 = StringVar()
    var16 = StringVar()
    var17 = StringVar()
    var18 = StringVar()
    var19 = StringVar()
    var20 = StringVar()
    var21 = StringVar()
    var22 = StringVar()
    var23 = StringVar()
    var24 = StringVar()
    var25 = StringVar()
    var26 = StringVar()
    var27 = StringVar()
    var28 = StringVar()
    var29 = StringVar()
    var30 = StringVar()
    var31 = StringVar()
    var32 = StringVar()
    var33 = StringVar()
    var34 = StringVar()
    var35 = StringVar()

    bvar = StringVar()

    # Spinach, Tomatoes, Cauliflower, Potato, Bitter gourd, Carrot, Capsicum, Green chili, Brinjal
    l1 = Label(lframe1, text="Spinach", width=13, font='bold')
    l1.grid(row=0, column=0)
    e1 = Entry(lframe1, width=5, textvariable=var1, bd=7)
    e1.grid(row=0, column=1)
    ll11 = Label(lframe1, text='EXPIRY DATE')
    ll11.grid(row=1, column=0)
    # ---------
    l2 = Label(lframe2, text="Tomatoes", width=13, font='bold')
    l2.grid(row=0, column=0)
    e2 = Entry(lframe2, width=5, textvariable=var2, bd=7)
    e2.grid(row=0, column=1)
    ll12 = Label(lframe2, text='EXPIRY DATE')
    ll12.grid(row=1, column=0)

    # ------------------------------
    l3 = Label(lframe3, text="Cauliflower", width=13, font='bold')
    l3.grid(row=0, column=0)
    e3 = Entry(lframe3, width=5, textvariable=var3, bd=7)
    e3.grid(row=0, column=1)
    ll13 = Label(lframe3, text='EXPIRY DATE')
    ll13.grid(row=1, column=0)

    # -------------------------------------
    l4 = Label(lframe4, text="Potato", width=13, font='bold')
    l4.grid(row=0, column=0)
    e4 = Entry(lframe4, width=5, textvariable=var4, bd=7)
    e4.grid(row=0, column=1)
    ll14 = Label(lframe4, text='EXPIRY DATE')
    ll14.grid(row=1, column=0)
    # -----------------------------------------
    l5 = Label(lframe5, text="Bittergourd", width=13, font='bold')
    l5.grid(row=0, column=0)
    e5 = Entry(lframe5, width=5, textvariable=var5, bd=7)
    e5.grid(row=0, column=1)
    ll15 = Label(lframe5, text='EXPIRY DATE')
    ll15.grid(row=1, column=0)

    l6 = Label(lframe6, text="Carrot", width=13, font='bold')
    l6.grid(row=0, column=0)
    e6 = Entry(lframe6, width=5, textvariable=var6, bd=7)
    e6.grid(row=0, column=1)
    ll16 = Label(lframe6, text='EXPIRY DATE')
    ll16.grid(row=1, column=0)

    l7 = Label(lframe7, text="Capsicum", width=13, font='bold')
    l7.grid(row=0, column=0)
    e7 = Entry(lframe7, width=5, textvariable=var7, bd=7)
    e7.grid(row=0, column=1)
    ll17 = Label(lframe7, text='EXPIRY DATE')
    ll17.grid(row=1, column=0)

    l8 = Label(lframe8, text="Brinjal", width=13, font='bold')
    l8.grid(row=0, column=0)
    e8 = Entry(lframe8, width=5, textvariable=var8, bd=7)
    e8.grid(row=0, column=1)
    ll18 = Label(lframe8, text='EXPIRY DATE')
    ll18.grid(row=1, column=0)

    l9 = Label(lframe9, text="Green Chili", width=13, font='bold')
    l9.grid(row=0, column=0)
    e9 = Entry(lframe9, width=5, textvariable=var9, bd=7)
    e9.grid(row=0, column=1)
    ll19 = Label(lframe9, text='EXPIRY DATE')
    ll19.grid(row=1, column=0)

    l10 = Label(lframe10, text="Alphonso", width=13, font='bold')
    l10.grid(row=0, column=0)
    e10 = Entry(lframe10, width=5, textvariable=var10, bd=7)
    e10.grid(row=0, column=1)
    ll20 = Label(lframe10, text='EXPIRY DATE')
    ll20.grid(row=1, column=0)  # lphonso Mangoes, Pomegranates, Bananas, Peaches, Apples

    l11 = Label(lframe11, text="Mangoes", width=13, font='bold')
    l11.grid(row=0, column=0)
    e11 = Entry(lframe11, width=5, textvariable=var11, bd=7)
    e11.grid(row=0, column=1)
    ll21 = Label(lframe11, text='EXPIRY DATE')
    ll21.grid(row=1, column=0)

    l12 = Label(lframe12, text="Pomegranates", width=13, font='bold')
    l12.grid(row=0, column=0)
    e12 = Entry(lframe12, width=5, textvariable=var12, bd=7)
    e12.grid(row=0, column=1)
    ll22 = Label(lframe12, text='EXPIRY DATE')
    ll22.grid(row=1, column=0)

    l13 = Label(lframe13, text="Bananas", width=13, font='bold')
    l13.grid(row=0, column=0)
    e13 = Entry(lframe13, width=5, textvariable=var13, bd=7)
    e13.grid(row=0, column=1)
    ll23 = Label(lframe13, text='EXPIRY DATE')
    ll23.grid(row=1, column=0)

    l14 = Label(lframe14, text="Peaches", width=13, font='bold')
    l14.grid(row=0, column=0)
    e14 = Entry(lframe14, width=5, textvariable=var14, bd=7)
    e14.grid(row=0, column=1)
    ll24 = Label(lframe14, text='EXPIRY DATE')
    ll24.grid(row=1, column=0)

    l15 = Label(lframe15, text="Kiwi", width=13, font='bold')
    l15.grid(row=0, column=0)
    e15 = Entry(lframe15, width=5, textvariable=var15, bd=7)
    e15.grid(row=0, column=1)
    ll25 = Label(lframe15, text='EXPIRY DATE')  # Watermelon,guava and grapes
    ll25.grid(row=1, column=0)

    l16 = Label(lframe16, text="Watermelon", width=13, font='bold')
    l16.grid(row=0, column=0)
    e16 = Entry(lframe16, width=5, textvariable=var16, bd=7)
    e16.grid(row=0, column=1)
    ll26 = Label(lframe16, text='EXPIRY DATE')  # Watermelon,guava and grapes
    ll26.grid(row=1, column=0)

    l17 = Label(lframe17, text="Guava", width=13, font='bold')
    l17.grid(row=0, column=0)
    e17 = Entry(lframe17, width=5, textvariable=var17, bd=7)
    e17.grid(row=0, column=1)
    ll27 = Label(lframe17, text='EXPIRY DATE')  # Watermelon,guava and grapes
    ll27.grid(row=1, column=0)

    l18 = Label(lframe18, text="Grapes", width=13, font='bold')
    l18.grid(row=0, column=0)
    e18 = Entry(lframe18, width=5, textvariable=var18, bd=7)
    e18.grid(row=0, column=1)
    ll28 = Label(lframe18, text='EXPIRY DATE')
    ll28.grid(row=1, column=0)

    l181 = Label(lframe181, text='PULSES', width=13, font='bold')
    l181.grid(row=0, column=0)
    l281 = Label(lframe181, text='Varieties available', height=1, width=27)
    l281.grid(row=1, column=0)

    # Moong, Chana, Toor, Masoor, Urad, Arhar, Kidney Beans

    l19 = Label(lframe19, text="Moong", width=13, font='bold')
    l19.grid(row=0, column=0)
    e19 = Entry(lframe19, width=5, textvariable=var19, bd=7)
    e19.grid(row=0, column=1)
    ll29 = Label(lframe19, text='EXPIRY DATE')
    ll29.grid(row=1, column=0)

    l20 = Label(lframe20, text="Chana", width=13, font='bold')
    l20.grid(row=0, column=0)
    e20 = Entry(lframe20, width=5, textvariable=var20, bd=7)
    e20.grid(row=0, column=1)
    ll30 = Label(lframe20, text='EXPIRY DATE')
    ll30.grid(row=1, column=0)

    l21 = Label(lframe21, text="Toor", width=13, font='bold')
    l21.grid(row=0, column=0)
    e21 = Entry(lframe21, width=5, textvariable=var21, bd=7)
    e21.grid(row=0, column=1)
    ll31 = Label(lframe21, text='EXPIRY DATE')
    ll31.grid(row=1, column=0)

    # Masoor, Urad, Arhar, Kidney Beans

    l22 = Label(lframe22, text="Masoor", width=13, font='bold')
    l22.grid(row=0, column=0)
    e22 = Entry(lframe22, width=5, textvariable=var22, bd=7)
    e22.grid(row=0, column=1)
    ll32 = Label(lframe22, text='EXPIRY DATE')
    ll32.grid(row=1, column=0)

    l23 = Label(lframe23, text="Urad", width=13, font='bold')
    l23.grid(row=0, column=0)
    e23 = Entry(lframe23, width=5, textvariable=var23, bd=7)
    e23.grid(row=0, column=1)
    ll33 = Label(lframe23, text='EXPIRY DATE')
    ll33.grid(row=1, column=0)

    l24 = Label(lframe24, text="Arhar", width=13, font='bold')
    l24.grid(row=0, column=0)
    e24 = Entry(lframe24, width=5, textvariable=var24, bd=7)
    e24.grid(row=0, column=1)
    ll34 = Label(lframe24, text='EXPIRY DATE')
    ll34.grid(row=1, column=0)

    l25 = Label(lframe25, text="Kidney Beans", width=13, font='bold')
    l25.grid(row=0, column=0)
    e25 = Entry(lframe25, width=5, textvariable=var25, bd=7)
    e25.grid(row=0, column=1)
    ll35 = Label(lframe25, text='EXPIRY DATE')
    ll35.grid(row=1, column=0)

    l26 = Label(lframe26, text="Dry Beans", width=13, font='bold')
    l26.grid(row=0, column=0)
    e26 = Entry(lframe26, width=5, textvariable=var26, bd=7)
    e26.grid(row=0, column=1)
    ll36 = Label(lframe26, text='EXPIRY DATE')
    ll36.grid(row=1, column=0)

    # Wheat, Millet, Corn, Maize, and Rice.

    l27 = Label(lframe27, text="Wheat", width=13, font='bold')
    l27.grid(row=0, column=0)
    e27 = Entry(lframe27, width=5, textvariable=var27, bd=7)
    e27.grid(row=0, column=1)
    ll37 = Label(lframe27, text='EXPIRY DATE')
    ll37.grid(row=1, column=0)

    l28 = Label(lframe28, text="Millet", width=13, font='bold')
    l28.grid(row=0, column=0)
    e28 = Entry(lframe28, width=5, textvariable=var28, bd=7)
    e28.grid(row=0, column=1)
    ll38 = Label(lframe28, text='EXPIRY DATE')
    ll38.grid(row=1, column=0)

    l29 = Label(lframe29, text="Corn", width=13, font='bold')
    l29.grid(row=0, column=0)
    e29 = Entry(lframe29, width=5, textvariable=var29, bd=7)
    e29.grid(row=0, column=1)
    ll39 = Label(lframe29, text='EXPIRY DATE')
    ll39.grid(row=1, column=0)

    l30 = Label(lframe30, text="Maize", width=13, font='bold')
    l30.grid(row=0, column=0)
    e30 = Entry(lframe30, width=5, textvariable=var30, bd=7)
    e30.grid(row=0, column=1)
    ll40 = Label(lframe30, text='EXPIRY DATE')
    ll40.grid(row=1, column=0)

    l31 = Label(lframe31, text="Rice", width=13, font='bold')
    l31.grid(row=0, column=0)
    e31 = Entry(lframe31, width=5, textvariable=var31, bd=7)
    e31.grid(row=0, column=1)
    ll41 = Label(lframe31, text='EXPIRY DATE')
    ll41.grid(row=1, column=0)

    l32 = Label(lframe32, text="Milk", width=13, font='bold')
    l32.grid(row=0, column=0)
    e32 = Entry(lframe32, width=5, textvariable=var32, bd=7)
    e32.grid(row=0, column=1)
    ll42 = Label(lframe32, text='EXPIRY DATE')
    ll42.grid(row=1, column=0)

    l33 = Label(lframe33, text="Egg", width=13, font='bold')
    l33.grid(row=0, column=0)
    e33 = Entry(lframe33, width=5, textvariable=var33, bd=7)
    e33.grid(row=0, column=1)
    ll43 = Label(lframe33, text='EXPIRY DATE')
    ll43.grid(row=1, column=0)

    l34 = Label(lframe34, text="AmPanna", width=13, font='bold')
    l34.grid(row=0, column=0)
    e34 = Entry(lframe34, width=5, textvariable=var34, bd=7)
    e34.grid(row=0, column=1)
    ll44 = Label(lframe34, text='EXPIRY DATE')
    ll44.grid(row=1, column=0)

    l35 = Label(lframe35, text="Kokum Juice", width=13, font='bold')
    l35.grid(row=0, column=0)
    e35 = Entry(lframe35, width=5, textvariable=var35, bd=7)
    e35.grid(row=0, column=1)
    ll45 = Label(lframe35, text='EXPIRY DATE')
    ll45.grid(row=1, column=0)

    # ------------------------------------------------------------------------------------------------4





    def insert_val():
        if(pepcheck()==-1):
            li = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16,
                  var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30,
                  var31, var32, var33, var34, var35]
            for i in li:
                i.set('')
            return
        else:
            pass


        try:
            mycursor.execute("CREATE TABLE khamba (id int, name VARCHAR(25), items VARCHAR(60), quantity int)")
            li = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16,
                  var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30,
                  var31, var32, var33, var34, var35]
            li_item = ["Spinach", "Tomatoes", "Cauliflower", "Potato", "Bittergourd", "Carrot", "Capsicum", "Brinjal",
                       "Green Chilli",
                       "Alphonso", "Mangoes", "Pomegranates", "Bananas", "Peaches", "Kiwi", "Watermelon", "Guava",
                       "Grapes",
                       "Moong",
                       "Chana", "Toor",
                       "Masoor", "Urad", "Arhar", "Kidney Beans", "Dry Beans", "Wheat", "Millet", "Corn", "Maize",
                       "Rice",
                       "Milk", "Egg", "AmPanna", "Kokum Juice"]
            cnt1 = 0
            cnt2=0
            for i in li:

                if (i.get() != ''):
                    cnt2+=1
                    sql = "INSERT INTO khamba (id,name,items,quantity) VALUES (%s,%s,%s,%s)"
                    val = (cnt2, user_verification.get(), li_item[cnt1], int(i.get()))
                    mycursor.execute(sql, val)

                    mydb.commit()
                cnt1 += 1
            cart_view()
            # ("CREATE TABLE custom (id VARCHAR(27),name VARCHAR(50),item VARCHAR(30),quantity VARCHAR(10))")
        except:

            li = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16,
                  var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30,
                  var31, var32, var33, var34, var35]
            li_item = ["Spinach", "Tomatoes", "Cauliflower", "Potato", "Bittergourd", "Carrot", "Capsicum", "Brinjal",
                       "Green Chilli",
                       "Alphonso", "Mangoes", "Pomegranates", "Bananas", "Peaches", "Kiwi", "Watermelon", "Guava",
                       "Grapes",
                       "Moong",
                       "Chana", "Toor",
                       "Masoor", "Urad", "Arhar", "Kidney Beans", "Dry Beans", "Wheat", "Millet", "Corn", "Maize",
                       "Rice",
                       "Milk", "Egg", "AmPanna", "Kokum Juice"]
            cnt1 = 0
            cnt2=0
            for i in li:

                if (i.get() != ''):
                    cnt2+=1
                    sql = "INSERT INTO khamba (id,name,items,quantity) VALUES (%s,%s,%s,%s)"
                    val = (cnt2, user_verification.get(), li_item[cnt1], int(i.get()))
                    mycursor.execute(sql, val)

                    mydb.commit()
                cnt1+=1
            cart_view()
            # create table with id,name,product bought, name will remain same for different product brought

    def lookup():
        cnt = 0
        li = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16,
              var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30,
              var31, var32, var33, var34, var35]
        li_price = [100, 23, 257, 23, 56, 21, 87, 33, 89, 34, 37, 42, 56, 78, 42, 89, 32, 83, 36, 45, 100, 23, 257, 23,
                    56, 21, 87, 33, 89, 34, 37, 432, 56, 78, 42]
        cnt = 0
        x=0




        try:
         for i in li:

              if (i.get() != ''):
                 x+=(li_price[cnt]*int(i.get()))
              cnt+=1
              bvar.set(x)
        except:
            messagebox.showerror("error","Invalid field Input")
            bvar.set('')
            for i in li:
                i.set('')


    def check_prices():

        t = Toplevel(main_screen)
        t.title("Price list")
        t.geometry("700x700")
        t.config(bg='#add957')
        li_item = ["Spinach", "Tomatoes", "Cauliflower", "Potato", "Bittergourd", "Carrot", "Capsicum", "Brinjal",
                   "Green Chilli",
                   "Alphonso", "Mangoes", "Pomegranates", "Bananas", "Peaches", "Kiwi", "Watermelon", "Guava", "Grapes",
                   "Moong",
                   "Chana", "Toor",
                   "Masoor", "Urad", "Arhar", "Kidney Beans", "Dry Beans", "Wheat", "Millet", "Corn", "Maize",
                   "Rice",
                   "Milk", "Egg", "AmPanna", "Kokum Juice"]

        li_expiry = ["1/11/20", "23/11/20", "5/11/20", "27/11/20", "5/11/20", "8/11/20", "9/11/20", "11/11/20",
                     "14/11/20", "13/11/20",
                     "16/11/20", "2/11/20", "3/11/20", "23/11/20", "7/11/20", "30/11/20", "7/11/20", "8/11/20",
                     "3/11/20", "2/11/20",
                     "9/11/20", "8/11/20", "22/11/20", "6/11/20", "18/11/20", "23/11/20", "27/11/20", "12/11/20",
                     "16/11/20", "4/11/20",
                     "24/11/20", "26/11/20", "21/11/20", "9/11/20"]

        li_price = [100, 23, 257, 23, 56, 21, 87, 33, 89, 34, 37, 432, 56, 78, 42, 89, 32, 83, 36, 45, 100, 23, 257, 23,
                    56, 21, 87, 33, 89, 34, 37, 432, 56, 78, 42]

        frame = Frame(t, bd=3, bg="#add957")

        cnt = 1
        k = 0
        l3 = Label(t, text="item")
        l3.grid(row=0, column=0)
        for i in li_item:
            l = Label(t, text=i, fg='red', padx=50, bg="#add957", width=30)
            l.grid(row=cnt, column=k)

            cnt += 1

        cnt2 = 1
        l4 = Label(t, text="Price in ₹")
        l4.grid(row=0, column=1)
        for j in li_price:
            l1 = Label(t, text=j, fg='red', padx=50, bg="#add957", width=30)
            l1.grid(row=cnt2, column=k + 1)
            cnt2 += 1

        bbx = Button(t, width=20, text="EXIT", font='bold', command=t.destroy, bg='red')
        bbx.grid(row=36, column=1, columnspan=3)

    # cart values
    def cart_view():

        global toop
        toop = Toplevel(main_screen)
        toop.geometry('500x700')
        toop.config(bg='#ebbc23')

        frame = Frame(toop, bg='orange')
        frame.pack()

        l1 = LabelFrame(frame, bg='orange', bd=7, relief='ridge', padx=10)
        l1.grid(row=0, column=0)
        l2 = LabelFrame(frame, bg='orange', bd=7, relief='ridge', padx=10)
        l2.grid(row=1, column=0)
        l3 = LabelFrame(frame, bg='orange', bd=7, relief='ridge', padx=10)
        l3.grid(row=2, column=0)
        l4 = LabelFrame(frame, bg='orange', bd=7, relief='ridge', padx=10)
        l4.grid(row=3, column=0)
        l5 = LabelFrame(frame, bg='orange', bd=7, relief='ridge', pady=50)
        l5.grid(row=4, column=0)
        global envar1
        global envar2
        global envar3
        global envar4
        envar1 = StringVar()
        envar2 = StringVar()
        envar3 = StringVar()
        envar4 = StringVar()

        # reset function

        def reset():
            envar1.set('')
            envar2.set('')
            envar3.set('')
            envar4.set('')

        def check(fs):
            for i in fs:
                if i.isalpha():
                    return -1

            fs = int(fs)
            cnt = 0
            while (fs != 0):
                cnt += 1
                fs //= 10
            if (cnt != 10):
                return -1

        # place order option
        def place_order():
            if (envar1.get() == '' or envar2.get() == '' or envar3.get() == '' or envar4.get() == ''):
                messagebox.showinfo("error", "Please Select  all entry")

            elif (check(envar4.get()) == -1):
                messagebox.showerror("error", "Invalid Phone Number")
                en4.delete(0, END)
            else :
                show()


        Label(l1, text='Enter Your Name', font='Arial', width=15, bg='orange').pack()
        en1 = Entry(l1, bd=8, width=25, font='bold', textvariable=envar1)
        en1.pack()

        Label(l2, text='Enter Your Address', font='Arial', width=17, bg='orange').pack()
        en2 = Entry(l2, bd=8, width=25, font='bold', textvariable=envar2)
        en2.pack()

        Label(l3, text='Enter Your Landmark', font='Arial', width=17, bg='orange').pack()
        en3 = Entry(l3, bd=8, width=25, font='bold', textvariable=envar3)
        en3.pack()

        Label(l4, text='Enter You Phone Number', font='Arial', width=20, bg='orange').pack()
        en4 = Entry(l4, bd=8, width=25, font='bold', textvariable=envar4)
        en4.pack()

        Label(l5, text="Please Select One", font='Arial', width=20, bg='orange').pack()
        bbx1 = Button(l5, text="Reset", bd=25, bg='red', font='bold', width=10, command=reset).pack()
        bbx2 = Button(l5, text="Place Order", bd=25, bg='red', font='bold', width=10, command=place_order).pack()

        toop.mainloop()

    bx1 = Button(lframe36, text='Total Cost', width=19, height=3, font='bold', command=lookup, bg='#ff4242', bd=7)
    bx1.pack()
    ex1 = Entry(lframe36, state=DISABLED, textvariable=bvar, bd=3, font='bold')
    ex1.pack()

    bx2 = Button(lframe36, text="Proceed to Buy", width=19, font='bold', command=insert_val, bg='#ff4242', bd=7)
    bx2.pack()

    bx3 = Button(lframe36, text="Check Prices", width=19, font='bold', bg='#ff4242', command=check_prices, bd=7)
    bx3.pack()


# inserting the items bought by user in system
def pepcheck():
        li = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16,
              var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29, var30,
              var31, var32, var33, var34, var35]
        x=0
        try :
            for i in li :
                if(i.get()!=''):
                    x+=int(i.get())
        except:
            messagebox.showerror("Invalid","Invalid entry in fields")
            for i in li:
                i.set('')
            return -1
        return 0

def show():
    xyz = Toplevel(main_screen)
    xyz.geometry('1300x1300')
    xyz.title("Bill")
    xyz.config(bg='#649dfa')
    x=user_verification.get()
    mycursor.execute("SELECT items,quantity   FROM khamba where name='"+x+"'")
    
    lx1=Label(xyz,text="****************This is your bill *************",font='bold')
    lx1.grid(row=0,column=0,columnspan=3)
    lx2=Label(xyz,text="*************Currently we are accepting only cash *****************",font='bold')
    lx2.grid(row=1,column=0,columnspan=3)



    i = 0
    for log in mycursor:
        for j in range(len(log)):
            e = Label(xyz, width=10, fg='blue')
            e.grid(row=i+2, column=j)
            e.config(text=log[j])
        i = i + 1


    def info_delete():
        sql = "DELETE FROM khamba WHERE name = '"+user_verification.get()+"'"

        mycursor.execute(sql)

        mydb.commit()
        messagebox.showinfo("order","Order Placed will reach you within 24 hours")

    pex_add=envar2.get()+"  "+envar3.get()+"  "+envar3.get()
    lex_add=Label(xyz,text="Your address" +pex_add,bg="#649dfa")
    lex_add.grid(row=i,column=8)
    fixb=Button(xyz,text='confirm order',bg='orange',command=info_delete)
    fixb.grid(row=i+5,column=1)
    bixb=Button(xyz,text='Exit',bg='orange',command=xyz.destroy)
    bixb.grid(row=i+5,column=2)
    xyz.mainloop()



def admin():
    global adm
    adm=Toplevel(main_screen)
    adm.geometry('300x1000')
    adm.config(bg='#859ec7')

    my_imgx = Image.open("admiimg.jpg")
    my_imgx = my_imgx.resize((200, 200), Image.ANTIALIAS)
    my_imgx = ImageTk.PhotoImage(my_imgx)
    my_labelx = Label(adm, image=my_imgx)
    my_labelx.image = my_imgx
    my_labelx.grid(row=1, column=0,columnspan=3, padx=20, pady=10)


    lxlogin=Label(adm,text="Below is the user Database")
    lxlogin.grid(row=0,column=0)
    try:
      mycursor.execute("SELECT * FROM usersystem")

      Label(adm,text="Login ID").grid(row=2,column=0)
      Label(adm,text="Password ID").grid(row=2,column=1)

      i = 0
      for log in mycursor:
          for j in range(len(log)):
              e = Label(adm, width=10, fg='blue')
              e.grid(row=i + 3, column=j,pady=10)
              e.config(text=log[j])
          i = i + 1
    except:
        messagebox.showerror("user","No user tillnow")

















def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Account Login")
    main_screen.config(bg="#47f5f2")

    my_img1 = Image.open("organic_logo.jpg")
    my_img1 = my_img1.resize((200, 200), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(my_img1)
    my_label = Label(main_screen, image=my_img1)
    my_label.image = my_img1
    my_label.pack()

    Label(text="Select Your Choice", bg="#f5f50a", width="22", height="2", font=("Calibri", 13)).pack()
    Label(text="", bg="#47f5f2").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="", bg='#47f5f2').pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="", bg='#47f5f2').pack()
    Button(text="Admin Page",height='2',width=30,command=admin).pack()

    main_screen.mainloop()


if __name__ == "__main__":
    main_account_screen()
