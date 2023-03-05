import cv2
# resim okuma

# img = cv2.imread('me.png.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Profil', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Kamera açma ve anlık alma
"""
vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    # kınp = cv2.waitKey(0)
    kınp = cv2.waitKey(1) # buraya 0 verirseniz anlık alır

    if kınp == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

"""


# Video açtırma || Video (canlı) Açma && video  yavaşlatma-hızlatma...
"""
vid_ac = cv2.VideoCapture(0)

if vid_ac.isOpened() == False:
    print("!!!  Videoya Erişilemedi  !!!")

while vid_ac.isOpened():
    ret, frame = vid_ac.read()

    if ret == True:
        cv2.imshow('frame', frame)

        kInp = cv2.waitKey(1)
        if kInp == ord("q"):
            break
    else:
        break

vid_ac.release()
cv2.destroyAllWindows()
"""


# Video açıp kaydetme
"""
vid_save = cv2.VideoCapture(0)

widht = int(vid_save.get(3))
height = int(vid_save.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
size = (widht, height)

result = cv2.VideoWriter(
    'record.avi', fourcc, 24, size)

while True:
    ret, frame = vid_save.read()

    if ret == True:
        result.write(frame)
        cv2.imshow('frame', frame)

        kInp = cv2.waitKey(1)
        if kInp == ord("w"):
            break

    else:
        break

vid_save.release()
result.release()
cv2.destroyAllWindows()
"""
