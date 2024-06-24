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

pip install pyfftw

# Raspberry Pi Only
pip install -r requirements.txt
python monitor-simple.py



# Tesseract (OCR)
https://github.com/UB-Mannheim/tesseract/wiki
Install the binary

pip install pytesseract

# add to path
export PATH=$PATH:/c/Program Files/Tesseract-OCR

# Getting this to work with TouchDesigner
https://docs.derivative.ca/Category:Python#Installing_Custom_Python_Packages
Under the Edit->Preferences menu, tick "Add External Python to Search Path". You can add the search path by modifying the Preference labelled "Python 32/64 bit Module Path". Multiple paths are separated by semicolons (;).

# pcap

# maybe? but pypcap recommended to check out npcap
pip install pypcap

https://npcap.com/
Install in WinAPI Compatibility Mode
pip install libpcap
pip install Cython
# from pypcap/ (and after copying npcap SDK to pypcap/wdpcap/)
# add noexcept to __pcap_handler: "noexcept with gil:"
cython pcap.pyx

# try this method...
pip install pcap-ct

# or...
pip install scapy

cd /e/git/python-prodj-link/
python listener.py