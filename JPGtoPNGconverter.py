import sys
import os
from PIL import Image, ImageFilter

# grab the arguments
sourceFolder = sys.argv[1]
targetFolder = sys.argv[2]

# check if targetFolder exists or create it
if not os.path.exists(targetFolder):
    os.makedirs(targetFolder)

# loop through sourceFolder and convert images to png

for image in os.listdir(sourceFolder):
    img = Image.open(f'{sourceFolder}{image}')
    clean_name = os.path.splitext(image)[0]
    filename = f'{targetFolder}{clean_name}.png'
    # save images to new folder
    img.save(filename, 'png')



print(sourceFolder)
print(targetFolder)

exit()
