import pygame  # Librería principal
from enemigo_Galaxi import enemy  
from nave_principal import nave, Projectile  
# Inicializar Pygame
pygame.init()

# Medidas de la pantalla
ancho = 1000
alto = 800
ventana = pygame.display.set_mode([ancho, alto])
FPS = 60
pantalla_abierta = True
time = pygame.time.Clock()  # pygame.time está relacionado a todo lo que tenga que ver con el tiempo
vidas = 5
puntos = 0 

# Parámetros de los enemigos
enemy_width = 50
enemy_height = 50
enemy_spacing = 100
row_spacing = 50  # Separación entre filas
rows = 3
cols = 10
enemies = []  # Lista para almacenar enemigos

# Crear objetos
nave_principal = nave(450, 700, 50, 50, (0, 0, 255), True, 100, 20, 10)

# Función para crear enemigos en filas
def create_enemies():
    for row in range(rows):
        for col in range(cols):
            x = col * (enemy_width + enemy_spacing) + enemy_spacing
            y = row * (enemy_height + row_spacing) + enemy_spacing
            # Alternar dirección de movimiento
            speed = 2 if row % 2 == 0 else -2  # Primera y tercera fila a la derecha, segunda a la izquierda
            nuevo_enemigo = enemy(x, y, enemy_width, enemy_height, (255, 0, 0), True, 50, 10, speed)
            enemies.append(nuevo_enemigo)

# Gestión de teclas
def manage_keys(teclas):
    dx, dy = 0, 0
    if teclas[pygame.K_w]:
        dy = -1
    elif teclas[pygame.K_s]:
        dy = 1
    elif teclas[pygame.K_a]:
        dx = -1
    elif teclas[pygame.K_d]:
        dx = 1
    nave_principal.move(dx, dy)
    
    if teclas[pygame.K_SPACE]:  
        nave_principal.shoot()

# Comandos para la movilidad y uso de la pantalla
create_enemies()  # Crear enemigos al inicio

while pantalla_abierta:
    time.tick(FPS)

    # Actualizar y mover enemigos
    for enemigo in enemies:
        enemigo.move()  # Asegúrate de que la clase enemy tenga un método move

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    manage_keys(keys)  # Pasar las teclas a la función

    for event in events:
        if event.type == pygame.QUIT:
            pantalla_abierta = False  

    # Limpiar pantalla
    ventana.fill((0, 0, 0))  
    nave_principal.draw(ventana)  # Dibujar nave
    
    # Dibujar enemigos
    for enemigo in enemies:
        enemigo.draw(ventana)  # Asegúrate de que la clase enemy tenga un método draw
        

    # Actualizar y dibujar proyectiles
    nave_principal.projectiles.update()  # Actualizar proyectiles
    nave_principal.projectiles.draw(ventana)  # Dibujar proyectiles
    

    pygame.display.update()

pygame.quit()