import RPi.GPIO as GPIO
import time, os, serial, smtplib
import numpy as np
import pandas as pd
import cv2 as cv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class Emailer:
    def __int__(self):
        pass
    def sendMAil(self,ImgFileName):
        img_data = open(ImgFileName).read()
        msg = MIMEMultipart()
        msg['subject'] = '<obstacle detected>'
        msg['From'] = 'chharshith7@gmail.com'
        msg['To'] = 'harshithchukkabhotla@gmail.com'
        text = MIMEText('Human alert')
        msg.attach(text)
        image = MIMEImage(img_data,name=os.path.basename(ImgFileName))
        msg.attach(image)
    def photo_capture(self):
        cap = cv.VideoCapture(0)
        if cap.isOpened()==False:
            cap = cv.VideoCapture(1)
            try:
                while(1):
                    ret_img_frame=cap.read()
                    if GPIO.input(40)==1:
                        print("Obstacle Detected")
                        cv.imshow("output",ret_img_frame)
                        cv.waitkey(40)
                        cv.imwrite("mail_image.jpg",ret_img_frame)
                        self.sendMAil('mail_image.jpg')
                        time.sleep(.5)
                    else:
                        print("Not Detected")
                        time.sleep(0.5)
                        k=cv.waitkey(10)
            except:
                print("error")
            finally:
                print("--><--")


if __name__ == "__main__":
    email = Emailer()
    email.emailer(alert_type='')
