from multiprocessing.sharedctypes import Value
import time
import pygame
from button import Button
import array as arr


pygame.init()

#schermo
screen = pygame.display.set_mode()
x, y = screen.get_size()
x = x*75/100
y = y*75/100
screen = pygame.display.set_mode((x,y))

#icona.exe
icona = pygame.image.load('propic.png')
pygame.display.set_icon(icona)

#titolo .exe
pygame.display.set_caption("space game")

#creare uno sfondo
bg = pygame.image.load('wal.png')

#musica base
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

#font vari
def font(size):
    return pygame.font.Font('JustBubble.ttf', size)

def player():

    run = True
    while run:
        screen.blit(bg, (0,0)) 
        
        pos_mouse = pygame.mouse.get_pos()
        
        menu_text = font(75).render("Quanti giocatori?" + "\n da 2 a 4", True, "#aaf99f")
        menu_rect = menu_text.get_rect(center = (x/2,100))
        
        screen.blit(menu_text, menu_rect)
        
        gioca2 = Button(image= pygame.image.load("Quit Rect.png"), pos = (x/6,y/2), text_input = "2 Giocatori", font = font(50), base_color = "#aaf99f", hovering_color="White")
        gioca3 = Button(image= pygame.image.load("Quit Rect.png"), pos = (3*(x/6),y/2), text_input = "3 Giocatori", font = font(50), base_color = "#aaf99f", hovering_color="White")
        gioca4 = Button(image= pygame.image.load("Quit Rect.png"), pos = (5*(x/6),y/2), text_input = "4 Giocatori", font = font(50), base_color = "#aaf99f", hovering_color="White")
        puls_quit = Button(image=pygame.image.load("Quit Rect.png"), pos=(x/2, (y/1.2)), text_input="INDIETRO", font = font(35), base_color="#aaf99f", hovering_color="White")
        
        for button in [gioca2, gioca3, gioca4, puls_quit]:
            button.changeColor(pos_mouse)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gioca2.checkForInput(pos_mouse):
                    scelta = 2
                    play(scelta) 
                    return scelta
                if gioca3.checkForInput(pos_mouse):
                    scelta = 3
                    play(scelta)
                if gioca4.checkForInput(pos_mouse):
                    scelta = 4
                    play(scelta)
                if puls_quit.checkForInput(pos_mouse):
                    menu()
            
        pygame.display.update()

def play(scelta):
    print(scelta)

    #immagini user
    player_image = [pygame.image.load('p1.png'), pygame.image.load('p2.png'), pygame.image.load('p3.png'), pygame.image.load('p4.png')]

    #spazio per il testo
    inp_rect = pygame.Rect(x/2-(x*0.1), y/2,140, 32)

    #posizioni immagini
    player_x = [x/(scelta*2), 3*(x/(scelta*2)), 5*(x/(scelta*2)), 7*(x/(scelta*2))]
    player_y = [y-64, y-64, y-64, y-64]

    #caduta
    player_change = [0,0,0,0]

    #valori score e set
    score_ = [0,0,0,0]

    set_ = [0,0,0,0]

    #posizione testo score
    text_posX = [x/(scelta*2), 3*(x/(scelta*2)), 5*(x/(scelta*2)), 7*(x/(scelta*2))]
    text_posY = 10

    #nickname
    username = ["", "", "", ""]

    #funzione per mostrare il punteggio set
    def show_score(score_, scelta, x, y):
        for cont in range (scelta):
            score = font(32).render("Score: " + str (score_[cont]), True, (255,255,255))
            screen.blit(score, (x[cont],y))
            

    #funzione per mostrare il punteggio set        
    def show_set(scelta, set_, x, y ):
        for cont in range (scelta):
            set = font(32).render("Set: " + str (set_[cont]), True, (255,255,255))
            screen.blit(set, (x[cont],y))
    
    #funzione per stampare le immagini
    def giocatori(player_image, x, y, scelta):
        for cont in range (scelta):
            screen.blit(player_image[cont], (x[cont],y[cont]))
    
    y_in = y/2 - 50

    #funzione per chiedere in input il nome
    def req(a):
        richiesta = font(45).render("Inserisci lo username del giocatore " + str (a) + "\n", True, (255,255,255))
        rect = richiesta.get_rect()
        rect.center = (x/2), y_in
        screen.blit(richiesta, rect)
    
    #countdown fine set
    def countscore(nome, gioc):
        if(gioc[cont]<4):
            score = font(50).render("complimenti " + nome[cont] + " hai vinto il tuo " + str (gioc[cont]) +" game!", True, "White")
            rett = score.get_rect()
            rett.center = (x/2), y_in
            screen.blit(score, rett)
            pygame.display.update()
            pygame.time.wait(1500)
            pygame.display.update()
    
    #richiesta username a schermo
    p = 0
    name = True
    con = 0
    while name:
        con += 1 
        us = True
        if(con <= scelta):
            while us:
                screen.blit(bg, (0,0))
                req(con)
                for event in pygame.event.get():
                    if(event.type == pygame.quit):
                        us = False
                    if(event.type == pygame.KEYDOWN):
                        if(event.key == pygame.K_RETURN):
                            us = False
                        elif(event.key == pygame.K_BACKSPACE):
                            username[con-1] = username[con-1][:-1]
                        else:
                            username[con-1] += event.unicode
                user = font(32).render(username[con-1], True, (0,0,0))
                screen.blit(user, (inp_rect.x+5,inp_rect.y+5))
                pygame.display.update()
        else:
            name = False
            us = False
        pygame.time.wait(350)
    pygame.display.update()
