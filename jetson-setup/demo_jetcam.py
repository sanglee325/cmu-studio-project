from jetcam.csi_camera import CSICamera
import cv2

camera = CSICamera(width=224, height=224, capture_width=1080, capture_height=720, capture_fps=30)

image = camera.read()

cv2.imwrite("test.png", image)
