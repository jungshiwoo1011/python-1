# -*- coding: utf-8 -*-
import random
import pygame

# 초기화
pygame.init()

user_name = input("이름을 입력하세요 : ")

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 (제목장)
pygame.display.set_caption("못난놈 잘난놈 못된놈 잘된놈 못말리는놈 잘말리는놈 피하기")

# FPS
clock = pygame.time.Clock()

# 이동속도 고정
chaaracter_speed = 1
enemy_speed = 2

# 이미지 불러오기 (배경)
bg = pygame.image.load("pygame/source/bg.png")

# 스프라이트 불러오기
character = pygame.image.load("pygame\source\character.png")

# 스프라이트의 크기와 좌표 세팅
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2 )
character_yPos = (screen_height / 2) - (character_height / 2)

# 적군 불러오기
enemy = pygame.image.load("pygame\source\enemy.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_xPos = random.randint(0, (screen_width - enemy_width))
enemy_yPos = 0

# 폰트 정해주기
game_font40 = pygame.font.Font(None, 40)
game_font20 = pygame.font.Font(None, 20)

# 게임제한시간
total_time = 0

# 시작시간 정보
start_ticks = pygame.time.get_ticks()

to_x = 0
to_y = 0

# 이벤트 루프 - 종료까지 대기
running = True
while running:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xPos += to_x * dt
    character_yPos += to_y * dt

# 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width

# 세로 스크린내 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    enemy_yPos += enemy_speed
    if enemy_yPos > screen_height:
        enemy_yPos = 0
        enemy_speed = random.randint(1, 3)
        enemy_xPos = random.randint(0, screen_width - enemy_width)


        
# 충돌 처리하기
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

# 충돌 이벤트 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌! 충돌!")
        running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font40.render (f"time : {str(int(total_time + elapsed_time))}"), False, (0, 0, 0)
    userName = game_font20.render (f"{user_name} servival time : {str(int(total_time + elapsed_time))}"), False, (0, 0, 0)

    # screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(timer, (10,10))
    screen.blit(userName, (10, 50))

    pygame.display.update()
# 종료처리
pygame.quit()