import pygame
import time
import random as rn
from pygame.locals import *

size=40
bgcolor=(98,168,69)

class Game:
    def __init__(self):
        pygame.init()

        self.surface =  pygame.display.set_mode((600,560))
        self.surface.fill(bgcolor)
        self.snake=snake(self.surface,length=2)
        self.snake.draw()
        self.apple=apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = snake(self.surface,length =2)
        self.apple = apple(self.surface)


    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2  and x1 <x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        
        return False   


    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.flip() 

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x ,self.apple.y):
            self.apple.move()
            self.snake.inc_length()

        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]) :   
                raise "game over"
    
    def score(self):
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"score:{self.snake.length-1}",True,(255,255,255))
        self.surface.blit(score,(490,20))
    
    
    def show_game_over(self):
        self.surface.fill(bgcolor)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length-1}", True, (255, 255, 255))
        self.surface.blit(line1, (150, 200))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (42, 240))

        pygame.display.flip()





    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if pause==False:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.35)
                
class apple:
    def __init__(self,parent_screen):
        self.image=pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen= parent_screen
        self.x=size*3
        self.y=size*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    
    def move(self):
        self.x=rn.randint(0,13)*40
        self.y=rn.randint(0,13)*40

           


class snake:
    def __init__(self,parent_screen,length):
        self.length= length
        self.parent_screen= parent_screen
        self.block= pygame.image.load("resources/block.jpg").convert()
        self.length=length
        self.x=[size]*length
        self.y=[size]*length
        self.direction='right'
        
    def draw(self,):
        self.parent_screen.fill(bgcolor) 

        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def inc_length(self):
        self.length+= 1
        self.x.append(-1)
        self.y.append(-1)
        
    


    def move_up(self):
       self.direction='up'
     
    def move_down(self):
        self.direction='down'
       
    def move_right(self):
        self.direction='right'

    def move_left(self):
        self.direction='left'
        

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction =='up':
            self.y[0]-=size
       
        if self.direction =='down':
            self.y[0]+=size
      
        if self.direction =='left':
            self.x[0]-=size
    
        if self.direction =='right':
            self.x[0]+=size
        
        self.draw()
        


if __name__=="__main__":
    game=Game()
    game.run()
 
    
