
import recorder as re
import helper as he
import os
from keras.models import load_model
import cv2
import numpy as np

IMAGE_DIR = "Images"

#record = re.recorder()

###remove file if already present
record.fileCheck()

#3now start recording
record.record()

cropper = he.FaceCropper()
IMAGE_INDEX = 1
for file in os.listdir(IMAGE_DIR):
    image = os.path.join(IMAGE_DIR,file)
    IMAGE_INDEX = cropper.generate(image,IMAGE_INDEX)

EAnalysis = load_model("../Emotion_analysis")


sad = np.array([["Image","Emotion"]], dtype=object)
predit = np.array([[ 'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise','Neutral']],dtype=object)
for file in os.listdir(he.FACEDIR):
    face = os.path.join(he.FACEDIR,file)
    img = cv2.imread(face)
    lastimg = cv2.resize(img, (48, 48))
    gray_image = lastimg/255
    out = gray_image[np.newaxis, :, :]
    predictions = EAnalysis.predict(out)
    emotion = he.getEmotion(predictions)
    sad = np.append(sad,[[face,emotion]],axis=0)
    predit = np.append(predit,predictions,axis=0)

f=open('emotion.dat','ab')
np.savetxt(f,sad,fmt='%s')
f.close()

x=open('prediction.dat','ab')
np.savetxt(x,predit,fmt='%s')
x.close()