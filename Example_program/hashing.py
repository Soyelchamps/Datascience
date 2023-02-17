import hashlib


def hash_password(contrasena_gen):
    # adding 5gz as password
    salt = "5gz"
    # Adding salt at the last of the password
    dataBase_password = contrasena_gen + salt
    # Declaring Password
    password_hashed = hashlib.md5(dataBase_password.encode())
    print(password_hashed.hexdigest())

    return password_hashed
