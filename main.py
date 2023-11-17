import cv2
import time
import datetime
import logging
from imageanalysis import *
from record import *
from threading import Thread

while True:
    try:
        if cv2.waitKey(1) & 0xFF == 27:
            break
        else:
            analyzeimage()
            
    except BaseException:
            logging.exception('An exception was thrown!')
            pass
    



