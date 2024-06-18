from PIL import Image, ImageGrab
import pytesseract
import numpy as np
import time

st = time.time()

tl = (56, 735)
br = (651+130, 793+50)

img = ImageGrab.grab(
  bbox=(tl[0], tl[1], br[0], br[1]),
  include_layered_windows=False,
  all_screens=False,
  xdisplay=None
)

text = pytesseract.image_to_string(img)

# create a list with ten elements of the type (None, 0)
my_list = [[None, 0] for _ in range(10)]
pos = 0
for word in text.split():
  # check if word is an integer
  try:
    num = int(word)
    if pos > 1:
      my_list[pos-1][1] = num
  except ValueError:
    if pos <= 9:
      if word in ['INTRO', 'UP', 'DOWN', 'OUTRO', 'VERSE', 'CHORUS']:
        my_list[pos][0] = word
        pos += 1

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

print(my_list)
