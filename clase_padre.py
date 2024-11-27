# Clase base para los objetos del juego
import pygame

class prota:
    def __init__(self, x, y, width, height, color, shot, life, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shot = shot
        self.life = life 
        self.damage = damage 

    # Funcion para dibujar los objetos de las clases hijos   
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))