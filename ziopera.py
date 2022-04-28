from multiprocessing.sharedctypes import Value
from time import sleep
import pygame
from button import Button

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
    p = 0
    print(scelta)
    #immagini player
    pi1 = pygame.image.load('p1.png')
    pi2 = pygame.image.load('p2.png')
    pi3 = pygame.image.load('p3.png')
    pi4 = pygame.image.load('p4.png')

    #pi = [pygame.image.load('p1.png'), pygame.image.load('p2.png'), pi3 = pygame.image.load('p3.png'), pi4 = pygame.image.load('p4.png')]
    
    #spazio per il testo input
    input_rect = pygame.Rect((x/2-(x*10/100)), y/2, 140, 32)
    
    #posizione iniziale giocatori
    px = (x/8)
    px1 = 3*(x/8)
    px2 = 5*(x/8)
    px3 = 7*(x/8)
    
    py = y - 64
    py1 = y - 64
    py2 = y - 64
    py3 = y - 64
    
    #caduta
    py_change = 0
    py1_change = 0
    py2_change = 0
    py3_change = 0
    
    #score e set
    score_val = 0
    score_val1 = 0
    score_val2 = 0
    score_val3 = 0
    
    s = 0 #set = 0
    s1 = 0 #set1 = 0
    s2 = 0 #set2 = 0
    s3 = 0 #set3 = 0

    #posizione testo score
    textX = (x/8)
    textY = 10
    
    #nomi user si potrebbe usare una lista come con le pi
    user_text = ["", "", "", ""]
    
    #funzione che stampa le scritte set e score
    def show_score(x,y,val):
        score = font(32).render("Score: " + str (val), True, (255,255,255))
        screen.blit(score, (x,y))
    
    def show_set(x,y,vsl):
        set = font(32).render("Set: " + str (vsl), True, (255,255,255))
        screen.blit(set, (x,y))

    #funzione che stampa le immagini dei giocatori
    def player1(x,y):
        screen.blit(pi1,(x,y))
        
    def player2(x1,y1):
        screen.blit(pi2,(x1,y1))
    
    def player3(x2,y2):
        screen.blit(pi3,(x2,y2))
        
    def player4(x3,y3):
        screen.blit(pi4,(x3,y3))
    
    #coordinate richesta nick input
    count_d = False
    y_in = (y/2)-50#(y/2-(y*20/100))
    
    a = 1
    
    #richiesta username
    def req(a):
        request = font(45).render("Inserisci lo username del giocatore " + str (a) + "\n", True, (0,0,0))
        rect = request.get_rect()
        rect.center = (x/2), y_in
        screen.blit(request, rect)
    
    
    #countdown
    def countdown():
        m = 3
        while m < 0:
            count = font(75).render(str (m), True, (255,255,255))
            m -= 1
            rect2 = count.get_rect()
            rect2.center = (x/2), y_in
            screen.blit(bg, (0,0))
            screen.blit(count, rect2)
            pygame.display.update()
            pygame.time.wait(1000)
        return True;
        
    #gioco vero e proprio
    for cont in range (scelta) :
        con = cont+1
        us = True
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
                        user_text[cont] = user_text[cont][:-1]
                    else:
                        user_text[cont] += event.unicode
            user = font(32).render(user_text[cont], True, (0,0,0))
            screen.blit(user, (input_rect.x+5, input_rect.y+5))
            pygame.display.update()
        print(user_text[cont])
        pygame.time.wait(350)

    game = True
    z = True
    while game:
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or z == False):
                game = False
            if(count_d == False):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        py += -300
                    elif event.key == pygame.K_UP:
                        py1 += -25
                    elif event.key == pygame.K_KP_ENTER:
                        py2 += -25
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(event.button == 3):
                        py3 += -25
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        py_change = 0.2
                    elif event.key == pygame.K_UP:
                        py1_change = 0.2
                    elif event.key == pygame.K_KP_ENTER:
                        py2_change = 0.2
                if event.type == pygame.MOUSEBUTTONUP:
                    if(event.button == 3):
                        py3_change = 0.2
        
        #vittoria score
        if((py<=0) or (py1<=0) or (py2<=0) or (py3<=0)):
            if(py <=0):
                score_val += 1
            if(py1 <=0):
                score_val1 += 1
            if(py2 <=0):
                score_val2 += 1
            if(py3 <=0):
                score_val3 += 1
            if(score_val != 4 or score_val1 != 4 or score_val2 != 4 or score_val3 != 4):
                count_d = countdown()

        #restart
        if(score_val != 0 or score_val1 != 0 or score_val2 != 0 or score_val3 != 0):
            py = y-64
            py1 = y-64
            py2 = y-64
            py3 = y-64

        if(p<3):
            if(s1 != 3 or s != 3 or s2 != 3 or s3 != 3 and score_val == 4 or score_val1 == 4 or score_val2 == 4 or score_val3 == 4):
                if(score_val == 4 or score_val1 == 4 or score_val2 == 4 or score_val3 == 4):
                    if(score_val == 4):
                        a = user_text1
                        s += 1
                    elif(score_val1 == 4):
                        s1 += 1
                        a = user_text2
                    elif(score_val2 == 4):
                        s2 += 1
                        a = user_text3
                    elif(score_val3 == 4):
                        s3 += 1
                        a = user_text4
                    p += 1 
                    if(p!=3):
                        score = font(50).render("Complimenti " + a + " hai vinto il " + str (p) + " set!", True, (255,0,0))
                        rect1 = score.get_rect()
                        rect1.center = (x/2), y_in
                        screen.blit(score, rect1)
                        pygame.display.update()
                        pygame.time.wait(3000)
                        score_val = score_val1 = score_val2 = score_val3 = 0
                        pygame.display.update()
        else:
            if(s1 == 3 or s == 3 or s2 == 3 or s3 == 3):
                if(score_val == 4 or score_val1 == 4 or score_val2 == 4 or score_val3 == 4):
                    #pygame.event.wait()
                    if(score_val == 4):
                        a = user_text1
                    elif(score_val1 == 4):
                        a = user_text2
                    elif(score_val2 == 4):
                        a = user_text3
                    elif(score_val3 == 4):
                        a = user_text4
                    score = font(50).render("Complimenti " + str (a) + " hai vinto!", True, (255,0,0))
                    screen.blit(score, (100,320))
                    pygame.display.update()
                    pygame.time.wait(1500)
                    pygame.display.update()
                    z = False
        #bordi lato verticale
        if(py <= 0):
            py = 0
        elif(py >= y - 64):
            py = y - 64
        if(py1 <=0):
            py1 = 0
        elif(py1>=(y - 64)):
            py1= y - 64
        if(py2 <=0):
            py2 = 0
        elif(py2>=(y - 64)):
            py2 = y - 64
        if(py3 <=0):
            py3 = 0
        elif(py3>=(y - 64)):
            py3 =  y - 64

        py += py_change
        py1 += py1_change
        py2 += py2_change
        py3 += py3_change

        player1(px,py)
        player2(px1,py1)
        player3(px2,py2)
        player4(px3,py3)

        show_score(textX - 32, textY,score_val)
        show_score((textX * 3) -32, textY,score_val1)
        show_score((textX * 5) -32, textY,score_val2)
        show_score((textX * 7) -32, textY,score_val3)

        show_set(textX - 32, textY + 32, s)
        show_set((textX * 3) -32 , textY + 32, s1)
        show_set((textX * 5) -32, textY + 32, s2)
        show_set((textX * 7) -32, textY + 32, s3)

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