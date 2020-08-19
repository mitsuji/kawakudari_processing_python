# kawakudari_processing_python

This project implements part of the [std15.h](https://github.com/IchigoJam/c4ij/blob/master/src/std15.h) API (from [c4ij](https://github.com/IchigoJam/c4ij)) with [Processing](https://processing.org/) Python mode, and [Kawakudari Game](https://ichigojam.github.io/print/en/KAWAKUDARI.html) on top of it.

It will allow programming for [IchigoJam](https://ichigojam.net/index-en.html)-like targets using a Python-like programming language.
```
std15 = None
running = True
x = 15
def setup():
    size(512, 384)
    global std15
    std15 = Std15(512, 384, 32, 24)
    
def draw():
    global running
    if not running :
        return
    
    global x    
    if frameCount % 5 == 0 :
        if keyPressed:
            if keyCode == LEFT :
                x-=1
            if keyCode == RIGHT :
                x+=1
    
        std15.locate(x,5)
        std15.putc(ord('0'))
        std15.locate(floor(random(32)), 23)
        std15.putc(ord('*'))
    
        std15.scroll()
        
        if std15.scr(x, 5) != 0:
           running = False 
    
    std15.pAppletDraw()
```

## Prerequisite

* [Download](https://processing.org/download/) and install Processing application suitable for your environment.
* Install Python mode


