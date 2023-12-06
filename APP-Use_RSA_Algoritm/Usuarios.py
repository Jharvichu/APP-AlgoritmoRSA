from Algorithms import encrypt

class Usuarios():
    cant_users = 0
    def __init__(self,nombre,contrasena):
        self.nombre = nombre;
        self.contrasena = contrasena

        self.conectado = False
        self.intentos = 3;

        Usuarios.cant_users+=1  
    
    def CifrarContraseña(self,KeyPublic):
        a = encrypt(self.contrasena,KeyPublic)
        return a
    
    def conectar(self,contrasenia):
        miContrasena = contrasenia
        if miContrasena == self.contrasena :
            print("Esta conectado")
            self.conectado = True
        else :
            self.cant_users -= 1
            print("Esta mal su contraseña, intente denuevo")










