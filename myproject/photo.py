#!/usr/bin/python3

from PIL import Image

#img = Image.opem(path)
# On successful execution of this statement
# an object of Image type is returne and stored in img variable

try:
    img = Image.open(path)

except IOERROR:
    pass
#use above statement within try bvlock, as it can
#raise an IOERROR if file cannot be found, 
#or image cannot be opened
