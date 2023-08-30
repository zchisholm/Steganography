from stegano import lsb

# Can only interpret .png files for now

secret = lsb.hide("./tests/stock-photography-trends11.png", "Hello World")
secret.save("./tests/stock-photography-trends11(1).png")

clear_message = lsb.reveal("./tests/stock-photography-trends11(1).png")
print(clear_message)