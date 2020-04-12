import pygame
import time
import random


pygame.mixer.pre_init(44100,16, 2, 4096)
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH = 160
PADDLE_HEIGHT = 20
BLACK = (0, 0, 0)
#image hitbox
BALL_WIDTH = 10
BALL_HEIGHT = 13

#create the window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Pong Game!')




clock = pygame.time.Clock()
ballImg = pygame.image.load ('cannon ball.png')
paddleImg = pygame.image.load  ('steelstrip.png')


def mainMenu():
    gameDisplay.fill(WHITE)
    displayMessage()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()
                if event.key == pygame.K_1:
                    rules()
                if event.key == pygame.K_2:
                    pygame.quit()

def rules():
    gameDisplay.fill(WHITE)
    pygame.display.update()
    ruleDisplay('The objective of this game is to achieve 10 points without dying', 400, 50)
    ruleDisplay('Use the left and right keys to move your paddle', 400, 150)
    ruleDisplay('If the ball touches the ground, you lose a life', 400, 250)
    ruleDisplay('You have 3 lives to win this game', 400, 350)
    ruleDisplay('Press backspace to return to main menu', 400, 450)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    mainMenu()



def loss():
    lossMessage('You lost...')

def lossMessage(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH * 0.45), (DISPLAY_HEIGHT * 0.5))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)


def victory():
    victoryMessage('Victory!')
    
def victoryMessage(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((DISPLAY_WIDTH * 0.45), (DISPLAY_HEIGHT * 0.5))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)

def ruleDisplay(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)
def mainMenuMusic():
    pygame.mixer.music.load("Way Back Home.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    
def textObjects (text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def displayMessage():
    welcomeDisplay('Welcome to PONG',400,60)
    welcomeDisplay('Press Space to Start',400,200)
    welcomeDisplay('Rules (Press 1)',400,350)
    welcomeDisplay('Quit (Press 2)', 400,500) 
def score(count):
    scoreDisplay('Score: ' + str(count))

def life(count):
    lifeDisplay('Life: ' + str(count))
    
def scoreDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = textObjects(str(text), largeText)
    textRect.center = ((DISPLAY_WIDTH * 0.1), (DISPLAY_HEIGHT * 0.1))
    gameDisplay.blit(textSurf, textRect)
    
def welcomeDisplay(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    textSurf, textRect = textObjects(str(text), largeText)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)


def lifeDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = textObjects(str(text), largeText)
    textRect.center = ((DISPLAY_WIDTH * 0.9), (DISPLAY_HEIGHT * 0.1))
    gameDisplay.blit(textSurf, textRect)
    
def ball(a, b):
    gameDisplay.blit(ballImg, (a, b))

def paddle(x, y):
    gameDisplay.blit(paddleImg, (x, y))
        
def gameLoop():
    paddleX = (DISPLAY_WIDTH * 0.45)
    paddleY = (DISPLAY_HEIGHT * 0.8)
    ballX = (DISPLAY_WIDTH * 0.45)
    ballY = (DISPLAY_HEIGHT * 0.1)
    scoreCount = 0
    lifeCount = 3
    paddleVelocity = 0
    ballXVelocity = -0.5
    ballYVelocity = 0.5
    mainMenuMusic()
    gameExit = False
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddleVelocity = -2
                elif event.key == pygame.K_RIGHT:
                    paddleVelocity = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddleVelocity = 0                
                 
        paddleX = paddleX + paddleVelocity
        ballX = ballX + ballXVelocity
        ballY = ballY + ballYVelocity 
        gameDisplay.fill(WHITE)
        paddle(paddleX, paddleY)
        ball(ballX, ballY)
        score(scoreCount)
        life(lifeCount)
        if paddleX > DISPLAY_WIDTH - PADDLE_WIDTH:
            paddleX = 800 - PADDLE_WIDTH
        if paddleX < 0:
            paddleX = 0
            
        if ballX > DISPLAY_WIDTH - BALL_WIDTH or ballX <= 0:
            ballXVelocity = ballXVelocity * -1
        if  ballY <= 0:
            ballYVelocity = ballYVelocity * -1
        if ballY > DISPLAY_HEIGHT - BALL_HEIGHT:
            lifeCount = lifeCount - 1
            a = (DISPLAY_WIDTH *0.45)
            b = (DISPLAY_HEIGHT * 0.1)
            time.sleep(1)

        if ballY + BALL_HEIGHT == DISPLAY_HEIGHT*0.8 and ballX > paddleX and ballX < paddleX + PADDLE_WIDTH:
            ballYVelocity = ballYVelocity * -1
            scoreCount = scoreCount + 1
        elif ballY + BALL_HEIGHT == DISPLAY_HEIGHT*0.8 and ballX + BALL_WIDTH > paddleX and ballX + BALL_WIDTH < paddleX + PADDLE_WIDTH:
            ballYVelocity = ballYVelocity * -1
            scoreCount = scoreCount + 1

        
        if scoreCount == 10:
            victory()
            mainMenu()
        if lifeCount == 0:
            loss()
            mainMenu()
        pygame.display.update()
        clock.tick(600)
mainMenu()




