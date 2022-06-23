# import cv2

# list_of_points = []


# # Get the mouse position
# def get_point(event, x, y, flags, param):
#     global list_of_points
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, y)
#         cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
#         list_of_points.append((x, y))
#         cv2.imshow('image', image)


# # Create a window
# scale = 0.5
# image = cv2.imread('C9/C9_base_26.01.2021_06.00.00.jpg')
# image = cv2.resize(image, dsize=None, fx=scale, fy=scale)
# # image = cv2.imread('test_TDN.png')
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', get_point)
# cv2.imshow('image', image)
# key = cv2.waitKey(0)
# if key == ord('q'):
#     print(list_of_points)
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     with open('plate_zone_2.txt', 'w+') as f:
#         for point in list_of_points:
#             f.write(str(int(point[0] / scale)) + ' ' + str(int(point[1] / scale)) + '\n')
#     cv2.destroyAllWindows()

from calendar import c
import cv2
import numpy as np


list_points = []

with open("plate_zone_2.txt", "r") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(" ")
        x, y = int(x), int(y)
        list_points.append([x, y])
    
points = np.array(list_points, dtype=np.int32)
points = points.reshape((-1, 1, 2))
    
alpha = 0.3

img = cv2.imread("C9/C9_base_26.01.2021_06.00.00.jpg")
img_copy = img.copy()

cv2.fillPoly(img, [points], (0, 0, 255))

img = cv2.addWeighted(img, alpha, img_copy, 1-alpha, 0)

img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
cv2.imshow("img", img)
key = cv2.waitKey(0)