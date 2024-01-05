from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk

window=Tk()
window.title('login')
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)
###---------- Condiciones de los datos de usuario ---------------------------------------------------------------------------------------

def singup():

    cedula=CI.get()
    contraseña=clave.get()
    ConfCont=CON_clave.get()
    nombre=name.get()
    nacimiento=bday.get()
    estadoN=EdoNac.get()
    Gender=Genero.get()

    if contraseña==ConfCont:
        try:#la funcion try: mientras que el archivo este disponible lo leerà e ingresara datos
            file=open('probando.txt','r+')
            d=file.read()
            r.ast.literal_eval(d)

            dict2={'cedula','contraseña','nombre','nacimiento','estadoN','Gender'}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('probando.txt','w')
            w=file.write(str(r))

            #messagebox.showinfo('singup','cuenta creada con exito')
            screen=Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')

            Label(screen, text='Hello Everyone', bg='#fff' ,font=('Calibri (Body)',50,'bold')).pack(expand=True)

            screen.mainloop()

        except:#y si el archivo no existe, 'except' lo crearà

            file=open('probando.txt','w')
            pp=str({'cedula','contraseña','nombre','nacimiento','estadoN','Gender'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('error','las contraseñas no coinciden')


###-----------------------------------------------------------------------------------------------------------

frame=Frame(window,width=350,height=350,bg='white')
frame.place(x=285,y=45)

heading = Label(frame , text='Crear una cuenta' , fg='#57a1f8' , bg='white' , font=('Microsoft YaHei UI Light' , 23,'bold'))
heading.place(x=50,y=5)

imag = PhotoImage(file='singup.png')
Label(window , image=imag , border=0 , bg='white').place(x=265 , y=100)

### cuadros de entrada de datos --------------------------------------------------

## lista desplegable para el sexo ---------------------------------------

sexos=['M','F','NB']

def selection_changed(event):
    selection = Genero.get()

Genero = ttk.Combobox(values=sexos)
Genero.bind("<<ComboboxSelected>>", selection_changed)
Genero.place(x=720, y=260)

## lista desplegable para los estados -----------------------------------

edos=['AMZ','ANZ','APU','ARG','BAR','BOL','CBB','CCS','COJ','DtA','FLC','GUA','LAR','MÈR','MIR','MON','NvE','PGS','SCR','TCH','TRJ','VRG','YRY','ZUL']

def selection_changed(event):
    selection = EdoNac.get()

EdoNac = ttk.Combobox(values=edos)
EdoNac.bind("<<ComboboxSelected>>", selection_changed)
EdoNac.place(x=700, y=170)

## cuadro para ingresar el F de nacimiento-------------------------------
def on_entry(e):
    bday.delete(0,'end')
def on_leave(e):
    if bday.get()=='':
        bday.insert(0,'Nacimiento: dd/mm/aaaa')

bday = Entry(window, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light' , 11))
bday.place(x=630,y=80)
bday.insert(0, 'Nacimiento: dd/mm/aaaa')
bday.bind('<FocusIn>', on_entry)
bday.bind('<FocusOut>', on_leave)

Frame(window, width=225, height=2, bg='black').place(x=625,y=107)

## cuadro para ingresar el Nombre-------------------------------
def on_entry(e):
    name.delete(0,'end')
def on_leave(e):
    if name.get()=='':
        name.insert(0,'Nombre')

name = Entry(window, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light' , 11))
name.place(x=30,y=290)
name.insert(0, 'Nombre')
name.bind('<FocusIn>', on_entry)
name.bind('<FocusOut>', on_leave)

Frame(window, width=200, height=2, bg='black').place(x=25,y=317)

## cuadro para confirmar la contraseña------------------------------

def on_entry(e):
    CON_clave.delete(0,'end')
def on_leave(e):
    if CON_clave.get()=='':
        CON_clave.insert(0,' Confirmar Contraseña')

CON_clave = Entry(window, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light' , 11))
CON_clave.place(x=30,y=220)
CON_clave.insert(0, 'Confirmar Contraseña')
CON_clave.bind('<FocusIn>', on_entry)
CON_clave.bind('<FocusOut>', on_leave)

Frame(window, width=180, height=2, bg='black').place(x=25,y=247)

## cuadro para ingresar la Contraseña-------------------------------
def on_entry(e):
    clave.delete(0,'end')
def on_leave(e):
    if clave.get()=='':
        clave.insert(0,'Contraseña')

clave = Entry(window, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light' , 11))
clave.place(x=30,y=150)
clave.insert(0, 'Contraseña')
clave.bind('<FocusIn>', on_entry)
clave.bind('<FocusOut>', on_leave)

Frame(window, width=225, height=2, bg='black').place(x=25,y=177)

## cuadro para ingresar la cedula-------------------------------
def on_entry(e):
    CI.delete(0,'end')
def on_leave(e):
    if CI.get()=='':
        CI.insert(0,'Cèdula')

CI = Entry(window, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light' , 11))
CI.place(x=30,y=80)
CI.insert(0, 'Cèdula')
CI.bind('<FocusIn>', on_entry)
CI.bind('<FocusOut>', on_leave)

Frame(window, width=270, height=2, bg='black').place(x=25,y=107)

###------------------------------------------------------------------------------------------------------

Button(window, width=40,pady=7,text='¡Listo!' , bg='#57a1f8', fg='white', border=0, command=singup).place(x=315 , y=400)




window.mainloop()