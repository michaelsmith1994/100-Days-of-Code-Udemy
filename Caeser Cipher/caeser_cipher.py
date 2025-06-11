from cipher_logic import message_cipher 
from caeser_logo import cipher_logo

def encypt_or_decrypt(x):
    if(x.lower() == "encrypt"):
        return('Mask')
    elif(x.lower() == "decrypt"):
        return("Reveal")
    else:
        return("Invalid response")

def get_key_and_message():
    x = input("What index do we wish to shift our cipher? : ")
    y = input("What is the secret message? : ")
    return(x, y)


def main():
    print(cipher_logo)
    cipher_key = 0
    message = ''

    while(encypt_or_decrypt != "Invalid response"):
        encrypt_decrypt = encypt_or_decrypt(input("Do you want to encrypt or decrypt a message? : "))
        if(encrypt_decrypt == "Mask"):
            cipher_key, message = get_key_and_message()
            encrypted_message = message_cipher(cipher_key, message)
            print(encrypted_message)
        elif(encrypt_decrypt == "Reveal"):
            cipher_key, message = get_key_and_message()
            encrypted_message = message_cipher(-int(cipher_key), message)
            print(encrypted_message)
        else:
            print("System error, check encrypt_or_decrypt function logic.")
            continue
        break

if __name__ == "__main__":
    main()