####################################
#     This code is free to use     #
####################################
class Error(Exception):
    '''This will display an error'''
    pass

def Check_For_Empty(value):
    '''This throws an error msg if the input is empty'''
    if not value: 
        raise Error("  INPUT CANNOT BE EMPTY")
####################################
def Question_Number():
    while True:
        try: 
            firstQuestion = input('Options available:\nEncrypt[1]\nDecrypt[2]\nChoose a Number: ').strip()
            if firstQuestion not in ['1', '2']:
                raise Error("  INVALID CHOICE\n  Enter numbers 1 or 2")
            return firstQuestion
        except Error as e: 
            print(f"  ERROR: {e}")
###################################
def Question_Direction(encryption):
    while True: 
        try: 
            prompt = 'Enter a positive direction: ' if encryption else 'Enter a negative direction: '
            direction = int(input(prompt))

            if (encryption and direction <= 0) or (not encryption and direction >= 0):
                raise Error('  INVALID DIRECTION\n  Direction must be positive for encryption and negative for decryption')
            return direction 
        except ValueError:
            print('  ERROR: Enter a valid number')
        except Error as e:
            print(f"  ERROR: {e}")
###################################
def Cipher(msg, key, direction):
    customAlphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZzÁáÉéÍíÓóÚúÜü1234567890,./;'[]=-)(*&^%$#@!<>?:{}+_"
    finalMsg = ''
    keyIndex = 0

    for Character in msg: 
        if Character not in customAlphabet: 
            finalMsg += Character # This appends the original character of every character that is not in the customAlphbet
            continue
        else:             

            keyCharacter = key[keyIndex % len(key)] # This line gets the key index of the input, and the % len(key) makes sure that there is always a valid charcter selected, due to the index always going up by 1 because of the next line
            keyIndex += 1 # This makes sure that all characters are selected 

            offset = customAlphabet.index(keyCharacter) # This selects the index of customAlphabet according to the number of keyCharacter
            
            msgIndex = customAlphabet.find(Character)

            newMsgIndex = (msgIndex + offset * direction) % len(customAlphabet)
            
            finalMsg += customAlphabet[newMsgIndex]

    return finalMsg
###################################
def Main(): 
    try: 
        enOrDecryptQuestion = Question_Number()
        encryption = enOrDecryptQuestion == '1'
        Check_For_Empty(enOrDecryptQuestion)

        keyQuestion = input('Enter your key:').strip()
        Check_For_Empty(keyQuestion)

        directionQuestion = Question_Direction(encryption)
        Check_For_Empty(directionQuestion)

        textQuestion = input('Enter your text: ').strip()
        Check_For_Empty(textQuestion)


        Final_Result = Cipher(textQuestion, keyQuestion, directionQuestion)
        
        operation = 'E' if encryption else "D" # E stands for Encryption and D for Decryption
        print(f'\n{operation}:\n  {Final_Result}')

    except Error as e:
        print(f'ERROR: {e}')
    except KeyboardInterrupt:
        print("\nProcess cancelled by user")
    except Exception as e: 
        print(f'Error : {e}')

if __name__ == "__main__":
    Main() 
# This if statement was placed so that if this file is used as a module or something like that, it wouldn't start the code on launch/automatically.


















