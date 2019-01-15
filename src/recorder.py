
import pyaudio
import wave
import threading
import time
import subprocess
import cv2
import numpy as np
import os
import shutil

#record audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"
IMAGE_DIR = "Images"

class recorder:
    def __init__(self):
        self.going = False
        self.process = None
        self.audoFilename = "audio.wav"
        self.videoFilename = 'video.avi'
       # if os.path.isdir(IMAGE_DIR):
       #     shutil.rmtree(IMAGE_DIR)
        
        #os.mkdir(IMAGE_DIR, 644)

    def record(self):

        self.recordAudio()
        cap = cv2.VideoCapture(0)
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.videoFilename,fourcc, 20.0, (640,480))
        count = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                frame = cv2.flip(frame,100)
                cv2.imwrite("Images/frame%d.jpg" % count, frame) 
                count += 1
                # write the flipped frame
                out.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        self.stopAudioRecord()
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def recordAudio(self):
        try:
            if self.process.is_alive():
                self.going = False
        except AttributeError:
            print("error")
        self.process = threading.Thread(target=self._audioRecord)
        self.process.start()

    def fileCheck(self):
        if os.path.exists(self.videoFilename):
            os.remove(self.videoFilename)
        if os.path.exists(self.audoFilename):
            os.remove(self.audoFilename)
    
    def _audioRecord(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        self.going = True
        
        while self.going:
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
    def stopAudioRecord(self):
        self.going = False

