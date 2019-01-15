
import recorder as re
import helper as he
import os


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
    