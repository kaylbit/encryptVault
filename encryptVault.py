#!/bin/python3
import base64

print("WELCOME TO ENCRYPT AND DECRYPT!")
options = ["Encrypt.", "Decrypt.", "Check encrypted saves.", "Exit"]

# Stores encrypted values (kept in memory only, not saved to file)
encrypted_Output = []

# Controls main loop
loopStop = False

# -------------------------
# Function: introUpdate
# Description: Display the main menu options
# -------------------------
def introUpdate():
    print("-" * 20)
    for act in range(len(options)):
        print(f"{act + 1}." + options[act]) 

# -------------------------
# Function: process
# Description: Handle main menu selection
# -------------------------
def process(userAction):
    global loopStop
    if userAction == 1:
        encrypt()
    elif userAction == 2:
        decrypt()
    elif userAction == 3:
        encryptedSaves()
    elif userAction == 4:
        print("Thank you for testing!!!")
        loopStop = True
    else:
        print("Error input")
        process(int(input("Choose again: ")))
        
# -------------------------
# Function: encrypt
# Description: Encrypts user input with Base64 and gives option to save
# -------------------------
def encrypt():
    inputUser = input("Input word to encrypt: ")
    encoded = base64.b64encode(inputUser.encode())  # Encode string -> Base64
    print(f"Input has been encrypted to '{encoded.decode()}'.")
    
    # Option to save encrypted string
    saved = input("Add to save?[y/n]: ").lower()
    if saved == "y" or saved == "yes":    
        print("Added to save.")
        encrypted_Output.append(encoded.decode()) 
    elif saved == "n" or saved == "no":
        return
    else:
        print("\nNot in the choices, select again")
        encrypt()

# -------------------------
# Function: decryptProcess
# Description: Decrypts Base64-encoded data
# -------------------------
def decryptProcess(data):
    data_decode = base64.b64decode(data)
    print(f"Input has been decrypted to '{data_decode.decode()}'")

# -------------------------
# Function: decrypt
# Description: Sub-menu for decryption
# -------------------------
def decrypt():
    print("-" * 20)
    print("1. Decrypt")
    print("2. Check encrypted saves.")
    print("3. Exit")
    inputUser = int(input("Select an action: "))
    
    if inputUser == 1:
        userInput = input("Decrypt: ")
        try:
            decryptProcess(userInput.encode())
        except Exception:
            print("\nThat is not a valid base64 string! Try again.")
            decrypt()  
    elif inputUser == 2:
        encryptedSaves()
    elif inputUser == 3:
        return
    else:
        print("\nNot in the list, select again")
        decrypt()
        
# -------------------------
# Function: encryptedSaves
# Description: Display list of saved encrypted strings
# -------------------------
def encryptedSaves():
    print("-" * 20)
    print("Encrypted List: ")
    for i in range(len(encrypted_Output)):
        print(f"{i + 1}. {encrypted_Output[i]}")
    
    if len(encrypted_Output) == 0:
        print("Empty")
        emptylist()   
    else:
        emptylist()

# -------------------------
# Function: emptylist
# Description: Allow user to decrypt from saved list or exit
# -------------------------
def emptylist():
    print("-" * 20)
    print("Select options: ")
    print("1. Decrypt")
    print("2. Exit.")
    userInput = int(input("Select: "))
    
    if userInput == 1:
        if len(encrypted_Output) == 0:
            print("Empty list") 
            return
        else:
            select = int(input("Choose number from list to decrypt: ")) - 1
            decryptProcess(encrypted_Output[select])
    elif userInput == 2:
        return
    else:
        print("\nNot in the option, select again")
        encryptedSaves()

# -------------------------
# Main Program Loop
# -------------------------
while not loopStop: 
    introUpdate()
    userAction = int(input("\nChoose an action [1, 2, 3, 4]: "))
    process(userAction)
