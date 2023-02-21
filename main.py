import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from openpyxl import load_workbook
import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

matplotlib.use('TkAgg')

# procesando el excel
def leyendoExcel(path):
    wb = load_workbook(path)
    ws = wb['Sheet1']
    all_rows = list(ws.rows)

    data = []
    for row in all_rows[1:]:
        value = row[1].value
        if (value is not None):
            data.append(value)

    #bins es el número de barras
    #alpha es la transparencia
    #patches: a list of Patch objects that represents the histogram bars.

    plt.hist(data, bins=30, alpha=0.5, color='#73C6B6')
    plt.xlabel('Edad', fontweight ="bold")
    plt.ylabel('Frecuencia', fontweight ="bold")
    plt.title('Edad de los perritos', fontweight ="bold")

    fig = plt.figure(1)
    # widget de lienzo canvas a partir de la figura fig
    canvas = FigureCanvasTkAgg(fig, master=window)
    #devuelve un objeto de widget
    plot_widget = canvas.get_tk_widget()
    plot_widget.pack(pady=10, padx=10, anchor="center")

   

    

def buscarArchivo():
    filepath = filedialog.askopenfilename(
        initialdir = "D:\analisisDeDatos\graficoGauss", 
        title = "Selecciona un archivo", 
        filetypes = (("Text files", "*.xlsx*"), ("all files", "*.*")))

    if not filepath:
        messagebox.showerror("Error", "No has seleccionado un archivo :c")
        return

    leyendoExcel(filepath)



window = tk.Tk()
window.title('Practica 1')
window.geometry("1500x700")
window.config(background = "white")
width = 1500
height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))-30
window.geometry(f'{width}x{height}+{x}+{y}')


lblFileExplorer = Label(window, text="\U0001F436 GRAFICA DE PERRITOS \U0001F436", width=screen_width , height=2, fg="black", bg="#73C6B6",  font=("Arial", 24))
button_explore = Button(window, text="Buscar archivo excel", width=30 , height=2,command=buscarArchivo)
button_exit = Button(window, text="Exit", width=30 , height=2, command=exit)
  

image = Image.open("perritoImage.jpg")
photo = ImageTk.PhotoImage(image)  
labelImagen = tk.Label(window, image=photo)

labelImagen.pack(pady=10, padx=10, anchor="e")
lblFileExplorer.pack(pady=10, padx=30, anchor="center")
button_explore.pack(pady=10, padx=30, anchor="center")
button_exit.pack(pady=10, padx=30, anchor="center")



window.mainloop()