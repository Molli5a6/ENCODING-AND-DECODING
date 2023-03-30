#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 
from tkinter.ttk import * 
from time import strftime
from tkinter import *
import base64
from tkinter import *
import tkinter.font


# In[2]:


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair - Message Encode and Decode")


# In[3]:


Label(root, text = 'ENCODE DECODE', font = 'arial 20 bold').pack()

Label(root, text = 'DataFlair',font = 'arial 20 bold').pack(side =BOTTOM)


# In[4]:


Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


# In[5]:


def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# In[6]:


def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)


# In[7]:


def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


# In[8]:


def Exit():
    root.destroy()


# In[9]:


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# In[ ]:


Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()


# In[ ]:




