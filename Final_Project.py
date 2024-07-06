from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# System Function
# Create Connection
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('medical.db')
    cursor = conn.cursor()

def check_input_type(input):
    try:
        # Convert it into integer
        int(input)
        return('int')
    except ValueError:
        try:
            # Convert it into float
            float(input)
            return('float')
        except ValueError:
            return('str')

# Interface Function
# Create Window
def create_window():
    main = Tk()
    # Import all image into Program
    import_img()
    main.title("Magnolia hospital")
    main.geometry("800x450")
    main.resizable(False, False)
    main.config(bg = "#28527a" )
    main.iconphoto(False,icon1)
    return main

# Main Window
def main_window():

    # Create Main Window Frame
    main_frame = Frame(window,height=450,width=800)
    main_frame.place(x=0,y=0)
    
    # Create Label
    Label(main_frame,image=bglogin).place(x=-2,y=-2)
    Label(main_frame,font="Tahoma 19",bg="#507f80",highlightbackground="#507f80",highlightthickness=3,height=1).place(x=107,y=247,relwidth=0.202)
    Label(main_frame,font="Tahoma 19",bg="#507f80",highlightbackground="#507f80",highlightthickness=3,height=1).place(x=107,y=182,relwidth=0.202)
    Label(main_frame,font="Tahoma 19",bg="#507f80",highlightbackground="#507f80",highlightthickness=3,height=1).place(x=107,y=117,relwidth=0.202)

    # Create Button, In Use Function: loginprofile, regis, seeappointment, quit
    Button(main_frame,text='LOGIN',bg="#57c9ca",font="Tahoma 14",height=1,width=15,bd=0,command=login_window).place(x=110,y=120)
    Button(main_frame,text='Register',bg="#57c9ca",font="Tahoma 14",height=1,width=15,bd=0,command=regist_window).place(x=110,y=185)
    Button(main_frame,text='See Appointment',bg="#57c9ca",font="Tahoma 14",height=1,width=15,bd=0,command=appointment_window).place(x=110,y=250)
    Button(main_frame,text='EXIT',bg="#6db3a8",font="Tahoma 19",activebackground = "#6db3a8",width=5,bd=0,fg="#ffffff",command=lambda:window.quit()).place(x=20,y=408,relheight=0.07)  

# Login Window
def login_window():

    # Function
    def login():
        if  user_entry.get() == "" :
            messagebox.showwarning("User","Enter username first!")
            user_entry.focus_force()
        else :
            if pwd_entry.get() == "" :
                messagebox.showwarning("User","Enter password first!")
                pwd_entry.focus_force()
            else:
                sql = "select * from doctor where User=? AND Pass=?"
                cursor.execute(sql,[user_entry.get(),pwd_entry.get()])
                result = cursor.fetchall()
                if result:
                    if result[0][5] == "1" :
                        user_entry.delete(0,END)
                        pwd_entry.delete(0,END)
                        login_frame.destroy()
                        admin_window()
                    else :
                        user_entry.delete(0,END)
                        pwd_entry.delete(0,END)
                        login_frame.destroy()
                        doctor_window()
                else :
                    messagebox.showwarning("Admin: ","Username or Password is invalid.")
                    pwd_entry.focus_force()
    
    def exit_login():
        user_entry.delete(0, END)
        pwd_entry.delete(0, END)
        login_frame.destroy()
    
    # Create Login Frame
    login_frame=Frame(window,height=450,width=800)
    login_frame.place(x=0,y=0)

    # Create Label
    Label(login_frame,image=bglogin).place(x=-2,y=-2)
    Label(login_frame,text="USERNAME",font="Tahoma 19",bg="#a4cfd0").place(x=122,y=85)
    Label(login_frame,text="PASSWORD",font="Tahoma 19",bg="#a4cfd0").place(x=120,y=170)
    
    # Create Entry
    user_entry = Entry(login_frame,bg="#d7fcfd",font="Tahoma 17",justify=CENTER)
    user_entry.place(x=85,y=130,relheight=0.07,relwidth=0.25)
    pwd_entry = Entry(login_frame,bg="#d7fcfd",show='*',font="Tahoma 17",justify=CENTER)
    pwd_entry.place(x=85,y=215,relheight=0.07,relwidth=0.25)

    # Create Button
    Button(login_frame,text='LOGIN',bg="#57c9ca",font="Tahoma 14",height=1,width=10,bd=0,command=login).place(x=131,y=270)
    Button(login_frame,image=back_img,bg="#6db3a8",activebackground = "#6db3a8",font="Tahoma 19",bd=0,fg="#ffffff",command=exit_login).place(x=20,y=408,relheight=0.07)

# Regist window
def regist_window():
    # Function
    def confirm_regist():
        # If, Else Statement
        if not fname.get():
            messagebox.showwarning("Register Fail:","Please Enter Your First Name")
        elif not lname.get():
            messagebox.showwarning("Register Fail:","Please Enter Your Last Name")
        elif chooseGender.get() == None:
            messagebox.showwarning("Register Fail:","Please Choose Your Gender")
        elif not age.get() :
            messagebox.showwarning("Register Fail:","Please Enter Your Age")
        elif not height.get() :
            messagebox.showwarning("Register Fail:","Please Enter Your Height")
        elif not weight.get() :
            messagebox.showwarning("Register Fail:","Please Enter Your Weight")
        else:
            # Check age type
            if check_input_type(age.get()) != 'int':
                messagebox.showwarning("Register Fail:","Age Should be full number")
                age.focus_force()
            else:
                # Check if age < 0
                if int(age.get()) < 0:
                    messagebox.showwarning("Register Fail:","Age Should not be lower than 0")
                    age.focus_force()
                else:
                    # Check Height type
                    if check_input_type(height.get()) == 'str':
                        messagebox.showwarning("Register Fail:","Height Should be Numeric.")
                        height.focus_force()
                    else:
                        # Check if height < 0
                        if float(height.get()) < 0:
                            messagebox.showwarning("Register Fail:","Height Should not be lower than 0")
                            height.focus_force()
                        else:
                            # Check weight type
                            if check_input_type(weight.get()) == 'str':
                                messagebox.showwarning("Register Fail:","Weight Should be Numeric.")
                                weight.focus_force()
                            else:
                                # Check if weight < 0
                                if float(weight.get()) < 0:
                                    messagebox.showwarning("Register Fail:","Height Should not be lower than 0")
                                    height.focus_force()       
                                else:
                                    # Save new info to database
                                    sql = '''
                                                    INSERT INTO patient(Fname,Lname,Gender,Age,Height,Weight)
                                                    VALUES (?,?,?,?,?,?)
                                        '''
                                    cursor.execute(sql,(fname.get(),lname.get(),chooseGender.get(),age.get(),height.get(),weight.get()))
                                    conn.commit()
                                    messagebox.showinfo("Admin:","Register Succesfull")

                                    regisframe.destroy()  

    # Variable
    chooseGender = StringVar()

    # Create Regist Frame
    regisframe =Frame(window,width=473,height=450)
    regisframe.place(x=327,y=0)

    # Create Label
    Label(regisframe ,image=bgregis).place(x=-2,y=-2)
    Label(regisframe,text="Firstname  :",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=80)
    Label(regisframe,text="Lastname  :",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=130)
    Label(regisframe,text="Gender      : ",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=180)
    Label(regisframe,text="Age           :",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=230)
    Label(regisframe,text="Height       : ",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=280)
    Label(regisframe,text="Weight      : ",bg="#a4cfd0",font="Tahoma 12 bold").place(x=100,y=330)

    # Create Entry
    fname = Entry(regisframe,width=25)
    fname.place(x=215,y=80,relheight=0.055)
    lname=Entry(regisframe,width=25)
    lname.place(x=215,y=130,relheight=0.055)

    # Create Combobox
    gender_box = ttk.Combobox(regisframe, textvariable=chooseGender, values=genderlst, state='readonly',width=22)
    gender_box.place(x=215,y=180,relheight=0.055)

    age = Entry(regisframe,width=25)
    age.place(x=215,y=230,relheight=0.055)
    height=Entry(regisframe,width=25)
    height.place(x=215,y=280,relheight=0.055)
    weight=Entry(regisframe,width=25)
    weight.place(x=215,y=330,relheight=0.055)

    # Create Button
    Button(regisframe,image=exitregis,bd=0,bg="#a4cfd0",activebackground = "#a4cfd0",command=regisframe.destroy).place(x=370,y=34)
    Button(regisframe,width=7,text = "DONE",bg="#e35b40",font="Tahoma 12",command=confirm_regist).place(x=210,y=380)

