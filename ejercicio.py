import pygame
import random

pygame.init()

#configuracion de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock= pygame.time.Clock()
pygame.display.set_caption('proyecto 1 - Juego del Espacion')

#crear imagenes
def  load_img(path, size=None)
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size) if size else img

player_img = load_img('player.png', (60,60))
enemy_img = load_img('enemy.png',(50,50))
bullet_img = load_img("bullet.png", (10, 20))

#cargar sonidos
pygame.mixer.music.load('musica.wav')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

shoot_sound = pygame.mixer.Sound('shoot.wav')
shoot_sound.set_volume(0.5)

#clases del videojuego
class Player:
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT - 90
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.speed
        if keys[pygame.K_RIGHT]: self.x += self.speed
        self.x= max(0, min(self.x, WIDTH - 60))

    def draw(self):
        screen.blit(player_img, (self.x self.y))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = 0
        self.speed = random.choice([1, 1, 2])

    def move(self): self.y += self.speed
    def draw(self): screen.blit(enemy_img, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.x = x + 25
        self.y = y
        self.speed = -10

    def move(self): self.y += self.speed
    def draw(self): screen.blit(bullet_img, (self.x, self.y))

#funciones generales
def draw_text(text, size, y, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, color)
    screen.blit(render, ((WIDTH - render.get_width())//2, y))

def start_screen():
    screen.fill((0, 0, 20))
    draw_text('GALATIC BATTLE', 72, HEIGHT//2 - 100, (0, 200, 255))
    draw_text('Preciona ESPACIO para iniciar', 36, HEIGHT//2 + 20)
    draw_text('Desarrollado por: ////', 32, HEIGHT//2 + 100, (180, 180, 180))

def game_over_screen(score):
    screen.fill((10, 0, 30))
    draw_text('GAME OVER', 72, HEIGHT //2 - 120, (255,50,50))
    draw_text(f'PUNTAJE:'(score), 48, HEIGHT //2 - 20)
    draw_text('Presiona R para reiniciar', 36, HEIGHT //2 + 60, (200, 200, 200))
    pygame.display.update()

#loop del juego
def game_loop():
    player = Player()
    player = []
    player = []
    score = 0

    while True:
        screen,fill((0, 0, 20))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return 'quit'
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE
                bullets.append(Bullet(player.x, player.y))
                shoot_sound.play()
        player.move(pygame.key.get_pressed)

        #dibujo 
        player.draw()
        for e in enemies: e.draw()
        for b in bullets: b.draw()

        #puntaje 
        draw = pygame.font.SysFont(None, 36).render(f'Puntaje: {score}', True, (255, 255, 255))
        screen.blit(draw, (10, 10))
        pygame.display.update()
        clock.tick(60)

# estados principales 
game_state = 'start'
final_score = 0

running = True 
while running:

    if game_state == 'start':
        start_screen()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                game_state = 'playing' 
    elif game_state == 'playing':
        result= game_loop()
        if result == 'quit':
            running = False
        elif result[0] == 'gameover':
            final_score = result[1]
            game_state = 'gameover'

    elif game_state == 'gameover':
        game_over_screen(final_score)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                game_state = 'start'

pygame.quit()
