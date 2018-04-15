import numpy as np
import cv2


face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose = cv2.CascadeClassifier('haarcascade_nose.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
specs_ori = cv2.imread('glasses.png', -1)

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][2] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src
    
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.rectangle(img, (x+w//2-20, y+h//2-20), (x+w//2+20, y+h//2+20), (0, 0, 255),2) 
        print(x+w/2, y+h/2)
    
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
 
            glass_symin = int(y + 1.5 * h / 5)
            glass_symax = int(y + 2.5 * h / 5)
            sh_glass = glass_symax - glass_symin

 
            face_glass_roi_color = img[glass_symin:glass_symax, x:x+w]
 
            specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
            transparentOverlay(face_glass_roi_color,specs)


    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('img.jpg', img)
        break

cap.release()
cv2.destroyAllWindows()

'''import numpy as np
import cv2
 
face_cascade = cv2.CascadeClassifier('frontalface_default.xml')
specs_ori = cv2.imread('glass/glass.png', -1)
cigar_ori = cv2.imread('mouth/cigar.png',-1)
 
cap = cv2.VideoCapture(0) #webcame video
# cap = cv2.VideoCapture('jj.mp4') #any Video file also
cap.set(cv2.CAP_PROP_FPS, 30)
 
 
 
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src
 
 
 
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
 
            glass_symin = int(y + 1.5 * h / 5)
            glass_symax = int(y + 2.5 * h / 5)
            sh_glass = glass_symax - glass_symin
 
            cigar_symin = int(y + 4 * h / 6)
            cigar_symax = int(y + 5.5 * h / 6)
            sh_cigar = cigar_symax - cigar_symin
 
            face_glass_roi_color = img[glass_symin:glass_symax, x:x+w]
            face_cigar_roi_color = img[cigar_symin:cigar_symax, x:x+w]
 
            specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
            cigar= cv2.resize(cigar_ori, (w, sh_cigar),interpolation=cv2.INTER_CUBIC)
            transparentOverlay(face_glass_roi_color,specs)
            transparentOverlay(face_cigar_roi_color,cigar,(int(w/2),int(sh_cigar/2)))
 
    cv2.imshow('Thugs Life', img)
 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cv2.imwrite('img.jpg', img)
        break
 
cap.release()
 
cv2.destroyAllWindows()'''
