import pygame, sys , random , time
pygame.init()

# Variables
width = 1200
height = 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jet Game')
clock = pygame.time.Clock()
player = pygame.image.load('imgs/rafale.png')
player = pygame.transform.scale(player , (128,128))
sky =  pygame.image.load('imgs/sky2.jpg')
sky = pygame.transform.scale(sky, (width , height))
x = width / 2 - 256
y = height -128
speed = 15
enemy  = pygame.image.load('imgs/pl15.png')
enemy = pygame.transform.scale(enemy , (64,64))
m = width - 134
n = height - 342
espeed = 25
crash = pygame.mixer.Sound('imgs/hit.wav')
font = pygame.font.SysFont(None , 48)
score = 0
# Game loop
running = True
while running:
    score_text = font.render(f"Score : {score}", True, (255,255,255))
    screen.blit(sky , (00,00))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    screen.blit(player , (x , y))
    screen.blit(enemy , (m,n))
    screen.blit(score_text, (20,20))
    erect = pygame.Rect(m , n , 32,32)
    prect = pygame.Rect(x , y , 64,64)
    
    if erect.colliderect(prect):
        crash.play()
        time.sleep(2)
        running = False
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    
        
    #Keep img inside
    if x < 0 :
       x = 0
    if x > 1000-128:
        x = 1000-128
    if y < 0:
        y = 0
    if y > 1000-128:
        y = 1000-128
       
    m -= espeed
    if m <= 0:
        m = width
        n = random.randint(0, height - 64)
        score += 1
    
     
       
    clock.tick(60)
pygame.quit()
sys.exit()
