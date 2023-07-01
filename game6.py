import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((480,360))
pygame.display.set_caption('Game')

play = True
while play:# 창이 종료하기 전까지 유지 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play =False
        if event.type == pygame.MOUSEMOTION:
            pass
            print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MOUSEBUTTONDOWN")

            print(pygame.mouse.get_pos())
            # 1 왼쪽클릭,2 휠클릭,3오른쪽클릭,4휠올리기,5휠 내리기
            print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            print("MOUSEBUTTONUP")
            print(pygame.mouse.get_pos())

pygame.quit()