# See Appointment Window
def appointment_window():
    # Function
    def seeappointmentclick():
        if not fname_entry.get():
            messagebox.showwarning("Admin :","Please Enter Your First Name")
        elif not lname_entry.get():
            messagebox.showwarning("Admin :","Please Enter Your Last Name")
        else:
            get_data()
            if fname_entry.get() not in fname_lst or lname_entry.get() not in lname_lst:
                messagebox.showwarning("Admin :","No such name in database or wrong first name or last name, please try again")
            else:
                # Call appointment date from Database
                sql = '''
                                select Date from patient
                                where Fname=? And Lname=?
                    '''
                cursor.execute(sql,(fname_entry.get(),lname_entry.get()))
                result = cursor.fetchone()

                date["text"]=result[0]

    def exit_appointment():
        fname_entry.delete(0,END)
        lname_entry.delete(0,END)
        seeappframe.destroy()

    def get_data():
        fname_lst.clear()
        lname_lst.clear()
        result = cursor.execute('select * from patient')
        for i,data in enumerate(result):
            fname_lst.append(data[1])
            lname_lst.append(data[2])

    # Variable
    fname_lst = []
    lname_lst = []

    # Create Appointment Date Window
    seeappframe =Frame(window,width=800,height=450)
    seeappframe.place(x=0,y=0)

    # Create Label
    Label(seeappframe,image=imgseebg).place(x=-2,y=-2)
    Label(seeappframe,text="Firstname",font="Tahoma 15",bg="#a4cfd0").place(x=230,y=110)
    Label(seeappframe,text="Lastname",font="Tahoma 15",bg="#a4cfd0").place(x=440,y=110)

    # Create Entry
    fname_entry = Entry(seeappframe,font="Tahoma 15",justify=CENTER)
    fname_entry.place(x=190,y=150,relwidth=0.22)
    lname_entry = Entry(seeappframe,font="Tahoma 15",justify=CENTER)
    lname_entry.place(x=400,y=150,relwidth=0.22)

    Label(seeappframe,text="Appointment date",font="Tahoma 15",bg="#a4cfd0").place(x=303,y=200)
    date = Label(seeappframe,text="",font="Tahoma 15")
    date.place(x=297,y=240,relwidth=0.22)

    # Create Button
    Button(seeappframe,image=imgexitsee,bg="#4a4b4b",bd=0,command=exit_appointment,activebackground = "#4a4b4b").place(x=620,y=40)
    Button(seeappframe,text="Search",font="Tahoma 12",command=seeappointmentclick).place(x=350,y=300)

