# requirements
# pip install qrcode
# pip install pillow
import qrcode

# Creating a QR code object.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# Taking the input from the user and converting it into a QR code.
qr.add_data(str(input("Enter the text to be converted to QR code: ")))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
