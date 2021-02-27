from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)







#define another color. Use one letter variable names to make it easy later

raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, k, r, k, k,
k, k, r, k, k, r, k, k
]
 
sense.set_pixels(raspimon)

#add a one-pixel mouth
sense.set_pixel(3,4, [255,0,0])
 

rmon1 = [o, y, y, y, y, y, y, o,
         o, o, n, y, y, n, o, o,
         y, k, k, y, y, w, k, y,
         y, w, k, y, y, k, k, y,
         y, y, y, k, k, y, y, y,
         n, n, n, y, y, n, n, n,
         n, n, n, y, y, n, n, n,
         n, n, n, y, y, n, n, n]

sense.set_pixels(rmon1)