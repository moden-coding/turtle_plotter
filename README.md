# Pixels in Ink: your photo

## Get your photo in
1. Drag your photo into the **photos** folder.
2. Use a **.jpg** or **.png**. iPhone photos are often **.heic**: see "Trouble" below.
3. Keep the name simple: `max.jpg` beats `IMG_4821 (2).jpeg`.

## Try it
Open **try_my_photo.py**, change these two lines, and run it:

```python
PHOTO = "dog.jpg"
COLUMNS = 30
```

A window opens showing your photo as a grid of gray squares. Too blocky? More columns.
Too slow? Fewer. Most portraits look good between **20 and 40** columns.

## Use it in your drawing
```python
from photo_tools import load_photo

pixels = load_photo("dog.jpg", 30)
```

`pixels` is a list of rows, **top row first**. `pixels[row][col]` is a brightness:
0 is black, 255 is white. From here it's your code: your `cell()`, your key, your loops.

Optional: `SIZE, LEFT, TOP = fit_to_sheet(pixels)` gives you a cell size and
starting corner that fill the sheet.

## Before you plot
- Delete `sheet()` and `preview(...)` calls.
- Push your photo AND your code to GitHub. The plotter needs both.

## Trouble
| You see | Do this |
|---|---|
| "Couldn't find a photo named..." | Check the spelling and capitals. The message lists the photos it can see. |
| "The Pillow package isn't installed" | Thonny: Tools > Manage packages > search **pillow** > Install. |
| "...is a HEIC photo" | Export it as JPG (Mac Preview: File > Export > JPEG), or install **pillow-heif** in Thonny. |
| Your photo comes out sideways | It shouldn't: tell your teacher. |
| It's taking forever to draw | Fewer columns, or `turtle.tracer(0)` at the top and `turtle.update()` at the end. |
