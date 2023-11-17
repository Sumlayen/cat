import cv2
import time
import datetime
import logging
from imageanalysis import *
from record import *
from threading import Thread

# def main():
while True:
    try:
        if cv2.waitKey(1) & 0xFF == 27:
            break
        else:
            analyzeimage()
    # while True:
    #     try:
    #         label, probability, camera_capture, box = analyzeimage()
           
    #         # if label == '':
    #         #      continue
            
    #         print(label)
            # if label == 'CAT' or label == 'DOG':
            #     print('I found a ' + str(label).lower() + '.')
            #     text = f"{label} {probability * 100:.2f}%"
            #     cv2.putText(camera_capture, text, (box[0], box[1] + 15),
            #         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            #     now = datetime.datetime.now()
            #     dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")

            #     filename = './evidence/gotcha-' + str(dt_string) + '.jpg'
                
            #     cv2.imwrite(filename, cv2.resize(camera_capture, (1920, 1080)))

            #     del label, probability, camera_capture, box

            #     recordvideo()    
            # else:
            #      del label, probability, camera_capture, box
            # time.sleep(10)
            
    except BaseException:
            logging.exception('An exception was thrown!')
            pass
    
 
# main()


