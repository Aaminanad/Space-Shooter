import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

BG = pygame.transform.scale(pygame.image.load("bg.space.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

STONE_WIDTH = 10
STONE_HEIGHT = 20
STONE_VEL = 5  

FONT = pygame.font.SysFont("pacifico", 40)

def draw(player, elapsed_time, stones):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "white", player)

    for stone in stones:
        pygame.draw.rect(WIN, "white", stone)

    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    stone_add_increment = 2000
    stone_count = 0
    stones = []
    hit = False

    while run:
        stone_count += clock.tick(60)
        if stone_count > stone_add_increment:
            for _ in range(3):
                stone_x = random.randint(0, WIDTH - STONE_WIDTH)
                stone = pygame.Rect(stone_x, -STONE_HEIGHT, STONE_WIDTH, STONE_HEIGHT)
                stones.append(stone)  # <-- Fixed
            stone_add_increment = max(200, stone_add_increment - 50)
            stone_count = 0

        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for stone in stones[:]:  
            stone.y += STONE_VEL
            if stone.y > HEIGHT:
                stones.remove(stone)
            elif stone.y + stone.height >= player.y and stone.colliderect(player):
                stones.remove(stone)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1,"white")
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break

        draw(player, elapsed_time, stones)



    pygame.quit()

if __name__ == "__main__":
    main()
          