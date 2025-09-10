# 게임 예제 2
import sys

import pygame

pygame.init()  # pygame 관련 값 초기화

windowSurface = pygame.display.set_mode((400, 300))  # 너비와 높이가 지정된 윈도우 객체 생성
pygame.display.set_caption("파이게임 애니메이션")  # 게임 스크린의 제목

carImg = pygame.image.load("car.png")  # 자동차 이미지 읽기
carImg = pygame.transform.scale(carImg, (70, 50))  # 원하는 크기로 리사이즈
carx = 10  # 이미지 표시용 x좌표
cary = 10  # 이미지 표시용 y좌표
direction = "right"  # 이미지 이동용 변수(우측부터 움직이도록 설정)
FPS = 30  # 초당 프레임 값 설정
fpsTimes = pygame.time.Clock()  # 게임 루프를 작성하기 전에 게임 루프의 주기 및 속도 결정용 객체

pygame.mixer_music.load("backsound3.mp3")  # 배경 음악 파일 읽기
pygame.mixer_music.play()  # 배경 음악 재생

while True:
    windowSurface.fill(color=(255, 255, 255))  # 게임 스크린 배경색

    if direction == "right":
        carx += 5
        if carx == 300:
            direction = "down"
    elif direction == "down":
        cary += 5
        if cary == 250:
            direction = "left"
    elif direction == "left":
        carx -= 5
        if carx == 10:
            direction = "up"
    elif direction == "up":
        cary -= 5
        if cary == 10:
            direction = "right"

    windowSurface.blit(carImg, (carx, cary))  # blit 함수를 이용해 이미지를 그림

    pygame.display.update()
    fpsTimes.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