# Admin Window
def admin_window():
    
    # Register Button Save to database not finish
    def adminregist():
        # Function
        def confirm():
            if len(fname.get()) == 0:
                messagebox.showwarning("Registered Fail","Please Enter Your First Name")
                fname.focus_force()
            elif len(lname.get()) == 0:
                messagebox.showwarning("Registered Fail","Please Enter Your Last Name")
                lname.focus_force()
            elif len(user.get()) == 0:
                messagebox.showwarning("Registered Fail","Please Enter Your User Name")
                user.focus_force()
            elif len(pwd.get()) == 0:
                messagebox.showwarning("Registered Fail","Please Enter Your Password")
                pwd.focus_force()
            elif len(conpwd.get()) == 0:
                messagebox.showwarning("Registered Fail","Please Confirm Your Password")
                conpwd.focus_force()
            else:
                if conpwd.get() != pwd.get():
                    messagebox.showwarning("Registered Fail","Your Confirm Password does not match Your Password")
                    conpwd.delete(0,END)
                    conpwd.focus_force()
                else:
                    exist_user = []
                    cursor.execute('SELECT User FROM doctor')
                    result = cursor.fetchall()
                    for i in result:
                        exist_user.append(i[0])
                    if user.get() in exist_user:
                        messagebox.showinfo("Registered Fail","This User is already existed in the system.")
                        user.focus_force()
                    else:
                        cursor.execute("INSERT INTO doctor (Fname,Lname, user, pass) VALUES (?,?,?,?)",(fname.get(),lname.get(),user.get(), pwd.get()))
                        conn.commit()
                        messagebox.showinfo("Succesfully Registered","New user added to system.")
                        fname.delete(0,END)
                        lname.delete(0,END)
                        user.delete(0,END)
                        pwd.delete(0,END)
                        conpwd.delete(0,END)
                        admin_regis.destroy()

        # Create Admin Register Frame
        admin_regis = Frame(admin_frame,height=450,width=800,bg="#7ccecb")
        admin_regis.place(x=0,y=0)

        # Create Label
        Label(admin_regis,image=bossregis).place(x=-2,y=-2)
        Label(admin_regis,text="Firstname   :",bg="#7ccecb",font="Tahoma 12 ").place(x=50,y=280)
        Label(admin_regis,text="Lastname   :",bg="#7ccecb",font="Tahoma 12 ").place(x=50,y=350)
        Label(admin_regis,text="Username  : ",bg="#7ccecb",font="Tahoma 12 ").place(x=390,y=250)
        Label(admin_regis,text="Password   :",bg="#7ccecb",font="Tahoma 12 ").place(x=390,y=320)
        Label(admin_regis,text="Confirm Password  : ",bg="#7ccecb",font="Tahoma 12 ").place(x=390,y=390)

        # Create Button
        Button(admin_regis,width=8,text="Done",font="Tahoma 12 bold", command=confirm).place(x=170,y=400,relheight=0.08)
        Button(admin_regis,image=back_img,bd=0,activebackground="#7ccecb",bg="#7ccecb",command=admin_regis.destroy).place(x=10,y=407,relheight=0.08)

        # Create Entry
        fname=Entry(admin_regis,width=33)
        fname.place(x=150,y=280,relheight=0.07)
        lname=Entry(admin_regis,width=33)
        lname.place(x=150,y=350,relheight=0.07)
        user=Entry(admin_regis,width=33)
        user.place(x=550,y=250,relheight=0.07)
        pwd=Entry(admin_regis,width=33, show='*')
        pwd.place(x=550,y=320,relheight=0.07)
        conpwd=Entry(admin_regis,width=33, show='*')
        conpwd.place(x=550,y=390,relheight=0.07)
    
    # Change Password Window
    # Interface Bug
    # Update Button Save to database not Finish
    def changepass():
        def get_data():
            # Clear old data
            nonlocal exist_idlst
            exist_idlst = []
            sql = 'select User from doctor'
            cursor.execute(sql)
            result = cursor.fetchall()

            # Add and change input type to list 
            for i,data in enumerate(result):
                exist_idlst.append(data[0])

        def update_pass():
            if len(id.get()) == 0:
                messagebox.showwarning("Attempt Fail","Please Enter Your ID.")
                id.focus_force()
            elif len(oldpwd.get()) == 0:
                messagebox.showwarning("Attempt Fail","Please Enter Your old password.")
                oldpwd.focus_force()
            elif len(newpwd.get()) == 0:
                messagebox.showwarning("Attempt Fail","Please Enter Your new password.")
                newpwd.focus_force()
            elif len(conpwd.get()) == 0:
                messagebox.showwarning("Attempt Fail","Please confirm your new password.")
                conpwd.focus_force()
            else:
                if newpwd.get() != conpwd.get():
                    messagebox.showwarning("Attempt Fail","Your confirm password does not match new password.")
                    conpwd.focus_force()     
                else:
                    sql = 'select Pass from doctor WHERE User=?'
                    cursor.execute(sql, [id.get()])
                    data_oldpwd = cursor.fetchone()
                    if oldpwd.get() != data_oldpwd[0]:
                        messagebox.showwarning("Attempt Fail","Incorrect Old password, please try again.")
                        oldpwd.focus_force()
                    else:
                        get_data()
                        if id.get() not in exist_idlst:
                            messagebox.showwarning('Attempt Fail', 'This ID does not exist please try again.')
                        else:
                            confirm = messagebox.askyesno('Confirm', 'Set your new password?')
                            if confirm == 'no':
                                None
                            else:
                                sql = '''
                                            update doctor
                                            set Pass=?
                                            where User=?
                                '''
                                cursor.execute(sql, [newpwd.get(), id.get()])
                                conn.commit()
                                id.delete(0, END)
                                oldpwd.delete(0, END)
                                newpwd.delete(0, END)
                                conpwd.delete(0, END)

        exist_idlst = []
        # Create Change Password Frame
        changebg = Frame(admin_frame,width=800,height=450,bg="#A4CFD0")
        changebg.place(x=0,y=0)

        # Create Label
        Label(changebg,image= img_nurse,bg="#A4CFD0").place(x=-2,y=-2)
        Label(changebg,text="ID                        :",bg="#A4CFD0",font="Tahoma 12 ").place(x=120,y=180)
        Label(changebg,text="Old Password        :",bg="#A4CFD0",font="Tahoma 12 ").place(x=120,y=230)
        Label(changebg,text="New Password       :",bg="#A4CFD0",font="Tahoma 12 ").place(x=120,y=280)
        Label(changebg,text="Confirm Password  : ",bg="#A4CFD0",font="Tahoma 12 ").place(x=120,y=330)

        # Create Button
        Button(changebg,width=7,text = "UPDATE",bg="#50988d",font="Tahoma 12", command=update_pass).place(x=270,y=390)
        Button(changebg,image=back_img,bd=0,activebackground="#A4CFD0",bg="#A4CFD0",command=changebg.destroy).place(x=10,y=407,relheight=0.08)
        
        # Create Entry
        id=Entry(changebg,width=35)
        id.place(x=290,y=178,relheight=0.06)
        oldpwd=Entry(changebg,width=35)
        oldpwd.place(x=290,y=228,relheight=0.06)
        newpwd=Entry(changebg,width=35)
        newpwd.place(x=290,y=278,relheight=0.06)
        conpwd=Entry(changebg,width=35)
        conpwd.place(x=290,y=328,relheight=0.06)
    
    admin_frame = Frame(window,height=450,width=800)
    admin_frame.place(x=0,y=0)
    Label(admin_frame,image=img_boss).place(x=-2,y=-2)
    Button(admin_frame,width=20,text="Register",font="Tahoma 12 bold",command=adminregist).place(x=50,y=180,relheight=0.08)
    Button(admin_frame,width=20,text="Change Password",font="Tahoma 12 bold",command=changepass).place(x=50,y=250,relheight=0.08)
    Button(admin_frame,image=img_close,bg="#98cdca",bd=0,activebackground = "#98cdca",command=admin_frame.destroy).place(x=5,y=405)

