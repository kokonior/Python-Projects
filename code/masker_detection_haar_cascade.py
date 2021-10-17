import cv2
import winsound
import glob


"""
Memanggil data training dari haarcascade
Data berupa wajah, mata, dan mulut.
"""
DeteksiWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
DeteksiMata = cv2.CascadeClassifier('haarcascade_eye.xml')
DeteksiMulut = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
DeteksiMasker = cv2.CascadeClassifier('cascade.xml')

"""
INISIALISASI DATA YANG AKAN DIGUNAKAN
Seperti nilai threshold yang dapat diatur sesuai tingkat cahaya yang ada, dari 80-105

"""
bw_threshold = 90

font = cv2.FONT_HERSHEY_TRIPLEX
org = (22, 22)
warna_font_pakai_masker = (248,248,255)
warna_font_tidak_pakai_masker = (0, 0, 255)
thickness = 2
font_scale = 1
#peringatan ="JANGAN LUPA PAKAI MASKER"
pakai_masker = "TERIMA KASIH SUDAH MEMAKAI MASKER"
tidak_pakai_masker = "TOLONG PAKAI MASKER ANDA"
count = 0
positif = 0
negatif = 0
#files = glob.glob("dataset/p/*.jpg")


# Mengambil video dari kamera internal
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('2.mp4')
#img = cv2.imread("dataset/p/b1.jpg")
#img = cv2.resize(img1,(240,300))

"""
OLAH VIDEO DIBAWAH INI
WHILE UNKOMEN
KLO OLAH FOTO/FOLDER
DI BAWAHNYA LAGI
"""
while 1:
#for file in files:
    #olah video di bawah
    # Mengambil setiap frame
    ret, img = cap.read()
    img = cv2.flip(img,1)
    
    #olah gambar di bawah
    #img = cv2.imread("dataset/p/b1.jpg")
    #img = cv2.resize(img1,(240,300))
    # mengubah citra dari rgb ke gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # mengubah citra dari gray ke bw dengan parameter hasil konversi dan nilai threshold di atas
    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('black_and_white', black_and_white)

    # mendeteksi wajah
    faces = DeteksiWajah.detectMultiScale(gray, 1.1, 4)

    # mendeteksi wajah dalam hitam putih
    faces_bw = DeteksiWajah.detectMultiScale(black_and_white, 1.1, 4)

    #mendeteksi masker
    masker = DeteksiMasker.detectMultiScale(gray,1.2,4)
    
    #deteksi masker
    if(len(masker) ==1):
        cv2.putText(img, pakai_masker, org, font, font_scale, warna_font_pakai_masker, thickness, cv2.LINE_AA)
        #print (pakai_masker)
        positif +=1
        for (x, y, w, h) in masker:
            cv2.rectangle(img, (x, y), (x + w, y + h), (30, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            #print("Image "+str(count)+"Tersimpan")
            #file='G:/Python/WPy64-3770/notebooks/DeteksiMasker/tersangka/kompre'+str(count)+'.jpg'
            #cv2.imwrite(file, img)
            count+=1
    #wajah tidak terdeteksi
    elif(len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, pakai_masker, org, font, font_scale, warna_font_pakai_masker, thickness, cv2.LINE_AA)
    elif(len(faces) == 0 and len(faces_bw) == 1):
        cv2.putText(img, pakai_masker, org, font, font_scale, warna_font_pakai_masker, thickness, cv2.LINE_AA)
    else:
        # Membuat kotak di wajah
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]


            # Deteksi Mulut
            mouth_rects = DeteksiMulut.detectMultiScale(gray, 1.5, 5)

        # Wajah terdeteksi tapi mulut tidak, yang berarti menggunakan masker
        if(len(mouth_rects) == 0):
            cv2.putText(img, pakai_masker, org, font, font_scale, warna_font_pakai_masker, thickness, cv2.LINE_AA)
            #print(pakai_masker)
            #positif +=1
        else:
            for (mx, my, mw, mh) in mouth_rects:
                cv2.rectangle(img,(mx, my), (mx+w, my+h), (255, 20, 55), 2)
                roi_gray = gray[my:my + h, mx:mx + w]
                roi_color = img[my:my + h, mx:mx + w]

                if(y < my < y + h):
                    cv2.putText(img, tidak_pakai_masker, org, font, font_scale, warna_font_tidak_pakai_masker, thickness, cv2.LINE_AA)
                    
                    # memainkan audio peringatan yang bernama WOY.wav 
                    #winsound.PlaySound('WOY.wav',winsound.SND_FILENAME)
                    
                    # menjepret sosok yang tidak memakai masker
                    #print("Image "+str(count)+"Tersimpan")
                    #file='G:/Python/WPy64-3770/notebooks/DeteksiMasker/tersangka/deteksi'+str(count)+'.jpg'
                    #cv2.imwrite(file, img)
                    count +=1
                    #print(tidak_pakai_masker)
                    #negatif +=1

                    #cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    break

    # Menampilkan frame beserta hasilnya
    cv2.imshow('Mask Detection', img)
    #print("Total Masker terdeteksi adalah: "+str(negatif))
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Tutup Video
cap.release()
cv2.destroyAllWindows()
