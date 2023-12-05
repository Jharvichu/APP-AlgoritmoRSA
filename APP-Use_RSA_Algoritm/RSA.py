import random 

#Algoritmo de potenciacion rapida
def Potencia(x,n):
    p = x
    r = 1
    while n > 0:
        if (n & 1):
            r *= p
            n -= 1
        p *= p
        n >>= 1
    return r

#Algoritmo que verifica se un numero es primo por 6k+-1
def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n%2 == 0 or n%3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

#Generar aleatoriamente primos a partir que cumple 6k+-1
def generate_prime():
    while True:
        k=random.randrange(Potencia(2,1),Potencia(2,32)) 
        p = 6*k + 1
        q = 6*k - 1
        if(is_prime(p)):
            return p
        if(is_prime(q)):
            return q

#Algoritmo de euclides MCD
def euclid_gcd(a, b):
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a

#Funcion modular con potencia (x^b) mod n
def modPot(x,n,b):
    p = x
    r = 1
    while n > 0:
        if (n & 1):
            r *= p
            r = r%b
            n -= 1
        p *= p
        p = p%b
        n >>= 1
    return r

#Algoritmo extendido de Euclides para encontrar el inverso multiplicativo de dos números
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d % phi
    
#Generar el valor de e aleatoriamente
def generate_E(phi):
    while True:
        e = random.randrange(2,phi)
        if(euclid_gcd(e,phi) == 1):
            return e
        
#Funcion de Euler
def Totient(p):
  return p-1

#Generar las llaves privadasa y publicas
def generate_key_pair(p,q):
  n = p * q
  phi = Totient(p)*Totient(q)
  e = generate_E(phi)
  d = multiplicative_inverse(e, phi)
  return ((e, n), (d, n))


#Encriptar un texto   C = (M^e) mod n
def encrypt(words,key_public):
    e, n = key_public
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        d = modPot(k,e,n)
        lista.append(d)
        i += 1
    return lista

#Desencriptar un texto encriptado   M = (C^d) mod n
def decrypt(cifra,key_private):
    d, n = key_private
    lista = []
    i = 0
    tamanho = len(cifra)
    while i < tamanho:
        texto = modPot(cifra[i],d,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return ''.join(lista)
