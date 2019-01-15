import cv2
import shutil
import os

FACEDIR = "Face"
class FaceCropper(object):
    CASCADE_PATH = "haarcascade_frontalface_default.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)
        if os.path.isdir(FACEDIR):
            shutil.rmtree(FACEDIR)
        
        os.mkdir(FACEDIR,0755)
        
    def generate(self, image_path,i):
        img = cv2.imread(image_path)
        if (img is None):
            print("Can't open image file")
            return 0

        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(img, 1.1, 3, minSize=(100, 100))
        if (faces is None):
            return 0

        facecnt = len(faces)
        if facecnt is 0:
            os.remove(image_path)
            return i
            
        height, width = img.shape[:2]

        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny:ny+nr, nx:nx+nr]
            lastimg = cv2.resize(faceimg, (96, 96))
            i += 1
            cv2.imwrite("/home/local/ZOHOCORP/siva-5548/Documents/Artificial intelligence/Interview Ai/Interview-Ai-bot/src/Face/image%d.jpg" % i, lastimg)
        return i