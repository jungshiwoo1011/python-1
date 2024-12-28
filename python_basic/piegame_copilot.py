import pygame
import random

# 설정
화면_너비 = 800
화면_높이 = 600
프레임_속도 = 60

흰색 = (255, 255, 255)
검정색 = (0, 0, 0)
빨간색 = (255, 0, 0)
초록색 = (0, 255, 0)
파란색 = (0, 0, 255)
갈색 = (139, 69, 19)

플레이어_속도 = 10  # 속도 증가
적_속도 = 5  # 속도 증가
총알_속도 = 15  # 속도 증가

최대_체력 = 100
시작_점수 = 0

# 플레이어 클래스
class Player:
    def __init__(self):
        self.rect = pygame.Rect(화면_너비 // 2, 화면_높이 - 50, 50, 50)
        self.speed = 플레이어_속도
        self.bullets = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 화면_너비:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()

        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        pygame.draw.rect(screen, 흰색, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

# 총알 클래스
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.speed = 총알_속도

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, 검정색, self.rect)

# 적 클래스
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, 화면_너비 - 50), 0, 50, 50)
        self.speed = 적_속도

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, 흰색, self.rect)

# 게임 클래스
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.Surface((화면_너비, 화면_높이))
        self.background.fill(갈색)
        self.player = Player()
        self.enemies = []
        self.last_spawn_time = pygame.time.get_ticks()
        self.start_time = pygame.time.get_ticks()
        self.game_over = False

    def update(self):
        if not self.game_over:
            self.player.update()
            for enemy in self.enemies:
                enemy.update()
                if enemy.rect.top > 화면_높이:
                    self.game_over = True
                if enemy.rect.top > 화면_높이:
                    self.enemies.remove(enemy)

            self.check_collisions()
            self.spawn_enemy()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.draw_timer()
        if self.game_over:
            self.draw_game_over()

    def spawn_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > 100:  # 0.1초 간격으로 적 생성
            enemy = Enemy()
            self.enemies.append(enemy)
            self.last_spawn_time = current_time

    def check_collisions(self):
        for enemy in self.enemies:
            for bullet in self.player.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.enemies.remove(enemy)
                    self.player.bullets.remove(bullet)
                    break

    def draw_timer(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) // 1000
        font = pygame.font.SysFont(None, 36)
        timer_text = font.render(f"Time: {elapsed_time}s", True, 흰색)
        self.screen.blit(timer_text, (화면_너비 - 150, 10))

    def draw_game_over(self):
        font = pygame.font.SysFont(None, 75)
        text = font.render("Game Over", True, 빨간색)
        self.screen.blit(text, (화면_너비 // 2 - text.get_width() // 2, 화면_높이 // 2 - text.get_height() // 2))

# 메인 함수
def main():
    pygame.init()
    screen = pygame.display.set_mode((화면_너비, 화면_높이))
    pygame.display.set_caption("총싸움 게임")
    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(프레임_속도)

    pygame.quit()

if __name__ == "__main__":
    main()