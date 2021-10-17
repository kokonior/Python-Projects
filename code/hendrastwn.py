# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5: #Accuracy
            # Object detected / Deteksi Object
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates / Koordinat Persegi Panjang
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Index Open Source Computer Vision Library
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes)
font = cv2.FONT_HERSHEY_SIMPLEX

[net]
batch=64
subdivisions=8
# Training
#width=512
#height=512
width=320
height=320
channels=3
momentum=0.949
decay=0.0005
angle=0
saturation = 1.5
exposure = 1.5
hue=.1

learning_rate=0.0013
burn_in=1000
max_batches = 500500
policy=steps
steps=400000,450000
scales=.1,.1

for i in range(len(boxes)):
    if i in indexes: 
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        color = (255,255,255)
        rectangle_bgr = (255, 255, 255) #background label
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y+30), font, 1, color, 2)

        
        #Load YOLO Algorithms\
net=cv2.dnn.readNet("yolov3.weights","yolov3.cfg")
#To load all objects that have to be detected
classes=[]
with open("coco.names","r") as f:
    read=f.readlines()
for i in range(len(read)):
    classes.append(read[i].strip("\n"))
#Defining layer names
layer_names=net.getLayerNames()
output_layers=[]
for i in net.getUnconnectedOutLayers():
    output_layers.append(layer_names[i[0]-1])
        
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
