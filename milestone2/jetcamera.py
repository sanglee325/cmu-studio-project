from jetcam.csi_camera import CSICamera
from jetcam.utils import bgr8_to_jpeg
import ipywidgets
from IPython.display import display

camera = CSICamera(width=224, height=224, capture_device=0)
camera.running = True

image_widget = ipywidgets.Image(format='jpeg')
def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)

camera.observe(update_image, names='value')
display(image_widget)
