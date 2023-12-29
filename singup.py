from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('login')
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)


frame=Frame(window,width=350,height=350,bg='white')
frame.place(x=285,y=45)

heading = Label(frame , text='Crear una cuenta' , fg='#57a1f8' , bg='white' , font=('Microsoft YaHei UI Light' , 23,'bold'))
heading.place(x=50,y=5)

imag = PhotoImage(file='singup.png')
Label(window , image=imag , border=0 , bg='white').place(x=265 , y=100)

window.mainloop()