import qrcode # Before anything install two packages 1. pip install qrcode 2. pip install Pillow
img = qrcode.make("https://www.linkedin.com/in/ahmad-fakhouri-65b431208/") #Put a link between the " "
img.show()
img.save("newQR.png")