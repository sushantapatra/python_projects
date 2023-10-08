import png
import pyqrcode

print(dir(pyqrcode))
# Import QRCode from pyqrcode
# String which represents the QR code
s = "Sushanta patra"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("mynameqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('mynameqr.png', scale=6)
