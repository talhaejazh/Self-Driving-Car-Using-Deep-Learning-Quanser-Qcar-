from Quanser.q_essential import Camera2D
import time
import struct
import numpy as np 
import cv2

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

################################################
#           Muhammad Talha Ejaz                #
#          talha.ej@hotmail.com                #   
################################################

## Timing Parameters and methods 

startTime = time.time()
def elapsed_time():
    return time.time() - startTime

sampleRate = 30.0
sampleTime = 1/sampleRate
simulationTime = 10.0
print('Sample Time: ', sampleTime)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# Additional parameters
counter = 0
imageWidth = 640
imageHeight = 480
cameraID = '3'

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
## Initialize the CSI cameras
myCam = Camera2D(camera_id=cameraID, frame_width=imageWidth, frame_height=imageHeight, frame_rate=sampleRate)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
## Main Loop
def frontcam():
    try:
        counter=0
        while elapsed_time() < simulationTime:
            
            # Start timing this iteration
            start = time.time()

            # Capture RGB Image from CSI
            myCam.read()
            #counter += 1

            # End timing this iteration
            end = time.time()

            # Calculate the computation time, and the time that the thread should pause/sleep for
            computationTime = end - start
            sleepTime = sampleTime - ( computationTime % sampleTime )
            
            # Display the four images
            cv2.imshow('Test Cam', myCam.image_data)
            
            # Pause/sleep for sleepTime in milliseconds
            msSleepTime = int(1000*sleepTime)
            # if msSleepTime <= 0:
            #     msSleepTime = 1 # this check prevents an indefinite sleep as cv2.waitKey waits indefinitely if input is 0
            #cv2.waitKey(msSleepTime)
            return myCam.image_data

    except KeyboardInterrupt:
        print("User interrupted!")

    finally:
        # Terminate all webcam objects    
        myCam.terminate()

for i in range(10):
  image=frontcam()
  cv2.imwrite(r"image{i}.png",image)
  #print(image.shape)
  i+=1
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
