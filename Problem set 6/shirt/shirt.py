import sys
import os
from PIL import Image, ImageOps
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv)==3:
    extensions=[".jpg","jpeg",".png"]
    path1=os.path.splitext(sys.argv[1])
    path2=os.path.splitext(sys.argv[2])
    if path1[1]==path2[1] and path1[1] in extensions:
        try:
            user_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")
        shirt=Image.open("shirt.png")
        size=shirt.size
        user_image =ImageOps.fit(user_image,size)
        user_image.paste(shirt,shirt)
        user_image.save(sys.argv[2])
    elif path1[1]!=path2[1]:
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")
else:
    print("something wrong")


