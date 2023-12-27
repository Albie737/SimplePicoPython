import time
from machine import Pin, I2C
from neopixel import NeoPixel


strip = NeoPixel(Pin(28), 15)

Red = 255,0,0
Green = 0,255,0
Blue = 0,0,255
Yellow = 255,255,0
Light_Blue = 0,255,255
Purple = 196,0,255
Pink = 252,0,60
Orange = 255,80,0
Lime = 128,255,1
White = 255,255,255
Clear = 0,0,0


def say(inputAll):
    print(inputAll)
    
def wait(duration):
    time.sleep(duration)

def setRGB(Location, R, G, B):
    strip[Location] = (R,G,B)
    strip.write()
    
def setCol(Location, Colour):
    strip[Location] = (Colour)
    strip.write()

def strSel(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    setCol(0,a)
    setCol(1,b)
    setCol(2,c)
    setCol(3,d)
    setCol(4,e)
    setCol(5,f)
    setCol(6,g)
    setCol(7,h)
    setCol(8,i)
    setCol(9,j)
    setCol(10,k)
    setCol(11,l)
    setCol(12,m)
    setCol(13,n)
    setCol(14,o)

def strFil(c):
    setCol(0,c)
    setCol(1,c)
    setCol(2,c)
    setCol(3,c)
    setCol(4,c)
    setCol(5,c)
    setCol(6,c)
    setCol(7,c)
    setCol(8,c)
    setCol(9,c)
    setCol(10,c)
    setCol(11,c)
    setCol(12,c)
    setCol(13,c)
    setCol(14,c)

def strCle():
    setCol(0,Clear)
    setCol(1,Clear)
    setCol(2,Clear)
    setCol(3,Clear)
    setCol(4,Clear)
    setCol(5,Clear)
    setCol(6,Clear)
    setCol(7,Clear)
    setCol(8,Clear)
    setCol(9,Clear)
    setCol(10,Clear)
    setCol(11,Clear)
    setCol(12,Clear)
    setCol(13,Clear)
    setCol(14,Clear)

def PixCl(Pixel):
    setCol(Pixel, Clear)
def pixCl(Pixel):
    setCol(Pixel, Clear)

def movePx1(P1,delay,rounds):
    counter = 0
    a = 0
    while counter < rounds:
        setCol(a,P1)
        time.sleep(delay)
        pixCl(a)
        a += 1
        if a == 15:
            time.sleep(delay)
            a = 0
        counter += 1

def movePx2(P1,P2,delay,rounds):
    counter = 0
    a = 0
    b = 1
    while counter < rounds:
        setCol(a,P1)
        setCol(b,P2)
        time.sleep(delay)
        pixCl(a)
        pixCl(b)
        a += 1
        b += 1
        if b == 15:
            a = -1
            b = 0
        counter += 1

def movePx3(P1,P2,P3,delay,rounds):
    counter = 0
    a = 0
    b = 1
    c = 2
    while counter < rounds:
        setCol(a,P1)
        setCol(b,P2)
        setCol(c,P3)
        time.sleep(delay)
        pixCl(a)
        pixCl(b)
        pixCl(c)
        a += 1
        b += 1
        c += 1
        if c == 15:
            a = -2
            b = -1
            c = 0
        counter += 1

def movePx4(P1,P2,P3,P4,delay,rounds):
    counter = 0
    a = 0
    b = 1
    c = 2
    d = 3
    while counter < rounds:
        setCol(a,P1)
        setCol(b,P2)
        setCol(c,P2)
        setCol(d,P4)
        time.sleep(delay)
        pixCl(a)
        pixCl(b)
        pixCl(c)
        PixCl(d)
        a += 1
        b += 1
        c += 1
        d += 1
        if d == 15:
            a = -3
            b = -2
            c = -1
            d = 0
        counter += 1

def movePx5(P1,P2,P3,P4,P5,delay,rounds):
    counter = 0
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    while counter < rounds:
        setCol(a,P1)
        setCol(b,P2)
        setCol(c,P2)
        setCol(d,P4)
        setCol(e,P5)
        time.sleep(delay)
        pixCl(a)
        pixCl(b)
        pixCl(c)
        pixCl(d)
        pixCl(e)
        a += 1
        b += 1
        c += 1
        d += 1
        e += 1
        if e == 15:
            a = -4
            b = -3
            c = -2
            d = -1
            e = 0
        counter += 1