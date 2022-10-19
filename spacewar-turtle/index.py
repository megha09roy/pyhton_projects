
import turtle
import random
import math


#creating the background
board=turtle.Screen()
board.title("Space War")
board.bgcolor("black")
board.setup(800,800)

#creating the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-360,-360)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(710)
	border_pen.lt(90)
border_pen.hideturtle()	

#heading
title=turtle.Turtle()
title.color("white")
title.penup()
title.setposition(8,354)

title.write("↨↨↨↨↨↨----- Space War ----↨↨↨↨↨↨",align="center",font=("Arial",22,"normal"))
title.hideturtle()

#score board
score=0
score_board=turtle.Turtle()
score_board.color("white")
score_board.penup()
score_board.setposition(210,310)

score_board.write("Score_Board : {} ".format(score),align="center",font=("Arial",15,"normal"))
score_board.hideturtle()

#player
sign=turtle.Turtle()
sign.speed(0)
sign.shape("classic")
sign.shapesize(3)
sign.color('yellow')

sign.penup()
sign.setposition(0,-250)
sign.left(90)
speed=4

#bullet of player
buspeed=10
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("circle")
bullet.shapesize(0.25, 0.25)
bullet.penup()
bullet.speed(0)
bullet.setposition(250,80)

#revive one new life
power=turtle.Turtle()
power.color("green")
power.shape("square")
power.right(45)
power.shapesize(0.75,0.75)
xc=random.randint(-300,300)
yc=random.randint(-300,300)
power.penup()
power.setposition(xc,yc)

#live sign
lives1=[]
for i in range(10):
    lives1.append(turtle.Turtle())
    
for i in range(3):
    lives1[i].color("green")
    lives1[i].shape("triangle")
    lives1[i].shapesize(1)
    lives1[i].right(90+180)
    lives1[i].penup()
    lives1[i].setposition(-320+(i*30),320)
    lives1[i].penup()

    
enemy1=[]
speed1=4
eb=[]

#creating the enemies
for i in range(12):
    enemy1.append(turtle.Turtle())
    eb.append(turtle.Turtle())
  
    
for i in range(12):
    enemy1[i].shape("circle")
   
    #enemy3[i].shape("triangle")
    enemy1[i].color("white")
    
    #enemy3[i].color("white") 
    enemy1[i].shapesize(random.randint(1,3))
    enemy1[i].speed(0)
    #enemy3[i].shapesize(2)
    enemy1[i].penup()
    
    eb[i].color("orange")#setting the  additional missiles 
    eb[i].shape("classic")
    
    eb[i].shapesize(1,1)
    eb[i].penup()
    
    
    xc=random.randint(-300,300)
    yc=random.randint(-300,300)
    enemy1[i].penup()
    enemy1[i].setposition(xc,yc)
    enemy1[i].penup()
    enemy1[i].setheading(random.randint(0,360))
    if i%4==0:
        eb[i].penup()
        eb[i].speed(buspeed*88)
        eb[i].setposition(xc+40,yc+40)
        eb[i].penup()
        eb[i].setheading(sign.heading())
        
    
bulletstate="ready"   
    
def right():
    sign.right(30)#move the player right
def left():
    sign.left(30)#move the player left

#collision in every case
def iscollison(t1,t2):
   distance=math.sqrt(math.pow(t1.xcor()-t2.xcor() ,2) +math.pow(t1.ycor() -t2.ycor() ,2) ) 
   if distance<15:
       return(True)
   else:
       return False
   
def move():
    sign.forward(speed*2)#moving the player
    
#firing the bullet of player
def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        x=sign.xcor()
        y=sign.ycor()
        bullet.speed(buspeed*6)
        bullet.setposition(x,y)
        bullet.setheading(sign.heading())
        bullet.speed(buspeed*6)
        bullet.showturtle()
 
#end of program        
def disp():
    over=turtle.Turtle()
    over.color("yellow")
    over.penup()
    over.setposition(10,0)
    over.write(">>>> GAME OVER <<<<",align="center",font=("Arial",28,"normal") )
    over.hideturtle()

#plyer lives    
def live():
    
    xc=random.randint(-300,300)
    yc=random.randint(-300,300)
    power.penup()
    power.setposition(xc,yc)

#speed of the missile
def fire():
    eb.forward(buspeed)
    eb.speed(buspeed)

