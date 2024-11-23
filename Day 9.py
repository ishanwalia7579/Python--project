import qrcode
from PIL import Image

# Data to be encoded
data = "https://example.com/"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create a colorful image from the QR Code instance
img = qr.make_image(fill_color="blue", back_color="yellow")

# Optionally, add some colorful patterns
width, height = img.size
for x in range(width):
    for y in range(height):
        if img.getpixel((x, y)) == (0, 0, 0):  # Black pixels
            img.putpixel((x, y), (255, 0, 0))  # Change to red

# Save the image
img.save("color full qr.png")

print("Colorful QR Code generated and saved as 'color full qr.png'")
