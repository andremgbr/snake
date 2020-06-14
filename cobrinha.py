import pygame
import random
import pandas
pygame.font.init()



class Cobra:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.resto = []

    def draw(self,window):
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,16,16))
        
    def move(self,dr,vel=16):
        if dr == 1:
            self.y -= vel
        if dr == 2:
            self.x += vel
        if dr == 3:
            self.y += vel
        if dr == 4:
            self.x -= vel

    def moveCorpo(self):
        for i in range(len(self.resto)-1,0,-1):
            self.resto[i] = self.resto[i-1]
        self.resto[0] = Corpo(self.x,self.y)
    

class Corpo(Cobra):
    def __init__(self,x,y):
        Cobra.__init__(self,x,y)

    def drawCorpo(self,window):
        pygame.draw.rect(window,(255,255,255),(self.x,self.y,16,16))


class Comida:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,window):
        pygame.draw.rect(window,(0,255,255),(self.x,self.y,16,16))

def grade(scl,WIDTH,LENGTH,window):
    for i in range(int(WIDTH/scl)+1):
        pygame.draw.line(window,(255,255,255),(i*scl,0),(i*scl,LENGTH),1)
    for i in range(int(LENGTH/scl)+1):
        pygame.draw.line(window,(255,255,255),(0,i*scl),(WIDTH,i*scl),1)
    
        
def menu_screen(WIN,pontos):
    WIDTH,LENGTH = 593,529
    run_menu = True
    df = pandas.read_csv('scoreBoard.csv')
    df = df.sort_values(by=["Pontos"], ascending=False)
    df = df.reset_index(drop=True)
    clock = pygame.time.Clock()
    fonte_type = pygame.font.SysFont('Arial',30)
    input_box = pygame.Rect(100,100,140,32)
    text =""

    while run_menu:
        clock.tick(30)
        WIN.fill((0,0,0))
        texto = fonte_type.render(text,True,(255,255,255))
       

        pygame.draw.rect(WIN,(51, 0, 51),(50,30,493,120))
        pygame.draw.rect(WIN,(51, 0, 51),(50,200,493,300))
        texto_nome = fonte_type.render("Seu Nome: ",True,(255,255,255))
        texto_pontos = fonte_type.render(f"Você fez  {pontos}  pontos",True,(255,255,255))
        texto_scoreBoard = fonte_type.render("QUADRO DOS MELHORES",True,(255,255,255))

        texto_primeiro = fonte_type.render(f"1ª -- {df.loc[0][0]} com {df.loc[0][1]} pontos",True,(255,255,255))
        texto_segundo = fonte_type.render(f"2ª -- {df.loc[1][0]} com {df.loc[1][1]} pontos",True,(255,255,255))
        texto_terceiro = fonte_type.render(f"3ª -- {df.loc[2][0]} com {df.loc[2][1]} pontos",True,(255,255,255))
        texto_quarto = fonte_type.render(f"4ª -- {df.loc[3][0]} com {df.loc[3][1]} pontos",True,(255,255,255))
        texto_quinto = fonte_type.render(f"5ª -- {df.loc[4][0]} com {df.loc[4][1]} pontos",True,(255,255,255))

        
        WIN.blit(texto,(texto_nome.get_width()+60,45))
        WIN.blit(texto_nome,(60 , 45))
        WIN.blit(texto_pontos,(60, 90))
        WIN.blit(texto_scoreBoard,(int(WIDTH/2) - int(texto_scoreBoard.get_width()/2), 215))

        WIN.blit(texto_primeiro,(60, 265))
        WIN.blit(texto_segundo,(60, 295))
        WIN.blit(texto_terceiro,(60, 325))
        WIN.blit(texto_quarto,(60, 355))
        WIN.blit(texto_quinto,(60, 385))

        
        pygame.display.update()


        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                return
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_RETURN:
                    df2 = pandas.DataFrame({"Nome":[text],"Pontos":[pontos]})
                  

                    df = df.append(df2)                      
                    df.to_csv('scoreBoard.csv',index=False)
                    menu_score(WIN)
                    
                    
         
                elif key.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += key.unicode

        tecla = pygame.key.get_pressed()
    

