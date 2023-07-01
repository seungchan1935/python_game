import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((480,360))
pygame.display.set_caption('Game')

x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

play = True
while play:# 창이 종료하기 전까지 유지 
    for envent in pygame.event.get():

        if envent.type == pygame.QUIT:
            play = False

        if envent.type == pygame.KEYDOWN: # 키보드 키를 눌렀을 때
            if envent.key == pygame.K_UP:
                print('UP')
                y_pos = y_pos - 10

            elif envent.key == pygame.K_DOWN:
                print("DOWN")
                y_pos = y_pos + 10
            elif envent.key == pygame.K_RIGHT:
                print('RIGHT')
                x_pos = x_pos + 10
            elif envent.key == pygame.K_LEFT:
                print('LEFT')
                x_pos = x_pos - 10
    
    background.fill((255,255,255))
    pygame.draw.circle(background,(0,0,255),(x_pos,y_pos),5)
    pygame.display.update()
    #pygame.draw.circle(surface=,color=,center=,radius=)
pygame.quit()