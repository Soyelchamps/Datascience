from hashing import hash_password
import string
import random


def main():
    # Pide la longiud del Password
    char = int(input("How long you want your password? "))
    # Imprime la longitud del Password
    print(char)
    # Funcion que general el password
    contrasena_gen = generar_contrasena(char)
    # Imprime el password
    print("password:", contrasena_gen)
    # Funcion para hashear el passwrod anteriormente generdo
    password_hashed = hash_password(contrasena_gen)
    # Imprime el password hasheado
    print("The password hashing is:", password_hashed)

# Funcion para generar el hasheo


def generar_contrasena(char):
    # caracteres que contiene una cadena de caracteres que se utilizarán para generar la contraseña.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # crea una contraseña a partir de la union de varios caracteres letras y numeros en un rango de longitud de char
    contrasena = ''.join(random.choice(caracteres) for i in range(char))
    # Regresa la contraseña
    return contrasena


if __name__ == "__main__":
    main()

    # print("Main is running ")
    # string = input(" Type your password: ")
    # print("here you go = ", password_hashed)
    # password_hashed = hash_password(string)
