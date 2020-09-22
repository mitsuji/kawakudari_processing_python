# kawakudari_processing_python

This project implements part of the [std15.h](https://github.com/IchigoJam/c4ij/blob/master/src/std15.h) API (from [c4ij](https://github.com/IchigoJam/c4ij)) with [Processing](https://processing.org/) Python mode, and [Kawakudari Game](https://ichigojam.github.io/print/en/KAWAKUDARI.html) on top of it.

It will allow programming for [IchigoJam](https://ichigojam.net/index-en.html)-like targets that display [IchigoJam FONT](https://mitsuji.github.io/ichigojam-font.json/) on screen using a Python-like programming language.
```
def setup():
    global std15
    global running
    global x

    size(512, 384)
    std15 = Std15(512, 384, 32, 24)
    running = True
    x = 15
    
def draw():
    global std15
    global running
    global x

    if not running :
        return
    
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
        std15.scroll(DIR_UP)
        
        if std15.scr(x, 5) != 0:
            std15.locate(0,23)
            std15.putstr("Game Over...")
            std15.putnum(frameCount)
            running = False
    
    std15.draw_screen()
```

## Prerequisite

* [Download](https://processing.org/download/) and install Processing application suitable for your environment.
* Install Python mode


## License
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
[CC BY](https://creativecommons.org/licenses/by/4.0/) [mitsuji.org](https://mitsuji.org)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

