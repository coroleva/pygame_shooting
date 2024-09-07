import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра Тир')

icon = pygame.image.load('img/тир.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/тир.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
lives = 3
font = pygame.font.SysFont(None, 40)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


MOVE_TARGET_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_TARGET_EVENT, 1000)

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOVE_TARGET_EVENT:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
            else:
                lives -= 1


    screen.blit(target_img, (target_x, target_y))


    draw_text(f'Очки: {score}', font, (255, 255, 255), 10, 10)
    draw_text(f'Жизни: {lives}', font, (255, 255, 255), 10, 50)


    if score >= 10:
        draw_text('Победа!', font, (0, 255, 0), SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    if lives <= 0:
        draw_text('Поражение!', font, (255, 0, 0), SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    pygame.display.update()

pygame.quit()

