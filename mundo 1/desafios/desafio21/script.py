from pygame import mixer

mixer.init()
mixer.music.load("mundo 1\desafios\desafio21/trilha_sonora.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Press 'p' to pause music, and 'r' to resume")
    print("Press 'v' to set volume to music")
    print("Press 's' to exit the program")
    option = str(input("  "))

    if(option == 'p'):
        mixer.music.pause()
    elif(option == 'r'):
        mixer.music.unpause()
    elif(option == 'v'):
        volume = float(input("Type the volume to set: "))
        mixer.music.set_volume(volume)
    elif(option == 's'):
        mixer.music.stop()
        break
    else:
        print("Command not found!")