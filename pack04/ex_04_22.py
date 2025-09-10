# 게임 예제 1
import sys

import pygame

pygame.init()  # pygame 관련 값 초기화

windowSurface = pygame.display.set_mode((400, 300))  # 너비와 높이가 지정된 윈도우 객체 생성
pygame.display.set_caption("안녕 파이게임")  # 게임 스크린의 제목

windowSurface.fill(color=(255, 255, 255))  # 게임 스크린 바탕 설정

# 선 그리기
pygame.draw.line(surface=windowSurface, color=(255, 0, 0), start_pos=(50, 30), end_pos=(100, 30), width=1)
pygame.draw.line(surface=windowSurface, color=(0, 0, 255), start_pos=(50, 50), end_pos=(200, 50), width=3)

# 원 그리기
pygame.draw.circle(surface=windowSurface, color=(255, 0, 0,), center=(100, 150), radius=30)

# 삼각형 그리기
pygame.draw.polygon(surface=windowSurface, color=(0, 255, 0), points=((250, 100), (200, 150), (300, 150)))

pygame.display.update()

while True:
    for event in pygame.event.get():    # 게임 도중 이벤트를 받음
        if event.type == pygame.QUIT:   # 이벤트 중 윈도우의 닫기 버튼을 눌렀을 때
            pygame.quit()               # 게임 종료
            sys.exit()                  # 응용 프로그램 종료
