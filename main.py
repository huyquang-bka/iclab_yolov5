from detect_yolov5 import Detection
import cv2

slot_list = []
with open("slot.txt", "r") as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x1, y1, w, h = line.split(" ")
        x1, y1, w, h = int(x1), int(y1), int(w), int(h)
        x2, y2 = x1 + w, y1 + h
        slot_list.append([x1, y1, x2, y2])
        
img = cv2.imread("C9/C9_base_26.01.2021_06.00.00.jpg")

detection = Detection()

weight_path = "weights/yolov5s.pt"
classes = [2, 7]
conf = 0.01
imgsz = 640
device = "cpu"

detection.setup_model(weight_path, classes, conf, imgsz, device)

detect_list = detection.detect(img)

    
for slot_box in slot_list:
    x1_slot, y1_slot, x2_slot, y2_slot = slot_box
    is_busy = False
    for detect_box in detect_list:
        x1, y1, x2, y2, name, conf = detect_box
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)
        if x1_slot <= center_x <= x2_slot and y1_slot <= center_y <= y2_slot:
            is_busy = True
            cv2.rectangle(img, (x1_slot, y1_slot), (x2_slot, y2_slot), (0, 0, 255), 2)
            cv2.putText(img, name, (x1_slot, y1_slot), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            break
    if not is_busy:
        cv2.rectangle(img, (x1_slot, y1_slot), (x2_slot, y2_slot), (0, 255, 0), 2)

img = cv2.resize(img, (1280, 720))
cv2.imshow("img", img)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
