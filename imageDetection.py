import cv2
from vehicle_detector import VehicleDetector
# Load Veichle Detector
vd = VehicleDetector()
img = cv2.imread("image.jpg")
vehicle_boxes = vd.detect_vehicles(img)
vehicle_count=len(vehicle_boxes)
vehicle_count_print=str(vehicle_count)
f=open("vehicle_count.txt","w")
f.write(vehicle_count_print)
f.close()
print(vehicle_count_print)
for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
cv2.imshow("Cars", img)
cv2.waitKey(0)
