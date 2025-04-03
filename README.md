# APP-AlgoritmoRSA

## Descripcion de la Aplicacion de Inicio de Sesion con RSA en Python

Esta aplicación de inicio de sesión en Python utiliza el algoritmo RSA para proteger las contraseñas de los usuarios durante el proceso de autenticación. A continuación, se proporciona una descripción general de la aplicación y su funcionalidad.

## Caracteristicas Principales:

1. **Generacion de Claves RSA:**
   - La aplicacion genera un par de claves RSA (pública y privada) a traves de funciones de aritmetica modular, se encuentra en el script algorithms.py.
2. **Cifrado de Contraseñas:**
   - Tras tener la claves RSA, se utiliza la ecuacion C = M^e mod N , donde M es el mensaje y C es el mensaje cifrado. La funcion que la realiza esta en el script algorithms.py.
3. **Descifrado de Contraseña:**
   - Tras tener la claves RSA, se utiliza la ecuacion M = C^d mod N , donde M es el mensaje y C es el mensaje cifrado.La funcion que la realiza esta en el script algorithms.py.
4. **Verificacion de Contraseñas:**
   - La contraseña ingresada se compara con la contraseña encriptada guardada en un archivo txt. La funcion se encuentra en el script App.py.

## Como abrir la aplicacion:

1. Abrir la carpeta creada "APP-AlgortimoRSA" y abrir la carpeta dentro de esta llamada de la misma manera
2. Dentro encontramos la carpeta APP-Use_RSA_Algoritm, junto con un archivo README y un archivo .gitignore.
3. Abrir APP-Use_RSA_Algoritm con la terminal 
4. En la terminal ejecutar "py .\App.py ".

## INSTRUCCIONES DE USO:

- El login acepta un usuario y una contraseña. Reconoce entre mayúscula y minúsculas.
- Credenciales ya existentes: User: admin   Password: 12345.
- En caso de querer crear nuevas credenciales, ingresar un nuevo usuario y una nueva contraseña y pulsar "Registrar".
- En caso la contraseña no corresponda al usuario, o el usuario no exista, aparecerá un cuadro de texto de error. En caso ambas credenciales sean correctas, aparecerá un cuadro de texto de éxito.
- El algoritmo RSA está aplicado en el cifrado de la contraseña. Para ver las contraseñas cifradas, ingresar a APP-AlgoritmoRSA\APP-AlgoritmoRSA\APP-Use_RSA_Algoritm\password.txt.
- El cifrado se aplica al registrar una nueva contraseña, y el descifrado se aplica al comparar la contraseña ingresada con la contraseña almacenada para cierto usuario.
