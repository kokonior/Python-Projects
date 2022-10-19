import qrcode
print()
print(".......................")


link = input("Type your text here : ")


img = qrcode.make(f'{link}')
img.save("Qr_code_generator\Qrcode.png")

print(f'Completed. \n Qrcode is saved as : Qrcode.png')
