# nave.py
import pygame
from clase_padre import prota


class nave(prota):  
    def __init__(self, x, y, width, height, color, shot, life, damage, speed):
        super().__init__(x, y, width, height, color, shot, life, damage)
        self.speed = speed
        self.projectiles = pygame.sprite.Group()  # Grupo para los proyectiles
        self.shoot_delay = 500  # Tiempo de espera entre disparos 
        self.last_shot = pygame.time.get_ticks()  # Tiempo del último disparo
        self.rect = pygame.Rect(x, y, width, height)  # Atributo rect para la nave

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        # Controlar límites
        self.x = max(0, min(self.x, 1000 - self.width))
        self.y = max(0, min(self.y, 800 - self.height))
        self.rect.topleft = (self.x, self.y)  # Actualizar la posición del rectángulo

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.shoot_delay:
            projectile = Projectile(self.x + self.width // 2, self.y)  # Crear un nuevo proyectil
            self.projectiles.add(projectile)  # Añadir el proyectil al grupo
            self.last_shot = current_time  # Actualizar el tiempo del último disparo

# Clase para los proyectiles
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Tamaño del proyectil
        self.image.fill((255, 255, 0))  # Color del proyectil
        self.rect = self.image.get_rect(center=(x, y))  # Posición inicial del proyectil
        self.speed = -20  # Velocidad del proyectil 

    def update(self):
        self.rect.y += self.speed  # Mover el proyectil hacia arriba
        if self.rect.bottom < 0:  # limitaciones del proyectil 
            self.kill()  # Eliminar el proyectil