# Doctor Main Window
def doctor_window():
    # Doctor Window Sub Window Function 
    def info():
        # Info Function
        def treeviewinfo():
            # Create Info Treeframe Frame
            treeframe_info = Frame(info_frame)
            treeframe_info .place(x=60,y=100)

            # Create Scrollbar
            treebar = Scrollbar(treeframe_info)
            treebar.pack(side=RIGHT,fill=Y)
            mytree_info = ttk.Treeview(treeframe_info,columns=("Fname","Lname"),height=10,yscrollcommand=treebar.set)
            mytree_info.pack()

            # Config scrollbar on the treeview
            treebar.config(command=mytree_info.yview)

            # Rename Heading
            mytree_info.heading("#0",text="",anchor=W)
            mytree_info.heading("Fname",text="First name",anchor=CENTER)
            mytree_info.heading("Lname",text="Last Name",anchor=CENTER)
        
            # Adjust Column Size
            mytree_info.column("#0",width=0,minwidth=0)
            mytree_info.column("Fname",anchor=W,width=225,minwidth=225)
            mytree_info.column("Lname",anchor=W,width=225,minwidth=225)
            mytree_info.delete(*mytree_info.get_children())
            
            # Reset Treeview
            mytree_info.delete(*mytree_info.get_children())

            # Import Data From Database
            sql = 'select * from patient'
            cursor.execute(sql)
            result = cursor.fetchall()

            # Insert Data From Database into list
            for i,data in enumerate(result):
                idinfo_lst.append(data[0])
                fnameinfo_lst.append(data[1])
                lnameinfo_lst.append(data[2])

            # Insert Data from list into Treeview
            for i, data in enumerate(idinfo_lst):
                mytree_info.insert('', 'end', values=(fnameinfo_lst[i], lnameinfo_lst[i]))
                        
            mytree_info.bind('<Double-1>',treeviewinfoclick)

            return mytree_info

        def searchinfo():
            # Reset Medical Stock Display
            mytree_info.delete(*mytree_info.get_children())

            # Insert Treeview Data
            for i, data in enumerate(fnameinfo_lst):
                if (search.get()).lower() in (fnameinfo_lst[i]).lower() or (search.get()).lower() in (lnameinfo_lst[i]).lower():
                    mytree_info.insert('', 'end', values=(fnameinfo_lst[i], lnameinfo_lst[i]))

        def changeinfo():
            # Function
            def update_change():
                # Variable
                nonlocal select_fname

                if not fname.get():
                    messagebox.showwarning("Register Fail:","Please Enter Your First Name")
                elif not lname.get():
                    messagebox.showwarning("Register Fail:","Please Enter Your Last Name")
                elif not age.get() :
                    messagebox.showwarning("Register Fail:","Please Enter Your Age")
                elif not height.get() :
                    messagebox.showwarning("Register Fail:","Please Enter Your Height")
                elif not weight.get() :
                    messagebox.showwarning("Register Fail:","Please Enter Your Weight")
                else:
                    # Check age type
                    if check_input_type(age.get()) != 'int':
                        messagebox.showwarning("Register Fail:","Age Should be full number")
                        age.focus_force()
                    else:
                        # Check if age < 0
                        if int(age.get()) < 0:
                            messagebox.showwarning("Register Fail:","Age Should not be lower than 0")
                            age.focus_force()
                        else:
                            # Check Height type
                            if check_input_type(height.get()) == 'str':
                                messagebox.showwarning("Register Fail:","Height Should be Numeric.")
                                height.focus_force()
                            else:
                                # Check if height < 0
                                if float(height.get()) < 0:
                                    messagebox.showwarning("Register Fail:","Height Should not be lower than 0")
                                    height.focus_force()
                                else:
                                    # Check weight type
                                    if check_input_type(weight.get()) == 'str':
                                        messagebox.showwarning("Register Fail:","Weight Should be Numeric.")
                                        weight.focus_force()
                                    else:
                                        # Check if weight < 0
                                        if float(weight.get()) < 0:
                                            messagebox.showwarning("Register Fail:","Height Should not be lower than 0")
                                            height.focus_force()       
                                        else:
                                            ans = messagebox.askyesno("Save Change", "Do you want to save change.")
                                            if ans == 'no':
                                                None
                                            else:
                                                # Save new info to database
                                                sql = '''
                                                            update patient
                                                            set Fname=?, Lname=?, Gender=?, Age=?, Height=?, Weight=?
                                                            where id=?
                                                '''
                                                cursor.execute(sql, [fname.get(), lname.get(), chooseGender, age.get(), height.get(), weight.get(), select_id])
                                                conn.commit()
                                                messagebox.showinfo("Change Complete:","Change Save.")
                                                showinfo_frame.destroy()
                                                updateinfo.destroy()

            # Variable
            nonlocal select_id, select_fname, select_lname, select_gender, select_age, select_height, select_weight
            chooseGender = select_gender

            # Create Update Info Frame
            updateinfo=Frame(doctor_frame,height=450,width=600,bg="#9bccc4")
            updateinfo.place(x=205,y=0)

            # Create Label
            Label(updateinfo,image=blueframe,bg="#9bccc4").place(x=-2,y=-2)
            Label(updateinfo,text="Firstname  :",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=80)
            Label(updateinfo,text="Lastname  :",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=130)
            Label(updateinfo,text="Gender      : ",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=180)
            Label(updateinfo,text="Age           :",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=230)
            Label(updateinfo,text="Height       : ",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=280)
            Label(updateinfo,text="Weight      : ",bg="#d7e3e3",font="Tahoma 12 bold").place(x=150,y=330)

            # Create Button
            Button(updateinfo,width=7,text = "UPDATE",bg="#50988d",font="Tahoma 12", command=update_change).place(x=260,y=380)
            Button(updateinfo,image=imgexitsee,bd=0,bg="#d7e3e3",activebackground = "#d7e3e3", command=updateinfo.destroy).place(x=500,y=34)

            # Create Entry
            fname = Entry(updateinfo,width=30)
            fname.place(x=265,y=80,relheight=0.055)
            fname.insert(0,select_fname)
            lname = Entry(updateinfo,width=30)
            lname.place(x=265,y=130,relheight=0.055)
            lname.insert(0,select_lname)

            # Create Combobox
            gender = ttk.Combobox(updateinfo, values=genderlst, state='readonly', textvariable=chooseGender,width=27)
            gender.place(x=265,y=180,relheight=0.055)
            gender.set(select_gender)

            # Create Entry
            age = Entry(updateinfo,width=30)
            age.place(x=265,y=230,relheight=0.055)
            age.insert(0,select_age)
            height = Entry(updateinfo,width=30)
            height.place(x=265,y=280,relheight=0.055)
            height.insert(0,select_height)
            weight = Entry(updateinfo,width=30)
            weight.place(x=265,y=330,relheight=0.055)
            weight.insert(0,select_weight)

        

        def treeviewinfoclick(event) :
            global select_customer, select_customer_ID
            nonlocal select_id, select_fname, select_lname, select_gender, select_age, select_height, select_weight, showinfo_frame

            # Create Show Full Info Frame
            showinfo_frame=Frame(doctor_frame,height=450,width=600,bg="#9bccc4")
            showinfo_frame.place(x=205,y=0)

            # Import Data from Database
            values = mytree_info.item(mytree_info.focus(),'values')
            cursor.execute("SELECT * FROM patient WHERE Fname=? AND Lname=?",[values[0],values[1]])
            result = cursor.fetchone()

            select_id = result[0]
            select_fname = result[1]
            select_lname = result[2]
            select_gender = result[3]
            select_age = str(result[4])
            select_height = str(result[5])
            select_weight = str(result[6])
            select_customer_ID = result[0]
            select_customer = select_fname+"  "+select_lname
            # Create Label
            Label(showinfo_frame,image=bginfo,bg="#9bccc4").place(x=-2,y=-2)
            
            
            # Show Profile Image ************************************************************
            if select_gender.lower() == "female":  
                Label(showinfo_frame,image=fprofile,bg="#65c8ff",bd=0,height=113,width=102).place(x=244,y=49)

            else:
                Label(showinfo_frame,image=mprofile,bg="#9bccc4",bd=0,height=113,width=102).place(x=244,y=49)


            Label(showinfo_frame,text="Name      : "+select_fname+"  "+select_lname,bg="#d7e3e3",font="Tahoma 11 bold").place(x=210,y=200)
            Label(showinfo_frame,text="Gender   : "+select_gender,bg="#d7e3e3",font="Tahoma 11 bold").place(x=210,y=235)
            Label(showinfo_frame,text="age          : "+select_age,bg="#d7e3e3",font="Tahoma 11 bold").place(x=210,y=270)
            Label(showinfo_frame,text="Height    : "+select_height,bg="#d7e3e3",font="Tahoma 11 bold").place(x=210,y=305)
            Label(showinfo_frame,text="Weight   : "+select_weight,bg="#d7e3e3",font="Tahoma 11 bold").place(x=210,y=340)

            # Create Button
            Button(showinfo_frame,text="update",bg="#50988d",width=10,height=2,command=changeinfo).place(x=460,y=370)
            Button(showinfo_frame,image=imglogout,bg="#d7e3e3",bd=0,command=showinfo_frame.destroy).place(x=40,y=375)

        # Variable
        idinfo_lst = []
        fnameinfo_lst = []
        lnameinfo_lst = []
        select_id = None
        select_fname = None
        select_lname = None
        select_gender = None
        select_age = None
        select_height = None
        select_weight = None
        showinfo_frame = None


        # Create Info Frame
        info_frame = Frame(doctor_frame,height=450,width=600,bg="#9bccc4")
        info_frame.place(x=205,y=0)

        # Create Label
        Label(info_frame,bg="#50988d").place(x=306,y=39,relheight=0.077,relwidth=0.076)

        # Create Button
        Button(info_frame,image=imgsearch,bg="#83c7bd",activebackground = "#abd4ce",bd=0.38,command=searchinfo).place(x=308,y=41,relheight=0.068,relwidth=0.07)
        
        # Create Entry
        search = Entry(info_frame,bg="#d7fcfd",font="Tahoma 17")
        search.place(x=60,y=40,relheight=0.07,relwidth=0.4)

        # Call Treeview Info To Display Treeview
        mytree_info = treeviewinfo()

    def stock():
        # Stock Window Function
        def add_data():
            # Access Database   
            cursor.execute("SELECT * FROM medical")
            result = cursor.fetchall()

            # Add data from Database to list
            for i,data in enumerate(result):
                IDstocklst.append(data[0])
                namestock_lst.append(data[1])
                pricestock_lst.append(float(data[2]))
                amtstock_lst.append(int(data[3]))

        def treeview():
            # Variable
            nonlocal add_data
            # Create Treeview Frame
            treeframe_stock = Frame(stock_frame)
            treeframe_stock .place(x=40,y=60)

            # Create Scrollbar
            treebar = Scrollbar(treeframe_stock)
            treebar.pack(side=RIGHT,fill=Y)
            mytree_stock = ttk.Treeview(treeframe_stock,columns=("name","price","amount"),height=10,yscrollcommand=treebar.set)
            mytree_stock.pack()

            # Config scrollbar on the treeview
            treebar.config(command=mytree_stock.yview)

            # Rename Headings
            mytree_stock.heading("#0",text="",anchor=W)
            mytree_stock.heading("name",text="Name",anchor=CENTER)
            mytree_stock.heading("price",text="Price",anchor=CENTER)
            mytree_stock.heading("amount",text="Amount",anchor=CENTER)
        
            # AdjustColumn Size
            mytree_stock.column("#0",width=0,minwidth=0)
            mytree_stock.column("name",anchor=W,width=300,minwidth=300)
            mytree_stock.column("price",anchor=E,width=100,minwidth=100)
            mytree_stock.column("amount",anchor=E,width=100,minwidth=100)

            # Reset Treeview
            mytree_stock.delete(*mytree_stock.get_children()) 

            add_data()

            # Add data form list to Treeview
                
            for i, data in enumerate(namestock_lst):
                mytree_stock.insert('', 'end', values=(namestock_lst[i], pricestock_lst[i], amtstock_lst[i]))
            
            # Event Bind Treeview
            mytree_stock.bind('<Double-1>',treeviewstockclick)

            return mytree_stock
        
        def treeviewstockclick(event) :
            nonlocal origin_name
            # Delete Exist Information in Entry
            namemed.delete(0,END)
            price.delete(0,END)
            amount.delete(0,END)

            values = mytree_stock.item(mytree_stock.focus(),'values')

            origin_name = values[0]
            # Insert Select Information into Entry
            namemed.insert(0,values[0])   
            price.insert(0,values[1])
            amount.insert(0,values[2])

        def search():

            # Reset Medical Stock Display
            mytree_stock.delete(*mytree_stock.get_children())

            # Reinsert Medical Stock Display
            for i, data in enumerate(namestock_lst):
                if (serch_stock.get().lower()) in (namestock_lst[i]).lower():
                    mytree_stock.insert('', 'end', values=(namestock_lst[i], pricestock_lst[i], amtstock_lst[i]))

        def add() :
            correction = check_input(namemed.get(),price.get(),amount.get(),'added')

            if correction == True:
                
                if namemed.get() in namestock_lst:
                    msg = messagebox.askquestion('Unsuccessfully Added','This Medicine is already existed, do you want to update old info?')
                    if msg == 'yes':
                        update()
                else:       
                    mytree_stock.insert('',index='end',values=(namemed.get(),price.get(),amount.get()))
                    cursor.execute("INSERT INTO medical (name,price,amount) VALUES (?,?,?)",(namemed.get(),price.get(),amount.get()))
                    conn.commit()
                    messagebox.showinfo("Succesfully Added","Succesfully Added new Medicine to Stock")
                    # Clear Existed list Data
                    IDstocklst.clear()
                    namestock_lst.clear()
                    pricestock_lst.clear()
                    amtstock_lst.clear()

                    # Add data to list
                    add_data()
                    # Clear Every Entry on Stock Page
                    clear()

        def update() :
            correction = check_input(namemed.get(),price.get(),amount.get(),'updated')
            
            if correction == True:
                selected = mytree_stock.focus()
                mytree_stock.item(selected,text="",values=(namemed.get(),price.get(),amount.get(), IDstocklst[namestock_lst.index(origin_name)]))

                sql = '''
                        update medical
                        set  name=?, price=? , amount =?
                        where id=?
                '''

                cursor.execute(sql,[namemed.get(),price.get(),amount.get(), IDstocklst[namestock_lst.index(origin_name)]])
                conn.commit()

                messagebox.showinfo("Admin:","Update succesfully")
                namemed.delete(0,END)
                price.delete(0,END)
                amount.delete(0,END)

        def remove() :
            deleterow = mytree_stock.selection()
            values = mytree_stock.item(mytree_stock.focus(),'values')
            print(values[0])
            sql = "delete from medical where name=?"
            mytree_stock.delete(deleterow)
            cursor.execute(sql,[values[0]])
            conn.commit()
            messagebox.showinfo("Admin:","Delete succesfully")
            clear()

        def clear():
            serch_stock.delete(0,END)
            namemed.delete(0,END)
            price.delete(0,END)
            amount.delete(0,END)

        def check_input(name, price, amt, str_type):
            # Check any if empty entry
            if len(name) == 0:
                messagebox.showwarning("Unsuccessfully"+str_type,"Please Enter Medicine Name")
                return False
            elif len(price) == 0:
                messagebox.showwarning("Unsuccessfully"+str_type,"Please Enter Medicine Price")
                return False
            elif len(amt) == 0:
                messagebox.showwarning("Unsuccessfully"+str_type,"Please Enter Medicine Amount")
                return False
            else:
                # Check any wrong input
                try:
                    # Check if price is numeric 
                    price = float(price)
                    try:
                        # Check if amount is integer
                        amt = float(amt)
                        try:
                            # Check if amount is float
                            amt = int(amt)
                            if price < 0:
                                messagebox.showwarning('Unsuccessfully'+str_type,'Price Should not be negative.')
                                return False
                            else:
                                if amt < 0:
                                    messagebox.showwarning('Unsuccessfully'+str_type,'Amount Should not be negative.')
                                    return False
                                else:
                                    return True
                        # Amount is not integer Error Message Popup
                        except ValueError:
                            messagebox.showwarning('Unsuccessfully'+str_type,'Amount Should be a Whole Number.')
                            return False
                    except ValueError:
                        messagebox.showwarning('Unsuccessfully'+str_type,'Amount Should be Numeric.')
                        return False
                # Price is not numeric Error Message Popup
                except ValueError:
                    messagebox.showwarning('Unsuccessfully'+str_type,'Price Should be Numeric.')
                    return False

        # Variable
        IDstocklst = []
        namestock_lst = []
        pricestock_lst = []
        amtstock_lst = []
        origin_name = None

        # Create Stock Frame
        stock_frame=Frame(doctor_frame,height=450,width=600,bg="#9bccc4")
        stock_frame.place(x=205,y=0)

        # Create Stock Frame Label
        Label(stock_frame,bg="#50988d").place(x=290,y=18,relheight=0.077,relwidth=0.076)
        Button(stock_frame,image=imgsearch,bg="#83c7bd",activebackground = "#abd4ce",bd=0.38,command=search).place(x=292,y=20,relheight=0.068,relwidth=0.07)
        serch_stock = Entry(stock_frame,bg="#d7fcfd",font="Tahoma 17")
        serch_stock.place(x=40,y=20,relheight=0.07,relwidth=0.4)

        # Create Stock Frame Button
        Button(stock_frame,text="Add ",width=15,height=2,command=add).place(x=35,y=400)
        Button(stock_frame,text="Update",width=15,height=2,command=update).place(x=175,y=400)
        Button(stock_frame,text="Delete",width=15,height=2,command=remove).place(x=315,y=400)
        Button(stock_frame,text="Clear",width=15,height=2,command=clear).place(x=455,y=400)

        # Create Entry Frame
        entry_frame = Frame(stock_frame,bg="#d7fcfd")
        entry_frame.place(x=40,y=300)

        # Create Entry Frame Label
        ccode= Label(entry_frame,text="Name",width=20,height=2,bg='DodgerBlue')
        ccode.grid(row=0,column=0,sticky='news')
        cname = Label(entry_frame,text="price",height=2,bg='DodgerBlue')
        cname.grid(row=0,column=1,sticky='news')
        cd = Label(entry_frame,text="amount",height=2,bg='DodgerBlue')
        cd.grid(row=0,column=2,sticky='news')
        
        # Create Entry Frame Entry
        namemed = Entry(entry_frame,justify=CENTER)
        namemed.grid(row=1,column=0,ipady=10,ipadx=69)
        price = Entry(entry_frame,justify=CENTER)
        price.grid(row=1,column=1,ipady=10,ipadx=2)
        amount = Entry(entry_frame,justify=CENTER)
        amount.grid(row=1,column=2,ipady=10,ipadx=2)

        mytree_stock = treeview()

    # Create Doctor Window Frame
    doctor_frame=Frame(window,height=450,width=800)
    doctor_frame.place(x=0,y=0)

    # Create Label
    Label(doctor_frame,image=bgdoctor).place(x=-2,y=-2)

    # Create Button
    Button(doctor_frame,text="Info",font="Tahoma 15",command=info).place(x=40,y=50,relwidth=0.15,relheight=0.1)
    Button(doctor_frame,text="Dispense",font="Tahoma 15", command=dispensationWindow).place(x=40,y=150,relwidth=0.15,relheight=0.1)
    Button(doctor_frame,text="Stock",font="Tahoma 15",command=stock).place(x=40,y=250,relwidth=0.15,relheight=0.1)
    Button(doctor_frame,text="Logout",font="Tahoma 15",command=doctor_frame.destroy).place(x=40,y=350,relwidth=0.15,relheight=0.1)

