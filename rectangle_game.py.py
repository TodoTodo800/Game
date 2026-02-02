import pygame 
import time
import pyttsx3
pygame.init()
speaker = pyttsx3.init()
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("Rectangle")

x=10
y=10
speed = 0.2

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w]:
        y-= speed
    if key[pygame.K_s]:
        y+= speed
    if key[pygame.K_a]:
        x-= speed
    if key[pygame.K_d]:
        x+= speed 
    if x<0:
        x=0
    if x > 1060:
        x = 1060
    if y< 0:
        y = 0
    if y> 700:
        y = 700
    
    screen.fill((200,200,200))
    ball = pygame.draw.rect(screen,(30,30,0),(x,y,20,20))
    red_rect1 = pygame.draw.rect(screen,(225,0,0),(60,0,20,500))
    red_rect2 = pygame.draw.rect(screen,(225,0,0),(140,340,20,700))
    red_rect3 = pygame.draw.rect(screen,(225,0,0),(200,0,20,500))
    red_rect4 = pygame.draw.rect(screen,(225,0,0),(260,340,20,700))
    red_rect5 = pygame.draw.rect(screen,(225,0,0),(320,0,20,500))
    red_rect6 = pygame.draw.rect(screen,(225,0,0),(400,340,20,700))
    red_rect7 = pygame.draw.rect(screen,(225,0,0),(460,0,20,600))
    red_rect8 = pygame.draw.rect(screen,(225,0,0),(520,340,20,700))
    red_rect9 = pygame.draw.rect(screen,(225,0,0),(600,0,20,500))
    red_rect10 = pygame.draw.rect(screen,(225,0,0),(650,300,20,700))
    red_rect11 = pygame.draw.rect(screen,(225,0,0),(700,0,20,670))
    red_rect12 = pygame.draw.rect(screen,(225,0,0),(750,120,20,700))
    red_rect13 = pygame.draw.rect(screen,(225,0,0),(800,0,20,670))
    red_rect14 = pygame.draw.rect(screen,(225,0,0),(850,120,20,700))
    red_rect15 = pygame.draw.rect(screen,(225,0,0),(900,0,20,450))
    red_rect16 = pygame.draw.rect(screen,(225,0,0),(945,100,20,700))
    red_rect17 = pygame.draw.rect(screen,(225,0,0),(1000,0,20,680))
    green_rect = pygame.draw.rect(screen,(0,225,0),(1060,0,20,750))
    
    if ball.colliderect(red_rect1):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect2):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect3):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect4):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect5):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect6):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect7):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect8):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect9):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect10):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect11):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect12):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect13):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect14):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect15):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect16):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(red_rect17):
        speaker.say("GameOver")
        time.sleep(2)
        run = False
    if ball.colliderect(green_rect):
        win = True
        if win:
            speaker.say("You Win!")
            time.sleep(5)
            run = False

    pygame.display.update()
speaker.runAndWait()
pygame.quit()





