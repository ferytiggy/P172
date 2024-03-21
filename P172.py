# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:31:58 2024

@author: Aidan
"""

from tkinter import *
root = Tk()
root.title("Herencia")
root.geometry("600x600")

label_name = Label(root, text="Nombre del usuario: ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Correo electrónico: ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root)

dictionary = {}
class Users: 
        
    def addUser(key, value): 
         global dictionary
         dictionary[key]=value
         label["text"]=dictionary
        

class GetUsers(Users): 
        
    def getUser(self):
        username = entry_name.get()
        email_id = entry_email.get()
        #accede a la función addUser de la clase users y dentro de ella pasa los parámetros como username, email_id.
        Users.addUser(username, email_id)

#Crea un objeto de la clase GetUsers.        
user = GetUsers()
btn = Button(root, text="Agregar detalles del usuario", command=user.getUser)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()