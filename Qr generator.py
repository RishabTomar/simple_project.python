
import qrcode

# Data to encode in the QR code
data = "Rishab Tomar"  # Change this to any data you want to encode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (module) in the QR code
    border=4,  # Thickness of the border
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qr_code.png")

# Optionally, you can show the image
img.show()
