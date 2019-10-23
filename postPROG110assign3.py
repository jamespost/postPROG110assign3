"""James Post PROG 110 Assignment 3"""
#this module was tested using Python 3.7.3, the print functions used in it will not work with python 2.x
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
        print("Amplify()")
        #increases the amplitude of the audio file by the amount of amplifyGain
        self.amplitudePeaks += amplifyGain
        print("\t", self.filename, " amplified by ", amplifyGain, " dB"," new amplitude peak is ", self.amplitudePeaks, " dB")

    def Fade(self, fadeType, fadeTime):
        """Fades in the signal of the audio file"""
        
        if fadeType == "In":
            #sets the amplitude of the file to a minimum value and increases that over fadeTime until it hits the original amplitude peak
            
            print("Fade In()")
            #initialize local variables
            self.originalAmplitudePeaks = self.amplitudePeaks
            self.amplitudePeaks = -120
            currentFadeTime = 0
            #while startFadeTime < fadeTime increase amplitudePeaks 
            while currentFadeTime < fadeTime:
                if self.amplitudePeaks < self.originalAmplitudePeaks:
                    self.amplitudePeaks += ((self.originalAmplitudePeaks -self.amplitudePeaks)/(fadeTime - currentFadeTime))
                    currentFadeTime += 1
                    print("\tcurrent amplitude is " , self.amplitudePeaks, " dB")
                else:
                    break  
        if fadeType == "Out":
            print("Fade Out()")
            #initialize local variables
            self.originalAmplitudePeaks = self.amplitudePeaks
            self.amplitudePeakMin = -120
            currentFadeTime = 0
            #while startFadeTime < fadeTime decrease amplitudePeaks
            while currentFadeTime < fadeTime:
                if self.amplitudePeaks > self.amplitudePeakMin:
                    self.amplitudePeaks -= ((self.originalAmplitudePeaks -self.amplitudePeakMin)/(fadeTime - currentFadeTime))
                    currentFadeTime += 1
                    print("\tcurrent amplitude is " , self.amplitudePeaks, " dB")
                else:
                    break 
    
    def Echo(self, delayTime, decayFactor):
        """Echos (repeats with amplitude decay) the signal of the audio file"""
        #repeat the file after delayTime and decrease its amplitude each repeat by decayFactor
        print("Echo()")
        print("\tKeep track of time passing until it matches delayTime")
        print("\tWhen time == delayTime play the file")
        print("\tEach time time == delayTime the amplitude of the file will decrease by decayFactor until the file amplitude == -120 dB")
            
    def Repeat(self, numRepeats):
        """Repeats the signal of the audio file"""
        #if numRepeats > 0 and the file has finished playing play the file again
        print("Repeat()")
        while numRepeats > 0:
            print("\tThe file has repeated playing")
            numRepeats -= 1

    def Normalize(self, threshold):
        """Normalizes (increases amplitude of the file until the maximum amplitude peak is equal to the normalization threshhold) the signal of the audio file"""
        print("Normalize()")
        #if amplitudePeaks < threshold, set amplitudePeaks to threshold
        if self.amplitudePeaks < threshold:
            amplitudePeaks = threshold
            print("\tNormalized audio to ", threshold, " dB")
        else:
            print("\tAmplitude cannot exceed Threshold")

#Functionality proof

#create an instance of an AudioEffect
myTestEffect = AudioEffect("testFileName")

#print its attributes
str(myTestEffect)

#run its Amplify() function
myTestEffect.Amplify(6)

#run its Fade() function as a fade in
myTestEffect.Fade("In",5)

#run its Fade() function as a fade out
myTestEffect.Fade("Out",5)

#run its Echo() function
myTestEffect.Echo(5,3)
#run its Repeat() function
myTestEffect.Repeat(3)

#run its Normalize() function
myTestEffect.Normalize(-3)