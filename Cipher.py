from tkinter import *

import mysql.connector
import random                                                                
import time  
import datetime
import tkinter.ttk as ttk
import tkinter.messagebox as mb
 
root = Tk()

root['bg']='Black'
  
root.geometry("1600x1800")

root.title("CIPHER window")
  
Title = Frame(root, width = 1600, relief = SUNKEN, bg='Black') 
Title.pack() 
  
f1 = Frame(root, width = 1600, relief = SUNKEN, bg='Black') 
f1.pack()

b1 = Frame(root, height=1200, width = 1600, relief = SUNKEN, bg='Black') 
b1.pack() 
  
date = datetime.datetime.now()
time= print (date.strftime("%Y-%m-%d %H:%M:%S"))
  
lblInfo = Label(Title, font = ('Times new roman', 50, 'bold'), text = "CIPHER WINDOW", fg = "Orange", bg='Black', bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
  
lblInfo = Label(Title, font=('Times new roman', 20, 'bold'), text = date, fg = "Orange", bg='Black', bd = 10, anchor = 'w') 
                          
lblInfo.grid(row = 1, column = 0)
  
name = StringVar() 
text = StringVar() 
code = StringVar() 
mode = StringVar() 
Result = StringVar()

def Save_database():
    if  txtname.get() == "" or txttext.get() == "" or txtcode.get() == "" or txtmode.get() == "":
        result = mb.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
         date = datetime.datetime.now()
         con=mysql.connector.connect(host='localhost', user='root', passwd='Useradmin@123')
         mycrsr=con.cursor()
         mycrsr.execute('CREATE DATABASE IF NOT EXISTS CIPHER')
         mycrsr.execute('USE CIPHER')
         mycrsr.execute('CREATE TABLE IF NOT EXISTS CIPHER_MSG_DATA(En_Name VARCHAR(20), En_Data VARCHAR(200), Acc_code VARCHAR(30), E_or_D VARCHAR(2), Result VARCHAR(200));')
         mycrsr.execute("INSERT INTO CIPHER_MSG_DATA (En_Name, En_Data, Acc_code, E_or_D, Result) VALUES(%s,%s,%s,%s,%s);", (str(name.get()), str(text.get()), str(code.get()), str(mode.get()), str(Result.get())))
         con.commit()
         mycrsr.close()
         con.close()
         name.set("")
         text.set("")
         code.set("")
         mode.set("")
         Result.set("")

def Exit(): 
    root.destroy() 

def Reset(): 
    name.set("") 
    text.set("") 
    code.set("") 
    mode.set("") 
    Result.set("") 
  
  
lblname = Label(f1, font = ('Times new roman', 16, 'bold'), text = "Name:", fg='Orange', bg='Black', bd = 16, anchor = "w") 
lblname.grid(row = 1, column = 0) 
txtname = Entry(f1, font = ('Times new roman', 16, 'bold'), textvariable = name, bd = 10, insertwidth = 4, bg = "white", justify = 'right') 
txtname.grid(row = 1, column = 1) 
    
lbltext = Label(f1, font = ('Times new roman', 16, 'bold'), text = "Text:", fg='Orange', bg='Black', bd = 16, anchor = "w") 
lbltext.grid(row = 2, column = 0) 
txttext = Entry(f1, font = ('Times new roman', 16, 'bold'), textvariable = text, bd = 10, insertwidth = 4, bg = "white", justify = 'right') 
txttext.grid(row = 2, column = 1) 
  
lblcode = Label(f1, font = ('Times new roman', 16, 'bold'), text = "Access Code:", fg='Orange',bg='Black', bd = 16, anchor = "w") 
lblcode.grid(row = 3, column = 0) 
txtcode = Entry(f1, font = ('Times new roman', 16, 'bold'), textvariable = code, bd = 10, insertwidth = 4, bg = "white", justify = 'right') 
txtcode.grid(row = 3, column = 1) 
  
lblmode = Label(f1, font = ('Times new roman', 16, 'bold'), text = "Encrypt(e)/Decrypt(d) (Enter e/d))", fg='Orange', bg='Black', bd = 16, anchor = "w") 
lblmode.grid(row = 4, column = 0) 
txtmode = Entry(f1, font = ('Times new roman', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, bg = "white", justify = 'right') 
txtmode.grid(row = 4, column = 1) 
  
lblResult = Label(f1, font = ('Times new roman', 16, 'bold'), text = "Converted Text", fg='Orange', bg='Black', bd = 16, anchor = "w") 
lblResult.grid(row = 6, column = 0) 
txtResult = Entry(f1, font = ('Times new roman', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, bg = "Yellow", justify = 'right') 
txtResult.grid(row = 6, column = 1) 
  
import base64 
  
def encode(code, clear): 
    enc = []
    for i in range(len(clear)): 
        code_c = code[i % len(code)] 
        enc_c = chr((ord(clear[i]) + ord(code_c)) % 256) 
        enc.append(enc_c) 
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
  
def decode(code, enc): 
    dec = [] 
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        code_c = code[i % len(code)] 
        dec_c = chr((256 + ord(enc[i]) - ord(code_c)) % 256) 
        dec.append(dec_c) 
    return "".join(dec) 
  
  
def Ref(): 
    print("Text= ", (text.get())) 
  
    clear = text.get() 
    c = code.get() 
    m = mode.get() 
  
    if (m == 'e'): 
        Result.set(encode(c, clear)) 
    else: 
        Result.set(decode(c, clear))
     
  
btnTotal = Button(b1, padx = 16, pady = 5, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Show Text", bg = "white", command = Ref).grid(row = 3, column = 0) 
  
btnReset = Button(b1, padx = 16, pady = 5, bd = 16, fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Reset", bg = "white", command = Reset).grid(row = 3, column = 1)
  
btnExit = Button(b1, padx = 16, pady = 5, bd = 16,  fg = "black", font = ('arial', 16, 'bold'), width = 10, text = "Exit", bg = "white", command = Exit).grid(row = 3, column = 3)

btnSave = Button(b1, padx=16, pady=5, text="Save", bd=16, fg="black", font= ('arial', 16, 'bold'), width=10, bg = "white", command=Save_database).grid(row=3, column=2) 

   
root.mainloop()





