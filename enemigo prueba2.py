import pygame,random
from time import sleep

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.1.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.lives = 10
        self.speed_x = 0
        self.speed_y = 0
    
        self.rect.x = 200
        self.rect.y = 318
    
    def damage(self):
      self.lives -= 1

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

    def __del__(self):                                                                         #       <----------------     Sobrecargar funcion DEL
      del self.image
      del self.rect

class Pelota2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pelota_2.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 5 

    def __del__(self):                                                                         #       <----------------     Sobrecargar funcion DEL
      del self.image
      del self.rect

class enemy(pygame.sprite.Sprite):
  def __init__(self,lvl,lives=0):
      super().__init__()
      self.lvl = lvl
      self.lives = lives
      self.image = pygame.image.load("enemigo_1.png").convert()
      self.image.set_colorkey((255,255,255))
      self.rect = self.image.get_rect()
      self.rect.x = 363 + (215)
      self.rect.y = 198 + (100)
      self.x_objetivo = 578                             
      self.y_objetivo = 298

      Level_names =[["BOT Harry","BOT Ron","BOT Hermione"],["BOT Luke","BOT Leia","BOT Solo"],["BOT Ayrton","BOT Cesar","BOT Luis","BOT Rafael"]]

      if self.lvl == 1:
        self.name = Level_names[0][random.randint(0,2)]
        self.lvl_alias = "Fácil"
        self.lives = 5
        self.pct_throw = 15
        self.pct_move = 300
        self.pct_none = 100
      elif self.lvl == 2:
        self.name = Level_names[1][random.randint(0,2)]
        self.lvl_alias = "Normal"
        self.lives = 10
        self.pct_throw = 25
        self.pct_move = 500
        self.pct_none = 100
      elif self.lvl == 3:
        self.name = Level_names[2][random.randint(0,3)]
        self.lvl_alias = "Difícil"
        self.lives = 15
        self.pct_throw = 45
        self.pct_move = 800
        self.pct_none = 100

  def __del__(self):
   del self.image
   del self.rect

  def move1(self):                                                                                        #       <----------------     Función MOVERSE
    validacion_x = self.rect.x >= self.x_objetivo - 5 and self.rect.x  <= self.x_objetivo + 5
    validacion_y = self.rect.y >= self.y_objetivo - 5 and self.rect.y  <= self.y_objetivo + 5
    if(validacion_x and validacion_y):
      self.x_objetivo = random.randint(440,615)
      self.y_objetivo = random.randint(210,390)
    else:
        # X izquierda
      if (self.x_objetivo < self.rect.x):
        self.rect.x -= 4 
        # X aderecha
      if (self.x_objetivo > self.rect.x):
        self.rect.x += 4 
        # Y arriba 
      if (self.y_objetivo > self.rect.y):
        self.rect.y += 4 
        # Y abajo 
      if (self.y_objetivo < self.rect.y):
        self.rect.y -= 4 

  def move2(self):
    validacion_x = self.rect.x >= self.x_objetivo - 5 and self.rect.x  <= self.x_objetivo + 5
    validacion_y = self.rect.y >= player.rect.y - 15 and self.rect.y  <= player.rect.y + 15
    if(validacion_x and validacion_y):
      self.x_objetivo = random.randint(440,615)
      self.y_objetivo = random.randint(210,390)
    else:
        # X izquierda
      if (self.x_objetivo < self.rect.x):
        self.rect.x -= 4 
        # X aderecha
      if (self.x_objetivo > self.rect.x):
        self.rect.x += 4 
        # Y arriba 
      if (player.rect.y > self.rect.y):
        self.rect.y += 4 
        # Y abajo 
      if (player.rect.y < self.rect.y):
        self.rect.y -= 4 

  def atak(self):
    pelota_enemigo = Pelota2()
    pelota_enemigo.rect.x = self.rect.x - 10
    pelota_enemigo.rect.y = self.rect.y + 20
    pelota_enemy_list.add(pelota_enemigo)
    all_sprite_list.add(pelota_enemigo)
    
  def nada(self):
    self.action_timer = random.randint(0,100)
    #print("..............")

  def damage(self):
    self.lives -= 1
    

  def porcentaje(self):
    self.pct = random.randint(14,1000)
    if self.pct <= self.pct_throw:
      self.atak()

    elif self.pct > self.pct_throw and self.pct <= self.pct_move:               
      self.move1()
      
    else:
      self.nada()


'''
def win_text():
  win = pygame.image.load("you_win.png")
  screen.blit(win,(0,0))
  sleep(2)
  del win


def lose_text():
  lose = pygame.image.load("you_lose.png")
  screen.blit(lose,(0,0))
  sleep(3)
  nivel1 = False
  nivel2 = False
  nivel3 = False


def next_lvl():
  next_level = pygame.image.load("next_level.png")
  screen.blit(next_level,(0,0))
  sleep(2)
  del next_level
'''





pygame.init()
screen = pygame.display.set_mode([844,508])
fondo = pygame.image.load("fondo.png").convert()
clock = pygame.time.Clock()
nivel1 = True
nivel2 = False
nivel3 = False


all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
pelota_enemy_list = pygame.sprite.Group()                                              #       <----------------     Lista de pelotas enemigo
pelota_player_list = pygame.sprite.Group()                                             #       <----------------     Lista de pelotas jugador

