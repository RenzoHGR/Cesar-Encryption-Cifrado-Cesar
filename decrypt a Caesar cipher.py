def descifrar_cifrado_cesar(cadena_cifrada, desplazamiento):
    cadena_descifrada = ""
    #un ejemplo k3uqdq"1256"#.
    for caracter in cadena_cifrada:
        if caracter.isalpha():
            if caracter.islower():
                nueva_posicion = (ord(caracter) - ord('a') - desplazamiento) % 26 + ord('a')
                caracter_descifrado = chr(nueva_posicion)
            elif caracter.isupper():
                nueva_posicion = (ord(caracter) - ord('A') - desplazamiento) % 26 + ord('A')
                caracter_descifrado = chr(nueva_posicion)
        else:
            caracter_descifrado = caracter
        cadena_descifrada += caracter_descifrado
    return cadena_descifrada

cadena_cifrada = input("Inserta la palabra cifrada: ")
desplazamiento = int(input("Inserta el valor de desplazamiento: "))

resultado = descifrar_cifrado_cesar(cadena_cifrada, desplazamiento)
print("La palabra descifrada es:", resultado)
