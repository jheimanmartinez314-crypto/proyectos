import pygame # type: ignore
import random
import sys

# Inicializar
pygame.init()

# Pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flores Amarillas 🌼")

# Colores
NEGRO = (10, 10, 10)
AMARILLO = (255, 215, 0)
BLANCO = (255, 255, 255)

# Fuente
fuente = pygame.font.SysFont("Arial", 32)

# Clase flor
class Flor:
    def __init__(self):
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(-50, -10)
        self.vel = random.uniform(1, 3)
        self.radio = random.randint(5, 10)

    def caer(self):
        self.y += self.vel
        if self.y > ALTO:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, ANCHO)

    def dibujar(self):
        pygame.draw.circle(pantalla, AMARILLO, (int(self.x), int(self.y)), self.radio)

# Crear flores
flores = [Flor() for _ in range(60)]

# Estado
mostrar_mensaje = False

# Loop
reloj = pygame.time.Clock()

while True:
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mostrar_mensaje = True

    # Dibujar flores
    for flor in flores:
        flor.caer()
        flor.dibujar()

    # Texto inicial
    texto = fuente.render("Haz clic 💛", True, BLANCO)
    pantalla.blit(texto, (ANCHO//2 - 90, ALTO//2 - 20))

    # Mensaje romántico
    if mostrar_mensaje:
        mensaje1 = fuente.render("🌼 Te regalo flores amarillas 🌼", True, AMARILLO)
        mensaje2 = fuente.render("Porque eres muy especial 💛", True, BLANCO)

        pantalla.blit(mensaje1, (ANCHO//2 - 230, ALTO//2 + 40))
        pantalla.blit(mensaje2, (ANCHO//2 - 200, ALTO//2 + 80))

    pygame.display.flip()
    reloj.tick(60)