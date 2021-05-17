from gtts import gTTS
def assistant_speaks(output): 
    global num 
     #num to rename every audio file  
    # with different name to remove ambiguity 
    num =+1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='vi', slow = False) 
     #saving the audio file given by google text to speech 
    file = 'troly.mp3' 
    toSpeak.save(file)
    # os.system("omxplayer sound.mp3")
    #os.system('omxplayer file')  
    # playsound package is used to play the same file. 
    #pygame.mixer.music.load(file)
    #pygame.mixer.music.play()
    # os.remove(file)
assistant_speaks("chức năng trợ lý ảo")