import numpy as np
import cv2

#SOURCE http://www.life2coding.com/python-opencv-based-face-masking-tutorial/
#inspiration taken from this site while I wrote majority of the code
def runCV(shirt, glasses):
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #nose = cv2.CascadeClassifier('haarcascade_nose.xml')
    upperBody = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    cap = cv2.VideoCapture(0)
    #adjust camera fps
    #I find lower fps could speed up run time, will find a better fix later
    cap.set(cv2.CAP_PROP_FPS, 10)
    if glasses != 0:
        specs_ori = cv2.imread(glasses, -1)
    if shirt != 0:
        tshirt_ori = cv2.imread(shirt, -1)
    
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
        
    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 4)
        waists = face.detectMultiScale(gray, 1.3, 5)
        #works better on distinct backgrounds
        bodies = upperBody.detectMultiScale(gray, 1.2, 5)
        #draw rectangle on face
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            #cv2.rectangle(img, (x+w//2-20, y+h//2-20), (x+w//2+20, y+h//2+20), (0, 0, 255),2) 
            #print(x+w/2, y+h/2)
        
        #draw rectangle on upperbody
        for (x, y, w, h) in bodies:
            cv2.rectangle(img,(x,y),(x+w,y+h+int(h/2)),(0,0,255),3)
        
        #overlay glasses on face
        if glasses != 0:
            for (x, y, w, h) in faces:
                if h > 0 and w > 0:
        
                    glass_symin = int(y + 1.2 * h / 5)
                    glass_symax = int(y + 2.8 * h / 5)
                    sh_glass = glass_symax - glass_symin
        
                    face_glass_roi_color = img[glass_symin:glass_symax, x:x+w]
        
                    specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
                    transparentOverlay(face_glass_roi_color,specs)
        
        #overlay shirt on upperbody
        if shirt != 0:
            for (x, y, w, h) in bodies:
                if h > 0 and w > 0:
                    
                    tshirt_symin = int(y + 3 * h /6)
                    tshirt_symax = int(y + 10 * h / 5)
                    sh_tshirt = tshirt_symax - tshirt_symin
                    
                    body_tshirt_roi_color = img[tshirt_symin:tshirt_symax, x:x+w]
                    
                    tshirt = cv2.resize(tshirt_ori, (w, sh_tshirt), interpolation=cv2.INTER_CUBIC)
                    transparentOverlay(body_tshirt_roi_color, tshirt)
    
    
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('img.jpg', img)
            break
    
    cap.release()
    cv2.destroyAllWindows()