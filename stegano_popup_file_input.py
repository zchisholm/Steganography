from stegano import lsb
from tkinter import Tk    
from tkinter.filedialog import askopenfilename
import os

#Can only interpret .png files for now

def encode(encodedFileName: str):
    file_path = askopenfilename()
    message = input("Enter Message: ")
    secret = lsb.hide(file_path, message)
    secret.save(encodedFileName)
    encodeChk(message, encodedFileName)

def encodeChk(msg, encodedFileName):
    if msg == lsb.reveal(encodedFileName):
        print("Your message has been successfully encoded")
    else:
        print("Ecoding failed. Please try again")
        loop = False


def decode():
    file_path = askopenfilename()
    clear_message = lsb.reveal(file_path)
    print(clear_message)

def continueLoopPrompt():
    response = input("Do you have another file that you would like to encode or decode (y/n)?: ").upper()
    if response == "Y":
        return True
    else:
        return False

if __name__ == "__main__":
    #Setting things up. The bool loop is to continuously run program.
    loop = True
    count = 0
    #Creating a dir for the encoded images if one doesn't already exist
    encodeDir = "./encoded-images/"
    os.makedirs(os.path.dirname(encodeDir), exist_ok=True)

    inital_prompt = "Would you like to encode or decode a message? /n Enter 'E' or 'D' or 'Q' to Quit: "
    while loop is True:
        ans = input(inital_prompt).upper()
        if ans == "E":
            encodedFileName = "./encoded-images/SECRET"+str(count)+".png"
            encode(encodedFileName)
            count += 1
            loop = continueLoopPrompt()
        elif ans == "D":
            decode()
            loop = continueLoopPrompt()
        elif ans == "Q":
            print("Quiting program now. Goodbye ^-^")
            break
        else:
            print("Your input was invalid. Please Enter 'E' to encode and 'D' to decode.")
