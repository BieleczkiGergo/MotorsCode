import pygame
from gpiozero import Motor, OutputDevice

pygame.init()
ablak = pygame.display.set_mode((300, 300))
speed = 0.9

motor1 = Motor(25,24)
motor2 = Motor(22,23)
motor3 = Motor(16,26)
motor4 = Motor(6,5)

time = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a")
                motor1.backward(speed)
                motor2.backward(speed)
                motor3.forward(speed)
                motor4.forward(speed)
            if event.key == pygame.K_d:
                print("d")
                motor1.forward(speed)
                motor2.forward(speed)
                motor3.backward(speed)
                motor4.backward(speed)
            if event.key == pygame.K_w:
                print("w")
                motor1.forward(speed)
                motor2.forward(speed)
                motor3.forward(speed)
                motor4.forward(speed)
            if event.key == pygame.K_s:
                print("s")
                motor1.backward(speed)
                motor2.backward(speed)
                motor3.backward(speed)
                motor4.backward(speed)
            if event.key == pygame.K_p:
                print("quiting")
                pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
            if event.key == pygame.K_a:
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
            if event.key == pygame.K_w:
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()
            if event.key == pygame.K_s:
                motor1.stop()
                motor2.stop()
                motor3.stop()
                motor4.stop()

    time.tick(60)