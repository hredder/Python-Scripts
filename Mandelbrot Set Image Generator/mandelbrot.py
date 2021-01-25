from PIL import Image
import cmath
import math

#Made by Henry Redder

def mandelbrot(count, seed, constant):

    while (count <= 255 and abs(seed) <= 2):
        seed = seed*seed + constant
        count = count + 1
    
    return count

        
WIDTH = 1080
HEIGHT = 720

im = Image.new('RGB', (WIDTH, HEIGHT), color=0)
pixels = im.load()

for x in range(WIDTH):
    for y in range(HEIGHT):

        realNum = 4*(x-WIDTH/2)/WIDTH
        complexNum = 2.5*(y-HEIGHT/2)/HEIGHT
        mand = mandelbrot(0,0, realNum + complexNum*1.0j)
        color = int(255-mand)
        pixels[x, y] = (color, color, color)

im.show()
#Optional Export
#im.save("C:\\Users\\goali\\Desktop\\fractal.jpg")