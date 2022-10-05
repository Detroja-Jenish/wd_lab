import pygame
import math
import numpy
import random

w = 1080
h = 2300

surf_h = surf_w = 600
fontSize = int(surf_h/8)
surf_Position = (w/2 - surf_w/2, h/2 - surf_h/2)

position_directory = {
(0,0):[surf_w/6, surf_h/6],
(0,1):[3*surf_w/6, surf_h/6],
(0,2): [5*surf_w/6, surf_h/6],

(1,0):[surf_w/6, 3*surf_h/6],
(1,1):[3*surf_w/6, 3*surf_h/6],
(1,2):[5*surf_w/6, 3*surf_h/6],

(2,0):[surf_w/6, 5*surf_h/6],
(2,1):[3*surf_w/6, 5*surf_h/6],
(2,2):[5*surf_w/6, 5*surf_h/6]
}

A = [];
B = [];

win = numpy.array([
[0,0,0],
[0,0,0],
[0,0,0]
])

player1 = False;
player2 = True;
over = False;
finish = True;
victory = False;

player_A ='Kahan' # O
player_B = 'Jenish' # X

score_A = ''
score_B = ''

final_A = 0
final_B = 0

#board_bg = (239,205,232)
board_bg = (random.randrange(70,156),random.randrange(100,206),random.randrange(90,226))
main_bg = (220,248,191)
white = (0,0,0)

pygame.init()

screen = pygame.display.set_mode((w,h));
screen.fill(main_bg);

surf = pygame.Surface((surf_w,surf_h))
surf.fill(board_bg)
       
def board(color,X1,y1,X2, y2,size):
    pygame.draw.line(surf,color,(X1,y1),(X2,y2),size)
    
#(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(◕ᴥ◕)(*_*)(*_*)(*_*)(*_*)(*_*)--------------#

def show_text(surf,print,textColor , text_bg , x,y):
    global fontSize
    font = pygame.font.Font('freesansbold.ttf',fontSize);
    text = font.render(print,True,textColor, text_bg)
    textRect = text.get_rect()
    textRect.center = (x,y)
    surf.blit(text,textRect)

#----------------------------------------------------#

def tickMark():
    global mx,my,player1,player2,row,col
    mx -= w/2 - surf_w/2;
    my -= h/2 - surf_h/2;

#    if mx > 0  and mx < surf_w/3:
#        col = 0;
#    elif mx > surf_w/3 and mx < 2*surf_w/3:
#        col = 1;      
#    elif mx > 2*surf_w/3 and mx < surf_w:
#        col = 2;
#    else:
#        pass;
    if mx > 0  and mx < surf_w:
          col = math.floor(mx/(surf_w/3));
    else: pass;
                   
#    if my > 0 and my < surf_h/3:
#        row = 0;
#    elif my > surf_h/3 and my < 2*surf_h/3:
#        row = 1;
#    elif my > 2*surf_h/3 and my < surf_h:
#        row = 2;
#    else:
#        pass;
    if my > 0  and my < surf_h:
          row = math.floor(my/(surf_h/3));
    else: pass;
               
    if mx > 0 and mx < surf_w and my > 0 and my < surf_h:
                    
        [x,y] = position_directory[(row,col)]
        if player1:
            if [x,y] not in A and [x,y] not in B:
                A.append([x,y]);
                win[row,col] = 1
                player1 = False;
                player2 = True
                                                    
        elif player2:
            if [x,y] not in A and [x,y] not in B:
                B.append([x,y]);
                win[row,col] = 2
                player1 = True;
                player2 = False;

