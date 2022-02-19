import os
import argparse
import json
import winsound as sd
import time
import ctypes
import screeninfo as sinfo

import cv2
import open3d as o3d

def calibration(args: argparse.ArgumentParser) -> None:
    
    if not os.path.isdir("calibration"):
        os.mkdir("calibration")
    
    #kinect = o3d.io.AzureKinectSensor(o3d.io.AzureKinectSensorConfig())
    
    #if not kinect.connect(0):
    #    raise RuntimeError("[FAIL] Failed to connect to sensor")
    
    crt = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # 2. Webcam
    #u = ctypes.windll.user32
    #wdw_w, wdw_h = u.GetSystemMetrics(0), u.GetSystemMetrics(1)
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    print("[INFO] Created Window")
    
    error = 10.0
    
    # 1-way 
    ret, frame = cap.read()
    print("[INFO] 1-way Captured, and Synchronization")
    time.sleep(2)
    print("[INFO] 1-way Sleep Down")   
    
    #screen_num = len(sinfo.get_monitors())
    screen_x, screen_y = sinfo.get_monitors()[-1].x, sinfo.get_monitors()[-1].y
    
    # 2. Webcam
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow("window", screen_x, screen_y)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    print("[INFO] Set Window")  
    
    # 2-way
    cv2.imshow("window", frame)
    cv2.waitKey(33)
    print("[INFO] 2-way Shown, and Synchronization")
    time.sleep(2)
    cv2.imwrite("calibration/1-way.jpg", frame)
    print("[INFO] 3-way Captued, and Synchronization") 
    time.sleep(2)
    
    # 3-way
    ret, frame = cap.read()
    cv2.imwrite("calibration/3-way.jpg", frame)
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Calibration
    
    #image = cv2.imread("calibration/3-way.jpg")
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    
    #if ret == True:
    #    corner = cv2.cornerSubPix(gray, corners, (9, 6), (-1, -1), crt)
    #    frame = cv2.drawChessboardCorners(frame, (9, 6), corner, ret)
    
    """
    while error > 1.0:
        # Image Input
        rgbd = kinect.capture_frame(0)    
        if rgbd is None:
            continue
        
        # 2. Webcam
        ret, frame = cap.read()
    
        sd.Beep(2000, 100)
        # Calibration using ChessBoard
    """
    
    # Make Config File
    pass

if __name__ == '__main__':
    calibration(argparse.ArgumentParser())