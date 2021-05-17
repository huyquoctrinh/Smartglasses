import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/kinh/json_file/abc.json"
def assistant_speaks(output): 
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
    # saving the audio file given by google text to speech 
    file = "assist.mp3" 
    toSpeak.save(file)
    os.system("omxplayer {}".format(file))
     
    os.remove(file)
def ocr():

    os.system("fswebcam -r 1280x720 --no-banner /home/pi/Desktop/kinh/image.jpg")
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

    with io.open('/home/pi/Desktop/kinh/image.jpg', 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    if texts==[]:
        assistant_speaks('không có chữ gì ở phía trước bạn')
    else:
        for text in texts:
            sleep(3)
            print('\n"{}"'.format(text.description))
            assistant_speaks(text.description)
            break
ocr()