#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

# ---------------------------
# Importacion de los módulos
# ---------------------------
 
import pygame
from pygame.locals import *
import os
import sys
import random
 
# -----------
# Constantes
# -----------
 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "imagenes"
SND_DIR = "sonidos"
 
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

        
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print ("Error, no se puede cargar la imagen: ", ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

def load_sound(nombre_sonido, dir_sonido):
    #Encontramos la ruta completa del sonido
    ruta_sonido = os.path.join(dir_sonido, nombre_sonido)
    sound = pygame.mixer.Sound(ruta_sonido)
    return sound


# -----------------------------------------------
# Creamos los sprites (clases) de los objetos del juego:
 
#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE PELOTA)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 
class Pelota(pygame.sprite.Sprite):
    "La bola y su comportamiento en la pantalla"
 
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("asteroid.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = y
        self.speed = [3, 3]
 
    def updateAsteroid(self):
        if self.rect.left < -40 or self.rect.right > SCREEN_WIDTH +  40:
            self.speed[0] = -self.speed[0]
        if self.rect.top < -40:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        self.rect.centery = self.rect.centery + float(1)
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            
            gameover()


    

 
#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE JUGADOR)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 

class Player(pygame.sprite.Sprite):
    "Define el comportamiento de las paletas de ambos jugadores"
 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("rocket.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.width = 30
        self.rect.height = 80
        self.rect.centerx = x
        self.rect.centery = y
 
    def humano(self):
        # Controlar que la paleta no salga de la pantalla
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE NUBE)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 

class Cloud(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("cloud4.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.width = 30
        self.rect.height = 50
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = y
        self.speed = [1, 1]
 
    def update(self):
        self.rect.centery = self.rect.centery + float(1)


    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            
            
            gameover()

#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE TESLA)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 

class Tesla(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("tesla.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.width = 30
        self.rect.height = 50
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [1, 1]
 
    def updateTesla(self):
        self.image = load_image("tesla.png", IMG_DIR, alpha=True)
        self.rect.centery = self.rect.centery + float(1)
       
        #self.rect.move_ip((self.speed[0], self.speed[1]))
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            
            
            gameover()
#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE AVION IZQUIERDA)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 


class Plane1(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Plane1.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = random.randint(0, SCREEN_HEIGHT)
        self.speed = [1, 1]

    def updatePlane1(self):
        self.rect.centerx = self.rect.centerx - int(2)

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            
            gameover()
            

#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE AVION DERECHA)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------# 

class Plane2(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Plane2.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = random.randint(0, SCREEN_HEIGHT)
        self.speed = [1, 1]

    def updatePlane2(self):
        self.rect.centerx = self.rect.centerx + int(2)

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            
            gameover()
            
#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE MISIL)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------#
class Missile(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("missile_down.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = y
        self.speed = [1, 1]

    def updateMissile(self):
        self.rect.centery = self.rect.centery + int(4)

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            
            gameover()            

                       
            
#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE PLANETA 1)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------#
class Planet1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("planet1.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [0, 0]

    def updatePlanet1(self):
        self.rect.centery = self.rect.centery + 1

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            
            gameover()        

#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE IRONMAN y ASTRONAUTA)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-------#

class Human(pygame.sprite.Sprite):
 
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("iron.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = y
        self.speed = [1, 1]
 
    def updateIron(self):
        if self.rect.left < -40 or self.rect.right > SCREEN_WIDTH +  40:
            self.speed[0] = -self.speed[0]
        if self.rect.top < -40:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        self.rect.centery = self.rect.centery + float(1)
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            
            gameover()






#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE SATELITE)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-----#
        
class Satelite(pygame.sprite.Sprite):
 
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("satelite.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = y
        self.speed = [2, 2]
 
    def updateSatelite(self):
        if self.rect.left < -40 or self.rect.right > SCREEN_WIDTH +  40:
            self.speed[0] = -self.speed[0]
        if self.rect.top < -40:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        self.rect.centery = self.rect.centery + float(1)
 
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            
            gameover()

        
            


#------x-x-x-x-x-x-x-x-x-x-x-x-(CLASE WIN LINE)-x-x-x-x-x-x-x-x-x-x-x-x-x-x------#
class Winline(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("fondo2.jpg", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = y
        self.speed = [1, 1]

    def updateWinline(self):
        self.rect.centery = self.rect.centery + int(2)

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            
            gamewin()  
            
# ------------------------------
# Funcion principal del juego
# ------------------------------
 
 
def main():    
    pygame.init()
    #creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Up -n- up")


    #---------------Cargamos los objetos----------------#
    #Cargo fondo
    fondo = load_image("fondodeg2.jpg", IMG_DIR, alpha=False)
    fondo2 = load_image("fondo2.jpg", IMG_DIR, alpha=False)
    linea_meta = Winline(-9400)

    #Cargo sonidos
    sound_main = load_sound("maintheme.wav", SND_DIR)
    sound_fuelon = load_sound("fuelon.wav", SND_DIR)
    sound_steamon = load_sound("steamon.wav", SND_DIR)


    sound_main.play()
    sound_main.set_volume(100)
    
    #Cargo Nubes

    Roadster = Tesla(320, -4000)
    nube1 = Cloud(random.randint(-800, -10))
    nube2 = Cloud(random.randint(-800, -10))
    nube3 = Cloud(random.randint(-800, -10))
    nube4 = Cloud(random.randint(-800, -10))
    nube5 = Cloud(random.randint(-800, -10))
    nube6 = Cloud(random.randint(-1000, -10))
    nube7 = Cloud(random.randint(-1000, -10))
    nube8 = Cloud(random.randint(-1000, -10))
    nube9 = Cloud(random.randint(-1000, -10))
    nube10 = Cloud(random.randint(-1000, -10))
    nube11 = Cloud(random.randint(-1500, -10))
    nube12 = Cloud(random.randint(-1500, -10))
    nube13 = Cloud(random.randint(-1500, -10))
    nube14 = Cloud(random.randint(-1500, -10))
    nube15 = Cloud(random.randint(-1500, -10))
    nube16 = Cloud(random.randint(-2000, -1000))
    nube17 = Cloud(random.randint(-2000, -1000))
    nube18 = Cloud(random.randint(-2000, -1000))
    nube19 = Cloud(random.randint(-2000, -1000))
    nube20 = Cloud(random.randint(-2000, -1000))
    
    #Cargo Aviones
    avion1 = Plane1(700)
    avion2 = Plane2(440)
    avion3 = Plane1(900)

    #Cargo Asteroides    
    asteroid1 = Pelota(random.randint(-4000, -2000))
    asteroid2 = Pelota(random.randint(-4000, -2000))
    asteroid3 = Pelota(random.randint(-4000, -2000))
    asteroid4 = Pelota(random.randint(-4000, -2000))
    asteroid5 = Pelota(random.randint(-4000, -2000))
    asteroid6 = Pelota(random.randint(-4000, -2000))
    asteroid7 = Pelota(random.randint(-4000, -2000))
    asteroid8 = Pelota(random.randint(-4000, -2000))

    
    #Cargo Misiles
    misil1 = Missile(random.randint(-6000, -3000))
    misil2 = Missile(random.randint(-6000, -3000))
    misil3 = Missile(random.randint(-6000, -3000))
    misil4 = Missile(random.randint(-6000, -4000))
    misil5 = Missile(random.randint(-6000, -4000))

    #Cargo Satelites
    sat1 = Satelite(random.randint(-5000, -1000))
    sat2 = Satelite(random.randint(-5000, -1000))
    sat3 = Satelite(random.randint(-5000, -1000))
    sat4 = Satelite(random.randint(-5000, -1000))
    sat5 = Satelite(random.randint(-4000, -2000))
    sat6 = Satelite(random.randint(-4000, -3000))
    sat7 = Satelite(random.randint(-4000, -3000))

    iron = Human(-4000)
    
    #Cargo Planetas
    planeta1 = Planet1(213, -4000)

    #Cargo Player
    jugador1 = Player((SCREEN_WIDTH / 2), SCREEN_HEIGHT)

    pygame.time.wait(3000)

 
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)  # Activa repeticion de teclas
    pygame.mouse.set_visible(False)


 
    # el bucle principal del juego
    arranca = -9120
    while True:
        clock.tick(60)
        # Obtenemos la posicon del mouse
#       pos_mouse = pygame.mouse.get_pos()
#       mov_mouse = pygame.mouse.get_rel()
        # Actualizamos los obejos en pantalla

        arranca += 1

        
        jugador1.humano()
        Roadster.updateTesla()
        nube1.update()
        nube2.update()
        nube3.update()
        nube4.update()
        nube5.update()
        nube6.update()
        nube7.update()
        nube8.update()
        nube9.update()
        nube10.update()
        nube11.update()
        nube12.update()
        nube13.update()
        nube14.update()
        nube15.update()
        nube16.update()
        nube17.update()
        nube18.update()
        nube19.update()
        nube20.update()
        
        avion1.updatePlane1()
        avion2.updatePlane2()
        avion3.updatePlane1()

        asteroid1.updateAsteroid()
        asteroid2.updateAsteroid()
        asteroid3.updateAsteroid()
        asteroid4.updateAsteroid()
        asteroid5.updateAsteroid()
        asteroid6.updateAsteroid()
        asteroid7.updateAsteroid()
        asteroid8.updateAsteroid()
                
        misil1.updateMissile()
        misil2.updateMissile()
        misil3.updateMissile()
        misil4.updateMissile()
        misil5.updateMissile()

        sat1.updateSatelite()
        sat2.updateSatelite()
        sat3.updateSatelite()
        sat4.updateSatelite()
        sat5.updateSatelite()
        sat6.updateSatelite()
        sat7.updateSatelite()

        iron.updateIron()
        
        planeta1.updatePlanet1()

        linea_meta.updateWinline()
        
        # Comprobamos si colisionan los objetos
        Roadster.colision(jugador1)
        nube1.colision(jugador1)
        nube2.colision(jugador1)
        nube3.colision(jugador1)
        nube4.colision(jugador1)
        nube5.colision(jugador1)
        nube6.colision(jugador1)
        nube7.colision(jugador1)
        nube8.colision(jugador1)
        nube9.colision(jugador1)
        nube10.colision(jugador1)
        nube11.colision(jugador1)
        nube12.colision(jugador1)
        nube13.colision(jugador1)
        nube14.colision(jugador1)
        nube15.colision(jugador1)
        nube16.colision(jugador1)
        nube17.colision(jugador1)
        nube18.colision(jugador1)
        nube19.colision(jugador1)
        nube20.colision(jugador1)

        avion1.colision(jugador1)
        avion2.colision(jugador1)
        avion3.colision(jugador1)

        asteroid1.colision(jugador1)
        asteroid2.colision(jugador1)
        asteroid3.colision(jugador1)
        asteroid4.colision(jugador1)
        asteroid5.colision(jugador1)
        asteroid6.colision(jugador1)
        asteroid7.colision(jugador1)
        asteroid8.colision(jugador1)

        misil1.colision(jugador1)
        misil2.colision(jugador1)
        misil3.colision(jugador1)
        misil4.colision(jugador1)
        misil5.colision(jugador1)

        sat1.colision(jugador1)
        sat2.colision(jugador1)
        sat3.colision(jugador1)
        sat4.colision(jugador1)
        sat5.colision(jugador1)
        sat6.colision(jugador1)
        sat7.colision(jugador1)

        iron.colision(jugador1)

        planeta1.colision(jugador1)

        linea_meta.colision(jugador1)

 
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    sound_fuelon.play()
                    sound_fuelon.set_volume(0.1)
                    jugador1.image = load_image("rocket_upfuel.png", IMG_DIR, alpha=True)
                    jugador1.rect.centery -= 2
                elif event.key == K_DOWN:
                    sound_steamon.play()
                    sound_steamon.set_volume(0.03)
                    jugador1.image = load_image("rocket_downfuel.png", IMG_DIR, alpha=True)
                    jugador1.rect.centery += 2
                elif event.key == K_LEFT:
                    sound_fuelon.play()
                    jugador1.image = load_image("rocket_leftfuel.png", IMG_DIR, alpha=True)
                    jugador1.rect.centerx -= 3
                elif event.key == K_RIGHT:
                    sound_fuelon.play()
                    jugador1.image = load_image("rocket_rightfuel.png", IMG_DIR, alpha=True)
                    jugador1.rect.centerx += 3
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == K_UP:
                    sound_fuelon.stop()
                    jugador1.image = load_image("rocket.png", IMG_DIR, alpha=True)
                    jugador1.rect.centery += 0
                elif event.key == K_DOWN:
                    sound_steamon.stop()
                    jugador1.image = load_image("rocket.png", IMG_DIR, alpha=True)
                    jugador1.rect.centery += 0
                elif event.key == K_RIGHT:
                    sound_fuelon.stop()
                    jugador1.image = load_image("rocket.png", IMG_DIR, alpha=True)
                    jugador1.rect.centerx += 0
                elif event.key == K_LEFT:
                    sound_fuelon.stop()
                    jugador1.image = load_image("rocket.png", IMG_DIR, alpha=True)
                    jugador1.rect.centerx += 0

            # Si el mouse no esta quieto mover la paleta a su posicion
##            elif mov_mouse[1] != 0:
##                jugador1.rect.centery = pos_mouse[1]

        
            
        screen.blit(fondo,(0, arranca))
            
##        screen.blit(Roadster.image, Roadster.rect)
        screen.blit(nube1.image, nube1.rect)
        screen.blit(nube2.image, nube2.rect)
        screen.blit(nube3.image, nube3.rect)
        screen.blit(nube4.image, nube4.rect)
        screen.blit(nube5.image, nube5.rect)
        screen.blit(nube6.image, nube6.rect)
        screen.blit(nube7.image, nube7.rect)
        screen.blit(nube8.image, nube8.rect)
        screen.blit(nube9.image, nube9.rect)
        screen.blit(nube10.image, nube10.rect)
        screen.blit(nube11.image, nube11.rect)
        screen.blit(nube12.image, nube12.rect)
        screen.blit(nube13.image, nube13.rect)
        screen.blit(nube14.image, nube14.rect)
        screen.blit(nube15.image, nube15.rect)
        screen.blit(nube16.image, nube16.rect)
        screen.blit(nube17.image, nube17.rect)
        screen.blit(nube18.image, nube18.rect)
        screen.blit(nube19.image, nube19.rect)
        screen.blit(nube20.image, nube20.rect)
        
        screen.blit(avion1.image, avion1.rect)
        screen.blit(avion2.image, avion2.rect)
        screen.blit(avion3.image, avion3.rect)

        screen.blit(asteroid1.image, asteroid1.rect)
        screen.blit(asteroid2.image, asteroid2.rect)
        screen.blit(asteroid3.image, asteroid3.rect)
        screen.blit(asteroid4.image, asteroid4.rect)
        screen.blit(asteroid5.image, asteroid5.rect)
        screen.blit(asteroid6.image, asteroid6.rect)
        screen.blit(asteroid7.image, asteroid7.rect)
        screen.blit(asteroid8.image, asteroid8.rect)
        

        screen.blit(misil1.image, misil1.rect)
        screen.blit(misil2.image, misil2.rect)
        screen.blit(misil3.image, misil3.rect)
        screen.blit(misil4.image, misil4.rect)
        screen.blit(misil5.image, misil5.rect)

        screen.blit(sat1.image, sat1.rect)
        screen.blit(sat2.image, sat2.rect)
        screen.blit(sat3.image, sat3.rect)
        screen.blit(sat4.image, sat4.rect)
        screen.blit(sat5.image, sat5.rect)
        screen.blit(sat6.image, sat6.rect)
        screen.blit(sat7.image, sat7.rect)

        screen.blit(iron.image, iron.rect)

        screen.blit(planeta1.image, planeta1.rect)

        screen.blit(linea_meta.image, linea_meta.rect)


        screen.blit(jugador1.image, jugador1.rect)
        
        pygame.display.flip()
 
#------------------------x-x-x-x-x-x-x-x-x-x-x-x-(PANTALLA GAMEOVER)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-----------------------#

def gameover():    
    pygame.init()
    #creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Up -n- up")
    pygame.mixer.stop()
    sound_loose = load_sound("loosesound.wav", SND_DIR)
    sound_loose.play()

    # cargamos los objetos
    fondo = load_image("gameover_screen.jpg", IMG_DIR, alpha=False)
    
 
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)  # Activa repeticion de teclas
    pygame.mouse.set_visible(True)
 
    # el bucle principal del juego
    while True:
        clock.tick(60)
        # Obtenemos la posicon del mouse
        pos_mouse = pygame.mouse.get_pos()
        mov_mouse = pygame.mouse.get_rel()
 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == K_r:
                    main()
                  

            
    
        
        screen.blit(fondo,(0, 0))
        pygame.display.flip()

#------------------------x-x-x-x-x-x-x-x-x-x-x-x-(PANTALLA GAMEWIN)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-----------------------#

def gamewin():    
    pygame.init()
    #creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Up -n- up")
    pygame.mixer.stop()
    sound_win = load_sound("winsound.wav", SND_DIR)
    sound_win.play()

    # cargamos los objetos
    fondo2 = load_image("gamewin_screen.jpg", IMG_DIR, alpha=False)
    
 
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)  # Activa repeticion de teclas
    pygame.mouse.set_visible(True)
 
    # el bucle principal del juego
    while True:
        clock.tick(60)
        # Obtenemos la posicon del mouse
        pos_mouse = pygame.mouse.get_pos()
        mov_mouse = pygame.mouse.get_rel()

 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == K_r:
                    main()

            
    
        
        screen.blit(fondo2,(0, 0))
        pygame.display.flip()




#------------------------x-x-x-x-x-x-x-x-x-x-x-x-(PANTALLA CAPE CAÑAVERAL)-x-x-x-x-x-x-x-x-x-x-x-x-x-x-----------------------#


def capecanaveral():    
    pygame.init()
    #creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Up -n- up")


    #---------------Cargamos los objetos----------------#
    #Cargo fondo
    fondo = load_image("fondodeg2.jpg", IMG_DIR, alpha=False)
    fondo2 = load_image("fondo2.jpg", IMG_DIR, alpha=False)
    linea_meta = Winline(-9600)

    #Cargo sonidos
    sound_main = load_sound("maintheme.wav", SND_DIR)
    sound_fuelon = load_sound("fuelon.wav", SND_DIR)
    sound_steamon = load_sound("steamon.wav", SND_DIR)


    
    #Cargo Player
    jugador1 = Player((SCREEN_WIDTH / 2), SCREEN_HEIGHT)
  
 
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)  # Activa repeticion de teclas
    pygame.mouse.set_visible(False)


 
    # el bucle principal del juego
    clock.tick(60)
        # Obtenemos la posicon del mouse
#       pos_mouse = pygame.mouse.get_pos()
##      mov_mouse = pygame.mouse.get_rel()
        # Actualizamos los obejos en pantalla


        
    jugador1.humano()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            
            
                            
    screen.blit(fondo,(0, -9120))
            
        
    screen.blit(jugador1.image, jugador1.rect)
        

    pygame.display.flip()
    
    main()

        
 
#if __name__ == "__main__":
    #main()

 
if __name__ == "__main__":
    capecanaveral()
    
    
