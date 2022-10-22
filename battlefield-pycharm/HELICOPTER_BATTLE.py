#add score sound game over change color starting notation speed
import pygame
import random
from pygame import mixer
import time
import datetime

pygame.init()

screen = pygame.display.set_mode([895,450])

pygame.display.set_caption("Battle Grounds")
logo=pygame.image.load("Images/missile_1.png")
pygame.display.set_icon(logo)

introduce=pygame.image.load("Images/intro.png")
score_font=pygame.font.Font('freesansbold.ttf',44)
display = score_font.render(f"Battle Grounds", True, (255, 255, 255))
check=True

while check:

    screen.fill((0,0,125))
    screen.blit(introduce,(300,100))
    for event in pygame.event.get():  # checking all the keyboards input

        if event.type == pygame.KEYDOWN:  # pressing any botttom on the keyboard
            if event.key == pygame.K_SPACE:
                check=False

    screen.blit(display, (265,360))
    pygame.display.update()
#time.sleep(5)
score=0
lives=3
mixer.music.load('Music/background.WAV')
mixer.music.play(-1)

check=True
pic_land=pygame.image.load("Images/land_real.jpg")

pic_land_1=pygame.image.load("Images/land_real.jpg")
pic_scroll_1=752
pic_speed_1=0.1

Draw=[pygame.image.load("Images/live.png"),pygame.image.load("Images/live.png"),pygame.image.load("Images/live.png")]
x=720
y=20

pic_helicopter=pygame.image.load("Images/helicopter.png")
pic_helicopter_x=30
pic_helicopter_y=30
pic_helicopter_speed_x=0
pic_helicopter_speed_y=0

pic_missile_5=pygame.image.load("Images/missile_5.png")
pic_missile_5_x=pic_helicopter_x
pic_missile_5_y=pic_helicopter_y
pic_missile_5_speed=0.5
bulletstate="ready"



launcher=pygame.image.load("Images/launcher.png")
launcher_x=500
launcher_y=360

pic_missile_1=pygame.image.load("Images/missile_1.png")
pic_missile_1_x=launcher_x
pic_missile_1_y=launcher_y
pic_missile_1_speed_x=0.2
pic_missile_1_speed_y=0.2



pic_missile_4=pygame.image.load("Images/missile_4.png")
pic_missile_4_x=pic_helicopter_x
pic_missile_4_y=pic_helicopter_y
pic_missile_4_speed=0.3
bulletstate_1="ready"

pic_space=pygame.image.load("Images/spaceship.png")
pic_space_x=500
pic_space_y=60
pic_space_speed=0.3


pic_ship=[pygame.image.load("Images/pirateship.png"),pygame.image.load("Images/pirateship.png"),pygame.image.load("Images/pirateship.png"),pygame.image.load("Images/pirateship.png")]

pic_ship_x=[]
pic_ship_y=[]
pic_ship_speed_x=[]
for i in range(4):
    pic_ship_x.append(300+(i*190))
    pic_ship_y.append(190+(i*20))
    pic_ship_speed_x.append(0.04)

pic_ship_1=pygame.image.load("Images/pirate1.png")
pic_ship_1_x=300
pic_ship_1_y=200
pic_ship_1_speed=0.04

pic_missile_6=pygame.image.load("Images/missile_6.png")
pic_missile_6_x=pic_ship_1_x
pic_missile_6_y=pic_ship_1_y
pic_missile_6_speed_x=0.2
pic_missile_6_speed_y=0.2


pic_tank=[pygame.image.load("Images/tank.png"),pygame.image.load("Images/tank.png")]
pic_missile_2=[pygame.image.load("Images/missile_2.png"),pygame.image.load("Images/missile_2.png")]
pic_tank_x=[]
pic_tank_y=[]
pic_tank_speed_x=[]
pic_tank_speed_y=[]

pic_missile_2_x=[]
pic_missile_2_y=[]
pic_missile_2_speed_x=[]
pic_missile_2_speed_y=[]
bulletstate_2=[]
for i in range(2):
    pic_tank_x.append(50+(i*140))
    pic_tank_y.append(320+(i*30))
    pic_tank_speed_x.append(0.01+0.01*i)


    pic_missile_2_x.append(pic_tank_x[i])
    pic_missile_2_y.append(pic_tank_y[i])
    pic_missile_2_speed_x.append(0.1)
    pic_missile_2_speed_y.append(0.1)
    bulletstate_2.append("ready")


pic_cloud=[pygame.image.load("Images/cloud_1.png"),pygame.image.load("Images/cloud_1.png"),pygame.image.load("Images/cloud_1.png")]
pic_cloud_x=[]
pic_cloud_y=[]
pic_cloud_chng=[]
for i in range(3):
    pic_cloud_x.append(200+i*300)
    pic_cloud_y.append(random.randint(20,60))
    pic_cloud_chng.append(0.05)



