from cryptography.fernet import Fernet

# GENERAR CLAVE
key = Fernet.generate_key()

# CREAR CIFRADOR
cipher = Fernet(key)

# TEXTO ORIGINAL
texto = "Hola mundo secreto"

# ENCRIPTAR
texto_encriptado = cipher.encrypt(texto.encode())

print("Texto Encriptado:")
print(texto_encriptado)

# DESENCRIPTAR
texto_desencriptado = cipher.decrypt(texto_encriptado)

print("\nTexto Desencriptado:")
print(texto_desencriptado.decode())