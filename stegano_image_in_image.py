from stegano import lsb

#Can only interpret .png files for now
# Making the file selection

def fileSelection():
    file_path = "tests/imagein.png"
    message = "tests/test_image.png"
    return file_path, message

def encoding():
    pass

if __name__ == "__main__":
    file_path, message = fileSelection()
    secret = lsb.hide(file_path, message)
    secret.save("tests/test_image.png")
    clear_message = lsb.reveal("tests/test_image.png")
    print(clear_message)