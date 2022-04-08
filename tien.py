# import cv2
import os
from time import sleep
from google.cloud import vision
from gtts import gTTS

def assistant_speaks(output): 
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
    # saving the audio file given by google text to speech 
    file = "/home/pi/kinh/atien.mp3" 
    toSpeak.save(file)
    os.system("omxplayer -o alsa {}".format(file))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "abc.json"
s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
nameArray = ["motnghin", "hainghin", "namnghin", "muoinghin", "haimuoinghin", "nammuoinghin", "mottramnghin", "haitramnghin", "namtramnghin"]
numArray = ["1000", "2000", "5000", "10000", "20000", "50000", "100000", "200000", "500000"]

def checkNotInString(s, exceptIndex):
    for i in range(9):
        if (i != exceptIndex):
            if (nameArray[i] in s):
                return False
    for i in range(exceptIndex + 1, 9):
        if (numArray[i] in s):
            return False
    return True

def remove_accents(input_str):
    s = ''
    for c in input_str:
        if (c in s1): s += s0[s1.index(c)]
        else: s += c
    return s

def detect_text(path):
    from google.cloud import vision
    import io
    #from google.cloud.vision import types
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    s = ""
    for text in texts:
        s += text.description.replace("\n", " ").replace("  ", " ") + " "
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    s = remove_accents(s).lower().replace(" ", "").replace("н", "h").replace(".", "").replace(",", "")
    '''if ("1000" in s and "mot" in s and checkNotInString(s, 0)): return "một nghìn"
    if ("motnghin" in s): return "một nghìn"
    if ("2000" in s and "hai" in s and checkNotInString(s, 1)): return "hai nghìn"
    if ("hainghin" in s or "hаinghin" in s): return "hai nghìn"
    if ("5000" in s and "nam" in s and checkNotInString(s, 2)): return "năm nghìn"
    if ("namnghin" in s): return "năm nghìn"
    if ("10000" in s and "muoi" in s and checkNotInString(s, 3)): return "mười nghìn"
    if ("muoinghin" in s): return "mười nghìn"
    if ("20000" in s and "hai" in s and checkNotInString(s, 4)): return "hai mươi nghìn"
    if ("haimuoinghin" in s): return "hai mươi nghìn"
    if ("50000" in s and "nam" in s and checkNotInString(s, 5)): return "năm mươi nghìn"
    if ("nammuoinghin" in s): return "năm mươi nghìn"
    if ("100000" in s and "mot" in s and checkNotInString(s, 6)): return "một trăm nghìn"
    if ("mottramnghin" in s): return "một trăm nghìn"
    if ("200000" in s and "hai" in s and checkNotInString(s, 7)): return "hai trăm nghìn"
    if ("haitramnghin" in s): return "hai trăm nghìn"
    if ("500000" in s and "nam" in s and checkNotInString(s, 8)): return "năm trăm nghìn"
    if ("namtramnghin" in s): return "năm trăm nghìn"'''
    if ("1000" in s and checkNotInString(s, 0)): return "một nghìn"
    if ("motnghin" in s): return "một nghìn"
    if ("2000" in s and checkNotInString(s, 1)): return "hai nghìn"
    if ("hainghin" in s or "hаinghin" in s): return "hai nghìn"
    if ("5000" in s and checkNotInString(s, 2)): return "năm nghìn"
    if ("namnghin" in s): return "năm nghìn"
    if ("10000" in s and checkNotInString(s, 3)): return "mười nghìn"
    if ("muoinghin" in s): return "mười nghìn"
    if ("20000" in s and checkNotInString(s, 4)): return "hai mươi nghìn"
    if ("haimuoinghin" in s): return "hai mươi nghìn"
    if ("50000" in s and checkNotInString(s, 5)): return "năm mươi nghìn"
    if ("nammuoinghin" in s): return "năm mươi nghìn"
    if ("100000" in s and checkNotInString(s, 6)): return "một trăm nghìn"
    if ("mottramnghin" in s): return "một trăm nghìn"
    if ("200000" in s and checkNotInString(s, 7)): return "hai trăm nghìn"
    if ("haitramnghin" in s): return "hai trăm nghìn"
    if ("500000" in s and checkNotInString(s, 8)): return "năm trăm nghìn"
    if ("namtramnghin" in s): return "năm trăm nghìn"
    print()
    print(path)
    print(s)
    return("trong ảnh không có tiền")

def detect_labels(path):
    from google.cloud import vision
    import io
    from google.cloud.vision import types
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    v = []
    p = []
    for label in labels:
        v.append(label.description)
        p.append(label.score)
    for i in range(len(v)): print(v[i], p[i])
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    for i in range(len(v)):
        if ("money" in v[i].lower() or "dollar" in v[i].lower() or "cash" in v[i].lower() or "bank" in v[i].lower()):
            return(detect_text(path))
    return("trong ảnh không có tiền")
def detect_money():
    os.system("fswebcam -r 1280x720 --no-banner /home/pi/image_tien.jpg")
    s = detect_text('image_tien.jpg')
    print(s)
    assistant_speaks(s)
# detect_money()

