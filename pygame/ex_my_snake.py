highscore = 50

import pygame, random, sys
pygame.init()

def salva(p):
    f = open(sys.argv[0], "r")
    x = f.readline()
    x = f.readlines()
    f.close()
    f = open(str(p) + "\n")
    for i in x :
        f.write(i)
    f.close()


def record():
    f = open(sys.argv[0], "r")
    x = int(f.readline())
    f.close()
    return x


def gameover(x):
    global m, snake
    
    if m == False:
        global size, w, h, verdanabig, fontino
        s = verdanabig.render(str(len(snake.s)-3), True, (0,0,0))
    
    if record() > len(snake.s)- 3:
        s2 = fontino.render("Record: " + str(record()), True, (0,0,0))
    else:
        s2 = fontino.render("Nuovo Record!", True, (0,0,0))
        salva(len(snake.s)- 3)
        f2 = mini.render("Primi F2", True, (0,0,0))
        r = s.get_rect()
        r2 = s2.get_rect()

    while not (x):
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and evento.key == pygame.K_F2:
            snake = Snake()
            fruit = Fruit()
            game()
        
        sceen.fill((300, 300, 190))
        sceen.blit(s, ((w - r.w)/ 2, (h - r.h)/ 2 -20, r[2], r[3]))
        sceen.blit(s2, ((w - r2.w)/ 2, (h - r2.h)/ 2 +20, r2[2], r2[3]))
        screen.blit(f2, (15, h - 20, 0, 0))
        pygame.display.update()
        pygame.time.delay(100)


def head(): # surface of black for the head
    s = pygame.Surface((10, 11))
    s.fill((0, 0, 0))
    return s


def body(): # surface of gray for the body
    s = pygame.Surface((10, 10))
    s.fill((96, 96, 96))
    return s

def Fruit(): # surface of red for the fruit
    s = pygame.Surface((5, 5))
    s.fill((155, 0,0))
    r = pygame.Rect(random.randrange(0, 11) * 19, random.randrange(0,10)* 19, 19, 19)
    return s, r

class Snake: # class our snake
    def __init__(self, w =3):
        self.dir = 1, 0
        self.s = []
        
        for i in range(w): # the cicle create a snake's body
            self.s.append((w + 3 - i, 3))

    def move(self, dir=False):   # move the snake's head        
        global size, w, h, fruit # in the list self.s

        if dir == False:
            dir=self.dir
        elif (dir[0]==self.dir[0] and dir[1]==-1*self.dir[1]) or (dir[1]==self.dir[1] and dir[0]==-1*self.dir[0]):
            dir=self.dir
        else:	
            self.dir=dir
            x=[[self.s[0][0]+dir[0],self.s[0][1]+dir[1]]]

            z = -1
            
            if x[0][0] <0:
                x[0][0] = gameover()
            elif x[0][0] <0:
                x[0][0] = gameover()
            elif x[0][0] > w/20 -1:
                x[0][0] = gameover()
            elif x[0][0] > h/20 -1:
                x[0][0] = gameover()
            else:
                self.dir = dir
                x=[[self.s[0][0]+dir[0],self.s[0][1]+dir[1]]]

            if fruit[1].colliderct(r) == 1: # check if the snake touches the fruit
                z = None
                fruit = Fruit()

            self.s = x # update the list with pieces of snake
            x =[]

            for i in self.s:
                x.append(pygame.Rect(i[0]* 20, i[1]* 20, 20, 20))

            for i in x[2:]: # check if the snake touches himself
                if x[0].colliderect(i)==True:
                    return False
            return None

    def press(self, sc):
        sc.blit(head(), (self.s[0][0] * 20, self.s[0][1] * 10, 210, 50))

        for i in self.s[1:]:
            sc.blit(body(), (i[0] * 20, i[0] * 20, 20, 20))


size = w, h = 600, 440
window = pygame.display.set_mode(size) # I create the window
pygame.display.set_caption("Snake")
snake = Snake()
fruit = Fruit()

try:
    verdanabig=pygame.font.SysFont("verdana.ttf",50)
    fontino=pygame.font.SysFont("verdana.ttf",25)
    mini=pygame.font.SysFont("verdana.ttf",20)
except:
    try:
		verdanabig=pygame.font.SysFont(pygame.font.get_default_font(),50)
		fontino=pygame.font.SysFont(pygame.font.get_default_font(),25)
		mini=pygame.font.SysFont(pygame.font.get_default_font(),20)
    except:
        verdanabig=pygame.font.Font(pygame.font.get_default_font(),50)
        fontino=pygame.font.Font(pygame.font.get_default_font(),25)
        mini=pygame.font.Font(pygame.font.get_default_font(),20)

def game():
    global snake,fruit,m
    pause = False	# true se il gioco e' in pausa
    while 1:		# ciclo del gioco
        m = True
        
        evento = pygame.event.poll()		# prima di tutto verifico se si vuole chiudere

        if evento.type == pygame.QUIT:
            break
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F2:	# regolo la pausa
            snake = Snake()
            fruit = Fruit()
        elif evento.type == pygame.KEYDOWN and evento.key==pygame.K_p:	# regolo la pausa
            if pause == False:
                pause = True
            else:
            	pause = False
	
        if pause == False:
            keys = pygame.key.get_pressed()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:	
                m = snake.move((0,-1))
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                m = snake.move((0,1))
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            	m = snake.move((1,0))
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            	m = snake.move((-1,0))
            else:
            	m = snake.move()

            if m == False:
            	break		# se m diventa m dopo la funzione Muovi vuol dire che la testa ha fatto collisione con un pezzo
            window.fill((255,255,183))	# quindi game over!	|	riempio lo sfondo
            snake.press(window)		# stampo snake
            window.blit(fruit[0],fruit[1])	# stampo frutto
            pt = mini.render(str(len(snake.s)-3),True,(0,0,0))
            window.blit(pt,(15,h-20,0,0))
            pygame.display.update()				# aggiorno
            pygame.time.delay(100)				# pausa di un decimo di sec tra un fotogramma e l'altro
	gameover(m)					# parte gameover


game()
