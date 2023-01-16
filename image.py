from PIL import Image

filepath = 'new.jpg' # image size (2400, 1600)

foo = Image.open(filepath) # open Image

foo = foo.resize((480,320)) # resize (480, 320)
foo.save('final.jpg', optimize=True, quality=60) # save image after resize

