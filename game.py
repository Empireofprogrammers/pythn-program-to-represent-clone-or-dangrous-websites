import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import *
import webbrowser
import pyautogui
import time
import sys
root=Tk()
ROOT = tk.Tk()
ROOT.withdraw()
E_mail = simpledialog.askstring(title="E-Mail",
                                  prompt="Enter your E-mail:- ")
Password =simpledialog.askstring(title="Password",
                                  prompt="Enter your Password:- ")
Google_email_and_password_db = {
    "bla@gmail.com":"74859jfkjr",
    "google@1234gmail.com":"Google is better than any one@123*3",
    "haritraiclass7@gmail.com":"security@123withKaliandpytho54r454r",
    "harit500@gmail.com":"1234!#hack"
    }
dark_web = {
    "bla@gmail.com":"74859jfkjr",
    "google@1234gmail.com":"Google is better than any one@123*3",
    }
def have_i_been_pawn(mail):
        if mail in Google_email_and_password_db.keys():
            if mail in dark_web:
                messagebox.showerror('Unsafe', 'You have been pawned')  
            else:     
                messagebox.showinfo('safe', 'You are safe on internet ')
        elif mail not in Google_email_and_password_db.keys():
            messagebox.showerror('Error',"Invalid E-mail")
def close_game():
    button['state'] = DISABLED
    pyautogui.click(739,225)
    time.sleep(1)
    pyautogui.hotkey("ctrl","w")
    E_mail_for_have_i_been_pawn = simpledialog.askstring(title="E-Mail",
                                  prompt="Enter your E-mail to check if has been pawned:- ")
    
    print(have_i_been_pawn(E_mail_for_have_i_been_pawn))
def close_app():
    sys.exit()
def online_gaming_site(your_email,password):
    global button
    if your_email in Google_email_and_password_db.keys():
        check = Google_email_and_password_db[your_email]
        if check == password:
            button = Button(root,text = "Stop Game",command=close_game)
            button.pack()
            button2 = Button(root,text = "Close app",command=close_app)
            button2.pack()
            if your_email not in dark_web:
                dark_web[your_email] = password
            webbrowser.open('https://diep.io/')
            root.mainloop()
        else:
            messagebox.showerror('Incorrect Details', 'Password is Incorrect')
    else:
        messagebox.showerror('Incorrect Details', 'Email is Incorrect')
online_gaming_site(E_mail,Password)
