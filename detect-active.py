from ctypes import windll
dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))

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


def load_coords(pixel_box):
  global coords
  phrase_button_width = round((pixel_box[2] - pixel_box[0]) / 4)
  coords = [
    (pixel_box[0], pixel_box[1]),
    (pixel_box[0] + phrase_button_width, pixel_box[1]),
    (pixel_box[0] + 2 * phrase_button_width, pixel_box[1]),
    (pixel_box[0] + 3 * phrase_button_width, pixel_box[1]),
    (pixel_box[2], pixel_box[1]),
    (pixel_box[0], pixel_box[3]),
    (pixel_box[0] + phrase_button_width, pixel_box[3]),
    (pixel_box[0] + 2 * phrase_button_width, pixel_box[3]),
    (pixel_box[0] + 3 * phrase_button_width, pixel_box[3]),
    (pixel_box[2], pixel_box[3])
  ]

load_coords(pixel_box)

def read_active_phrase():
  for i in range(len(coords)):
    coord = coords[i]
    pixel = getpixel(coord[0], coord[1])
    if (pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200):
      return i
  return -1

if __name__ == '__main__':
  load_coords(pixel_box)
  val = read_active_phrase()
  print(val)
