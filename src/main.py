import pyaudio
import wave
import threading
import time
import subprocess
import cv2
import numpy as np
import os


#record audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "tmp.wav"

class recorder:
    def __init__(self):
        self.going = False
        self.process = None
        self.filename = "ScreenCapture.mpg"
    def record(self,filename):
        try:
            if self.process.is_alive():
                self.going = False
        except AttributeError:
            print("test")
        self.process = threading.Thread(target=self._record)
        self.process.start()
        self.filename = filename
    def _record(self):
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
        

    def stop_recording(self):
        self.going = False


#record video and audio
def RecordVideo():
    if os.path.exists('output.avi'):
        print("video exists")
        os.remove('output.avi')
    
    if os.path.exists('tmp.wav'):
        print("audio exists")
        os.remove('tmp.wav')
        
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    audio = recorder()
    audio.record(audio.filename)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,100)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    audio.stop_recording()
    cap.release()
    out.release()
    cv2.destroyAllWindows()

RecordVideo()