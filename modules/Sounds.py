import playsound


def click():
    try:
        playsound.playsound("modules\soundeffects\click.mp3")
    except:
        print("playsound error")
