"""James Post PROG 110 Assignment 3"""
class AudioEffect():#define a class name "AudioEffect" using psuedocode
    def __init__(self, filename):
        """Initialize effect attributes"""
        #store the filename of the audiofile being passed in
        self.filename = filename
        #calculate bit-depth
        self.bitDepth = int(16)#default bit depth is 16bit
        #calculate sample-rate
        self.sampleRate = int(44100)#default sample rate is 44100
        #calculate length of audio file
        self.length = int(44100) #default file length is 44100 samples (1 second)
        #calculate amplitude peaks
        self.amplitudePeaks = float(0)#default peak is 0dB        

    def __str__(self):#This is code is based off of the example code from "carClassy.py" but doesn't seem to format correctly
            """Defines what to do when the default python str() function is called on an instance"""
            print("Audio File Info:")
            print("\tFilename = " , self.filename)
            print("\tBit Depth = " , self.bitDepth)
            print("\tSample Rate = " , self.sampleRate)
            print("\tLength = " , self.length)
            print("\tAmplitude Peaks = " , self.amplitudePeaks)
            return("")

    def Amplify():
        