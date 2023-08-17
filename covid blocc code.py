import pygame
import random
import sys
import time
import os
import colorama
from colorama import Fore, Style
ans=input(Fore.YELLOW+"do you want to conitnue? yes/no::")
ans='yes'



while ans=='yes':
    print(Fore.RED+ "                       |C O V I D - 1 9|")
    print()
    print(Fore.BLACK+ "Select the option number:")
    print(Fore.CYAN+ "  1.About Covid-19")
    print(Fore.CYAN+ "  2.Symptoms")
    print(Fore.CYAN+ "  3.Cure/vaccines")
    print(Fore.CYAN+ "  4.Precautions")
    print(Fore.CYAN+ "  5.Important phone numbers")
    print(Fore.CYAN+ "  6.How to play the game")
    print(Fore.CYAN+ "  7.Change personalize game")
    print(Fore.CYAN+ "  8.Game")
    print()
    a=int(input(Fore.BLACK+'Enter option number:'))
    if a==1:
        print(Fore.YELLOW+ "    1.History of Covid-19")
        print(Fore.YELLOW+ "    2.How does Covid-19 spread?")
        print(Fore.YELLOW+ "    3.Eduaction during Covid-19")
        b=int(input(Fore.BLACK+'    Enter option number:'))
        if b==1:
            print(Fore.YELLOW+'                                                                                             |About Covid-19|')
            print(Fore.MAGENTA+'                                                                                          |History of Covid -19|')
            print(Fore.GREEN+'')
            myfile=open("history.txt",'r')
            str=myfile.read()
            print(str)
            print("_______________________________________________________________________________________________________________________________________________________________________________________")
        elif b==2: 
            print(Fore.YELLOW+'                                                                                             |About Covid-19|')
            print(Fore.MAGENTA+'                                                                                        |How does Covid-19 spread?|')
            print(Fore.GREEN+'')
            myfile=open("spread.txt",'r')
            str=myfile.read()
            print(str)
            print("_______________________________________________________________________________________________________________________________________________________________________________________")
        elif b==3:
            print(Fore.YELLOW+'                                                                                             |About Covid-19|')
            print(Fore.MAGENTA+'                                                                                        |Eduaction during Covid-19|')
            print(Fore.GREEN+'') 
            myfile=open("education.txt",'r')
            str=myfile.read()
            print(str)
            print("_______________________________________________________________________________________________________________________________________________________________________________________")
        else:
            print("Enter a valid number")
    elif a==2:
        print(Fore.MAGENTA+'                                                                                                |Symptoms|')
        print(Fore.GREEN+'') 
        myfile=open("symptoms.txt",'r')
        str=myfile.read()
        print(str)
        print("_______________________________________________________________________________________________________________________________________________________________________________________")
    elif a==3:
        print(Fore.MAGENTA+'                                                                                        |Cure/vaccines|')
        print(Fore.GREEN+'') 
        myfile=open("vac.txt",'r')
        str= myfile.read()
        print(str)
        print("_______________________________________________________________________________________________________________________________________________________________________________________")
    elif a==4:
        print(Fore.MAGENTA+'                                                                                                |Precautions|')
        print(Fore.GREEN+'')
        myfile=open("pre.txt",'r')
        str=myfile.read()
        print(str)
        print("_______________________________________________________________________________________________________________________________________________________________________________________")
    elif a==5:
        print()
        print(Fore.YELLOW+'                                                                                                 |Important phone numbers|')
        print(Fore.GREEN+'')
        myfile=open("phone.txt",'r')
        str=myfile.read()
        print(str)
        print("_______________________________________________________________________________________________________________________________________________________________________________________")
    elif a==6:
        print()
        print(Fore.YELLOW+'                                                                                                 |How to play the game|')
        print(Fore.GREEN+'')
        myfile=open("htp.txt",'r')
        str=myfile.read()
        print(str)
        print("_______________________________________________________________________________________________________________________________________________________________________________________")
    elif a==7:
        print()
        print(Fore.BLACK+' SELECT OPTION')
        print(Fore.GREEN+'1. Change color of player: ')
        print(Fore.GREEN+'2. Change color of enemy: ')
        print(Fore.GREEN+'3. Change speed of enemy: ')
        a=int(input(Fore.BLACK+' SELECT OPTION'))
        if a==1:
            print(Fore.YELLOW+'RED    -(255,0,0)')
            print(Fore.YELLOW+'GREEN  -(183,255,0)')
            print(Fore.YELLOW+'BLUE   -(0,255,255)')
            print(Fore.YELLOW+'YELLOW -(255,242,0)')
            global huc
            huc=input('Enter the RGB color: ')
        if a==2:
            print(Fore.YELLOW+'RED    -(255,0,0)')
            print(Fore.YELLOW+'GREEN  -(183,255,0)')
            print(Fore.YELLOW+'BLUE   -(0,255,255)')
            print(Fore.YELLOW+'YELLOW -(255,242,0)')
            global enc
            enc=input('Enter the RGB color: ')
            
        if a==3:
            global speed
            speed=int(input('Enter speed for block drop:'))
    elif a==8:
        print(Fore.YELLOW+"Stay home. Stay safe. Enjoy the game.")
        

        pygame.init()

        width=450   #screen size
        height=600
 
        enc=(255,0,0)                  #block color
        huc=(204,255,0) 
        background_col=(0,0,0)

        player_size=50                                   #human
        player_pos=[width/2,height-2*player_size]

        enemy_size=50                                       #virus
        enemy_pos=[random.randint(0,width-enemy_size),0]

        speed=25         #block fall
        
        screen=pygame.display.set_mode((width,height))       #put up a screen
     
        game_over=False

        clock=pygame.time.Clock()                         #frames/second rate

        def detect_collision(player_pos,enemy_pos):
            p_x=player_pos[0]
            p_y=player_pos[1]

            e_x=enemy_pos[0]
            e_y=enemy_pos[1]
       
            if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+ enemy_size)):                   #position h== position v
                if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
                    return True
            else:
                return False


        pygame.mixer.init()
        pygame.mixer.music.load("novaa.mp3")          #music
        pygame.mixer.music.play()

        pygame.event.get()
        while not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:            #close
                        sys.exit()
                if event.type==pygame.KEYDOWN:
                    x=player_pos[0]
                    y=player_pos[1]                    #position
                    if event.key==pygame.K_LEFT:       #left arrow key
                        x-=player_size
                    elif event.key==pygame.K_RIGHT:     #right arrow key
                        x+=player_size
                    player_pos=[x,y]

            screen.fill(background_col)           #bg color

        #Update position of enemy
            if enemy_pos[1]>=0 and enemy_pos[1]<height:       #virus fall height
                enemy_pos[1]+=speed
            else:
                enemy_pos[0]=random.randint(0,width-enemy_size)        #reach ground
                enemy_pos[1]=0       

            if detect_collision(player_pos,enemy_pos):
                game_over=True
                sys.exit()                                           #end game
           
            pygame.draw.rect(screen,huc, (player_pos[0],player_pos[1],player_size,player_size))             #virus n human defining
            pygame.draw.rect(screen,enc, (enemy_pos[0], enemy_pos[1],enemy_size,enemy_size))                    
     
            clock.tick(30)
            pygame.display.update()
           

    else:
        print("Enter a valid number")

    ans=input(Fore.BLACK+"Do you want to continue?yes/no")
else:
    print(Fore.RED+"Stay home. Stay safe. Bye.")
    exit()