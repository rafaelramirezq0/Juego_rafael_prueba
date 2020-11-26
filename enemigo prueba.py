import pygame,random
#from time import sleep




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.1.png").convert()
        self.image.set_colorkey((255,255,255)) #Blanco
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
    
        self.rect.x = 200
        self.rect.y = 318

    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x      
    
    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
        #Limitaciones
        if self.rect.x >= 365:
            if self.rect.x >= 365 and self.rect.y <= 210:
                self.rect.x = 365
                self.rect.y = 210
            elif self.rect.x >= 365 and self.rect.y >= 390:
                self.rect.x = 365
                self.rect.y = 390
            self.rect.x = 365
        elif self.rect.x <= 55:
            if self.rect.x <= 55 and self.rect.y <= 210:
                self.rect.x = 55
                self.rect.y = 210
            elif self.rect.x <= 55 and self.rect.y >= 390:
                self.rect.x = 55
                self.rect.y = 390
            self.rect.x = 55
        elif self.rect.y <= 210:
            self.rect.y = 210
        elif self.rect.y >= 390:
            self.rect.y = 390
class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pelota_2.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5
class Pelota2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pelota_2.png").convert()
        self.image.set_colorkey((0,0,0)) #Negro
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 5 



class enemy(pygame.sprite.Sprite):
  def __init__(self,lvl,status=True):
      super().__init__()
      self.lvl = lvl
      self.status = status
      self.image = pygame.image.load("enemigo_1.png").convert()
      self.image.set_colorkey((255,255,255))
      self.rect = self.image.get_rect()
      self.rect.x = 363+ (215)
      self.rect.y = 198+ (100)

      Level_names =[["BOT Harry","BOT Ron","BOT Hermione"],["BOT Luke","BOT Leia","BOT Solo"],["BOT Ayrton","BOT Cesar","BOT Luis","BOT Rafael"]]

      if self.lvl == 1: # Fácil   15 35 50
        self.name = Level_names[0][random.randint(0,2)]
        self.lvl_alias = "Fácil"
        self.pct_throw = 15
        self.pct_move = 50
        self.pct_none = 100

      elif self.lvl == 2: # Normal  25 35 40
        self.name = Level_names[1][random.randint(0,2)]
        self.lvl_alias = "Normal"
        self.pct_throw = 25
        self.pct_move = 60
        self.pct_none = 100

      elif self.lvl == 3: # Dificil  45 45 10
        self.name = Level_names[2][random.randint(0,3)]
        self.lvl_alias = "Difícil"
        self.pct_throw = 45
        self.pct_move = 90
        self.pct_none = 100

  def move1(self):
      #self.pos1x = random.randint(300 ,600)
      self.pos1x = 50
      self.pos1y = random.randint(207,390)
      print("----------------------------")

        #---- 4 CASOS ----- 
        # arriba izquierda
      if (self.pos1x < self.rect.x) and (self.pos1y < self.rect.y):
          while (self.pos1x < self.rect.x) and (self.pos1y < self.rect.y):
              self.rect.x -= 8
              self.rect.y -= 8
        
        # arriba derecha
      if (self.pos1x > self.rect.x) and (self.pos1y < self.rect.y):
          while (self.pos1x > self.rect.x) and (self.pos1y < self.rect.y):
              self.rect.x += 8
              self.rect.y -= 8

        # abajo izquierda
      if (self.pos1x < self.rect.x) and (self.pos1y > self.rect.y):
          while (self.pos1x < self.rect.x) and (self.pos1y > self.rect.y):
              self.rect.x += 8
              self.rect.y += 8

        # abajo derecha
      if (self.pos1x > self.rect.x) and (self.pos1y > self.rect.y):
          while (self.pos1x > self.rect.x) and (self.pos1y < self.rect.y):
              self.rect.x -= 8
              self.rect.y += 8   

  def move2(self):
    nueva_pos2()




  def atak(self):
    print("* ATAKA *")
    pelota_enemigo = Pelota2()
    pelota_enemigo.rect.x = enemigo1.rect.x - 10
    pelota_enemigo.rect.y = enemigo1.rect.y +20
    pelota_list.add(pelota_enemigo)
    all_sprite_list.add(pelota_enemigo)
    print()
    
  def nada(self):
    self.rect.x = self.rect.x
    self.rect.y = self.rect.y
    
    print("..............")
    #sleep(random.randint(1,3))
    

  def porcentaje(self):
    self.pct = random.randint(0,100)
    #print("Num porcentaje: ",self.pct)
    if self.pct <= self.pct_throw:
      self.atak()
      #return

    elif self.pct > self.pct_throw and self.pct < self.pct_move:
      self.pct_mover = random.randint(0,100)
      self.move1pct = 40
      self.move2pct = 60

      #if self.pct_mover <= self.move1pct and self.lvl == 1 or self.lvl == 2:
      #  self.move()
      if self.lvl == 3:
        self.move2()
      #return
      
    else:
      self.nada()
      #return

  def perder(self):
    self.status = False




def nueva_pos2():
  '''
  Solo condicionales x , y
  '''
  p_finx = random.randint(420 ,735)
  p_finy = random.randint(207,390)

  while enemigo1.rect.x < p_finx:
    enemigo1.rect.x += 1
  while enemigo1.rect.x > p_finx:
    enemigo1.rect.x -= 1
  while enemigo1.rect.y < p_finy:
    enemigo1.rect.y += 1
  while enemigo1.rect.y > p_finy:
    enemigo1.rect.y -= 1


pygame.init()
screen = pygame.display.set_mode([844,508])
fondo = pygame.image.load("fondo_final.png").convert()
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
pelota_list = pygame.sprite.Group()

enemigo1 = enemy(3)
player = Player()
all_sprite_list.add(enemigo1)
all_sprite_list.add(player)




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.changespeed(-3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,3)
            if event.key == pygame.K_SPACE:
                pelota = Pelota()
                pelota.rect.x = player.rect.x + 10
                pelota.rect.y = player.rect.y -20 
                all_sprite_list.add(pelota)
                pelota_list.add(pelota)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.changespeed(3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,-3)
    print(enemigo1.rect.x, enemigo1.rect.y)
    enemigo1.porcentaje()     ###### ENEMIGO
    all_sprite_list.update()


    screen.fill((255,255,255))
    screen.blit(fondo,[0,0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
