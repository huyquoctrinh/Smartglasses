import cv2, os
from time import sleep

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/kinh/json_file/abc.json"

def takephoto():
    
# initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()

    if ret:
    #cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    #cv2.destroyWindow('SnapshotTest')
        cv2.imwrite('image.jpg',image)
    cam.release()
    
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open('image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')
    if texts==[]:
        print('không có chữ gì ở phía trước bạn')
    else:
        for text in texts:
            sleep(3)
            print('\n"{}"'.format(text.description))

if __name__ == '__main__':
    takephoto()
    detect_text('')