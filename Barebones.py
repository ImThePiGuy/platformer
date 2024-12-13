# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:33:54 2024

@author: jared
"""

  
import keyboard  # using module keyboard
import tkinter as tk # using tkinter for graphics
#import time

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
    #Keyboard inputs        
    #Collision detecton
    #Update positions
    #Random debug
    # Draw -     
    jeff.draw()
    root.update()
