"""James Post PROG 110 Assignment 3"""
class AudioEffects():#define a class name "AudioEffects"
    def __init__(self, filename):
        """Initialize effect attributes"""
        #calculate length of audio file
        self.length = int(44100) #default file length is 44100 samples (1 second)
        #calculate amplitude peaks
        self.amplitudePeaks = float(0)#default peak is 0dB
        #calculate sample-rate
        self.sampleRate = int(44100)#default sample rate is 44100
        #calculate bit-depth
        self.bitDepth = int(16)#default bit depth is 16bit
