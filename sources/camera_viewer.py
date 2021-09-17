import camera_viewer_ui
import pypylon.pylon as py
import cv2 as cv
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import time
import numpy as np

class CameraViewer(camera_viewer_ui.Ui_MainWindow, QMainWindow):
    get_image_signal = Signal(np.ndarray)
    def __init__(self):
        super(CameraViewer, self).__init__()
        self.setupUi(self)
        self.cam = None
        self.tlf = py.TlFactory.GetInstance()
        self.list_devices = self.tlf.EnumerateDevices()
        for device in self.list_devices:
            self.comboBoxCamera.addItem(device.GetModelName())
        
        # converter
        self.converter = py.ImageFormatConverter()
        self.converter.OutputPixelFormat = py.PixelType_BGR8packed
        self.converter.OutputBitAlignment = py.OutputBitAlignment_MsbAligned

        self.pushButtonStart.clicked.connect(self.run_camera)
        self.pushButtonStop.clicked.connect(self.stop_camera)
        self.pushButtonSoftwareTrigger.clicked.connect(self.trigger_camera)
        self.get_image_signal.connect(self.update_image)

        self.pushButtonStart.setEnabled(True)
        self.pushButtonStop.setEnabled(False)
        self.pushButtonSoftwareTrigger.setEnabled(False)

    def run_camera(self):
        selected_cam_idx = self.comboBoxCamera.currentIndex()
        cam_dev = self.list_devices[selected_cam_idx]
        self.cam = py.InstantCamera(self.tlf.CreateDevice(cam_dev))
        self.cam.Open()
        if self.cam.IsOpen():
            self.cam.TriggerMode.SetValue("On")
            self.cam.TriggerSelector.SetValue("FrameStart")
            self.cam.TriggerSource.SetValue("Software")
            self.cam.StartGrabbing(py.GrabStrategy_LatestImageOnly)
            if self.cam.IsGrabbing():
                self.pushButtonStart.setEnabled(False)
                self.pushButtonStop.setEnabled(True)
                self.pushButtonSoftwareTrigger.setEnabled(True)
            else:
                print("Grab error")
        else:
            print("Open camera error")

    def stop_camera(self):
        if self.cam.IsGrabbing():
            self.cam.StopGrabbing()
        if self.cam.IsOpen():
            self.cam.Close()
        if self.cam.IsGrabbing() == False and self.cam.IsOpen() == False:
            self.pushButtonStart.setEnabled(True)
            self.pushButtonStop.setEnabled(False)
            self.pushButtonSoftwareTrigger.setEnabled(False)

    def trigger_camera(self):
        if self.cam.IsGrabbing():
            self.cam.ExecuteSoftwareTrigger()
            try:
                grab = self.cam.RetrieveResult(1000, py.TimeoutHandling_ThrowException)
                if grab.GrabSucceeded():
                    img = self.converter.Convert(grab)
                    bgr_img = img.GetArray()
                    bgr_img_small = cv.resize(bgr_img, (640, 480))
                    self.get_image_signal.emit(bgr_img_small)
                grab.Release()
            except:
                print("Grab error")


    def closeEvent(self, event):
        if self.cam != None:
            self.stop_camera()
    
    @Slot(np.ndarray)
    def update_image(self, frame):
        h, w, c = frame.shape
        image = QImage(frame.data, w, h, 3*w, QImage.Format_RGB888)
        pixmap = QPixmap(image)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)

if __name__ == "__main__":
    cam_viewer = QApplication()
    cam_viewer_gui = CameraViewer()
    cam_viewer_gui.show()
    cam_viewer.exec_()