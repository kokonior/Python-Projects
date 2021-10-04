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

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes)
font = cv2.FONT_HERSHEY_SIMPLEX


for i in range(len(boxes)):
    if i in indexes: 
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        color = (255,255,255)
        rectangle_bgr = (255, 255, 255) #background label
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y+30), font, 1, color, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
