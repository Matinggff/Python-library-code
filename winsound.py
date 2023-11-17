# Play music
import winsound
from random import randint

def create_music():
    sum_duration = 0
    while True:
        duration = randint(200, 1000)
        sum_duration += duration
        winsound.Beep(randint(50, 2000), duration)
        if sum_duration >= 6000:
            break
create_music()