enemigo1 = enemy(1)
player = Player()
all_sprite_list.add(enemigo1)
all_sprite_list.add(player)

while nivel1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              pygame.quit()
            if event.key == pygame.K_UP:
                player.changespeed(-3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,3)
            if event.key == pygame.K_SPACE:
                if(len(pelota_player_list) <= 3):                            
                  pelota = Pelota()
                  pelota.rect.x = player.rect.x + 10
                  pelota.rect.y = player.rect.y + 20 
                  all_sprite_list.add(pelota)
                  pelota_player_list.add(pelota)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.changespeed(3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,-3)
    enemigo1.porcentaje()                                                       
    all_sprite_list.update()

    pygame.sprite.groupcollide(pelota_enemy_list,pelota_player_list,True,True)               
    
    for pelota in pelota_player_list:                             
      if pelota.rect.x >= 844:
        pelota_player_list.remove(pelota)

    for pelota in pelota_enemy_list:                         
      if pelota.rect.x <= -40: #COLLISION 
        pelota_enemy_list.remove(pelota)

    if pygame.sprite.spritecollide(player, pelota_enemy_list, True, collided = None):
      player.damage()

    if pygame.sprite.spritecollide(enemigo1, pelota_player_list, True, collided = None):
      enemigo1.damage()
    
    print(player.lives,enemigo1.lives)

    if enemigo1.lives == 0:
        sleep(2)
        all_sprite_list.remove(enemigo1)
        del enemigo1
        del pelota_player_list
        del pelota_enemy_list
        pelota_player_list = pygame.sprite.Group()
        pelota_enemy_list = pygame.sprite.Group()
        nivel1 = False
        player.rect.x = 200
        player.rect.y = 318
        player.lives = 10
        nivel2 = True
    elif player.lives == 0:
        nivel1 = False


    screen.fill((255,255,255))
    screen.blit(fondo,[0,0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)



enemigo2 = enemy(2)
all_sprite_list.add(enemigo2)

while nivel2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              pygame.quit()
            if event.key == pygame.K_UP:
                player.changespeed(-3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,3)
            if event.key == pygame.K_SPACE:
                if(len(pelota_player_list) <= 3):                        
                  pelota = Pelota() 
                  pelota.rect.x = player.rect.x + 10
                  pelota.rect.y = player.rect.y + 20 
                  all_sprite_list.add(pelota)
                  pelota_player_list.add(pelota)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.changespeed(3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,-3)
    enemigo2.porcentaje()                                                       
    all_sprite_list.update()

    pygame.sprite.groupcollide(pelota_enemy_list,pelota_player_list,True,True)               
    
    for pelota in pelota_player_list:                             
      if pelota.rect.x >= 844:
        pelota_player_list.remove(pelota)

    for pelota in pelota_enemy_list:                         
      if pelota.rect.x <= -40: #COLLISION 
        pelota_enemy_list.remove(pelota)

    if pygame.sprite.spritecollide(player, pelota_enemy_list, True, collided = None):
      player.damage()

    if pygame.sprite.spritecollide(enemigo2, pelota_player_list, True, collided = None):
      enemigo2.damage()
    
    print(player.lives,enemigo2.lives)


    if enemigo2.lives == 0:
        sleep(2)
        all_sprite_list.remove(enemigo2)
        del enemigo2
        del pelota_player_list
        del pelota_enemy_list
        pelota_player_list = pygame.sprite.Group()
        pelota_enemy_list = pygame.sprite.Group()
        nivel2 = False
        player.rect.x = 200
        player.rect.y = 318
        player.lives = 10
        nivel3 = True
    elif player.lives == 0:
        nivel2 = False




    screen.fill((255,255,255))
    screen.blit(fondo,[0,0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)



enemigo3 = enemy(3)
all_sprite_list.add(enemigo3)

while nivel3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              pygame.quit()
            if event.key == pygame.K_UP:
                player.changespeed(-3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,3)
            if event.key == pygame.K_SPACE:
                if(len(pelota_player_list) <= 3):                      
                  pelota = Pelota()
                  pelota.rect.x = player.rect.x + 10
                  pelota.rect.y = player.rect.y + 20 
                  all_sprite_list.add(pelota)
                  pelota_player_list.add(pelota)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.changespeed(3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(0,-3)
    enemigo3.porcentaje()                                                       
    all_sprite_list.update()

    pygame.sprite.groupcollide(pelota_enemy_list,pelota_player_list,True,True)               
    
    for pelota in pelota_player_list:                             
      if pelota.rect.x >= 844:
        pelota_player_list.remove(pelota)

    for pelota in pelota_enemy_list:                         
      if pelota.rect.x <= -40: #COLLISION 
        pelota_enemy_list.remove(pelota)

    if pygame.sprite.spritecollide(player, pelota_enemy_list, True, collided = None):
      player.damage()

    if pygame.sprite.spritecollide(enemigo3, pelota_player_list, True, collided = None):
      enemigo3.damage()
    
    print(player.lives,enemigo3.lives)

    if enemigo3.lives == 0:
        sleep(2)
        nivel3 = False
    elif player.lives == 0:
        nivel3 = False

    screen.fill((255,255,255))
    screen.blit(fondo,[0,0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
