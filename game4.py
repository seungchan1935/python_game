import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((1080,720))
pygame.display.set_caption('Game')


x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

to_x = 0
to_y = 0

fps = pygame.time.Clock()

play = True
while play:# 게임 플레이

    deltaTime = fps.tick(2000)

    for envent in pygame.event.get(): # 키보드 마우스 컨트롤

        if envent.type == pygame.QUIT:
            play = False

        if envent.type == pygame.KEYDOWN: # 키보드 키를 눌렀을 때
            if envent.key == pygame.K_w:
                print('UP')
                to_y = -1

            elif envent.key == pygame.K_s:
                print("DOWN")
                to_y = 1
            elif envent.key == pygame.K_d:
                print('RIGHT')
                to_x = 1
            elif envent.key == pygame.K_a:
                print('LEFT')
                to_x = -1

        if envent.type == pygame.KEYUP: # 키보드 키를 올렸을 때
            
            to_x = 0
            to_y = 0
            
            
            if envent.key == pygame.K_w:
                print('UP')
                to_y = 0

            elif envent.key == pygame.K_s:
                print("DOWN")
                to_y = 0
            elif envent.key == pygame.K_d:
                print('RIGHT')
                to_x = 0
            elif envent.key == pygame.K_a:
                print('LEFT')
                to_x = 0
    

    x_pos += to_x
    y_pos += to_y

    background.fill((255,255,255)) # 배경화면 색 채우기
    pygame.draw.circle(background,(0,0,255),(x_pos,y_pos),10)
    pygame.display.update() # 계속 업데이트
    
pygame.quit()