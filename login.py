from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def singin():
    username=user.get()
    password=code.get()

    if username=='admin' and pasword=='1234':
        print('hello world')

img = PhotoImage(file='login.png')
img.zoom(2)

Label(root,image=img, bg='white').place(x=70,y=100)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text= 'Inicio de sesion' ,fg='#57a1f8' ,bg='white' ,font=('Microsoft YaHei UI Light' ,23, 'bold'))
heading.place(x=50,y=5)

#######--------------------------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Nombre de Usuario')

user = Entry(frame, width=25 ,fg='black' ,border=0, bg='white' ,font=('Microsoft YaHei UI Light' ,11))
user.place(x=30 ,y=80)
user.insert(0,'Nombre de Usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

#######--------------------------------------------------------------------

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Contrasena')

code = Entry(frame, width=25 ,fg='black' ,border=0, bg='white' ,font=('Microsoft YaHei UI Light' ,11))
code.place(x=30 ,y=150)
code.insert(0,'Contrasena')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)
######----------------------------------------------------------------------

Button(frame, width=39, pady=7, text='Iniciar Sesion', bg='#57a1f8', fg='white', border=0, command='singin').place(x=35,y=204)
label=Label(frame, text='¿no esta registrado?', fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=50,y=270)

sing_up= Button(frame, width=12, text='Registrate Aqui', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sing_up.place(x=190, y=270)





root.mainloop()