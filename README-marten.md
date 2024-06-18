# create virtual environment named `venv`
virtualenv venv

# activate that environment
source ./venv/Scripts/activate

# not sure if this is the correct pip
# had to update PyQt5 version
pip install -r requirements.txt

# other deps
pip install image-similarity-measures
# 10.3.0
pip install --upgrade Pillow

pip instal pyfftw


# Tesseract (OCR)
https://github.com/UB-Mannheim/tesseract/wiki
Install the binary

pip install pytesseract

# add to path
export PATH=$PATH:/c/Program Files/Tesseract-OCR