# Medicine Dispense Window
def dispensationWindow():

    # Function
    def datalst():
        sql = 'select * from medical'
        cursor.execute(sql)
        result = cursor.fetchall()
        
        # Add and change input type to list 
        for i,data in enumerate(result):
            id_lst.append(data[0])
            name_lst.append(data[1])
            price_lst.append(float(data[2]))
            amt_lst.append(int(data[3]))   

    def appointmentFrame():
        # Variable
        nonlocal appDate
        nonlocal appMonth
        nonlocal appYear
        datelst = []
        monthlst = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        yearlst = []

        # Create Frame
        
        Label(dispenseFrame, text='Next Appointment Date : ',bg="#daf7fa").place(x=30,y=350)

        # Add date and year to datelst yearlst
        for i in range(1, 32):
            datelst.append(i)
        for i in range(2021, 2101):
            yearlst.append(i)



        # Create Combobox
        dateCombo = ttk.Combobox(dispenseFrame, values=datelst, textvariable=appDate, state='readonly',width=15,height=2)
        dateCombo.set('Date')
        dateCombo.place(x=30,y=380)

        monthCombo = ttk.Combobox(dispenseFrame, values=monthlst, textvariable=appMonth, state='readonly',width=15,height=2)
        monthCombo.set('Month')
        monthCombo.place(x=144,y=380)

        yearCombo = ttk.Combobox(dispenseFrame, values=yearlst, textvariable=appYear, state='readonly',width=15,height=2)
        yearCombo.set('Year')
        yearCombo.place(x=258,y=380)

    def refreshDisplay():
        # Variable
        nonlocal id_lst
        nonlocal name_lst
        nonlocal price_lst
        nonlocal amt_lst

        # Reset Medical Stock Display
        mediDisplay.delete(*mediDisplay.get_children())

        # Reinsert Medical Stock Display
        for i, data in enumerate(name_lst):
            if (search_box.get()).lower() in (name_lst[i]).lower():
                mediDisplay.insert('', 'end', values=(id_lst[i], name_lst[i], price_lst[i], amt_lst[i]))

    def createDisplay():
        # Create TreeView Frame
        displayFrame = Frame(dispenseFrame,width=140,height=100)
        displayFrame.place(x=490,y=75)
        
        # Create Scrollbar
        displaybar = Scrollbar(displayFrame)
        displaybar.pack(side=RIGHT,fill=Y)
        mediDisplay = ttk.Treeview(displayFrame,columns=('ID','Name', 'Price', 'Amount'),yscrollcommand=displaybar.set)
        mediDisplay.pack()

        # Config scrollbar on the treeview
        displaybar.config(command=mediDisplay.yview)

        # Rename Headings
        mediDisplay.heading("#0",text="",anchor=W)
        mediDisplay.heading("ID",text="ID",anchor=W)
        mediDisplay.heading("Name",text="Name",anchor=W)
        mediDisplay.heading("Price",text="Price",anchor=CENTER)
        mediDisplay.heading("Amount",text="Amount",anchor=W)

        # AdjustColumn Size
        mediDisplay.column("#0",width=0,minwidth=0)
        mediDisplay.column("ID",anchor=W,width=0,minwidth=0)
        mediDisplay.column("Name",anchor=W,width=120)
        mediDisplay.column("Price",anchor=CENTER,width=40)
        mediDisplay.column("Amount",anchor=W,width=55)

        # Reset Treeview
        mediDisplay.delete(*mediDisplay.get_children())

        # Insert Treeview Data
        for i, data in enumerate(id_lst):
            mediDisplay.insert('', 'end', values=(id_lst[i], name_lst[i], price_lst[i], amt_lst[i]))

        return mediDisplay

    def createOrderDisplay():

        # Variable
        nonlocal orderIDlst
        nonlocal orderNamelst
        nonlocal orderPricelst
        nonlocal orderAmtlst
        nonlocal ordertotalpricelst

        # Create TreeView Frame
        displayFrame = Frame(dispenseFrame,width=100,height=100)
        displayFrame.place(x=50,y=60)
        #   เพิ่มสีในtreeview
        sty = ttk.Style()
        sty.theme_use("default")
        sty.configure("Treeview",
        background = "#b0e5ea",
        foreground = "black",
        fieldbackground = "#b0e5ea"
        )
        sty.map('Treeview',background = [('selected','#5ab5be')])

        # Create Scrollbar
        displaybar = Scrollbar(displayFrame)
        displaybar.pack(side=RIGHT,fill=Y)
        orderDisplay = ttk.Treeview(displayFrame,columns=('ID','Name', 'Price', 'Amount', 'Total Price'),yscrollcommand=displaybar.set)
        orderDisplay.pack()

        # Config scrollbar on the treeview
        displaybar.config(command=orderDisplay.yview)

        # Rename Headings
        orderDisplay.heading("#0",text="",anchor=W)
        orderDisplay.heading("ID",text="ID",anchor=W)
        orderDisplay.heading("Name",text="Name",anchor=W)
        orderDisplay.heading("Price",text="Price",anchor=CENTER)
        orderDisplay.heading("Amount",text="Amount",anchor=W)
        orderDisplay.heading("Total Price",text="Total Price",anchor=W)

        # AdjustColumn Size
        orderDisplay.column("#0",width=0,minwidth=0)
        orderDisplay.column("ID",anchor=W,width=0,minwidth=0)
        orderDisplay.column("Name",anchor=W,width=110)
        orderDisplay.column("Price",anchor=CENTER,width=40)
        orderDisplay.column("Amount",anchor=W,width=56)
        orderDisplay.column("Total Price",anchor=W,width=80)

        # Reset Treeview
        orderDisplay.delete(*orderDisplay.get_children())

        # Insert Treeview Data
        for i, data in enumerate(orderIDlst):
            index = i-1
            orderDisplay.insert('', 'end', values=(orderIDlst[index], orderNamelst[index], orderPricelst[index], orderAmtlst[index], ordertotalpricelst[index]))

    def clickOrder(event):

        def confirmOrder(amt):
            # name = value[2], amt = disamt_box.get()
            # Variable
            nonlocal selectName
            nonlocal id_lst
            nonlocal name_lst
            nonlocal price_lst
            nonlocal amt_lst
            nonlocal ordertotalpricelst
            nonlocal confirmWin

            amt = int(amt)

            # Check if amt is 0 Cancel
            if amt == 0:
                cancelOrder()
            else:
                # Find Select Name Index
                select_index = name_lst.index(selectName)

                # Change Available Amount
                newamt = amt_lst[select_index]-int(amt)
                amt_lst[select_index] = newamt
                total_price = amt*price_lst[select_index]

                # Add Select Row to order list(orderIDlst, orderNamelst, orderPricelst, orderAmtlst)

                orderIDlst.append(id_lst[select_index])
                orderNamelst.append(name_lst[select_index])
                orderPricelst.append(price_lst[select_index])
                orderAmtlst.append(amt)
                ordertotalpricelst.append(total_price)

                setnew_total(total_price)

                # Refresh Right Display
                refreshDisplay()

                # Refresh Left Display
                createOrderDisplay()
                # Close order window
                confirmWin.destroy()
                confirmWin = None

        def cancelOrder():
            nonlocal confirmWin
            confirmWin.destroy()
            confirmWin = None
        
        def check_input(event):
            # Combobox List
            value = event.widget.get()

            if value == '':
                disamt_box['values'] = avl_lst
            else:
                data = []
                for item in avl_lst:
                    if value.lower() in item.lower():
                        data.append(item)

                disamt_box['values'] = data

        # import value from mediDisplay
        values = mediDisplay.item(mediDisplay.focus(),'values')

        # Import Select name
        selectName = values[1]
        
        # Variable
        avl_lst = []
        amt = IntVar()
        nonlocal name_lst
        nonlocal amt_lst
        nonlocal confirmWin

        # Find Select Name Index and find available amount
        select_index = name_lst.index(selectName)
        avl_amt = amt_lst[select_index]

        # Add Number to avl_lst
        for i in range(1, (avl_amt+1)):
            avl_lst.append(i)

        # Check Exist Confirm Window
        if confirmWin != None:
            return None
        

        # Create Confirm Window parent is 'window', value[1] is medical Name
        confirmWin = Toplevel(window)
        confirmWin.geometry("280x100")
        confirmWin.configure(bg='#daf7fa')
        Label(confirmWin, text=values[1],font="Tahoma 12 ",bg='#daf7fa').place(x=10,y=0)
        Label(confirmWin, text='Dispense Amount :',bg='#daf7fa').place(x=10,y=30)

        # Dispense amount combo box
        disamt_box = ttk.Combobox(confirmWin, textvariable=amt, state='readonly')
        disamt_box['values'] = avl_lst
        disamt_box.bind('<KeyRelease>', check_input)
        disamt_box.place(x=130,y=32)

        # Exit and Confirm 
        exbt = Button(confirmWin, text = 'Cancel', command=cancelOrder)
        exbt.place(x=50,y=60)
        cfbt = Button(confirmWin, text = 'Confirm', command=lambda:confirmOrder(amt.get()))
        cfbt.place(x=170,y=60)

    def saveData():
        msg = messagebox.askquestion('Confirm Order','Confirm Order')
        if msg == 'no':
            return None
        else:
            # save new stock in database
            for i, data in enumerate(orderIDlst):
                sql = '''
                                update medical
                                set amount=?
                                where name=?
                    '''
                cursor.execute(sql, [amt_lst[i], name_lst[i]])

            date = appDate.get() + appMonth.get() + appYear.get()
            
            # Save new appointment date in data base 
            sql = '''
                            update patient
                            set Date=?
                            where id=?
                '''
            cursor.execute(sql, [date, select_customer_ID])

            conn.commit()




            # destroy old window
            # HAVE NOT DONE *******************************************
    
    def setnew_total(cost):
        nonlocal total_cost
        total_cost += cost
        total_var.set(total_cost)


    # Variable
    confirmWin = None
    orderIDlst = []
    orderNamelst = []
    orderAmtlst = []
    orderPricelst = []
    ordertotalpricelst = []
    id_lst = []
    name_lst = []
    price_lst = []
    amt_lst = []
    appDate = StringVar()
    appMonth = StringVar()
    appYear = StringVar()
    total_var = StringVar()
    total_cost = 0

    # Import data in database to list(id_lst, name_lst, price_lst, amt_lst)
    datalst()

    # Create Dispense, left, right Frame 'window' is parent
    dispenseFrame = Frame(window,width=800,height=450,bg="#A4CFD0")
    
    Label(dispenseFrame,image=img,bg="#A4CFD0").place(x=-2,y=-2)
    Label(dispenseFrame,text="Total Price  :",font="Tahoma 12 ",bg="#daf7fa").place(x=70,y=305)
    Label(dispenseFrame, textvariable=total_var,width=15,height=2,bg="#7edce7").place(x=190,y=300)
 
    # choose customer
    Label(dispenseFrame, text='Customer Name : ',bg="#daf7fa").place(x=40,y=30)

    # Add Label Customer Name HERE ****************************************************************************
    Label(dispenseFrame,text=select_customer,font="Tahoma 12 ",bg="#daf7fa").place(x=140,y=28)
    
    # Show order
    createOrderDisplay()

    # Appointment Date
    appointmentFrame()

    # RIGHT FRAME ----------------------
    # medical serch box
    Label(dispenseFrame, text='Medical Name : ',bg="#daf7fa").place(x=450,y=32)
    Label(dispenseFrame,bg="#5baab2").place(x=547,y=29,relwidth=0.207,relheight=0.060)
    search_box = Entry(dispenseFrame, width=20,font="Tahoma 12 bold",bd=0)
    search_box.place(x=550,y=32,relwidth=0.2)

    search_bt = Button(dispenseFrame,image=searchimg,bg="#b1d5d9",command=refreshDisplay)
    search_bt.place(x=720,y=26)

    # Medical Stock
    mediDisplay = createDisplay()
    mediDisplay.bind('<Double-1>',clickOrder)

    # CANCEL Button Function Command *******************************************
    Button(dispenseFrame, text='back', command=dispenseFrame.destroy).place(x=560,y=340,relheight=0.10,relwidth=0.10)
    Button(dispenseFrame, text='Confirm', command=saveData).place(x=660,y=340,relheight=0.10,relwidth=0.10)
    # Place Dispense Frame in window
    dispenseFrame.place(x=0,y=0)

