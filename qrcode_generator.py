!pip install qrcode #install qrcode package from PyPi
import qrcode    #import qrcode
img=qrcode.make("https://youtu.be/Xh_jQPz7PIw") #desired link
img.save("project_vid_qr.jpg") #save it with your desired file-name.jpg