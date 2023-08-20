import cv2
import numpy as np

# Load the YOLOv3 network
net = cv2.dnn.readNetFromDarknet('yolov3-320.cfg', 'yolov3-320.weights')
# Load the COCO class labels
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Load the image
img = cv2.imread('test4.jpg')

# Resize the image to match YOLO input size
resized_img = cv2.resize(img, (416, 416))
# Convert the image to a blob
blob = cv2.dnn.blobFromImage(resized_img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Set the network input and forward it
net.setInput(blob)
output_layers = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers)

# Define the center line of the road as the midpoint of the image
center_line = resized_img.shape[1] // 2

# Define the threshold for confidence score and NMS
conf_threshold = 0.5
nms_threshold = 0.4

# Apply NMS to each class of detections
class_ids = []
confidences = []
boxes = []
for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if classes[class_id] in ['car', 'bus', 'truck', 'motorbike']:
            if confidence > conf_threshold:
                # Get the coordinates and dimensions of the bounding box
                center_x, center_y, width, height = list(map(int, detection[:4] * np.array([resized_img.shape[1], resized_img.shape[0], resized_img.shape[1], resized_img.shape[0]])))
                top_left_x = center_x - (width // 2)
                top_left_y = center_y - (height // 2)
                
                # Add the box information to the lists
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([top_left_x, top_left_y, width, height])

# Apply NMS to the boxes
indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# Count the number of vehicles in each lane and of each type, and draw bounding boxes around them
left_lane_vehicles = 0
right_lane_vehicles = 0
left_car_count = 0
right_car_count = 0
left_bus_count = 0
right_bus_count = 0
right_truck_count = 0
left_truck_count = 0

left_motorbike_count = 0
right_motorbike_count = 0

for i in indices:
    #i = i[0]
    class_id = class_ids[i]
    confidence = confidences[i]
    box = boxes[i]
    top_left_x, top_left_y, width, height = box
    bottom_right_x = top_left_x + width
    bottom_right_y = top_left_y + height
    
    # Check the orientation of the bounding box
    if bottom_right_x < center_line:
        left_lane_vehicles += 1
        if classes[class_id] == 'car':
            left_car_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
        elif classes[class_id] == 'bus':
            left_bus_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 2)
        elif classes[class_id] == 'truck':
            left_truck_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 0), 2)
        elif classes[class_id] == 'motorbike':
            left_motorbike_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 255, 0), 2)
        #cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), 2)
    elif top_left_x > center_line:
        right_lane_vehicles += 1
        if classes[class_id] == 'car':
            right_car_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)
        elif classes[class_id] == 'bus':
            right_bus_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 255), 2)
        elif classes[class_id] == 'truck':
            right_truck_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (128, 0, 0), 2)
        elif classes[class_id] == 'motorbike':
            right_motorbike_count += 1
            cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 128), 2)
        #cv2.rectangle(resized_img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)


# Print the results
# print(f"Number of vehicles in the left lane: {left_lane_vehicles}")
# print(f"Number of vehicles in the right lane: {right_lane_vehicles}")
# print(f"number of cars in left lane : {left_car_count}")
# print(f"number of bikes in left lane : {left_motorbike_count}")
# print(f"number of trucks in left lane : {left_truck_count}")
# print(f"number of busses in left lane : {left_bus_count}")
# print(f"Number of cars in right lane: {right_car_count}")
# print(f"Number of bikes in right lane: {right_motorbike_count}")
# print(f"Number of buses in right lane: {right_bus_count}")
# print(f"Number of trucks in right lane: {right_bus_count}")

#evluate green time

green_time = (right_bus_count*1.5) + right_car_count + (right_motorbike_count*0.5) + (right_truck_count*1.5)

# Save the output image
cv2.imwrite('output.jpg', resized_img)