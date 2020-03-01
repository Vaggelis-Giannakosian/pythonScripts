from PIL import Image, ImageFilter

# OPEN IMAGE
img = Image.open('img/zoltan-tasi.jpg')

# APPLY FILTER
# filtered_image = img.filter(ImageFilter.SHARPEN)

# CONVERT IMAGE MODE
# filtered_image = img.convert('L')

# ROTATE IMAGE
# crooked = filtered_image.rotate(45)

# SAVE IMAGE
# crooked.save("crooked.png", 'png')

# RESIZE IMAGE
# size = filtered_image.size
# print(size)
# newSize = (int(i / 2) for i in size)
# print(newSize)
# resized = filtered_image.resize(newSize)
# resized.save("resized.png", 'png')

# CROP IMAGE
# Parameters:
# box – a 4-tuple defining the left, upper, right, and lower pixel coordinate.
# box = (20,20,500,500)
# cropped = img.crop(box)
# cropped.save("cropped.png", 'png')


# CREATE THUMBNAIL

# Keep analogy using resize method
# width,height = img.size
# ratio = height/200
# new_size = (int(width/ratio), int(height/ratio))
# new_img = img.resize(new_size)
# print(new_size)


# USE thumbnail method -- Thumbnail method does not return a new image. Modified the already existing one.
img.thumbnail((230, 400))
img.save("thumbnail.jpg")


# OPEN IMAGE
# crooked.show()


# print(dir(img))

