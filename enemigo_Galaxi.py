from clase_padre import prota

            
class enemy(prota):
    def __init__(self, x, y, width, height, color, shot, life, damage, speed):
        super().__init__(x, y, width, height, color, shot, life, damage)
        self.speed = speed

    def move(self):
        self.x += self.speed
        # Controlar límites para el enemigo
        if self.x > 1000:  # Si el enemigo sale de la pantalla, lo reiniciamos
            self.x = -self.width  # Reiniciar a la izquierda
            

            
