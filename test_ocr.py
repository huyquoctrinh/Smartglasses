from time import sleep
import os
from google.cloud import vision
# import speech_recognition as sr  
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="abc.json"
# client = vision.ImageAnnotatorClient()
os.system("fswebcam -r 1280x720 --no-banner /home/pi/image.jpg")
# cam = cv2.VideoCapture(-1)
# ret, image = cam.read()

# if ret:
# #cv2.imshow('SnapshotTest',image)
# #cv2.waitKey(0)
# #cv2.destroyWindow('SnapshotTest')
#     cv2.imwrite('/home/pi/image.jpg',image)
# cam.release()
from google.cloud import vision
import io
client = vision.ImageAnnotatorClient()

with io.open('/home/pi/image.jpg', 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')
k = 0
for text in texts:
    k = 1
    sleep(3)
    print('\n"{}"'.format(text.description))
    assistant_speaks(text.description)
if (k==0):
    print("không có gì trước mắt bạn")