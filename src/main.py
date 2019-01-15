
import recorder as re
import helper as he
import os
from keras.models import load_model
import cv2
import numpy as np

IMAGE_DIR = "Images"

record = re.recorder()

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

img = cv2.imread("/home/local/ZOHOCORP/siva-5548/Documents/Artificial intelligence/Interview Ai/Interview-Ai-bot/src/Face/image15.jpg")
lastimg = cv2.resize(img, (48, 48))
gray_image = lastimg/255
out = gray_image[np.newaxis, :, :]
predictions = EAnalysis.predict(out)
print(he.getEmotion(predictions))