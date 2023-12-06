from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from Usuarios import Usuarios
from Algorithms import *

root = Tk()
#Variables globales
user = StringVar()
password = StringVar()
usertxtpath = "user.txt"
passwordtxtpath = "password.txt"
keystxtpath = "keys.txt"

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
    nombre = user.get()
    contra = password.get()
    User = Usuarios(nombre,contra)
    test = Buscar(User)
    if test == 1:
        MessageBox.showinfo("Conectado","Se inicio sesion correctamente")
    elif test == 2: 
        MessageBox.showerror("Error","Contraseña Incorrecta")
    elif test == 3:
        MessageBox.showerror("Error","Usuario No Encontrado")
    else:
        MessageBox.showerror("Error", "Vuelva a iniciar la aplicación")

###Funcion para registrar
#Crea ol objeto User con su contraseña (sin encriptar)
def registrar():
    nombre = user.get()
    contra = password.get()
    newUser = Usuarios(nombre,contra)
    Encriptar(newUser)
    MessageBox.showinfo("Nuevo Usuario creado", "Se ha guardado y encriptado con éxito a un nuevo usuario y contraseña")

def Encriptar(newUser):
    p = generate_prime()
    q = generate_prime()
    key_public, key_private = generate_key_pair(p,q)
    saveKeys(key_public[0],key_private[0],key_private[1],keystxtpath)
    saveInformation(newUser.nombre,usertxtpath,newUser.CifrarContraseña(key_public),passwordtxtpath)
    print("usuario: "+newUser.nombre)
    print("contra: "+newUser.contrasena)
    print("Primos p = %d y q = %d"%(p,q))
    print("Llaves generadas: "+str(key_public)+" "+str(key_private))   
    print("Contraseña encriptada",newUser.CifrarContraseña(key_public))

def Buscar(User):
    personas = getUsers(usertxtpath)
    contraseñas = [list(map(int, fila.split())) for fila in getPasswords(passwordtxtpath)]
    llaves = [list(map(int, fila.split())) for fila in getKeys(keystxtpath)]
    if User.nombre in personas:
        index = personas.index(User.nombre)
        contra_encript = contraseñas[index]
        keyprivate = (llaves[index][1],llaves[index][2])
        contra_desencript = decrypt(contra_encript,keyprivate)
        if(User.contrasena == contra_desencript) :
            print("Contraseña desencriptada : ",contra_desencript)
            return 1
        else :
            return 2
    else :
        return 3

        

            





#Se ejecuta siempre
#Creo que se puede colocar la aqui para que lo guarde en un txt
if __name__=="__main__":
    createGUI()