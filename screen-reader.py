from ctypes import windll
import sys
from PIL import ImageGrab
from image_similarity_measures.evaluate import evaluation
from image_similarity_measures.quality_metrics import rmse
dc= windll.user32.GetDC(0)
import numpy as np

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))

# these ara coordinates for top-left and bottom-right for the phrase buttons.
# bottom-right is still the top-left corner of the last button.
# TODO consider doing some math based on window size.
tl = (56, 735)
br = (651, 793)
width = int((br[0] - tl[0]) / 4)

coords = [
    tl,
    (tl[0] + width, tl[1]),
    (tl[0] + 2 * width, tl[1]),
    (tl[0] + 3 * width, tl[1]),
    (br[0], tl[1]),
    (tl[0], br[1]),
    (tl[0] + width, br[1]),
    (tl[0] + 2 * width, br[1]),
    (tl[0] + 3 * width, br[1]),
    br
]

def read_active_phrase():
  for coord in coords:
    pixel = getpixel(coord[0], coord[1])
    print(pixel)

def check_phrase_image():
  img = ImageGrab.grab(
    bbox=(tl[0], tl[1], br[0], br[1]),
    include_layered_windows=False,
    all_screens=False,
    xdisplay=None
  )
  print(img)
  # similarity = evaluation(org_img_path="images\\rekordbox-2-3-2-1-2-phrases.png",
  #          pred_img_path="images\\rekordbox-2-3-2-1-2-phrases copy.png",
  #          metrics=["rmse", "psnr"])
  # print(similarity)
  res = rmse(org_img=img, pred_img=img)
  print(res)


try:
  check_phrase_image()
except:
  sys.exit(1)
