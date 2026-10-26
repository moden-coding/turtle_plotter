# My Pixels in Ink portrait
# Name: ______________________

import turtle
from photo_tools import load_photo, preview, show_numbers

# ---- Paper setup: 1 unit = 1 mm, (0,0) = top-left corner ----
SHEET_W = 278   # landscape A4; for portrait use 210
SHEET_H = 215   # landscape A4; for portrait use 297

screen = turtle.Screen()
screen.setup(width=SHEET_W * 3, height=SHEET_H * 3)       # window shaped like the paper
screen.setworldcoordinates(0, -SHEET_H, SHEET_W, 0)       # to
# ---------------------------------------------------------------
# 1. YOUR PHOTO
#    Drag your photo into the photos folder, then set these two lines.
# ---------------------------------------------------------------
PHOTO = "gann academy entrance.jpg"     # the photo's exact name, in quotes (capitals count)
COLUMNS = 60          # how many cells across. Rows are worked out for you.

pixels = load_photo(PHOTO, COLUMNS)

# pixels is a list of rows, TOP row first.
#   pixels[row][col] is one cell's brightness: 0 = black, 255 = white
#   len(pixels)      is how many rows
#   len(pixels[0])   is how many columns
#
# Need more? Add any of these inside load_photo( ... ):
#   rotate=90       turn the photo clockwise (90, 180, or 270) if it comes out sideways
#   square=True     keep only a square from the middle of the photo
#   contrast=False  skip the automatic darkening/lightening
# Example:  pixels = load_photo(PHOTO, COLUMNS, rotate=90, square=True)
#
# Helpers for testing (delete before you plot):
#   preview(pixels)        shows your grid as gray squares in its own window
#   show_numbers(pixels)   prints every number
preview(pixels)


# ---------------------------------------------------------------
# 2. YOUR TURTLE
# ---------------------------------------------------------------
t = turtle.Turtle()
t.speed(0)


# ---------------------------------------------------------------
# 3. YOUR FUNCTIONS
#    Your shading functions, your key, your cell(). Paste or write them here.
# ---------------------------------------------------------------



# ---------------------------------------------------------------
# 4. YOUR DRAWING
#    Loop through pixels and draw every cell. Remember: row 0 is the TOP.
# ---------------------------------------------------------------



# t.hideturtle()
turtle.done()
