# %%
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import PiecewiseAffineTransform, warp
from skimage import data
from math import prod
from copy import deepcopy

import cv2

checkerboard_size = (5,4)
points_dst = np.zeros((prod(checkerboard_size),2), np.float32)
i = 0

def draw_circle(event,x,y,flags,param):
    global points_dst, i
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img_with_points,(x,y),5,(255,0,0),-1)
        cv2.drawMarker(img_with_points, (x, y),(255,0,0), markerType=cv2.MARKER_STAR, 
            markerSize=40, thickness=1, line_type=cv2.LINE_AA)
        points_dst[i,0] = x
        points_dst[i,1] = y
        i += 1
        print(points_dst)


def redraw_markers(img, markers):
    img_with_points = deepcopy(img)
    for marker in markers:
        cv2.drawMarker(img_with_points, tuple(marker),(255,0,0), markerType=cv2.MARKER_STAR, 
            markerSize=40, thickness=1, line_type=cv2.LINE_AA)
    return img_with_points

img = cv2.imread('materials/55x85_5x4_with_border.png')
img_with_points = deepcopy(img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find Corners
ret, corners = cv2.findChessboardCorners(gray, checkerboard_size,None)

# If found, add image points (after refining them)
if ret == True:
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    points_src = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
    points_src = points_src.reshape(prod(checkerboard_size),2)
    # Draw and display the corners
    img_with_points = cv2.drawChessboardCorners(img_with_points, checkerboard_size, points_src,ret)
else:
    print("No image corners were detected.")

cv2.namedWindow('img')
cv2.setMouseCallback('img',draw_circle)

# wait until user clicks on every corner
while(1):
    cv2.imshow('img',img_with_points)
    k = cv2.waitKeyEx(20)
    if k == ord('w'): #w = UP
        points_dst[i-1,1] -=1
        img_with_points = redraw_markers(img, points_dst)
        #print(points_dst)
    if k == ord('s'): #s = DOWN
        points_dst[i-1,1] +=1
        img_with_points = redraw_markers(img, points_dst)
        #print(points_dst)
    if k == ord('a'): #a = LEFT
        points_dst[i-1,0] -=1
        img_with_points = redraw_markers(img, points_dst)
        #print(points_dst)
    if k == ord('d'): #d = RIGHT
        points_dst[i-1,0] +=1
        img_with_points = redraw_markers(img, points_dst)
        #print(points_dst)
    if k == ord('q'):
        break
    # if i == prod(checkerboard_size):
    #     break

#cv2.destroyAllWindows()

# %%

tform = PiecewiseAffineTransform()
tform.estimate(points_dst, points_src)

out_rows = img.shape[0]
out_cols = img.shape[1]
out = warp(img, tform, output_shape=(out_rows, out_cols))

cv2.imshow('out',out)
k = cv2.waitKeyEx(0)

# %% Save parameters
np.savez('params.npz', points_src=points_src, points_dst=points_dst)
#_ = outfile.seek(0)
#npzfile = np.load('params.npz')
#sorted(npzfile.files)

#npzfile['points_src']
# %%
