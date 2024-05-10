def cifrar_cifrado_cesar(cadena_original, desplazamiento):
    cadena_cifrada = ""
    for caracter in cadena_original:
        if caracter.isalpha():
            if caracter.islower():
                nueva_posicion = (ord(caracter) - ord('a') + int(desplazamiento)) % 26 + ord('a')
                caracter_cifrado = chr(nueva_posicion)
            elif caracter.isupper():
                nueva_posicion = (ord(caracter) - ord('A') + int(desplazamiento)) % 26 + ord('A')
                caracter_cifrado = chr(nueva_posicion)
        else:
            caracter_cifrado = caracter
        cadena_cifrada += caracter_cifrado
    return cadena_cifrada

cadena_original = input("Inserta la palabra que deseas cifrar: ")
desplazamiento = input("Inserta el valor de desplazamiento: ")

resultado = cifrar_cifrado_cesar(cadena_original, desplazamiento)
print("La cadena cifrada es:", resultado)
