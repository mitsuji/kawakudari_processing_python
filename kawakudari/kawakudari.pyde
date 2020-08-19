from ichigojam import Std15

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
