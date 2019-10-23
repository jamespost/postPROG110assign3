"""James Post PROG 110 Assignment 3"""
#this class was tested using Python 3.7.3
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
        self.amplitudePeaks = float(-12)#default peak is -12dB        

    def __str__(self):#This is code is based off of the example code from "carClassy.py" but only formats properly in Python3, not Python2
            """Defines what to do when the default python str() function is called on an instance"""
            print("Audio File Info:")
            print("\tFilename = " , self.filename)
            print("\tBit Depth = " , self.bitDepth)
            print("\tSample Rate = " , self.sampleRate, " kHz")
            print("\tLength = " , self.length, " samples")
            print("\tAmplitude Peaks = " , self.amplitudePeaks, " dB")
            return("")

    #Psuedocode of AudioEffect functions
    def Amplify(self, amplifyGain):
        """Amplifys the signal of the audio file"""

        #increases the amplitude of the audio file by the amount of amplifyGain
        self.amplitudePeaks += amplifyGain
        print(self.filename, " amplified by ", amplifyGain, " dB"," new amplitude peak is ", self.amplitudePeaks, " dB")

    def FadeIn(self, fadeTime):
        """Fades in the signal of the audio file"""
        #sets the amplitude of the file to a minimum value and increases that over fadeTime until it hits the original amplitude peak
        #initialize local variables
        self.originalAmplitudePeaks = self.amplitudePeaks
        self.amplitudePeaks = -120
        currentFadeTime = 0
        #while startFadeTime < fadeTime increase amplitudePeaks by fadeFactor
        while currentFadeTime < fadeTime:
            if self.amplitudePeaks < self.originalAmplitudePeaks:
                self.amplitudePeaks += ((self.originalAmplitudePeaks -self.amplitudePeaks)/(fadeTime - currentFadeTime))
                currentFadeTime += 1
                print("current amplitude is " , self.amplitudePeaks, " dB")
            else:
                break            


    def FadeOut(self, fadeFactor, fadeTime):
        """Fades out the signal of the audio file"""

    def Echo(self, delayTime, decayFactor):
        """Echos (repeats with amplitude decay) the signal of the audio file"""
    
    def Repeat(self, numRepeats):
        """Repeats the signal of the audio file"""

    def Normalize(self, threshold):
        """Normalizes (increases amplitude of the file until the maximum amplitude peak is equal to the normalization threshhold) the signal of the audio file"""

        #if amplitudePeaks < threshold, set amplitudePeaks to threshold
        if self.amplitudePeaks < threshold:
            amplitudePeaks = threshold
            print("Normalized audio to ", threshold, " dB")
        else:
            print("Amplitude cannot exceed Threshold")