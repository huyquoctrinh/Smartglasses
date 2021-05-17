
import argparse
import io
from google.cloud import vision
from google.cloud.vision import types
import os
# def takephoto():
    
# # initialize the camera
#     cam = cv2.VideoCapture(0)
#     ret, image = cam.read()

#     if ret:
#     #cv2.imshow('SnapshotTest',image)
#     #cv2.waitKey(0)
#     #cv2.destroyWindow('SnapshotTest')
#         cv2.imwrite('/home/pi/logo.jpg',image)
#     cam.release()
def detect_logo(image_file):
    # takephoto()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/mindx_hack/thi.json"
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.logo_detection(image=image)
    annotations = response.logo_annotations
    for annotation in annotations:
        print(0)
    return annotation.description
# os.popen('espeak "{}" --stdout | aplay 2>/dev/null'.format(annotation.description))
path = 'D:/starbuck.png'
result = detect_logo(path)
print(result)
# /home/pi/Desktop/MATKINHTHONGMINH/