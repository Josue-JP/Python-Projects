
def cipher(message, key, direction=1):
    key_index = 0
    # Include both lowercase and uppercase letters, numbers, and symbols
    alphabet = 'AaÁáBbCcÇçDdEeÉéFfGgHhIiÍíJjKkLlMmNnÑñOoÓóPpQqRrSsTtUuÚúVvWwXxYyZz0123456789'  # Extended alphabet and added numbers were added to throw people off
    final_message = ''

    for char in message:  # Keep the message as is (case-sensitive)
        if char not in alphabet:  # If the character is not in the alphabet (e.g., spaces or symbols)
            final_message += char
        else:
            # Get the corresponding key character for encryption/decryption
            key_char = key[key_index % len(key)]  # No lowercase conversion
            key_index += 1

            # Find the position of the key character in the alphabet
            offset = alphabet.index(key_char)

            # Find the position of the current character in the message
            index = alphabet.find(char)

            if index == -1:
                continue  # Skip characters not in the alphabet

            # Calculate the new index based on the direction (encryption/decryption)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

# Main program
mainQuestion = input('Type one of the following options to do with your text. \nEncrypt or Decrypt:\n                   ').strip().capitalize()
custom_key = input("Enter your Key: \n                   ")
inputQuestion = input('Enter Your Text:\n                   ')

if mainQuestion == "Encrypt":
    def encrypt(message, key):
        return cipher(message, key, 1) # number 1 is the direction, and it is important

    encryptedMessage = encrypt(inputQuestion, custom_key)
    print("Result:\n                   " + encryptedMessage)

elif mainQuestion == "Decrypt": 
    def decrypt(message, key):
        return cipher(message, key, -1) # number -1 is the direction, and it is important

    decryptedMessage = decrypt(inputQuestion, custom_key)
    print("Result:\n                   " + decryptedMessage)

else:
    print("Reread the question and enter a valid response")
