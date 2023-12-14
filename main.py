import pygame as p
from sys import exit

p.init()

width = 800
height = 400
screen = p.display.set_mode((width, height))
p.display.set_caption('Runner')
clock = p.time.Clock()
test_font = p.font.Font('background/ZeroCool.ttf', 25)
font_game_over = p.font.Font('background/ZeroCool.ttf', 75)
game_active = True

background = p.image.load('background/2_game_background.png').convert() #init du background
background = p.transform.scale(background, (width, height))

game_over_surface = font_game_over.render('GAME OVER', False, 'WHITE').convert() # init du font 
game_over_rect = game_over_surface.get_rect(midtop = (400, 100)) #center pour le centre

score_surface = test_font.render('Zombies killed', False, 'Red').convert() # init du font 
score_rect = score_surface.get_rect(midtop = (100, 15)) #center pour le centre

zombie_vilain = p.image.load('background/walk_skeleton/00.png').convert_alpha()
zombie_vilain_reverse = p.transform.flip(zombie_vilain, True, False) #permet de tourner le perso dans lautre sens
zombie_rect = zombie_vilain.get_rect(midbottom = (750, 363)) #trace un rectangle autour du personnage, sinon le programme utilise limage par defaut et donc les bords sont bcp plus loin que le personnage en lui meme

samurai = p.image.load('background/Walk_samurai/00.png').convert_alpha() 
samurai_rect = samurai.get_rect(midbottom = (50, 363)) #permet de placer le perso a partir dun rectangle et non du top left de base, donc ici avec midbottom on part du bas du personnage.
#pour chaque perso on doit toujours creer deux variable, la surface et ensuite son rectangle

samurai_gravity = 0

move_left = False
move_right = False    # set up des flags 

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        if game_active:
            if event.type == p.KEYDOWN: #set up du flag TRUE quand on press la touche
                if event.key == p.K_ESCAPE:
                    p.quit()
                    exit()
                if event.key == p.K_SPACE and samurai_rect.bottom >= 363:
                    samurai_gravity = -8
                if event.key == p.K_LEFT:
                    move_left = True
                elif event.key == p.K_RIGHT:
                    move_right = True
            if event.type == p.KEYUP:  #set up du flag FLASE quand on relache la touche
                if event.key == p.K_LEFT:
                    move_left = False
                elif event.key == p.K_RIGHT:
                    move_right = False
        else:
            if event.type == p.KEYDOWN and event.key == p.K_SPACE:
                game_active = True
                samurai_rect.left = 50
                zombie_rect.left = 750
            
    if game_active:
        if move_left:
            samurai_rect.left -= 4
        if move_right:
            samurai_rect.right += 4 #si right ou left est vrai -> moove
        screen.blit(background, (0, 0))
        p.draw.rect(screen, 'Black', score_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(zombie_vilain_reverse, zombie_rect)
        
        zombie_rect.left -= 3
        if zombie_rect.right <= 0:
            zombie_rect.left = width

        #player
        samurai_gravity += 0.25
        samurai_rect.y += samurai_gravity
        if samurai_rect.bottom >= 363:
            samurai_rect.bottom = 363
        screen.blit(samurai, samurai_rect)
        #game over
        if zombie_rect.colliderect(samurai_rect):
            game_active = False
    else:
        screen.blit(game_over_surface, game_over_rect)

    p.display.update()
    clock.tick(60) # est utile pour dire a ma loop de ne pas run trop rapidement 
# pour les fps, penser a avoir des fps de 60 environ pour avoir une bonne portabilite
    


