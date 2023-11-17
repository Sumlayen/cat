import cv2
import datetime
import time
from servo import *
from threading import Thread
import logging

def recordvideo():
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
    filename = './evidence/gotcha-' + str(dt_string) + '.avi'
    t_end = time.time() + 60 * .2

    Thread(target=spin).start()
    try:
        #Thread(target=spin).start()
        cap = cv2.VideoCapture(0)    

        width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        writer= cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'X264'), 20, (width,height))

        while True:
            ret,frame= cap.read()

            if ret == True:
                writer.write(frame)
            else:
                break

            if time.time() > t_end:
                break

        cap.release()
        writer.release()

    except BaseException:
            logging.exception('An exception was thrown!')
            pass



