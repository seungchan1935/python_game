import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((480,360))
pygame.display.set_caption('Game')


# 창 유지하기
play = True # 창이 종료하기 전까지 유지 
while play:
    for envent in pygame.event.get():

        if envent.type == pygame.QUIT:
            play = False

        if envent.type == pygame.KEYDOWN: # 키보드 키를 눌렀을 때
            if envent.key == pygame.K_UP:
                print('UP')
            elif envent.key == pygame.K_DOWN:
                print("DOWN")

            elif envent.key == pygame.K_RIGHT:
                print('RIGHT')

            elif envent.key == pygame.K_LEFT:
                print('LEFT')

pygame.quit()