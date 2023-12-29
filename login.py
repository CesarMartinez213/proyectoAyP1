#import tkinter as Tk
from tkinter import *
#from PIL import Image, ImageTk
from tkinter import messagebox

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def singin():
    Cédula=user.get()
    Contraseña=code.get()

    if (Cédula == '30857225') and (Contraseña == '1234'):
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')

        Label(screen, text='Hello Everyone', bg='#fff' ,font=('Calibri (Body)',50,'bold')).pack(expand=True)

        screen.mainloop()
    elif (Cédula !='30857225') and (Contraseña !='1234'):
        messagebox.showerror("Invalid", "Cédula y contraseña invalidas")
    
    elif (Contraseña!='1234'):
        messagebox.showerror("Invalid", "Contraseña invalida")

    elif (Cédula!='30857225'):
        messagebox.showerror("Invalid", "Cédula invalida")

img = PhotoImage(file='login.png')

Label(root,image=img, bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

'''# Carga y reducción de la imagen
imag = Image.open('logo.png')
imag = imag.resize((imag.width // 2, imag.height // 2))
photo = ImageTk.PhotoImage(imag)

#medidas de el logo en bytes
frame_width = width = 774
frame_height = height = 242

# Cálculo de coordenadas para centrar
#x = (frame_width - photo.width()) // 2
#y = (frame_height - photo.height()) // 2

# Creación del Label con la imagen centrada
heading = Label(frame, image=photo, bg='white')
heading.place(x=350, y=350)'''

heading = Label(frame , text='Inicio de Sesión' , fg='#57a1f8' , bg='white' , font=('Microsoft YaHei UI Light' , 23,'bold'))
heading.place(x=50,y=5)

#######--------------------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Cédula')

user = Entry(frame, width=25 ,fg='black' ,border=0, bg='white' ,font=('Microsoft YaHei UI Light' ,11))
user.place(x=30 ,y=80)
user.insert(0,'Cédula')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

#######--------------------------------------------------------------------

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Contraseña')

code = Entry(frame, width=25 ,fg='black' ,border=0, bg='white' ,font=('Microsoft YaHei UI Light' ,11))
code.place(x=30 ,y=150)
code.insert(0,'Contraseña')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)
######----------------------------------------------------------------------

Button(frame, width=39, pady=7, text='Iniciar Sesion', bg='#57a1f8', fg='white', border=0, command=singin).place(x=35,y=204)
label=Label(frame, text='¿no esta registrado?', fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=50,y=270)

sing_up= Button(frame, width=12, text='Registrate Aqui', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sing_up.place(x=190, y=270)





root.mainloop()