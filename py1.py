######################################
#      This code is free to use      # 
######################################
class User_Input_Error(Exception):
    # Allows custom error messages
    pass
def Check_For_Empty(value):
    # Checks if Input is empty
    if not value:
        raise User_Input_Error("EMPTY INPUTS ARE NOT ALLOWED")
######################################
def En_or_Decrypt():
    while True:
        try:
            enOrDecrypt = input("Choose one: Encrypt[1] | Decrypt[2]").strip()
            if enOrDecrypt not in ['1','2']:
                raise User_Input_Error("ENTER NUMBERS 1 OR 2")
            return enOrDecrypt 
        except User_Input_Error as e:
            print(f"| {e}")
######################################
def Direction_Question(Encrypting):
    while True:
        try:
            directionQuestion = "Enter a positive direction: " if Encrypting else "Enter a negative direction: "
            direction = int(input(directionQuestion)).strip()

            if (Encrypting and direction <= 0) or (not Encrypting and direction >= 0):
                raise User_Input_Error("INVALID DIRECTION | DIRECTION MUST BE POSITIVE FOR ENCRYPTION AND NEGATIVE FOR DECRYPTION")
            return direction 
        except ValueError:
            print("| Invalid number value")
        except User_Input_Error as e:
            print(f"| {e}")
######################################
def Cipher(userText, userKey, userDirection):
    customAlphabet= ""
    keyIndex = 0 
    finalText = ""

    for eachChar in userText:
        if eachChar not in customAlphabet:
            finalText += eachChar # Allows for unkown characters to not be altered and just inserted into the finalText 
        else:
            keyCharcter = key[keyIndex% len(key)] # Ensures that a valid index is always selected
            keyIndex += 1 # Rotates through every letter in the key

            keyInt = customAlphabet.index(keyCharcter) # Selects the position of the current letter of key according to the customAlphabet as an int

                            charInt = customAlphabet.find(eachChar)# Selects the position of the current letter of usrText according to the customAlphabet as an int

            offset = (textInt + keyInt * direction) % len(customAlphabet)

            finalText += customAlphabet[offset]

    return finalText
######################################
def Main():
    try:
        questionOne = En_or_Decrypt()
        Encrypting = questionOne == "1"

        questionTwo = input("Enter your key: ").strip()
        Check_For_Empty(questionTwo)# Checks for empty Inputs

        questionThree = Direction_Question(Encrypting)

        questionFour = input("Enter text: ").strip()
        Check_For_Empty(questionFour)

        finalResult = Cipher(questionFour, questionTwo, questionThree)

        EncryptionOrDecryption = "ENCRYPTED" if Encrypting else ("DECRYPTED")
        print(f"{EncryptionOrDecryption}-RESULT:\n {finalResult}")
    except User_Input_Error as e: 
        print(f"|| {e}")
    except KeyboardInterrupt:
        print("\nPROCESS ENDED BY USER")
    except Exception as e:
        print(f"||| {e}")
######################################
if __name__ == "__main__":
    Main()
# This was placed so that if this file is used as a module or something like that, it wouldn't start the code on launch/automatically.
    
                                
            
