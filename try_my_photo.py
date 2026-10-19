# Try out your photo before you draw it.
#
# 1. Drag your photo into the photos folder.
# 2. Change the two lines below.
# 3. Run this file.

from photo_tools import load_photo, show_numbers, preview

PHOTO = "dog.jpg"     # your photo's exact name, in quotes
COLUMNS = 30          # how many cells across

pixels = load_photo(PHOTO, COLUMNS)

# A picture of your grid, one gray square per cell, in its own window:
preview(pixels)

# Some things to check in the shell:
print("rows:", len(pixels))
print("columns:", len(pixels[0]))
print("top-left cell:", pixels[0][0])

# Want to see every number? Take the # off the next line.
# show_numbers(pixels)
