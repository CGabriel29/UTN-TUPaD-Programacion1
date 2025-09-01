# Alfabeto español con letra Ñ

alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Solicita el corrimiento

corrimiento = int(input("ingrese un corrimiento (0-26): "))

# Guardamos el mensaje en arreglo

mensajes_encriptados = []

for i in range (1, 6):
    mensaje = input (f"Ingrese el mensaje {i}: ")
    mensaje_encriptado=""
    
    for caracter in mensaje:
        # Convertir a minuscula
        letra = caracter.lower()
        
        if letra in alfabeto:
            # Obtener indice y aplicar corrimiento
            indice_original= alfabeto.index(letra)
            nuevo_indice = (indice_original+corrimiento)%27
            nueva_letra = alfabeto [nuevo_indice]
            #Mantener mayusculas si corresponde
            if caracter.isupper():
                nueva_letra = nueva_letra.upper()
            
            mensaje_encriptado = nueva_letra
        
        else:
            # Mantener caracteres no alfabeticos
            mensaje_encriptado += caracter
            
    mensajes_encriptados.append(mensaje_encriptado)        
             
# Mostrar resultados
print ("\nMensajes encriptados:")
for idx, mensaje in enumerate(mensajes_encriptados, start=1):
     print(f"Oficial {idx}: {mensaje}")