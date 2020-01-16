import pygame
import random
pygame.init()
gameWindow = pygame.display.set_mode((700,700))
pygame.display.set_caption("My Game")

#game variables

#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
font = pygame.font.SysFont(None,55)
def text_score(text,color,x1,y1):
    screen_txt = font.render(text,True,color)
    gameWindow.blit(screen_txt,[x1,y1])


def plot_snk(gameWindow,color,snk_lst,length,width):
    for x1,y1 in snk_lst:
        pygame.draw.rect(gameWindow,color,[x1,y1,length,width])
#game loop
def gameloop():
    exit_game=False
    game_over=False
    x = 45
    y = 45
    v_x = 0
    v_y = 0
    food_x = random.randint(20,500/2)
    food_y = random.randint(20,500/2)
    length = 10
    width = 10
    length1 = 10
    width1 = 10
    clock = pygame.time.Clock()
    score=0
    size = 30
    snk_lst = []
    snk_len = 1
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_score("Game Over!!. Press enter to continue",red,20,20)
            for event in pygame.event.get():
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    print("Closed")
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        v_x = 10
                        v_y = 0
                    if event.key == pygame.K_LEFT:
                        v_x = -10
                        v_y = 0
                    if event.key == pygame.K_UP:
                        v_y = -10
                        v_x = 0
                    if event.key == pygame.K_DOWN:
                        v_y = 10
                        v_x = 0
            x = x + v_x
            y = y + v_y
            if abs(x - food_x)<6 and abs(y - food_y)<6:
                score+=1
                print("Score:",score)
                food_x = random.randint(0,500/2)
                food_y = random.randint(0,500/2)
                snk_len += 5
                
            gameWindow.fill(white)
            text_score("Score:"+str(score),red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,length1,width1]) #food
            head = []
            head.append(x)
            head.append(y)
            snk_lst.append(head)

            if len(snk_lst)>snk_len:
                del snk_lst[0]
            if head in snk_lst[:-1]:
                game_over=True
            if x<0 or x>500 or y<0 or y>500:
                game_over=True
                print("Game over")
            plot_snk(gameWindow,black,snk_lst,length,width)
        pygame.display.update()
        clock.tick(30)
            
    pygame.quit()
    quit()

gameloop()
