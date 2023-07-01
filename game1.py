import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Game')


# 창 유지하기
play = True # 창이 종료하기 전까지 유지 
while play:
    for envent in pygame.event.get():
        pass
        
        if envent.type == pygame.QUIT:
            play = False