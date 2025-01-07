######################################
#      This code is free to use      # 
######################################
# In this code, Q and q means question
class Invalid_Response(Exception):
    '''This will throw a custom error'''
    pass

def Empty_Input_Check(value): 
    '''This will throw a custom error if any of the values are empty'''
    if not value: 
        raise Invalid_Response("EMPTY INPUTS ARE NOT ALLOWED")
#####################################
def Number_Q():
    while True:
        try:
            numberQ = input('\nChoose one: Encrypt[1] | Decrypt[2]').strip()
            if numberQ not in ['1', '2']:
                raise Invalid_Response("ENTER NUMBERS 1 OR 2")
            return numberQ
        except Invalid_Response as e: 
            print(f'| {e}') 

            
#####################################
def Direction_Q(encrypting):
    while True: 
        try: 
            directionQ = "Enter a positive direction: " if encrypting else "Enter a negative direction: "
            direction = int(input(directionQ))

            if (encrypting and direction <= 0) or (not encrypting and direction >= 0):
                raise Invalid_Response("INVALID DIRECTION | DIRECTION MUST BE POSITIVE FOR ENCRYPTION AND NEGATIVE FOR DECRYPTION")
            return direction 
        except ValueError: 
            print("| Invalid number value")
        except Invalid_Response as e:
            print(f"| {e}")
#####################################
def Cipher(message, key, direction):
    customAlphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZzÁáÉéÍíÓóÚúÜü1234567890,./;'[]=-)(*&^%$#@!<>?:{}+_"
    finalMessage = ''
    keyIndex = 0

    for character in message:
        if character not in customAlphabet:
            finalMessage += character # This allows for unknown characters to be inserted into the fianlMessage without tampering it
        
        else:
            keyCharacter = key[keyIndex % len(key)] # This obtains the current character of the key input
            # len(key) ensures that there ^^^^^^^ is always a valid character selected 
            keyIndex += 1 # This ensures that each letter is selected

            offset = customAlphabet.index(keyCharacter) # This selects the index of keyCharacter in the customAlphabet

            messageIndex = customAlphabet.find(character)

            newMessageIndex = (messageIndex + offset * direction) % len(customAlphabet)
            # len(key) ensures that there is always a valid character selected 

            finalMessage += customAlphabet[newMessageIndex]

    return finalMessage
#####################################
def Main():
    try:
        qNumber = Number_Q()
        encrypting = qNumber == "1"

        qKey = input("Enter a key: ").strip()
        Empty_Input_Check(qKey) # This will check if qKey is empty

        qDirection = Direction_Q(encrypting)

        qText = input("Enter your text: ").strip()
        Empty_Input_Check(qText) # This will check if qText is empty


        
        Final_Result = Cipher(qText, qKey, qDirection)

        EorD = "E" if encrypting else "D" # E for Encrypt, D for Decrypt
        print(f"{EorD}_RESULT:\n  {Final_Result}")
    except Invalid_Response as e: 
        print(f"|| {e}")
    except KeyboardInterrupt:
        print("\nPROCESS ENDED BY USER")
    except Exception as e:
        print(f"||| {e}")

if __name__ == "__main__":
    Main()
# This if statement was placed so that if this file is used as a module or something like that, it wouldn't start the code on launch/automatically.


















