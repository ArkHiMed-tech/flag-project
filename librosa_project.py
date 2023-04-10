import librosa
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import time


audio_data = './hymn.wav'
x , sr = librosa.load(audio_data)
print(x)
lst = []
for i in range(10):
    lst.append(librosa.feature.mfcc(y=x[i*44100*2:(i+1)*44100*2], sr=44100))
percentrate = 0.5

def compare_mfcc(mfcc_1, mfcc_2):
    fin = []
    mfcc_2 = list(mfcc_2)
    for i in mfcc_1:
        i = list(i)
        prom = []
        for j in range(len(i)):
            kr = []
            for k in range(len(i[j])):
                kr.append(min(i[j][k], mfcc_2[j][k])/max(i[j][k], mfcc_2[j][k]))
            
            prom.append(sum(kr)/len(kr))
        fin.append(sum(prom)/len(prom))
    return max(fin)

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 44100 * 2
        self.p = None
        self.stream = None

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()

    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        zahvat_ochka = librosa.feature.mfcc(y=numpy_array, sr=44100)

        print(compare_mfcc(lst, zahvat_ochka))

        return None, pyaudio.paContinue

    def mainloop(self):
        while (self.stream.is_active()): 

            time.sleep(2.0) # КД


audio = AudioHandler()
audio.start()
audio.mainloop()
audio.stop()

