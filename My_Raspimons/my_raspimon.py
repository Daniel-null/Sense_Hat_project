from sense_hat import SenseHat
from time import sleep
import vision_lib

if __name__ == '__main__':
    
    sense = SenseHat()

    #add your colors
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

    #add your Raspimon lists, the first is an egg

#raspimon_egg =  [(128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128)]

open_eyes = [
k, k, d, d, d, d, k, k,
k, d, d, w, d, w, d, k,
d, d, d, k, d, k, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k 
]       

left_eye_closed = [
k, k, d, d, d, d, k, k,
k, d, d, d, d, w, d, k,
d, d, d, d, d, k, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k 
]       


closed_eyes =[
k, k, d, d, d, d, k, k,
k, d, d, d, d, d, d, k,
d, d, d, d, d, d, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k 
]

    #set the egg
#sense.set_pixels(raspimon_egg)


    #define some functions. See sample_raspimon.py for examples.



    #add a while loop to keep your Raspimon running...

while True:
    sense = SenseHat()
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(left_eye_closed)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_v()

    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.2)
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(left_eye_closed)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_h()
    sleep(.5)
    sense.flip_h()
    sleep(.5)
    sense.set_pixels(closed_eyes)
    sleep(.2)
    sense.set_pixels(open_eyes)
    sleep(.9)
    sense.flip_v()