# Import Image
def import_img():
    global icon1, bglogin, bgregis, exitregis, imgseebg, imgexitsee, bgdoctor, imgsearch, bginfo, imglogout, img_boss
    global img_close, bossregis, back_img, img_nurse, blueframe, searchimg, img, fprofile, mprofile
    icon1 = PhotoImage(file="images/icon.png")
    bglogin = PhotoImage(file="images/bglogin.png")
    bgregis = PhotoImage(file="images/regis.png")
    exitregis = PhotoImage(file="images/exitregis.png")
    imgseebg = PhotoImage(file="images/imgseebg.png")
    imgexitsee= PhotoImage(file="images/exitsee.png")
    bgdoctor = PhotoImage(file="images/bgdoctore.png")
    imgsearch = PhotoImage(file="images/search.png").subsample(2)
    bginfo=PhotoImage(file="images/bginfo.png")
    imglogout=PhotoImage(file="images/logoutuser.png")
    img_boss=PhotoImage(file="images/boss.png")
    img_close=PhotoImage(file="images/close.png").subsample(20)
    bossregis = PhotoImage(file="images/regisboss.png")
    back_img = PhotoImage(file="images/back.png").subsample(10)
    img_nurse= PhotoImage(file="images/nurse.png")
    blueframe = PhotoImage(file="images/updateinfo.png")
    searchimg =PhotoImage(file="images/searchs.png").subsample(40)
    img = PhotoImage(file="images/notes.png")
    fprofile= PhotoImage(file="images/profile_f.png")
    mprofile= PhotoImage(file="images/profile.png")

# Main Code
createconnection()
window = create_window()
main_window()

global genderlst, select_customer, select_customer_ID
genderlst = ['Male', 'Female']
select_customer = None
select_customer_ID = None

window.mainloop()
cursor.close()
conn.close()

