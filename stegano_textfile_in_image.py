from stegano import lsb
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

#Can only interpret .png files for now
# Making the file selection

def fileSelection():
    file_path = askopenfilename()
    text_file = askopenfilename()
    with open(text_file, 'r') as file:
        content = file.read()
    message = content
    return file_path, message

def encoding():
    pass

if __name__ == "__main__":
    file_path, message = fileSelection()
    secret = lsb.hide(file_path, message)
    secret.save("./tests/SECRET_textinimage.png")
    clear_message = lsb.reveal("./tests/SECRET_textinimage.png")
    print(clear_message)