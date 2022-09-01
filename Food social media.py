import tkinter
from tkinter import *
from tkinter import messagebox
import filecmp
from tkinter.font import Font
import random

root = Tk()
root.geometry("400x400")
root.title("FSM")
log_in_frame = Frame(root)
register_frame = Frame(root)

def log_in():
    register_frame.pack_forget()
    root.resizable(False, False)
    log_in_frame.pack(fill="both", expand=True)
    root.geometry("400x200")
    root.title("FSM Login/register")
    head_line = Label(log_in_frame,text="Welcome to FSM!\nLog in or register to continue",font='Aril 20 underline')
    head_line.place(relx=0.17, rely=0.00)
    user_name_label = Label(log_in_frame, text="User name:", font='Aril 16')
    password_label = Label(log_in_frame, text="Password:", font='Aril 16')
    user_name_enter = Entry(log_in_frame, width=16)
    password_enter = Entry(log_in_frame, width=16, show="*")
    user_name_label.place(relx=0.06, rely=0.3)
    user_name_enter.place(relx=0.35, rely=0.3)
    password_label.place(relx=0.06, rely=0.5)
    password_enter.place(relx=0.35, rely=0.5)
    register_button = Button(log_in_frame,text="new account", font='Aril 16', command=register)
    register_button.place(relx=0.35, rely=0.8)
    def login_compare():
        data = str([user_name_enter.get(), password_enter.get()])
        log_in_save = open('login_chece.txt', 'w')
        log_in_save.write("%s\n" % data)
        log_in_save.close()
        f1 = '/Users/sara/Desktop/Py4id/register_chece.txt'
        f2 = '/Users/sara/Desktop/Py4id/login_chece.txt'
        result = filecmp.cmp(f1, f2)
        if result == True:
            messagebox.showinfo('Logged in :)', "welcome " + str(user_name_enter.get()) + "!")
            import SaraChocolateBalls
            SaraChocolateBalls
        elif result != True:
            messagebox.showerror('Error', 'User name\nor password are not correct.')
    log_in_button = Button(log_in_frame, text="log in", font='Aril 16', command=login_compare, width=9)
    log_in_button.place(relx=0.35, rely=0.66)





def register():
    register_frame.pack(fill="both", expand=True)
    log_in_frame.pack_forget()
    root.resizable(False, False)
    root.geometry("580x300")
    root.title("FSM register new account")
    head_line = Label(register_frame,text="Hello!\nFill out the following to become a new member!", font='Aril 22 underline')
    head_line.place(relx=0.15, rely=0)
    first_name_label = Label(register_frame, text="First name:", font='Aril 18')
    last_name_label = Label(register_frame, text="Last name:", font='Aril 18')
    user_name_label = Label(register_frame, text="User name:", font='Aril 18')
    password_label = Label(register_frame, text="password:", font='Aril 18')
    password_confirm_label = Label(register_frame, text="confirm password:", font='Aril 18')
    email_label = Label(register_frame, text="email:", font='Aril 18')
    first_name_enter = Entry(register_frame,width=20)
    last_name_enter = Entry(register_frame,width=20)
    user_name_enter = Entry(register_frame,width=20)
    password_enter = Entry(register_frame,width=20, show="*")
    password_confirm_enter = Entry(register_frame,width=20, show="*")
    email_enter = Entry(register_frame, width=20)
    first_name_label.place(relx=0.04, rely=0.25)
    first_name_enter.place(relx=0.3, rely=0.25)
    last_name_label.place(relx=0.04, rely=0.35)
    last_name_enter.place(relx=0.3, rely=0.35)
    user_name_label.place(relx=0.04, rely=0.45)
    user_name_enter.place(relx=0.3, rely=0.45)
    password_label.place(relx=0.04, rely=0.55)
    password_enter.place(relx=0.3, rely=0.55)
    password_confirm_label.place(relx=0.04, rely=0.65)
    password_confirm_enter.place(relx=0.3, rely=0.65)
    email_label.place(relx=0.04, rely=0.75)
    email_enter.place(relx=0.3, rely=0.75)
    def register_procces():
        uinput = str([first_name_enter.get(), last_name_enter.get(), user_name_enter.get(), password_enter.get(), email_enter.get()])
        rc1 = str([user_name_enter.get(), password_enter.get()])
        if len(first_name_enter.get()) == 0:
            messagebox.showerror('Error', 'Enter first name')
        elif len(last_name_enter.get()) == 0:
            messagebox.showerror('Error', 'Enter Last name')
        elif len(user_name_enter.get()) == 0:
            messagebox.showerror('Error', 'Enter valid user name')
        elif len(password_enter.get()) == 0:
            messagebox.showerror('Error', 'Choose password')
        elif password_enter.get() != password_confirm_enter.get():
            messagebox.showerror('Error', 'passwords are not matching')
        elif len(email_enter.get()) == 0:
            messagebox.showerror('Error', 'Enter valid email')
        else:
            u_info = open('register_chece.txt', 'w')
            u_info.write("%s\n" % rc1)
            u_info.close()
            messagebox.showinfo("Welcome! " + str(user_name_enter.get()), "Your new account\nis good to go!")
            all_info = open('user_info.txt', 'w')
            all_info.write("%s\n" % uinput)
            all_info.close()
            log_in()
    def login_start():
        log_in()
    register_button = Button(register_frame, text="creat new\naccount", font='Aril 16', command=register_procces, height=4)
    register_button.place(relx=0.7, rely=0.6)
    login_button = Button(register_frame, text="Log in\nwindow", font='Aril 16', command=login_start, height=4)
    login_button.place(relx=0.7, rely=0.3)




log_in()
root.mainloop()