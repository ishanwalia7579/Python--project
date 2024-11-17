# create a Qr code generation object
import qrcode

# Data to be encoded
data = "https://www.example.com"

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")
