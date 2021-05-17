import cv2, os
from time import sleep
from script import get_audio, assistant_speaks
from google.cloud import vision
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/kinh/huy_test.json"
client = vision.ImageAnnotatorClient()


def takephoto():
    
# initialize the camera
    cam = cv2.VideoCapture()
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('image.jpg',image)
    cam.release()

def obj_detect():
    takephoto() # First take a picture
    """Run a label request on a single image"""

    with open('image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # response = client.logo_detection(image=image)


    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        sleep(4)
        y = labels.description
        # os.popen( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(label.description))
        print(label.description)
    return y
def tim():
	assistant_speaks("bạn muốn tìm đồ vật nào")
	dovat = get_audio()
	y = obj_detect()
	if str(dovat) in y: 
		assistant_speaks(dovat + "bạn muốn tìm ở bên hướng này nè ")
		i=1
		return i
	else:
		assistant_speaks("tìm hướng khác đi")
		i=0
		return i
if __name__ == '__main__':
    # try:
    #     main()
    # except:
    #     print('Loi Network')
	i=1
	while i==1:
		y = tim()
		if (y==0):
			continue
		if (y==1):
			break