#gioco    
    game = True
    z = True
    while game:
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or z == False):
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_y[0] += -300
                elif event.key == pygame.K_UP:
                    player_y[1] += -25
                elif event.key == pygame.K_KP_ENTER:
                     player_y[2] += -25
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 3):
                    player_y[3] += -25
            if event.type == pygame.KEYUP:   
                if event.key == pygame.K_SPACE:
                    player_change[0] = 0.2
                elif event.key == pygame.K_UP:
                    player_change[1] = 0.2
                elif event.key == pygame.K_KP_ENTER:
                    player_change[2] = 0.2
            if event.type == pygame.MOUSEBUTTONUP:
                if(event.button == 3):
                    player_change[3] = 0.2
        
        #vittoria score
        for cont in range (scelta):
            if (player_y[cont]<=0):
                score_[cont] += 1
                player_y[0]  = player_y[1] = player_y[2] = player_y[3] = y-64
                countscore(username, score_)
            if(p<3):
                if(set_[cont] != 3 and score_[cont] == 4):
                    if(score_[cont] == 4):
                        a = username[cont]
                        set_[cont] += 1
                        p += 1
                        if(p!=3):
                            score = font(50).render("complimenti " + a  + " hai vinto il tuo " + str(p) +" set!", True, (255,255,255))
                            rett = score.get_rect()
                            rett.center = (x/2), y_in
                            screen.blit(score, rett)
                            pygame.display.update()
                            pygame.time.wait(1500)
                            pygame.display.update()
                            score_[0] = score_[1] = score_[2] = score_[3] = 0
                elif set_[cont] == 3:
                    if(score_[cont] == 4):
                        a = username[cont]
                    score = font(50).render("complimenti " + a  + " hai vinto!", True, (255,255,255))
                    rett = score.get_rect()
                    rett.center = (x/2), y_in
                    screen.blit(score, rett)
                    pygame.display.update()
                    pygame.time.wait(1500)
                    pygame.display.update()
                    z = False
        for cont in range (scelta):
            if(player_y[cont] <= 0):
                player_y[cont] = 0
            elif(player_y[cont] >= (y-64)):
                player_y[cont] = (y-64)
        
        for cont in range (scelta):
            player_y[cont] += player_change[cont]
        
        giocatori(player_image, player_x, player_y, scelta)
        show_score(score_, scelta, text_posX, text_posY)
        show_set(scelta, set_, text_posX, text_posY + 32)     
        
        pygame.display.update()                   

def menu():
    running = True
    while running:
        screen.blit(bg, (0,0))
        
        pos_mouse = pygame.mouse.get_pos()
        
        menu_text = font(150).render("MAIN MENU", True, "#aaf99f")
        menu_rect = menu_text.get_rect(center = (x/2,100))
        
        screen.blit(menu_text, menu_rect)
        
        puls_gioca = Button(image=pygame.image.load("Play Rect.png"), pos=(x/2, 1.2*(y/3)), 
                            text_input="PLAY", font = font(75), base_color= "#aaf99f", hovering_color="White")
        puls_quit = Button(image=pygame.image.load("Quit Rect.png"), pos=(x/2, 2*(y/3)), 
                            text_input="ESCI", font = font(75), base_color="#aaf99f", hovering_color="White")
        
        screen.blit(menu_text, menu_rect)
        
        for button in [puls_gioca, puls_quit]:
            button.changeColor(pos_mouse)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puls_gioca.checkForInput(pos_mouse):
                    player()
                if puls_quit.checkForInput(pos_mouse):
                    pygame.quit()
                    running = False

        pygame.display.update()

menu()