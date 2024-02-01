from PIL import Image, ExifTags
import sys, os

filename = sys.argv[1]
dest_filename = sys.argv[2]

img = Image.open(filename)
exif_data = dict((ExifTags.TAGS[k], v) for k,v in img._getexif().items() if k in ExifTags.TAGS)

orientation = exif_data["Orientation"]
if(orientation == 8):
    img = img.rotate(90, expand = True)
elif(orientation == 3):
    img = img.rotate(180, expand = True)
elif(orientation == 6):
    img = img.rotate(270, expand = True)

img.thumbnail((400, 400), Image.LANCZOS)
img.save(os.path.join("../thumbnails/", dest_filename), "jpeg")

