from ichigojam import Std15


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
        std15.scroll()
        
        if std15.scr(x, 5) != 0:
            std15.locate(0,23)
            std15.putstr("Game Over...")
            std15.putnum(frameCount)
            running = False
    
    std15.draw_screen()
