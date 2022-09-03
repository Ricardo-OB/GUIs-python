from tkinter import Tk, Button, Label, filedialog, ttk, messagebox, Entry, END, StringVar, CENTER, NORMAL, DISABLED
from tkinter import *
from PIL import Image, ImageTk as itk
import numpy as np
#from PyQt5.QtWidgets import QFileDialog
from os import getcwd
import cv2, re

class interfaz:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('1250x670')
        self.raiz.title("Interfaz Kernels")
        
        titulo = Label(self.raiz, text='| Aplicar Filtros con Kernel |', font=('Traditional Arabic', 35, 'bold'), 
                       bg='lightgray')
        titulo.place(relx=0.5, rely=0.075, anchor='n')
        
        botonSelec = Button(self.raiz, text='Seleccionar Imagen', bg="lightblue", fg="black", 
                            cursor='hand2', font=('Lucida Bright', 12), command=self.selec_Imagen)
        botonSelec.place(relx=0.5, rely=0.2, anchor='n')
        
        subtitulo1 = Label(self.raiz, text='| Imagen Original |', font=('Lucida Bright', 12, 'bold'), 
                           bg='LightSalmon2', bd=6)
        subtitulo1.place(relx=0.187, rely=0.325, anchor='w')
        
        subtitulo2 = Label(self.raiz, text='| Imagen Filtrada |', font=('Lucida Bright', 12,'bold'),
                           bg='LightSalmon2', bd=6)
        subtitulo2.place(relx=0.82, rely=0.325, anchor='e')
        
        self.img_ent = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_ent.place(relx=0.09, rely=0.67, anchor='w')
        
        subtitulo3 = Label(self.raiz, text='Kernels: ', font=('Lucida Bright', 11))
        subtitulo3.place(relx=0.5, rely=0.74, anchor='s')
        
        subtitulo4 = Label(self.raiz, text='Si modificaste el kernel manualmente \n presiona el botón Convolucionar.', font=('Lucida Bright', 9))
        subtitulo4.place(relx=0.5, rely=0.43, anchor='s')
        
        self.botonCalc = Button(self.raiz, text='Convolucionar', bg="lightgreen", fg="black", state=DISABLED, 
                            cursor='hand2', font=('Lucida Bright', 11), command=self.calcular)
        self.botonCalc.place(relx=0.5, rely=0.45, anchor='n')
        
        fuente = ('Lucida Bright', '11')
        self.opc_kernel = ttk.Combobox(self.raiz, state=DISABLED, width=15, font=fuente)
        self.opc_kernel['values'] = ('Identidad','Bordes','Realzar', 'Sharpen', 'Box Blur','Gaussian Blur') 
        self.raiz.option_add('*TCombobox*Listbox.font', fuente)
        self.opc_kernel.bind("<<ComboboxSelected>>", self.nucleos)
        self.opc_kernel.current(0)
        self.opc_kernel.place(relx=0.5, rely=0.78, anchor='s')
        
        def validar(string):
            regex = re.compile(r"(\+|\-)?[0-9.]*$")
            result = regex.match(string)
            return (string == "" or (string.count('+') <= 1 and string.count('-') <= 1 
                        and string.count('.') <= 1 and result is not None and result.group(0) != ""))

        validatecommand = self.raiz.register(validar)
        
        self.one = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER,
                         validate='key', validatecommand=(validatecommand, "%S"))
        self.one.place(relx=0.45, rely=0.54, anchor='c',relwidth=0.04, relheight=0.045), self.one.insert(0,0)
        self.two = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.two.place(relx=0.5, rely=0.54, anchor='c',relwidth=0.04, relheight=0.045), self.two.insert(0,0)
        self.three = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.three.place(relx=0.55, rely=0.54, anchor='c',relwidth=0.04, relheight=0.045), self.three.insert(0,0)
        self.four = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.four.place(relx=0.45, rely=0.6, anchor='c',relwidth=0.04, relheight=0.045), self.four.insert(0,0)
        self.five = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.five.place(relx=0.5, rely=0.6, anchor='c',relwidth=0.04, relheight=0.045), self.five.insert(0,1)
        self.six = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.six.place(relx=0.55, rely=0.6, anchor='c',relwidth=0.04, relheight=0.045), self.six.insert(0,0)
        self.seven = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.seven.place(relx=0.45, rely=0.66, anchor='c',relwidth=0.04, relheight=0.045), self.seven.insert(0,0)
        self.eight = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.eight.place(relx=0.5, rely=0.66, anchor='c',relwidth=0.04, relheight=0.045), self.eight.insert(0,0)
        self.nine = Entry(self.raiz, width=7, font=('Lucida Bright', '11'), justify= CENTER, 
                         validate="key", validatecommand=(validatecommand, "%S"))
        self.nine.place(relx=0.55, rely=0.66, anchor='c',relwidth=0.04, relheight=0.045), self.nine.insert(0,0)
        
        self.img_filt = Label(self.raiz, width=57, height=29, borderwidth=1, relief="solid")
        self.img_filt.place(relx=0.91, rely=0.67, anchor='e')
        
        self.raiz.mainloop()
    
    def selec_Imagen(self):

        #self.file_name, extension = QFileDialog.getOpenFileName(None, "Imagen", getcwd(),"Archivos de imagen (*.png *.jpg)", options=QFileDialog.Options())
        self.file_name = filedialog.askopenfilename(title='Subir',filetypes=[('Imagenes', '*.jpg *.jpg')])
        #self.file_name, _ = QFileDialog.getOpenFileName(None, 'Buscar Imagen', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')

        imagen1 = cv2.imread(self.file_name, cv2.IMREAD_GRAYSCALE)
        r = 330 / imagen1.shape[1]
        dim = (360, int(imagen1.shape[0] * r))
        self.imagen2 = cv2.resize(imagen1,dim,interpolation=cv2.INTER_LINEAR)
        imagen3 = Image.fromarray(self.imagen2)
        imagen4 = itk.PhotoImage(imagen3, master=self.raiz)
        
        self.img_ent = Label(self.raiz, image=imagen4, width=355, height=410)
        self.img_ent.config(image=imagen4)
        self.img_ent.image=imagen4
        self.img_ent.place(relx=0.105, rely=0.67, anchor='w')
        
        self.img_filt = Label(self.raiz, image=imagen4, width=355, height=410)
        self.img_filt.config(image=imagen4)
        self.img_filt.image=imagen4
        self.img_filt.place(relx=0.895, rely=0.67, anchor='e')
        
        self.botonCalc.config(state=NORMAL)
        self.opc_kernel.config(state='readonly')
    
    def nucleos(self, event):
        
        if self.opc_kernel.get() == "Identidad":
            self.one.delete (0, END), self.one.insert(0,0)
            self.two.delete (0, END), self.two.insert(0,0)
            self.three.delete (0, END), self.three.insert(0,0)
            self.four.delete (0, END), self.four.insert(0,0)
            self.five.delete (0, END), self.five.insert(0,1)
            self.six.delete (0, END), self.six.insert(0,0)
            self.seven.delete (0, END), self.seven.insert(0,0)
            self.eight.delete (0, END), self.eight.insert(0,0)
            self.nine.delete (0, END), self.nine.insert(0,0)
            
            kernel1 = np.array([[0,0,0],[0,1,0],[0,0,0]])
            
        elif self.opc_kernel.get() == "Bordes":
            self.one.delete (0, END), self.one.insert(0,-1)
            self.two.delete (0, END), self.two.insert(0,-1)
            self.three.delete (0, END), self.three.insert(0,-1)
            self.four.delete (0, END), self.four.insert(0,-1)
            self.five.delete (0, END), self.five.insert(0,8)
            self.six.delete (0, END), self.six.insert(0,-1)
            self.seven.delete (0, END), self.seven.insert(0,-1)
            self.eight.delete (0, END), self.eight.insert(0,-1)
            self.nine.delete (0, END), self.nine.insert(0,-1)
            
            kernel1 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
            
        elif self.opc_kernel.get() == "Realzar":
            self.one.delete (0, END), self.one.insert(0,-2)
            self.two.delete (0, END), self.two.insert(0,-1)
            self.three.delete (0, END), self.three.insert(0,0)
            self.four.delete (0, END), self.four.insert(0,-1)
            self.five.delete (0, END), self.five.insert(0,1)
            self.six.delete (0, END), self.six.insert(0,1)
            self.seven.delete (0, END), self.seven.insert(0,0)
            self.eight.delete (0, END), self.eight.insert(0,1)
            self.nine.delete (0, END), self.nine.insert(0,2)
            
            kernel1 = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
            
        elif self.opc_kernel.get() == "Sharpen":
            self.one.delete (0, END), self.one.insert(0,0)
            self.two.delete (0, END), self.two.insert(0,-1)
            self.three.delete (0, END), self.three.insert(0,0)
            self.four.delete (0, END), self.four.insert(0,-1)
            self.five.delete (0, END), self.five.insert(0,5)
            self.six.delete (0, END), self.six.insert(0,-1)
            self.seven.delete (0, END), self.seven.insert(0,0)
            self.eight.delete (0, END), self.eight.insert(0,-1)
            self.nine.delete (0, END), self.nine.insert(0,0)
            
            kernel1 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
            
        elif self.opc_kernel.get() == "Box Blur":
            self.one.delete (0, END), self.one.insert(0,0.1111)
            self.two.delete (0, END), self.two.insert(0,0.1111)
            self.three.delete (0, END), self.three.insert(0,0.1111)
            self.four.delete (0, END), self.four.insert(0,0.1111)
            self.five.delete (0, END), self.five.insert(0,0.1111)
            self.six.delete (0, END), self.six.insert(0,0.1111)
            self.seven.delete (0, END), self.seven.insert(0,0.1111)
            self.eight.delete (0, END), self.eight.insert(0,0.1111)
            self.nine.delete (0, END), self.nine.insert(0,0.1111)
            
            kernel1 = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
        
        elif self.opc_kernel.get() == "Gaussian Blur":
            self.one.delete (0, END), self.one.insert(0,0.0625)
            self.two.delete (0, END), self.two.insert(0,0.125)
            self.three.delete (0, END), self.three.insert(0,0.0625)
            self.four.delete (0, END), self.four.insert(0,0.125)
            self.five.delete (0, END), self.five.insert(0,0.25)
            self.six.delete (0, END), self.six.insert(0,0.125)
            self.seven.delete (0, END), self.seven.insert(0,0.0625)
            self.eight.delete (0, END), self.eight.insert(0,0.125)
            self.nine.delete (0, END), self.nine.insert(0,0.0625)
            
            kernel1 = np.array([[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]])
        
        filtro = cv2.filter2D(self.imagen2,-1,kernel1)
        filtro = Image.fromarray(filtro)
        filtro = itk.PhotoImage(filtro, master=self.raiz)
        
        self.img_filt = Label(self.raiz, image=filtro, width=355, height=410)
        self.img_filt.config(image=filtro)
        self.img_filt.image=filtro
        self.img_filt.place(relx=0.895, rely=0.67, anchor='e')

    def calcular(self):
        
        uno = float(self.one.get()) 
        dos = float(self.two.get())
        tres = float(self.three.get())
        cuatro = float(self.four.get())
        cinco = float(self.five.get())
        seis = float(self.six.get())
        siete = float(self.seven.get())
        ocho = float(self.eight.get())
        nueve = float(self.nine.get())
        
        kernel_manual = np.array([[uno,dos,tres],[cuatro,cinco,seis],[siete,ocho,nueve]])
        
        filtro_manual = cv2.filter2D(self.imagen2,-1,kernel_manual)
        filtro_manual = Image.fromarray(filtro_manual)
        filtro_manual = itk.PhotoImage(filtro_manual, master=self.raiz)
        
        self.img_filt = Label(self.raiz, image=filtro_manual, width=355, height=410)
        self.img_filt.config(image=filtro_manual)
        self.img_filt.image=filtro_manual
        self.img_filt.place(relx=0.895, rely=0.67, anchor='e')

a = interfaz()