def menu_score(WIN):
    WIDTH,LENGTH = 593,529
    run_menu = True
    df = pandas.read_csv('scoreBoard.csv')
    df = df.sort_values(by=["Pontos"], ascending=False)
    df = df.reset_index(drop=True)
    print(df)
    clock = pygame.time.Clock()
    fonte_type = pygame.font.SysFont('Arial',30)
    input_box = pygame.Rect(100,100,140,32)
    text =""

    while run_menu:
        clock.tick(30)
        WIN.fill((0,0,0))

        pygame.draw.rect(WIN,(51, 0, 51),(50,30,493,120))
        pygame.draw.rect(WIN,(51, 0, 51),(50,200,493,300))
        texto_nome = fonte_type.render("PRESSIONE ESPAÇO p/ Jogar!!!",True,(255,255,255))
        texto_scoreBoard = fonte_type.render("QUADRO DOS MELHORES",True,(255,255,255))

        texto_primeiro = fonte_type.render(f"1ª -- {df.loc[0][0]} com {df.loc[0][1]} pontos",True,(255,255,255))
        texto_segundo = fonte_type.render(f"2ª -- {df.loc[1][0]} com {df.loc[1][1]} pontos",True,(255,255,255))
        texto_terceiro = fonte_type.render(f"3ª -- {df.loc[2][0]} com {df.loc[2][1]} pontos",True,(255,255,255))
        texto_quarto = fonte_type.render(f"4ª -- {df.loc[3][0]} com {df.loc[3][1]} pontos",True,(255,255,255))
        texto_quinto = fonte_type.render(f"5ª -- {df.loc[4][0]} com {df.loc[4][1]} pontos",True,(255,255,255))

        
        WIN.blit(texto_nome,(int(WIDTH/2)-int(texto_nome.get_width()/2) , 45))
        WIN.blit(texto_scoreBoard,(int(WIDTH/2) - int(texto_scoreBoard.get_width()/2), 215))

        WIN.blit(texto_primeiro,(60, 265))
        WIN.blit(texto_segundo,(60, 295))
        WIN.blit(texto_terceiro,(60, 325))
        WIN.blit(texto_quarto,(60, 355))
        WIN.blit(texto_quinto,(60, 385))

        
        pygame.display.update()
        
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                return
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_SPACE:
                    main()
    


            
def main():
    WIDTH,LENGTH = 593,529
    WIN = pygame.display.set_mode((WIDTH,LENGTH))
    scl = 16

    run = True
    clock = pygame.time.Clock()
    time = 0

    

    player = Cobra(0,10*scl)
    player.resto.append(Corpo(-30,10*scl))
    player.resto.append(Corpo(-60,10*scl))
    player.resto.append(Corpo(-90,10*scl))
    food = Comida(random.randint(0,36)*scl,random.randint(3,32)*scl)

                        
    dr = 2

    fonte_type = pygame.font.SysFont('Arial',21)
    pontos = 0
    prunto = False

    tick_level = 13
    while run:

        clock.tick(tick_level)
        WIN.fill((0,0,0))
        pygame.draw.rect(WIN,(255,255,255),(0,0,WIDTH,scl*3))
        
        texto = fonte_type.render("Pontos = " + str(pontos),True,(0,0,0))
        grade(scl,WIDTH,LENGTH,WIN)

        WIN.blit(texto,(int(WIDTH/2) - int(texto.get_width()/2),10))

        
        player.moveCorpo()
        player.move(dr)
        food.draw(WIN)
        player.draw(WIN)
        for i in player.resto:
            i.drawCorpo(WIN)

        pygame.display.update()
        

      

        if player.x>WIDTH-8 or player.x<0 or player.y>LENGTH-8 or player.y<scl*3:
            menu_screen(WIN,pontos)
            break

        for i in player.resto:
            if i.x == player.x and i.y == player.y:
                menu_screen(WIN,pontos)
                break

        if player.x == food.x and player.y == food.y or prunto:
            pontos +=1
            player.resto.append([])            
            food = Comida(random.randint(0,36)*scl,random.randint(3,32)*scl)
            prunto = False



        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                return
               
        
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w] or tecla[pygame.K_UP] and not dr == 3:
            dr = 1
        if tecla[pygame.K_d] or tecla[pygame.K_RIGHT] and not dr == 4:
            dr = 2
        if tecla[pygame.K_s] or tecla[pygame.K_DOWN] and not dr == 1:
            dr = 3
        if tecla[pygame.K_a] or tecla[pygame.K_LEFT] and not dr == 2:
            dr = 4
        if tecla[pygame.K_p]:
            prunto = True
        
main()
