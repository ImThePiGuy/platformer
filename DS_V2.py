'''
Canvas properties-
0,0 at bottom left , 1000x1000 "world coordinates" write translation code
Sprite properties-
write all positions at the bottom left of obj and have a hight and width

The objects that we need to have are person,platform,and camera
'''

import keyboard  # using module keyboard
import tkinter as tk # using tkinter for graphics
import time

# clock = [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
# xjump = [36,28.8,21.6,14.4,7.2,0,7.2,14.4,21.6,28.8,36]
# yjump = [6,57.84,98.16,126.96,144.24,-144.24,-126.96,-98.16,-57.84,-6]


class object:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y + 600 - height
        self.height = height
        self.width = width
        
    def draw(self):
        canvas.create_rectangle(self.x,self.y,self.x+self.height,self.y+self.width)
        
     
class character(object):
    def __init__(self,x,y,height,width,xvel,yvel):
        super().__init__(x,y,height,width)
        # yvel and xvel are x and y velocity
        self.xvel = xvel
        self.yvel = yvel
    
    def jump(self):
        if jumping:
            if jump_count >= -10:\
                neg = 1 if jump_count < 0: neg = -1 player_pos[1] -= (jump_count ** 2) * 0.5 * neg jump_count -= 1 else: jump_count = 10 jumping =
        
        pass
    

class platform(object):
    def __init__(self,x,y,height,width):
       super().__init__(x,y,height,width)
        
class camera(object):
    def __init__(self,x,y,height,width):
        super().__init__(x,y,height,width)

#Initilive canvas
root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Rectangle')
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)



#Mainloop will have the display coords funtion

jeff = character(100,0,100,100,0,0)

while True:
    canvas.delete('all')
    jeff.xvel = 0
    jeff.yvel = 0
    #Keyboard inputs        
    if keyboard.is_pressed('space'):
        jeff.jump()
    #Collision detecton
    #Update positions
 
    #Random debug
    print(jeff.x,jeff.y)
    # Draw -     
    jeff.draw()
    root.update()