pic_enemy=pygame.image.load("Images/enemy.png")

pic_enemy_x=540
pic_enemy_y=40
pic_enemy_chng_x=0.1
pic_enemy_chng_y=0.01

pic_missile_3=pygame.image.load("Images/missile_3.png")
pic_missile_3_x=pic_enemy_x
pic_missile_3_y=pic_enemy_y
pic_missile_3_speed=0.3



n=0


def score_board():

    display=score_font.render(f"Score:"+str(score//12),True,(255,0,0))
    screen.blit(display,(text_x,text_y))

def show():
    screen.blit(pic_land,(0,0))

def show_heli(x,y):
    screen.blit(pic_helicopter,(x,y))
def show_space(x,y):

    screen.blit(pic_space,(x,y))
def show_ship(x,x1,y1):
    for i in range(4):
        pic_ship_x[i] -= pic_ship_speed_x[i]
        if (int(pic_ship_x[i]) <20):
            pic_ship_x[i] = 815
        screen.blit(pic_ship[i], (pic_ship_x[i], pic_ship_y[i]))
    screen.blit(pic_missile_6,(x1,y1))
    screen.blit(pic_ship_1,(x,pic_ship_1_y))

def Launcher(x,y):


    screen.blit(launcher,(launcher_x,launcher_y))
    screen.blit(pic_missile_1, (x,y))

def cloud():
    for i in range(3):
        pic_cloud_x[i]-=pic_cloud_chng[i]
        if(pic_cloud_x[i]<10 ):
            pic_cloud_x[i]=800
        screen.blit(pic_cloud[i],(pic_cloud_x[i],pic_cloud_y[i]))

def Live():
    for i in range(3):
        screen.blit(Draw[i],(x+35*(i+1),y))

def enemy(x,y,x1,y1):
        screen.blit(pic_enemy,(x,y))
        screen.blit(pic_missile_3,(x1,y1))

def missile_5(x,y):
    global bulletstate
    bulletstate="fire"
    pic_missile_5_x = pic_helicopter_x
    screen.blit(pic_missile_5,(x+20,y+20))

def missile_4(x,y):
    global bulletstate_1
    bulletstate_1="fire"
    pic_missile_4_x = pic_helicopter_x
    screen.blit(pic_missile_4,(x+20,y+20))

while(check):

    screen.fill((0,0,0))


    show()
    if(lives<0):
        check=False

    Live()
    for event in pygame.event.get():  # checking all the keyboards input
        if event.type == pygame.QUIT:  # checking the entered event
            check = False
        if event.type == pygame.KEYDOWN:  # pressing any botttom on the keyboard
            if event.key == pygame.K_DOWN:
                pic_helicopter_speed_y=0.1
            if event.key == pygame.K_UP:
                pic_helicopter_speed_y=-0.1
            if event.key == pygame.K_LEFT:
                pic_helicopter_speed_x=-0.2
            if event.key == pygame.K_RIGHT:
                pic_helicopter_speed_x=0.1
            if event.key == pygame.K_SPACE:
                if(bulletstate=="ready"):
                     pic_missile_5_y=pic_helicopter_y
                     missile_5(pic_missile_5_x,pic_missile_5_y)
            if event.key == pygame.K_0:
                if(bulletstate_1=="ready"):
                     pic_missile_4_x=pic_helicopter_x
                     missile_4(pic_missile_4_x,pic_missile_4_y)

        if event.type == pygame.KEYUP:  # pressing any botttom on the keyboard
            if event.key == pygame.K_DOWN:
                pic_helicopter_speed_y= 0
            if event.key == pygame.K_UP:
                pic_helicopter_speed_y= 0
            if event.key == pygame.K_LEFT:
                pic_helicopter_speed_x= 0
            if event.key == pygame.K_RIGHT:
                pic_helicopter_speed_x= 0

    pic_helicopter_y+=pic_helicopter_speed_y
    pic_helicopter_x+=pic_helicopter_speed_x+0.05
    if(pic_helicopter_y<10  ):
        pic_helicopter_y+=4
    if(pic_helicopter_y>190):
        pic_helicopter_y-=4
    if (pic_helicopter_x < 10):
        pic_helicopter_x+=4
    if(pic_helicopter_x > 780):
        pic_helicopter_x -= 4

    show_heli(pic_helicopter_x,pic_helicopter_y)


    if(pic_missile_5_x>780):
        pic_missile_5_x=pic_helicopter_x
        bulletstate="ready"
    if(bulletstate=="fire"):

        pic_missile_5_x+=pic_missile_5_speed
        missile_5(pic_missile_5_x,pic_missile_5_y)

    if (pic_missile_4_y >390):
        pic_missile_4_y = pic_helicopter_y
        bulletstate_1= "ready"
    if (bulletstate_1 == "fire"):
        pic_missile_4_y += pic_missile_4_speed
        missile_4(pic_missile_4_x, pic_missile_4_y)

    pic_space_x-=pic_space_speed
    if(pic_space_x<-5):
        list=[1,2,3,4]
        choose=random.randint(0,40000)

        if(choose==4):
            pic_space_x=780
            pic_space_y = random.randint(50, 150)
    show_space(pic_space_x,pic_space_y)

    pic_ship_1_x+=pic_ship_1_speed
    if(pic_ship_1_x>840):
        pic_ship_1_x=10

    pic_missile_6_x+=pic_missile_6_speed_x
    pic_missile_6_y-=pic_missile_6_speed_y
    if(pic_missile_6_x>895):
        pic_missile_6_x=pic_ship_1_x
        pic_missile_6_y = pic_ship_1_y

    if (abs(pic_missile_4_x - pic_ship_1_x) < 25 and abs(pic_missile_4_y - pic_ship_1_y) < 10):
        pic_ship_1_x = random.randint(50, 200)
        score+=35

        for j in range(7000000):
            a = 1

    show_ship(pic_ship_1_x,pic_missile_6_x+45,pic_missile_6_y+40)

    if (abs(pic_missile_6_y - pic_helicopter_y) < 20 and abs(pic_missile_6_x - pic_helicopter_x) < 20):
        lives-=1
        pic_helicopter_x=120

    for i in range(2):
        pic_tank_x[i] += pic_tank_speed_x[i]

        if (int(pic_tank_x[i]) > 260 or int(pic_tank_x[i]) < 30):
            pic_tank_speed_x[i] = -(pic_tank_speed_x[i])
        pic_missile_2_x[i] += pic_ship_speed_x[i]
        pic_missile_2_y[i] -= pic_missile_2_speed_y[i]
        if (pic_missile_2_x[i] > 580):
            pic_missile_2_x[i] = pic_tank_x[i]
            pic_missile_2_y[i] = pic_tank_y[i]

        if (pic_missile_2_y[i] < 10):
            pic_missile_2_y[i] = pic_tank_y[i]
            pic_missile_2_x[i] = pic_tank_x[i]

        if (abs(pic_missile_4_x - pic_tank_x[i]) < 25 and abs(pic_missile_4_y - pic_tank_y[i]) < 10):
            pic_tank_x[i] = random.randint(50,200)
            score+=20

            for j in range(7000000):
                a = 1

        screen.blit(pic_tank[i], (pic_tank_x[i], pic_tank_y[i]))
        screen.blit(pic_missile_2[i], (pic_missile_2_x[i] + 46, pic_missile_2_y[i]))
        if (abs(pic_missile_2_y[i] - pic_helicopter_y) < 20 and abs(pic_missile_2_x[i] - pic_helicopter_x) < 20):
            lives-=1
            pic_helicopter_x=80






    pic_enemy_x -= pic_enemy_chng_x
    pic_enemy_y-=pic_enemy_chng_y
    if (pic_enemy_x < 240 or pic_enemy_x>780):
        pic_enemy_chng_x = -(pic_enemy_chng_x)
    if (pic_enemy_y < 20 or pic_enemy_y>160):
        pic_enemy_chng_y = -(pic_enemy_chng_y)
    pic_missile_3_x -= pic_missile_3_speed

    if (pic_missile_3_x < 10):
        pic_missile_3_x = pic_enemy_x
        pic_missile_3_y=pic_enemy_y
    if(abs(pic_missile_5_x-pic_enemy_x)<15 and abs(pic_missile_5_y-pic_enemy_y)<15):
        pic_enemy_x=random.randint(260,640)
        pic_enemy_y=random.randint(50,120)
        score+=50
        for i in range(90000):
            a=1

    enemy(pic_enemy_x,pic_enemy_y,pic_missile_3_x,pic_missile_3_y)

    if(abs(pic_missile_3_x-pic_helicopter_x)<10 and abs(pic_missile_3_y-pic_helicopter_y)<10):
        lives-=1

    cloud()

    pic_missile_1_x -= pic_missile_1_speed_x
    pic_missile_1_y -= pic_missile_1_speed_y
    if (pic_missile_1_x < 5):
        pic_missile_1_x = launcher_x
        pic_missile_1_y = launcher_y



    Launcher(pic_missile_1_x,pic_missile_1_y)

    if (abs(pic_missile_1_y - pic_helicopter_y) < 20 and abs(pic_missile_1_x - pic_helicopter_x) < 20):
        lives-=1
        pic_helicopter_x=30
    print(lives)

    pygame.display.update()