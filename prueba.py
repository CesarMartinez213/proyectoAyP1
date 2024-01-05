from tkinter import messagebox, ttk
import tkinter as tk

edos=['AMZ','ANZ','APU','ARG','BAR','BOL','CBB','CCS','COJ','DtA','FLC','GUA','LAR','MÈR','MIR','MON','NvE','PGS','SCR','TCH','TRJ','VRG','YRY','ZUL']

def selection_changed(event):
    selection = combo.get()
    '''messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )'''
window = tk.Tk()
window.config(width=300, height=200)
combo = ttk.Combobox(values=edos)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)
window.mainloop()