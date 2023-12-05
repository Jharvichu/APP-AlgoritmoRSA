from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from Usuarios import Usuarios

root = Tk()
#Variables globales
user = StringVar()
password = StringVar()

def createGUI():
    #Ventana principal y su nombre
    
    root.title("APP Login")

    ###Frame Pricipal
    mainframe = Frame(root)
    mainframe.pack()
    mainframe.config(width=480,height=320)#,bg="lightblue")

    ###Titulo de la ventana
    titulo = Label(mainframe,text="Login de Usuario",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    #Indicadores de texto
    userLabel = Label(mainframe,text = "Usuario: ")
    userLabel.grid(column=0,row=1)
    passLabel = Label(mainframe,text= "Contraseña: ")
    passLabel.grid(column=0,row=2)

    ###Entradas de texto
    #Usuario
    user.set("")
    userEntry = Entry(mainframe,textvariable=user)
    userEntry.grid(column=1,row=1)
    #Contraseña
    password.set("")
    passwordEntry = Entry(mainframe,textvariable=password,show="*")
    passwordEntry.grid(column=1,row=2)

    ###Botones
    #Iniciar Sesion
    iniciarSesionBoton = ttk.Button(mainframe,text="Iniciar Sesion",command=iniciarSesion)
    iniciarSesionBoton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)
    #Registrar
    registrarBoton = ttk.Button(mainframe,text="Registrar",command=registrar)
    registrarBoton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    root.mainloop()

#Funcion para iniciar secion
def iniciarSesion():
    user1.conectar(password.get())
    if user1.conectado == True:
        MessageBox.showinfo("Conectado","Se inicio sesion correctamente")
    if user1.conectado == False: 
        MessageBox.showerror("Error","Contraseña Incorrecta")

###Funcion para registrar
#Crea ol objeto User con su contraseña (sin encriptar)
def registrar():
    nombre = user.get()
    contra = password.get() 
    newUser = Usuarios(nombre,contra)
    personas.append(newUser)






#Se ejecuta siempre
#Creo que se puede colocar la aqui para que lo guarde en un txt
if __name__=="__main__":
    user1 = Usuarios("admin","1234")
    personas = [user1]
    createGUI()