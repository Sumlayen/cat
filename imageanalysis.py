import cv2
import time
import sched
import datetime
import logging
from record import *


def analyzeimage():
    cam = cv2.VideoCapture(0)

    success, camera_capture = cam.read()

    # if camera_capture:
    camera_capture = cv2.resize(camera_capture, (320, 320))
    # h = camera_capture.shape[0]
    # w = camera_capture.shape[1]
    w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    weights = 'ssd_mobilenet/frozen_inference_graph.pb'
    model = 'ssd_mobilenet/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

    net = cv2.dnn.readNetFromTensorflow(weights, model)

    #Load class labels the model was trained on.
    class_names = []
    with open('ssd_mobilenet/coco_names.txt', 'r') as f:
        class_names = f.read().strip().split('\n')

    #Create blob from image.
    blob = cv2.dnn.blobFromImage(
        camera_capture, 1.0/127.5, (320, 320), [127.5, 127.5, 127.5])

    #Pass the blob through network and get predictions.
    net.setInput(blob)
    output = net.forward() #shape: (1, 1, 100, 7)

    #Loop over number of detected objects.
    for detection in output[0, 0, :, :]: #output[0, 0, :, :] has a shape of: (100, 7)
        #Confidence of the model regarding detected object
        probability = detection[2]

        #If the confidence of the model is lower than 75%, we do nothing(continue looping) 
        if probability < 0.7:
            continue

        #Get (x, y) of bounding box
        box = [int(a * b) for a, b in zip(detection[3:7], [w, h, w, h])]
        box = tuple(box)

        #Draw bounding box on object.
        cv2.rectangle(camera_capture, box[:2], box[2:], (0, 255, 0), thickness=2)

        #Get ID of detected object   
        class_id = int(detection[1])
        
        #Draw name of predicted object along with probability
        #label = f"{class_names[class_id - 1].upper()} {probability * 100:.2f}%"
        label = class_names[class_id - 1].upper()

        print(label)
        #####Logic here to detect cat in this loop.  Fire off record function.
        #Return 1 if success then loop again in main.py.
        if label == 'CAT' or label == 'DOG':
                print('I found a ' + str(label).lower() + '.')
                text = f"{label} {probability * 100:.2f}%"
                cv2.putText(camera_capture, text, (box[0], box[1] + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                now = datetime.datetime.now()
                dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

                filename = './evidence/gotcha-' + str(dt_string) + '.jpg'
                
                cv2.imwrite(filename, cv2.resize(camera_capture, (1920, 1080)))

                # del label, probability, camera_capture, box
                cam.release()

                recordvideo()    
        else:
                continue
                # del label, probability, camera_capture, box
        time.sleep(10)
 
    