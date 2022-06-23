import cv2

img = cv2.imread("C9/C9_base_26.01.2021_06.00.00.jpg")

rois = cv2.selectROIs("img", img, False, False)

print(rois)

with open("slot.txt", "w+") as f:
    for roi in rois:
        f.write(str(roi[0]) + " " + str(roi[1]) + " " + str(roi[2]) + " " + str(roi[3]) + "\n")

cv2.imshow("img", img)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
