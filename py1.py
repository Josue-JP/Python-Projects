######################################
#      This code is free to use      # 
######################################
# In this code, Q and q mean question
######################################
class Input_Error(Exception):
    # Creates a custom error
    pass
def Empty_Check(value):
    # Throws an error on a empty input
    if not value:
        raise Input_Error("EMPTY INPUTS ARE NOT ALLOWED")
######################################
def Choice_Q():
    while True:
        try:
            choiceQ = input("\nChoose one: Encrypt[1] | Decrypt[2]").strip()
            if choiceQ not in ["1", "2"]:
                raise Input_Error("ENTER NUMBER 1 OR 2")
            return choiceQ
        except Input_Error as e:
            print(f"| {e}")
######################################
def Direction_Q(isEncrypting):
    while True:
        try: 
            directionQ = "Enter a positive direction: " if isEncrypting else "Enter a negative direction: "
            direction = int(input(directionQ))

            if (isEncrypting and direction <= 0) or (not isEncrypting and direction >= 0):
                raise Input_Error("INVALID DIRECTION | DIRECTION MUST BE POSITIVE FOR ENCRYPTION AND NEGATIVE FOR DECRYPTION")
            return direction
        except ValueError:
            print("| Invalid number value")
        except Input_Error as e:
            print(f"| {e}")
######################################
def Cipher(text, key, direction):
    customAlphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZzÁáÉéÍíÓóÚúÜü1234567890,./;'[]=-)(*&^%$#@!<>?:{}+_"
    keyIndex = 0
    finalText= ''

    for eachCharacter in text: 
        if eachCharacter not in customAlphabet:
            finalText += eachCharacter # Allows for unkown characters to not be altered and just inserted into the finalText 

        else:
            keyCharacter = key[keyIndex % len(key)] # Ensures that a valid index is always selected
            keyIndex += 1 # Scrolls through every index

            keyInt = customAlphabet.index(keyCharacter) # Selects the position of keyCharacter in customAlphabet as an int 

            textInt = customAlphabet.find(eachCharacter)

            offset = (textInt + keyInt * direction) % len(customAlphabet) 

            finalText += customAlphabet[offset]

    return finalText
######################################
def Main():
    try: 
        qChoice = Choice_Q()
        isEncrypting = qChoice == "1"

        qKey = input("Enter your key: ").strip()
        Empty_Check(qKey)# Check if empty

        qDirection = Direction_Q(isEncrypting)

        qText = input("Enter text: ").strip()
        Empty_Check(qText)


        Final_Result = Cipher(qText, qKey, qDirection)

        EorD = "ENCRYPTED" if isEncrypting else "DECRYPTED" 
        print(f"{EorD}-RESULT:\n {Final_Result}")
    except Input_Error as e:
        print(f"|| {e}")
    except KeyboardInterrupt:
        print("\nPROCESS ENDED BY USER")
    except Exception as e:
        print(f"||| {e}")

if __name__ == "__main__":
    Main()
# This was placed so that if this file is used as a module or something like that, it wouldn't start the code on launch/automatically.

