# Example posting a local image file:
import requests
from trans import translate_text
from gtts import gTTS
import os
import cv2
num=0

def assistant_speaks(output): 
    global num 
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'cap.mp3' 
    toSpeak.save(file)
    os.system("omxplayer sound.mp3")
    #os.system('omxplayer file')  
    # playsound package is used to play the same file. 
    #pygame.mixer.music.load(file)
    #pygame.mixer.music.play()
    #os.remove(file)
def caption():
    os.system("fswebcam -r 1280x720 --no-banner test.jpg")
    # cam = cv2.VideoCapture(0)
    # ret, image = cam.read()

    # if ret:
    #     #cv2.imshow('SnapshotTest',image)
    #     #cv2.waitKey(0)
    #     #cv2.destroyWindow('SnapshotTest')
    #     cv2.imwrite('test.jpg',image)
    # cam.release()
    r = requests.post(
        "https://api.deepai.org/api/densecap",
        files={
            'image': open('test.jpg', 'rb'),
        },
        headers={'api-key': '9a65a560-3629-4c87-8d97-2c09fe5d4379'}
    )
    a=r.json()['output']['captions'][0]['caption']
    b=r.json()['output']['captions'][1]['caption']
    c=r.json()['output']['captions'][2]['caption']
    res=str(a)+' and '+str(b)+' and '+str(c)
    vn=translate_text(res)
    print(vn)
    # assistant_speaks(vn)
    return vn
caption()