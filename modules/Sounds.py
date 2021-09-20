try:  
    from modules.playsound import playsound

    def click():
        playsound("modules\soundeffects\click.mp3")

except:
    print("playsound module missing, sounds will not be played")
    def click():
        pass