#----------------------------------------------------#
def Out_OR_Not():
    global victory, score_A, score_B;

    for i in range(0,3):
        
        if 0 not in win[i] and (2 not in win[i] or 1 not in win[i]):
            
            if win[i,1] == 1:
                    show_text(screen,str(player_A ) +" "+'won',white, main_bg, w/2, h/2-surf_h/2-fontSize);                    
                    score_A = 'won';
            else:
                    show_text(screen,str(player_B) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                    score_B = 'won';
                    
            [x1,y1] = position_directory[(i,0)]
            [x2,y2] = position_directory[(i,2)]
            board(white,x1, y1, x2, y2,10)
            victory = True
            break;
                
        elif 0 not in win[:,i] and (2 not in win[:,i] or 1 not in win[:,i]):
            victory = True;
            if win[1,i] == 1:
                show_text(screen,str(player_A) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_A = 'won';
            else:
                show_text(screen,str(player_B) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_B = 'won';
                    
            [x1,y1] = position_directory[(0,i)]
            [x2,y2] = position_directory[(2,i)]
            board(white,x1, y1, x2, y2,10)
            
            break;
                
        elif win[0,0]==win[1,1]==win[2,2] and win[1,1]!=0:
            victory = True
            if win[1,1] == 1:
                show_text(screen,str(player_A) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_A = 'won'
            elif win[1,1] == 2:
                show_text(screen,str(player_B) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_B = 'won'
                        
            [x1,y1] = position_directory[(0,0)]
            [x2,y2] = position_directory[(2,2)]
            board(white,x1, y1, x2, y2,10)
            break;
                    
        elif win[0,2]==win[1,1]==win[2,0] and win[1,1]!=0:
            victory = True

            if win[1,1] == 1:
                show_text(screen,str(player_A) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_A = 'won'
                        
            elif win[1,1] == 2:
                show_text(screen,str(player_B) + " " + "won",white, main_bg, w/2, h/2-surf_h/2-fontSize);
                score_B = 'won'
                        
            [x1,y1] = position_directory[(0,2)]
            [x2,y2] = position_directory[(2,0)]
            board(white,x1, y1, x2, y2,10)
            break

        elif 0 not in win:
            victory = True
            show_text(screen, str('Match is DRAW'),white, main_bg, w/2, h/2-surf_h/2-fontSize)
            break
            
#----------------------------------------------------#

def O_vs_X():
    
    for letter in A:
        [x,y]=letter
        show_text(surf,str("O"), main_bg,  board_bg,x,y)
    for letter in B:
         [x,y] =letter;
         show_text(surf,str("X"), main_bg, board_bg,x,y)          
         
#    show_text(screen, player_A + ' = '+ str(final_A), (0,0,0),main_bg, 150,50)  
#    show_text(screen, player_B + ' = ' + str(final_B), (0,0,0),main_bg,170,150)

    font = pygame.font.Font('freesansbold.ttf',int(fontSize/2));
    text_A = font.render(player_A + ' = '+ str(final_A),True, (115,40,20),main_bg)
    rect_A = text_A.get_rect()
    rect_A.topleft = (0,0)
    text_B = font.render(player_B + ' = '+ str(final_B), True, (20,115,60),main_bg)
    rect_B = text_A.get_rect()
    rect_B.topleft = (0,50)
    
    screen.blit(text_A,rect_A)
    screen.blit(text_B,rect_B)
    
def score():
	global score_A,score_B,final_A,final_B
	if score_A == 'won':
		final_A += 1
		score_A= ''
	if score_B == 'won':
	   final_B += 1
	   score_B = ''

#----------------------------------------------------#

def reset():
    global board_bg
    board_bg = (random.randrange(70,156),random.randrange(100,206),random.randrange(90,226));
    screen.fill(main_bg);
    surf.fill(board_bg);
    global  A,B,win, victory;
    del A[:];
    del B[:];
    win = numpy.zeros((3,3));
    victory = False;
    
#-------------/////////////////////////////------#----
    
def showPlayerName():
    if not victory:
        if player1:
            show_text(screen, player_A + "’s" +' '+'Turn',white, main_bg, w/2, h/2-surf_h/2-fontSize)
        else:
            show_text(screen, player_B + "’s" +' '+'Turn',white, main_bg, w/2, h/2-surf_h/2-fontSize)
    
#-------$$$$$$$$$$^^^^^^^^^^^$$$$$$$$$------#

while not over:
    global row,col
    screen.fill(main_bg)
    
    board(main_bg,surf_w/3, 0,surf_w/3, surf_h,10)
    board(main_bg,2*surf_w/3, 0, 2*surf_w/3, surf_h,10)
    board(main_bg,0, surf_h/3 , surf_w, surf_h/3,10)
    board(main_bg,0, 2*surf_h/3, surf_w, 2*surf_h/3,10)
    
    board((0,0,0),surf_w/3, 0,surf_w/3, surf_h,1)
    board((0,0,0),2*surf_w/3, 0, 2*surf_w/3, surf_h,1)
    board((0,0,0),0, surf_h/3 , surf_w, surf_h/3,1)
    board((0,0,0),0, 2*surf_h/3, surf_w, 2*surf_h/3,1)
    if not victory:
        score()
    
    O_vs_X()
    
    
    Out_OR_Not()
    
    showPlayerName()

    screen.blit(surf, surf_Position)

    if victory:
        show_text(screen,str("··––RESET––··"),white, main_bg, w/2, h/2 + surf_h/2+fontSize)  
            
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:  
            [mx,my] = pygame.mouse.get_pos()

            if not victory:
                tickMark()
                            
            else:
                if (mx>w/4 and mx<3*w/4) and (my<h/2 + surf_h/2+fontSize +fontSize/2 and my>h/2 + surf_h/2 +fontSize - fontSize/2):
                    reset();
                
    pygame.display.update();
    pygame.time.Clock().tick(30)