import pygame
import random

pygame.init()
win = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("First Game")

char_x = 50
char_y = 50
char_size = 50
char_speed = 1

food_size = 10
food_x = random.randint(10, 1190)
food_y = random.randint(10, 690)

food3_size = 10
food3_x = random.randint(10, 1190)
food3_y = random.randint(10, 690)

food2_size = 10
food2_x = random.randint(10, 1190)
food2_y = random.randint(10, 690)

refresh_speed = 10
count = 0

run = True

while run:
    pygame.time.delay(refresh_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and char_x > char_speed:
        char_x -= char_speed
    if keys[pygame.K_RIGHT] and char_x < 1200 - char_size:
        char_x += char_speed
    if keys[pygame.K_UP] and char_y > char_speed:
        char_y -= char_speed
    if keys[pygame.K_DOWN] and char_y < 700 - char_size:
        char_y += char_speed

    if food_x - char_size <= char_x <= food_x + char_size and food_y - char_size <= char_y <= food_y + char_size:
        refresh_speed -= 3
        food_x = random.randint(0, 1200)
        food_y = random.randint(0, 700)
        count += 1

    if food3_x - char_size <= char_x <= food3_x + char_size and food3_y - char_size <= char_y <= food3_y + char_size:
        char_size += 1
        food3_x = random.randint(0, 1200)
        food3_y = random.randint(0, 700)
        count += 1

    if food2_x - char_size <= char_x <= food2_x + char_size and food2_y - char_size <= char_y <= food2_y + char_size:
        refresh_speed += 3
        food2_x = random.randint(0, 1200)
        food2_y = random.randint(0, 700)
        count += 1

    if count == 25:
        run = False

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 255, 0), (food_x, food_y, food_size, food_size))
    pygame.draw.rect(win, (0, 0, 255), (food2_x, food2_y, food2_size, food2_size))
    pygame.draw.rect(win, (255, 255, 255), (food3_x, food3_y, food3_size, food3_size))

    pygame.draw.rect(win, (255, 0, 0), (char_x, char_y, char_size, char_size))
    pygame.display.update()

pygame.quit()
