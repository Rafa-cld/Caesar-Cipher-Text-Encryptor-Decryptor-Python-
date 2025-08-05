def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper():
                code = ((ord(char) - ord("A") + shift) % 26) + ord("A")
            else:
                code = ((ord(char) - ord("a") + shift) % 26) + ord("a")
            result += chr(code)
        else:
            result += char
    return result


# --- Entrada del usuario ---
text = input("Write a text: ")

# Validación del número (1-25)
while True:
    num = input("Enter a number between 1 and 25: ")
    try:
        number = int(num)
        if 1 <= number <= 25:
            break
        else:
            print("The number is not in the range 1 to 25. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Elegir modo: cifrar o descifrar
while True:
    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").strip().lower()
    if mode in ['e', 'encrypt']:
        encrypted = caesar_cipher(text, number, mode="encrypt")
        print("Encrypted text:", encrypted)
        break
    elif mode in ['d', 'decrypt']:
        decrypted = caesar_cipher(text, number, mode="decrypt")
        print("Decrypted text:", decrypted)
        break
    else:
        print("Invalid mode. Type 'E' to encrypt or 'D' to decrypt.")
