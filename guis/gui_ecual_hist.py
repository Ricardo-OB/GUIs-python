from tkinter import Tk, Button, Label, filedialog
from tkinter import *
from PIL import Image, ImageTk as itk
import numpy as np
import cv2 
from skimage import exposure,io,color
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from os import getcwd
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

class programa:
    
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1250x670')
        self.raiz.title("Ecualizador")
        
        lbl = Label(self.raiz, text='Ecualizador de Histograma', font=("Times New Roman", 20, 'bold'))
        lbl.place(relx=0.5, rely=0.075, anchor='n')

        boton = Button(self.raiz, text='Seleccionar Imagen', bg="lightblue", fg="black", command=self.seleccionar_img)
        boton.place(relx=0.5, rely=0.2, anchor='n')

        lbl_a = Label(self.raiz, text='Imagen Original', font=("Times New Roman", 12, 'bold'), bg='LightSalmon2', bd=6)
        lbl_a.place(relx=0.187, rely=0.325, anchor='w')

        lbl_b = Label(self.raiz, text='Imagen Final', font=("Times New Roman", 12, 'bold'), bg='LightSalmon2', bd=6)
        lbl_b.place(relx=0.82, rely=0.325, anchor='e')

        self.img_ent = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_ent.place(relx=0.09, rely=0.67, anchor='w')

        self.img_final = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_final.place(relx=0.91, rely=0.67, anchor='e')

        self.horizontal = Scale(self.raiz, from_=1, to=10, bd=2, length=310, width=18, orient=HORIZONTAL, tickinterval=1, resolution=0.25)
        self.horizontal.pack(side=BOTTOM)
        
        self.boton_slider = Button(self.raiz, text='Ingresar Valor', bg='lightgreen', command=self.obtener_valor, state=DISABLED)
        self.boton_slider.pack(side=BOTTOM)
        
        self.hist = Label(self.raiz, width=38, height=11, borderwidth=1, relief="solid")
        self.hist.place(relx=0.5, rely=0.57, anchor='center')

        toolbar = Frame(self.raiz, bg='lightgray')
        insboton = Button(toolbar, text='Eliminar Imagen', command=self.eliminar)
        insboton.pack(side=RIGHT, padx=3, pady=2)
        toolbar.pack(side=TOP, fill=X)
        
        self.raiz.mainloop()
            
    def seleccionar_img(self):
        
        self.file_name = filedialog.askopenfilename(title='Subir',filetypes=[('Imagenes', '*.jpg *.jpg')])
        #self.file_name, extension = QFileDialog.getOpenFileName(None, "Imagen", getcwd(),"Archivos de imagen (*.png *.jpg)", options=QFileDialog.Options())
        img = cv2.imread(self.file_name, cv2.IMREAD_GRAYSCALE)
        
        r = 330 / img.shape[1]
        dim = (360, int(img.shape[0] * r))
        imagen = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
        imagen = Image.fromarray(imagen)
        imagen = itk.PhotoImage(imagen, master=self.raiz)

        self.img_ent = Label(self.raiz, image=imagen, width=355, height=410)
        self.img_ent.config(image=imagen)
        self.img_ent.image=imagen
        self.img_ent.place(relx=0.105, rely=0.67, anchor='w')
        
        self.img_final = Label(self.raiz, image=imagen, width=355, height=410)
        self.img_final.config(image=imagen)
        self.img_final.image=imagen
        self.img_final.place(relx=0.895, rely=0.67, anchor='e')

        self.boton_slider.config(state=NORMAL)
        
    def obtener_valor(self):

        IMG = cv2.imread(self.file_name, cv2.IMREAD_GRAYSCALE)

        r = 330 / IMG.shape[1]
        dim = (360, int(IMG.shape[0] * r))
        IMG = cv2.resize(IMG, dim, interpolation=cv2.INTER_LINEAR)
        
        clip = self.horizontal.get()
        ecuali = cv2.createCLAHE(clipLimit=clip, tileGridSize=(8,8))
        img_ecual = ecuali.apply(IMG)

        self.IMAGEN = Image.fromarray(img_ecual)
        self.IMAGEN = itk.PhotoImage(self.IMAGEN)

        hist, bins = np.histogram(img_ecual.ravel(), 256, [0,256])

        fig = plt.Figure(figsize=(3.5,2.5), dpi=100)
        ax = fig.add_subplot()
        ax.axis('off')
        ax.hist(img_ecual.ravel(), 256, (0, 256))
        ax.grid()
        ax.plot(bins[:-1], hist-15)

        canvas = FigureCanvasTkAgg(fig, master=self.hist)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.57, anchor='center')

        self.img_final = Label(self.raiz, image=self.IMAGEN, width=355, height=410)
        self.img_final.config(image=self.IMAGEN)
        self.img_final.image=self.IMAGEN
        self.img_final.place(relx=0.895, rely=0.67, anchor='e')

    def eliminar(self):
        self.img_ent = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_ent.place(relx=0.09, rely=0.67, anchor='w')

        self.img_final = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_final.place(relx=0.91, rely=0.67, anchor='e')

        self.hist = Label(self.raiz, width=38, height=11, borderwidth=1, relief="solid")
        self.hist.place(relx=0.5, rely=0.57, anchor='center')

        self.boton_slider.config(state=DISABLED)

b = programa()

