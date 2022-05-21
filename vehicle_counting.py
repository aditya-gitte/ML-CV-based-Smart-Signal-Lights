import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("images/*.jpg")

vehicles_folder_count = 0

file=open('vehicle_count.txt','w')
cnt=1
# Loop through all the images
for img_path in images_folder:
    print("Img path", img_path)
    img = cv2.imread(img_path)

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)              #number of vehicles in one image of the folder
    file.write(f"vehicle count from image {cnt} = {vehicle_count} \n")
    vehicles_folder_count += vehicle_count          #total number of vehicles from all the images from the folder 

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    cv2.imshow("Cars", img)
    cv2.waitKey(10000)                 #waits for 10 seconds to after showing the picture with the detected cars marked before moving to the next image.
    cnt+=1

file.write(f"vehicle count from all the images is = {vehicles_folder_count} \n")
file.close()
print("Total current count", vehicles_folder_count)