# %%
import time

import cv2
import mss
import numpy as np
from skimage.transform import PiecewiseAffineTransform, warp

npzfile = np.load('params.npz')

projector_resolution = (1920,1080)
with mss.mss() as sct:
    # Part of the screen to capture
    monitor = sct.monitors[1]
    # monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        resized = cv2.resize(img,projector_resolution , interpolation = cv2.INTER_AREA) 

        tform = PiecewiseAffineTransform()
        tform.estimate(npzfile['points_dst'], npzfile['points_src'])
        
        out = warp(resized, tform, output_shape=(1080,1920))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", out)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break