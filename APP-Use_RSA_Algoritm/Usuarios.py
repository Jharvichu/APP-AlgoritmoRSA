class Usuarios():
    cant_users = 0
    def __init__(self,nombre,contrasena):
        self.nombre = nombre;
        self.contrasena = contrasena

        self.conectado = False
        self.intentos = 3;

        Usuarios.cant_users+=1  
    
    #iniciar sesion
    def conectar(self,contrasenia):
        #AQUI PUEDE IR 

        miContrasena = contrasenia
        if miContrasena == self.contrasena :
            print("Esta conectado")
            self.conectado = True
        else :
            self.cant_users -= 1
            print("Esta mal su contraseña, intente denuevo")

    def desconectar(self):
        if self.conectado :
            print("")
        else :
            print("")
    
    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else :
            conect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"









