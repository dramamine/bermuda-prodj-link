from PIL import Image, ImageGrab
import pytesseract
import numpy as np
import time
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

window = (1300, 1000)
phrase_box = (
  round(.03846 * window[0]),
  round(.8 * window[1]),
  round(.4423 * window[0]),
  round(.945 * window[1])
)
pixel_box = (
  round(0.0492 * window[0]),
  round(0.816 * window[1]),
  round(0.3662 * window[0]),
  round(0.884 * window[1])
)
phrase_button_width = round((phrase_box[2] - phrase_box[0]) / 4)

# tl = (56, 735)
# br = (651+130, 793+50)

def read_phrase_box(phrase_box):
  img = ImageGrab.grab(
    bbox=phrase_box,
    include_layered_windows=False,
    all_screens=False,
    xdisplay=None
  )

  text = pytesseract.image_to_string(img)
  # print(text)

  # create a list with ten elements of the type (None, 0)
  my_list = [[None, 0] for _ in range(10)]
  pos = 0
  for word in text.split():
    word = word.upper()

    # use regex to see if this is letter characters and then a number
    if re.match(r'^[A-Za-z]+\d+$', word):
      print("combo'ed: ", word)
      letters = re.match(r'^[A-Za-z]+', word).group()
      num = re.search(r'\d+', word).group()
      my_list[pos] = [letters, int(num)]
      pos += 1
      continue


    # check if word is an integer
    try:
      num = int(word)
      if pos > 0:
        my_list[pos-1][1] = num
    except ValueError:
      if pos <= 9:
        if word in ['INTRO', 'UP', 'DOWN', 'OUTRO', 'VERSE', 'CHORUS']:
          my_list[pos][0] = word
          pos += 1
  return my_list

if __name__ == '__main__':
  st = time.time()

  my_list = read_phrase_box(phrase_box)
  et = time.time()
  print(my_list)

  elapsed_time = et - st
  print('Execution time:', elapsed_time, 'seconds')