def scorebrd(anyw):
     score_board.penup()
     score_board.setposition(210,310)
     score_board.clear()
     score_board.write("Score_Board : {} ".format(anyw),align="center",font=("Arial",15,"normal"))
     score_board.hideturtle()
 
    #accelerating the player
def accelerate():
    sign.forward(buspeed)
    
lives=3#no. of lives of player

#Life cases in player
def hid_live(life):
    lives1[life].penup()
    lives1[life].setposition(-320+(life*30),320)
    lives1[life].clear()
    lives1[life].hideturtle()

    
def giv_live(life):
    lives1[life].color("green")
    lives1[life].shape("triangle")
    lives1[life].shapesize(1)
    lives1[life].right(90+180)
    lives1[life].penup()
    lives1[life].setposition(-320+(life*30),320)
    
        
def power_live():
 
 giv_live(lives)

 xc=random.randint(-400,400)
 yc=random.randint(-200,200)
 sign.penup()
 sign.goto(xc,yc)

 sign.setposition(xc,yc)

 move()
 
 live() 
    
#collision of the player with missile
def bullet_player() :      
 
 hid_live(lives)
 xc=random.randint(-400,400)
 yc=random.randint(-200,200)
 
 sign.penup()
 sign.goto(xc,yc)
 
 sign.setposition(xc,yc)
 move() 

#enemy collision with player
def enemy_player():

 
 hid_live(lives)
 xc=random.randint(-400,400)
 yc=random.randint(-200,200)
 sign.penup()
 sign.goto(xc,yc)

 sign.setposition(xc,yc)
 move()   

#reloading the bullet of the player
def enemy_bullet_colli(eny1):
          bullet.hideturtle()
          bulletstate="ready"
          xc=random.randint(-400,400)
          yc=random.randint(-200,200)
          enemy1[eny1].goto(xc,yc)
          
          
          enemy1[eny1].setposition(xc,yc)  

#setting the position of missile          
def enemy_bullet(eny1):
  if(eny1%4==0):
    x=random.randint(-320,320)
    y=random.randint(-320,320)
    eb[eny1].penup()
    eb[eny1].goto(x,y)
    eb[eny1].setposition(x,y)
    eb[eny1].penup()
    eb[eny1].setheading(sign.heading())
    eb[eny1].forward(buspeed+70)         

#key board function
board.listen()

board.onkeypress(right,"Right")
board.onkeypress(left,"Left")
board.onkeypress(fire_bullet,"space")
board.onkeypress(accelerate,"Up")




while True:
    
    
    #board.update()
    if(lives!=0):
      move()
      
      
      #list1=[-360,360]
      for eny in range(len(enemy1)):
          
        if(enemy1[eny].xcor()>360 or enemy1[eny].ycor()>360 or enemy1[eny].ycor()<-360 or enemy1[eny].xcor()<-360): 
            
                enemy1[eny].setheading(enemy1[eny].heading()+90)
                enemy1[eny].forward(speed1+15)
                
        elif(eb[eny].xcor()>360 or eb[eny].ycor()>360 or eb[eny].ycor()<-360 or eb[eny].xcor()<-360): 
             enemy_bullet(eny)                        
        
        elif(iscollison(enemy1[eny],bullet)):
          
          enemy_bullet_colli(eny)
          score=score+1
          scorebrd(score+1)
                
        elif(iscollison(enemy1[eny],sign)):
         lives=lives-1
         enemy_player()
                 
        elif( iscollison(eb[eny],sign) ):
          lives=lives-1
          bullet_player()       
                 
        elif(iscollison(power,sign)):
          lives=lives+1
          power_live()
         
       
        else:
            enemy1[eny].forward(speed1+15)
            if(eny%4==0):
                eb[eny].forward(buspeed+70)
                
                
           
            
            
      if(bulletstate=="fire"):
       
          bullet.forward(buspeed*6)
       
      if bullet.ycor() > 250 or bullet.ycor()<-250:
         bullet.hideturtle()
         bulletstate="ready"
         
      if bullet.xcor() > 500 or bullet.xcor()<-500:
        bullet.hideturtle()
        bulletstate="ready"
      
      
            
    else:
        for i in range(4):
            disp()
            
            delay=0.1 
                
        
   
    




